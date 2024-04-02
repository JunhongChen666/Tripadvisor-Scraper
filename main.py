import requests
from bs4 import BeautifulSoup

def scrap():
    url = "https://www.xiaohongshu.com/search_result?keyword=chloe&source=web_explore_feed&search_type=user"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        "Accept": "*/*",
        "Accept-Encoding": "*",
        'Accept-Language': 'en-US, en;q=0.5',
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    text = None
    if response.status_code == 200:
        text = response.text
        print("text",text)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # parse html
    soup = BeautifulSoup(text, "html.parser")
    # Find all the hotel elements in the HTML document
    # print(soup.findAll(attrs={"class": "user-list-item"}))


def main():
    scrap()

main()