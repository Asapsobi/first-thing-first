import jsons
import requests

api_url = "https://api.nobitex.ir/v2/orderbook/all"
data = requests.get(api_url).json()

del data['status']
currencies = list(data.keys())
print(currencies)
# loop through each main key
for currency in data:
    # check if there are bids and asks for this currency
    if not data[currency]['bids'] or not data[currency]['asks']:
        continue

    # get the max bids by finding the first value from the bids list
    max_bid = data[currency]["bids"][0][0]

    # get the min asks by finding the first value from the asks list
    min_ask = data[currency]["asks"][0][0]

    # print the required output
    print(f"{currency}: For max bids: {max_bid}, for min asks: {min_ask}") 
