import pandas as pd

FILE_NAME = "./user_data.csv"

columns = ['USER_ID', 'AGE']
df = pd.DataFrame(columns=columns)
df.to_csv(FILE_NAME, mode='w', header=True, index=False) 

data = [
  {"USER_ID": 1, "AGE": 25},
  {"USER_ID": 2, "AGE": 30},
  {"USER_ID": 3, "AGE": 22},
  {"USER_ID": 4, "AGE": 40},
  {"USER_ID": 5, "AGE": 28},
  {"USER_ID": 6, "AGE": 35},
  {"USER_ID": 7, "AGE": 27},
  {"USER_ID": 8, "AGE": 32},
  {"USER_ID": 9, "AGE": 26},
  {"USER_ID": 10, "AGE": 29},
  {"USER_ID": 11, "AGE": 31},
  {"USER_ID": 12, "AGE": 24},
  {"USER_ID": 13, "AGE": 33},
  {"USER_ID": 14, "AGE": 38},
  {"USER_ID": 15, "AGE": 23},
  {"USER_ID": 16, "AGE": 37},
  {"USER_ID": 17, "AGE": 36},
  {"USER_ID": 18, "AGE": 21},
  {"USER_ID": 19, "AGE": 34},
  {"USER_ID": 20, "AGE": 39},
  {"USER_ID": 21, "AGE": 45},
  {"USER_ID": 22, "AGE": 42},
  {"USER_ID": 23, "AGE": 41},
  {"USER_ID": 24, "AGE": 43},
  {"USER_ID": 25, "AGE": 48},
  {"USER_ID": 26, "AGE": 47},
  {"USER_ID": 27, "AGE": 44},
  {"USER_ID": 28, "AGE": 46},
  {"USER_ID": 29, "AGE": 50},
  {"USER_ID": 30, "AGE": 55},
  {"USER_ID": 31, "AGE": 45},
  {"USER_ID": 32, "AGE": 42},
  {"USER_ID": 33, "AGE": 41},
  {"USER_ID": 34, "AGE": 43},
  {"USER_ID": 35, "AGE": 48},
  {"USER_ID": 36, "AGE": 47},
  {"USER_ID": 37, "AGE": 44},
  {"USER_ID": 38, "AGE": 46},
  {"USER_ID": 39, "AGE": 50},
  {"USER_ID": 40, "AGE": 39},
  {"USER_ID": 41, "AGE": 45},
  {"USER_ID": 42, "AGE": 42},
  {"USER_ID": 43, "AGE": 41},
  {"USER_ID": 44, "AGE": 43},
  {"USER_ID": 45, "AGE": 48},
  {"USER_ID": 46, "AGE": 47},
  {"USER_ID": 47, "AGE": 44},
  {"USER_ID": 48, "AGE": 46},
  {"USER_ID": 49, "AGE": 50},
  {"USER_ID": 50, "AGE": 55}
]
df = pd.DataFrame(data)
df.to_csv(FILE_NAME, mode='a', header=False, index=False) 
