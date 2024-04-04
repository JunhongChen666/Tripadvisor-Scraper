import pandas as pd

F1 = "Toronto.csv"
F2 = "Vancouver.csv"
F3 = "Quebec City.csv"
F4=  "Washington DC.csv"
F5 = "New York.csv"
TMP_FILE = "tmp.csv"
OUTPUF_FILE= "item_data.csv"

def read_and_write_csv(input_file, output_file):
    # Read the input CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Process the data
    for index, row in df.iterrows():
        # Print the original row
        print(row)
        
        # Replace " with \" and \ with \\
        description = row['description']
        print(description)
        if not pd.isna(description):
            description = description.replace('\\', '\\\\').replace('"', '\\"')
            description = '"' + description + '"'
        df.at[index, 'description'] = description
    # Write the processed DataFrame to the output CSV file
    df[['labels', 'description']].to_csv(output_file, mode='a', header=False, index=False) 


columns = ['GENRES', 'DESCRIPTION']
df = pd.DataFrame(columns=columns)
df.to_csv(TMP_FILE, mode='w', header=True, index=False) 
read_and_write_csv(F1, TMP_FILE)
read_and_write_csv(F2, TMP_FILE)
read_and_write_csv(F3, TMP_FILE)
read_and_write_csv(F4, TMP_FILE)
read_and_write_csv(F5, TMP_FILE)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(TMP_FILE)

# Generate ITEM_ID values, you can replace this with your own logic for generating IDs
item_ids = range(1, len(df) + 1)

# Add the ITEM_ID column to the DataFrame
df.insert(0, 'ITEM_ID', range(1, len(df) + 1))

# Write the DataFrame back to a CSV file
df.to_csv(OUTPUF_FILE, index=False)



