import requests
import pandas as pd

url = 'https://api.spacexdata.com/v4/launches'

df = pd.read_json(url)

# print(df.columns)
print(df.dtypes)


# response = requests.get()
# data = response.json()

# df = pd.DataFrame(data)
# print(df.head())
