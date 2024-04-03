import pandas as pd

F1 = "Toronto.csv"
F2 = "Vancouver.csv"
F3 = "Quebec City.csv"
F4=  "Washington DC.csv"
F5 = "New York.csv"
OUTPUT_FILE = "item_data.csv"

def read_and_write_csv(input_file, output_file):
    # Read the input CSV file into a pandas DataFrame
    df = pd.read_csv(input_file, encoding="ISO-8859-1")
    
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


read_and_write_csv(F1, OUTPUT_FILE)
read_and_write_csv(F2, OUTPUT_FILE)
read_and_write_csv(F3, OUTPUT_FILE)
read_and_write_csv(F4, OUTPUT_FILE)
# read_and_write_csv(F5, OUTPUT_FILE)
