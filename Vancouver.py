import requests, time
from bs4 import BeautifulSoup
import pandas as pd

# Points of Interest & Landmarks in Toronto
LANDMARK_URL = "https://www.tripadvisor.ca/Attractions-g154943-Activities-c47-t163-Vancouver_British_Columbia.html"
#Nature & Parks in Toronto
PARK_URL= "https://www.tripadvisor.ca/Attractions-g154943-Activities-c57-Vancouver_British_Columbia.html"
#Museums in Toronto
MUSEUM_URL = "https://www.tripadvisor.ca/Attractions-g154943-Activities-c49-Vancouver_British_Columbia.html"
PREFIX = "https://www.tripadvisor.ca/"

FILE_NAME = "Vancouver.csv"

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) Safari/537.36',
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        'Accept-Language': "en-CA,en;q=0.9,zh-CN;q=0.8,zh-CA;q=0.7,zh;q=0.6",
        'Connection': "keep-alive",
        # "Content-Type": "application/json",
        "referer": "https://www.tripadvisor.ca/",
        "Cash-Control": "no-cache, must-revalidate"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        text = response.text
        # print(text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # parse html
    page = BeautifulSoup(text, features="lxml")
    return page

def retrieve_data_from_page(page, url, offset):
    try:
        #If scraping fails, try a few more times
        while page is None:
            time.sleep(1)
            page = parse_page(url)
        attraction_list = page.find_all("div", attrs={"class": "ALtqV z"})
        item_list = []
        
        tmp = attraction_list[0]
        attraction_url_element = tmp.find("div", attrs={"class", "alPVI eNNhq PgLKC tnGGX"})
        #If scraping fails, try a few more times
        while attraction_url_element is None:
            time.sleep(1)
            page = parse_page(url)
            attraction_list = page.find_all("div", attrs={"class": "ALtqV z"})
            tmp = attraction_list[0]
            attraction_url_element = tmp.find("div", attrs={"class", "alPVI eNNhq PgLKC tnGGX"})
        
        for attraction in attraction_list:
            attraction_url = ""
            attraction_url_element = attraction.find("div", attrs={"class", "alPVI eNNhq PgLKC tnGGX"})
            if attraction_url_element is not None:
                attraction_url = PREFIX + attraction_url_element.a["href"]
            else:
                print(url)
                print(attraction)

            attraction_page = parse_page(attraction_url)

            # name
            name = ""
            name_element = attraction_page.find(class_="biGQs _P fiohW eIegw")
            if name_element is not None:
                name = name_element.text.strip()
                print("name:", name)

            # rate
            rate = 0
            rate_element = attraction.find(class_="jVDab o W f u w JqMhy")
            if rate_element is not None:
                rate = rate_element.svg.title.text.strip()[0:3]
            print("rate:", rate)

            # img_url
            img_url = ""
            img_element = attraction_page.find(class_="yMdQy w")
            if img_element is not None:
                img_element = img_element.find("img")
                if img_element is not None:
                    img_url = img_element["src"]
            print("img_url", img_url)

            # label
            label_list = []
            label_list_element = attraction_page.find_all(class_="eojVo")
            for label_element in label_list_element:
                label = label_element.text.strip()
                label_list.append(label)
            print("label:", label_list)

            # address
            address = ""
            address2 = ""
            area_element = attraction_page.find(class_="wgNTK")
            if area_element is not None:
                address_element = area_element.find(class_="biGQs _P XWJSj Wb")
                if address_element is not None:
                    address = address_element.text.strip()
                address_2_element = area_element.find(class_="MK")
                if address_2_element is not None:
                    address_2_element = address_2_element.find(class_="biGQs _P fiohW fOtGX")
                    if address_2_element is not None:
                        address2 = address_2_element.text
            if address == "Read more":
                address = address2

            print("address:", address)

            # description
            description = ""
            card_element = attraction_page.find(class_="IxAZL")
            if card_element is not None:
                description_element = card_element.find("span", attrs={"class": "JguWG"})
                if description_element is not None:
                    description = description_element.text.strip()
            print("description:", description)

            # timeCost
            timeCost = ""
            if card_element is not None:
                timeCost_element = card_element.find(class_="_c")
                if timeCost_element is not None:
                    timeCost_element = timeCost_element.find(class_="biGQs _P pZUbB KxBGd")
                    if timeCost_element is not None:
                        timeCost = timeCost_element.text.strip()
            print("timeCost:", timeCost)

            # opentime
            opentime = ""
            opentime_element = attraction_page.find(class_="EFKKt")
            if opentime_element is not None:
                opentime = opentime_element.text.strip()
            print("opentime:", opentime)

            # heat
            heat = 0
            heat_element = attraction.find(class_="biGQs _P pZUbB osNWb")
            if heat_element is not None:
                heat = heat_element.text
            print("heat:", heat)

            item = {
                "name": name,
                "label": label,
                "address": address,
                "description": description,
                "timeCost": timeCost,
                "rate": rate,
                "heat": heat,
                "opentime": opentime,
                "img_url": img_url
            }
            item_list.append(item)
    except:
        print("error, url:", url)

    write_rows_to_csv(item_list)
    
    if hasNextPage(page):
        if f"-oa{offset-30}" in url:
            next_page_url = url.replace(f"oa{offset-30}", f'oa{offset}')
        else:
            parts = url.split('-')
            next_page_url = '-'.join(parts[:-1]) + f'-oa{offset}-' + parts[-1].strip()
        #flip page
        next_page = parse_page(next_page_url)
        retrieve_data_from_page(next_page, next_page_url, offset+30)

def hasNextPage(page):
    nextPageButton_element = page.find(class_="xkSty")
    arrow_element = None
    if nextPageButton_element is not None:
        arrow_element = nextPageButton_element.find(class_= "BrOJk u j z _F wSSLS tIqAi unMkR")
    if arrow_element is None:
        return False
    return True

def write_rows_to_csv(item_list):
    df = pd.DataFrame(item_list)
    df.to_csv(FILE_NAME, mode='a', header=False, index=False) 
        
def main():
    columns = ['name', 'label', 'address', 'description', 'timeCost', 'rate', 'heat', 'opentime', 'img_url']
    df = pd.DataFrame(columns=columns)
    df.to_csv(FILE_NAME, mode='w', header=True, index=False) 
    URLs = [PARK_URL, MUSEUM_URL, LANDMARK_URL]
    for URL in URLs:
        page = parse_page(URL)
        offset = 30
        retrieve_data_from_page(page, URL, offset)

if __name__ == '__main__':
    main()
