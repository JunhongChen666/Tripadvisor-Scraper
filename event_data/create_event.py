import pandas as pd
import time
import random

PROB = 0.3
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
    return types_set

columns = ['USER_ID', 'ITEM_ID', 'TIMESTAMP', 'EVENT_TYPE']
df = pd.DataFrame(columns=columns)
df.to_csv(OUTPUT_FILE, mode='w', header=True, index=False) 

def generate_events(input_file, output_file):

    type_list = list(get_genres(ITEM_FILE))
    l_len = len(type_list)
    print(l_len)
    print(type_list)
    # Iterate over each row to extract types
    for i in range(1, 51):
        type1 = type_list[i % l_len]
        type2 = type_list[(i+10)%l_len]
        type3 = type_list[(i+20)%l_len]
        type4 = type_list[(i+30)%l_len]
        rdf = pd.read_csv(input_file)  
        print("user:", i, "type1: ", type1, "type2: ", type2, "type3: ", type3, "type4: ", type4)
        for index, row in rdf.iterrows():
            types_str = row['GENRES']
            if pd.isna(types_str):
                print(f"Skipping row {index} with NaN types.")
                continue
            # Split the types string by '|' delimiter and add to the set
            types = types_str.split("|")
            data_list=[]
            if type1 in types and random.random()>PROB:
                data_list.append({"USER_ID": i, "ITEM_ID": index+1, "TIMESTAMPE":int(time.time()), "EVENT_TYPE": "click"})
            if type2 in types and random.random()>PROB:
                data_list.append({"USER_ID": i, "ITEM_ID": index+1, "TIMESTAMPE":int(time.time()), "EVENT_TYPE": "click"})
            if type3 in types and random.random()>PROB:
                data_list.append({"USER_ID": i, "ITEM_ID": index+1, "TIMESTAMPE":int(time.time()), "EVENT_TYPE": "click"})
            if type4 in types and random.random()>PROB:
                data_list.append({"USER_ID": i, "ITEM_ID": index+1, "TIMESTAMPE":int(time.time()), "EVENT_TYPE": "click"})

            if len(data_list)>0:
                df = pd.DataFrame(data_list)
                df.to_csv(output_file, mode='a', header=False, index=False, encoding='utf-8') 


generate_events(ITEM_FILE, OUTPUT_FILE)