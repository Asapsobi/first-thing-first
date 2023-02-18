import requests
import decimal
import json
horof=[]
usdt=[]
    
response = requests.get("https://api.wallex.ir/v2/depth/all")

markets = response.json()["result"]
kir_to_nobitex_ba_on_apieshon=0

for market in markets:

    letterlist=[]

    for letters in market :

        letterlist.append(letters)

    horof.append(letterlist)

    for letter in horof :

        if letter[-1]== "T" :

            horof.remove(letter)

            usdt.append(market)

for y in usdt :
    ValueOfMarketsUSD = markets.get(y)
    


    BidpricesUsdt=[]
    AskpricesUsdt=[]
    axxUsdt = []
    bxxUsdt = []



    AskValueOfMarketsUSDT = ValueOfMarketsUSD["ask"]
    BidValueOfMarketsUSDT = ValueOfMarketsUSD["bid"]



        
    for ApriceUsdt in AskValueOfMarketsUSDT:
            AskpricesUsdt.append([float(ApriceUsdt["price"])])
        
    for AordersUsdt in AskpricesUsdt:
            axxUsdt.append(AordersUsdt)
            Ask_Order_out_of_list_USDT = min(axxUsdt)
    
    for BpriceUsdt in BidValueOfMarketsUSDT:
            BidpricesUsdt.append([float(BpriceUsdt["price"])])
    
    for BordersUsdt in BidpricesUsdt:
            bxxUsdt.append(BordersUsdt)
            Bid_Order_out_of_list_USDT = (max(bxxUsdt))
        
            
    print("In market", y, "Ask price is", Ask_Order_out_of_list_USDT, "Bid price is", Bid_Order_out_of_list_USDT)



