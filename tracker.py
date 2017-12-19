import requests
import time

def getData():
  url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,XLM&tsyms=USD'
  r = requests.get(url)
  response_dict = r.json()
  for crypto in response_dict:
    print(crypto, response_dict[crypto])
    print('\n')

while True:
  getData()
  time.sleep(5)

