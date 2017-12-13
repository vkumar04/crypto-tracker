import requests
import time

url = 'https://bittrex.com/api/v1.1/public/getmarketsummaries'
r = requests.get(url)
response_dict = r.json()
results = response_dict['result']

def getData():
  for result in results:
    if result['MarketName'] == "BTC-LTC":
      ltc = result
    elif result['MarketName'] == "USDT-BTC":
      btc = result
    elif result['MarketName'] == "BTC-ETH":
      eth = result
  print (ltc['MarketName'], "last:", ltc['Last'])
  print (btc['MarketName'], "last:", btc['Last'])
  print (eth['MarketName'], "last:", eth['Last'])
  print ('\n')
while True:
  getData()
  time.sleep(30)