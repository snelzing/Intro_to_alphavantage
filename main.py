import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv('apikey.txt')
api_key = os.getenv('API_KEY')
filename = "alphavantage.csv"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=60min&apikey={api_key}&outputsize=compact&datatype=csv'
r = requests.get(url)

print(r.text)

with open(filename,'w') as fd:
    fd.write(r.text)
