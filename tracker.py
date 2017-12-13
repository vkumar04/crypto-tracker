import requests
import time

url = 'https://bittrex.com/api/v1.1/public/getmarketsummaries'
r = requests.get(url)
response_dict = r.json()
results = response_dict['result']

def getData():
  for result in results:
    if result['MarketName'] == "USDT-LTC":
      ltc = result
    elif result['MarketName'] == "USDT-BTC":
      btc = result
    elif result['MarketName'] == "USDT-ETH":
      eth = result
  print (ltc['MarketName'], ltc['Last'])
  print (btc['MarketName'], btc['Last'])
  print (eth['MarketName'], eth['Last'])
while True:
  getData()
  time.sleep(30)