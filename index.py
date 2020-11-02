import requests
btc = requests.get("http://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD")
btc_json = btc.json()
dolar = requests.get("https://hamyarandroid.com/api?t=currency")
dolar_json = dolar.json()
print(int(btc_json['high'] * dolar_json['list'][0]['price']))