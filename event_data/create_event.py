import pandas as pd
import time
ITEM_FILE = "item_data.csv"
OUTPUT_FILE = "event_data.csv"
def get_genres(input_file):
    df = pd.read_csv(input_file)  
    types_set = set()
    # Iterate over each row to extract types
    for index, row in df.iterrows():
        types_str = row['GENRES']
        if pd.isna(types_str):
            print(f"Skipping row {index} with NaN types.")
            continue
        # Split the types string by '|' delimiter and add to the set
        types_list = types_str.split('|')
        for t in types_list:
            types_set.add(t)
    print(types_set)
get_genres(ITEM_FILE)

columns = ['USER_ID', 'ITEM_ID', 'TIMESTAMP', 'EVENT_TYPE']
df = pd.DataFrame(columns=columns)
df.to_csv(OUTPUT_FILE, mode='w', header=True, index=False) 

def generate_events(input_file, output_file):
    rdf = pd.read_csv(input_file)  
    types_set = set()
    # Iterate over each row to extract types
    for index, row in rdf.iterrows():
        types_str = row['GENRES']
        if pd.isna(types_str):
            print(f"Skipping row {index} with NaN types.")
            continue
        # Split the types string by '|' delimiter and add to the set
        data_list = []
        write_data(index+1, types_str, data_list)
        if len(data_list)>0:
            df = pd.DataFrame(data_list)
            df.to_csv(OUTPUT_FILE, mode='a', header=False, index=False, encoding='utf-8') 

def write_data(item_id, types_str, data_list):
    userId = None
    if "Neighbourhoods" in types_str or "Points of Interest & Landmarks" in types_str:
        userId = 1
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Ski & Snowboard Areas" in types_str or "Observation Decks & Towers" in types_str:
        userId = 2
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Mysterious Sites" in types_str or "Lessons & Workshops" in types_str:
        userId = 3
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Theatres" in types_str or "Lighthouses" in types_str:
        userId = 4
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Farms" in types_str or "Islands" in types_str:
        userId = 5
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Monuments & Statues" in types_str or "Forests" in types_str:
        userId = 6
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Arenas & Stadiums" in types_str or "Children's Museums" in types_str:
        userId = 7
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Nature & Wildlife Areas" in types_str or "Geologic Formations" in types_str:
        userId = 8
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Caverns & Caves" in types_str or "Churches & Cathedrals" in types_str:
        userId = 9
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Biking Trails" in types_str or "Civic Centres" in types_str:
        userId = 10
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Antique Shops" in types_str or "Science Museums" in types_str:
        userId = 11
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Waterfalls" in types_str or "Cross-country Ski Areas" in types_str:
        userId = 12
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Beaches" in types_str or "Military Bases & Facilities" in types_str:
        userId = 13
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Architectural Buildings" in types_str or "Theatre & Performances" in types_str:
        userId = 14
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Paint & Pottery Studios" in types_str or "Military Museums" in types_str:
        userId = 15
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Educational sites" in types_str or "Gardens" in types_str:
        userId = 16
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Battlefields" in types_str or "Cemeteries" in types_str:
        userId = 17
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Parks" in types_str or "Marinas" in types_str:
        userId = 18
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Aquariums" in types_str or "Speciality & Gift Shops" in types_str:
        userId = 19
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Mountains" in types_str or "Zoos" in types_str:
        userId = 20
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Bodies of Water" in types_str or "Universities & Schools" in types_str:
        userId = 21
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "National Parks" in types_str or "Government Buildings" in types_str:
        userId = 22
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Speciality Museums" in types_str or "Public Transportation Systems" in types_str:
        userId = 23
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Hiking Trails" in types_str or "Convention Centres" in types_str:
        userId = 24
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Spas" in types_str or "Historic Walking Areas" in types_str:
        userId = 25
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Observatories & Planetariums" in types_str or "Lookouts" in types_str:
        userId = 26
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "State Parks" in types_str or "Bike Tours" in types_str:
        userId = 27
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Sports Complexes" in types_str or "Libraries" in types_str:
        userId = 28
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Castles" in types_str or "Playgrounds" in types_str:
        userId = 29
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)
    if "Scenic Walking Areas" in types_str or "Fountains" in types_str:
        userId = 30
        data = {"USER_ID": userId, "ITEM_ID":item_id, "TIMESTAMP": int(time.time()), "EVENT_TYPE": "CLICK"}
        data_list.append(data)

generate_events(ITEM_FILE, OUTPUT_FILE)