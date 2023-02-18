import requests
import decimal
import json
horof=[]
tmn=[]
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

        elif letter[-1]== "N" :

            horof.remove(letter)
        
            tmn.append(market)

    for x in tmn :
        ValueOfMarkets = markets.get(x)

    AskValueOfMarkets = ValueOfMarkets["ask"]
    BidValueOfMarkets = ValueOfMarkets["bid"]
    
    Bidprices = []
    Askprices = []
    
    axx = []
    bxx = []
    
    for Aprice in AskValueOfMarkets:
        Askprices.append([float(Aprice["price"])])
        
    for Aorders in Askprices:
        axx.append(Aorders)
        Ask_Order_out_of_list = min(axx)
    
    for Bprice in BidValueOfMarkets:
        Bidprices.append([float(Bprice["price"])])
    
    for Borders in Bidprices:
        bxx.append(Borders)
        Bid_Order_out_of_list = (max(bxx))
            
    print("In market", x, "Ask price is", Ask_Order_out_of_list, "Bid price is", Bid_Order_out_of_list)


tmn.remove("DAITMN")
tmn.remove("USDTTMN")
#print(tmn)
