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

for market in markets:

    letterlist=[]

    for letters in market :

        letterlist.append(letters)

    horof.append(letterlist)

    for letter in horof :

        if letter[-1]== "T" :

            horof.remove(letter)

            usdt.append(market)
usdt.remove("GMTTMN")
tmn.remove("DAITMN")
tmn.remove("USDTTMN")

xnxx_tmn_ask={}
xnxx_tmn_bid={}
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
    
    xnxx_tmn_ask.update({x:Ask_Order_out_of_list_TMN})
    xnxx_tmn_bid.update({x:Bid_Order_out_of_list_TMN})


    #print("In market", x, "Ask price is", Ask_Order_out_of_list_TMN, "Bid price is", Bid_Order_out_of_list_TMN)




xnxx_usdt_ask={}
xnxx_usdt_bid={}
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
        
    xnxx_usdt_ask.update({y:Ask_Order_out_of_list_USDT})
    xnxx_usdt_bid.update({y:Bid_Order_out_of_list_USDT})
xnxx_usdt_bid.pop("GMTTMN")
xnxx_usdt_ask.pop("GMTTMN")

    #print("In market", y, "Ask price is", Ask_Order_out_of_list_USDT, "Bid price is", Bid_Order_out_of_list_USDT)
print(len(xnxx_tmn_ask))
print(len(xnxx_tmn_bid))
print(len(xnxx_usdt_bid))
print(len(xnxx_usdt_ask))





#print(tmn)
