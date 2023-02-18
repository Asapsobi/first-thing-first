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
        if letter[-1]== "N" :

            horof.remove(letter)
        
            tmn.append(market)
tmn.remove("DAITMN")
tmn.remove("USDTTMN")
for x in tmn :
    ValueOfMarketsTMN = markets.get(x)
    

    AskValueOfMarketsTMN = ValueOfMarketsTMN["ask"]
    BidValueOfMarketsTMN = ValueOfMarketsTMN["bid"]

    BidpricesTmn = []
    AskpricesTmn = []

    axxTmn = []
    bxxTmn = []
    
    for ApriceTmn in AskValueOfMarketsTMN:
        AskpricesTmn.append([float(ApriceTmn["price"])])
        
    for AordersTmn in AskpricesTmn:
        axxTmn.append(AordersTmn)
        Ask_Order_out_of_list_TMN = min(axxTmn)
    
    for BpriceTmn in BidValueOfMarketsTMN:
        BidpricesTmn.append([float(BpriceTmn["price"])])
    
    for BordersTmn in BidpricesTmn:
        bxxTmn.append(BordersTmn)
        Bid_Order_out_of_list_TMN = (max(bxxTmn))

########################################################################################
       
    print("In market", x, "Ask price is", Ask_Order_out_of_list_TMN, "Bid price is", Bid_Order_out_of_list_TMN)





#print(tmn)
