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
        ValueOfMarketsTMN = markets.get(x)
    for y in usdt :
        ValueOfMarketsUSDT  = markets.get(y)

    AskValueOfMarketsTMN = ValueOfMarketsTMN["ask"]
    BidValueOfMarketsTMN = ValueOfMarketsTMN["bid"]
    AskValueOfMarketsUSDT = ValueOfMarketsUSDT["ask"]
    BidValueOfMarketsUSDT = ValueOfMarketsUSDT["bid"]

    BidpricesTmn = []
    AskpricesTmn = []
    BidpricesUsdt=[]
    AskpricesUsdt=[]

    axxTmn = []
    bxxTmn = []
    axxUsdt = []
    bxxUsdt = []
    
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
        
            
    print("In market", x, "Ask price is", Ask_Order_out_of_list_TMN, "Bid price is", Ask_Order_out_of_list_TMN)
    print("In market", y, "Ask price is", Ask_Order_out_of_list_USDT, "Bid price is", Ask_Order_out_of_list_USDT)



tmn.remove("DAITMN")
tmn.remove("USDTTMN")
#print(tmn)
