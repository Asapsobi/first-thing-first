import requests
import decimal
import json
import time
import os


def mamd() :
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
        
    USDTTMN_data=markets.get("USDTTMN")


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

    for z in USDTTMN_data :
        ValueOfMarketsUSDTTMN = USDTTMN_data.get(z)
        
        AskValueOfMarketsUSDTTMN = USDTTMN_data["ask"]
        BidValueOfMarketsUSDTTMN = USDTTMN_data["bid"]

        BidpricesUSDTTmn = []
        AskpricesUSDTTmn = []

        axxUSDTTmn = []
        bxxUSDTTmn = []
        for ApriceUSDTTmn in AskValueOfMarketsUSDTTMN:
            AskpricesUSDTTmn.append([float(ApriceUSDTTmn["price"])])
            
        for AordersUSDTTmn in AskpricesUSDTTmn:
            axxUSDTTmn.append(AordersUSDTTmn)
            Ask_Order_out_of_list_USDTTMN = min(axxUSDTTmn)
        
        for BpriceUSDTTmn in BidValueOfMarketsUSDTTMN:
            BidpricesUSDTTmn.append([float(BpriceUSDTTmn["price"])])
        
        for BordersUSDTTmn in BidpricesUSDTTmn:
            bxxUSDTTmn.append(BordersUSDTTmn)
            Bid_Order_out_of_list_USDTTMN = (max(bxxUSDTTmn))
        
        for new_Bid_Order_out_of_list_USDTTMN in Bid_Order_out_of_list_USDTTMN :
            Bid_Order_out_of_list_USDTTMN=float(new_Bid_Order_out_of_list_USDTTMN)

        for new_ask_Order_out_of_list_USDTTMN in Ask_Order_out_of_list_USDTTMN :
            Ask_Order_out_of_list_USDTTMN=float(new_ask_Order_out_of_list_USDTTMN)


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
        
        for new_Bid_Order_out_of_list_TMN in Bid_Order_out_of_list_TMN :
            Bid_Order_out_of_list_TMN=float(new_Bid_Order_out_of_list_TMN)

        for new_Ask_Order_out_of_list_TMN in Ask_Order_out_of_list_TMN :
            Ask_Order_out_of_list_TMN=float (new_Ask_Order_out_of_list_TMN)

        
        xnxx_tmn_ask.update({x:Ask_Order_out_of_list_TMN})
        xnxx_tmn_bid.update({x:Bid_Order_out_of_list_TMN})






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

        for new_Bid_Order_out_of_list_USDT in Bid_Order_out_of_list_USDT :
            Bid_Order_out_of_list_USDT=float(new_Bid_Order_out_of_list_USDT)

        for new_Ask_Order_out_of_list_USDT in Ask_Order_out_of_list_USDT :
            Ask_Order_out_of_list_USDT=float(new_Ask_Order_out_of_list_USDT)

        xnxx_usdt_ask.update({y:Ask_Order_out_of_list_USDT})
        xnxx_usdt_bid.update({y:Bid_Order_out_of_list_USDT})


    xnxx_usdt_bid.pop("GMTTMN")
    xnxx_usdt_ask.pop("GMTTMN")

    xnxx_tmn_ask_list=list(xnxx_tmn_bid.items())
    xnxx_tmn_bid_list=list(xnxx_tmn_bid.items())
    xnxx_usdt_ask_list=list(xnxx_usdt_ask.items())
    xnxx_usdt_bid_list=list(xnxx_usdt_bid.items())



    UsdtAskPrices=[]
    TmnBidPrices=[]
    UsdtBidPrices=[]
    TmnAskPrices=[]

    UsdtAskMarkets=[]
    UsdtBidMarkets=[]
    TmnBidMarkets=[]
    TmnAskMarkets=[]




    while kir_to_nobitex_ba_on_apieshon < 1 :


        for xnxx_tmn_ask_list_values in xnxx_tmn_ask_list :
            
            xnxx_tmn_ask_list_price = float((xnxx_tmn_ask_list_values)[1])

            xnxx_tmn_ask_list_markets =xnxx_tmn_ask_list_values[0]

            xnxx_tmn_ask_list_price_usdt = xnxx_tmn_ask_list_price/Bid_Order_out_of_list_USDTTMN

            TmnAskPrices.append(xnxx_tmn_ask_list_price_usdt)
            TmnAskMarkets.append(xnxx_tmn_ask_list_markets)


        for xnxx_tmn_bid_list_values in xnxx_tmn_bid_list :

            xnxx_tmn_bid_list_price =float ((xnxx_tmn_bid_list_values)[1])
    
            xnxx_tmn_bid_list_markets = xnxx_tmn_bid_list_values[0]

            xnxx_tmn_bid_list_price_usdt = xnxx_tmn_bid_list_price/Ask_Order_out_of_list_USDTTMN

            TmnBidPrices.append(xnxx_tmn_bid_list_price_usdt)
            TmnBidMarkets.append(xnxx_tmn_bid_list_markets)




        for xnxx_usdt_bid_list_values in xnxx_usdt_bid_list :

            xnxx_usdt_bid_list_price = float((xnxx_usdt_bid_list_values)[1])

            xnxx_usdt_bid_list_markets = xnxx_usdt_bid_list_values[0]

            UsdtBidPrices.append(xnxx_usdt_bid_list_price)
            UsdtBidMarkets.append(xnxx_usdt_bid_list_markets)


        
        for xnxx_usdt_ask_list_values in xnxx_usdt_ask_list :

            xnxx_usdt_ask_list_price =float ((xnxx_usdt_ask_list_values)[1])

            xnxx_usdt_ask_list_markets = xnxx_usdt_ask_list_values[0]

            UsdtAskPrices.append(xnxx_usdt_ask_list_price)
            UsdtAskMarkets.append(xnxx_usdt_ask_list_markets)



        while kir_to_nobitex_ba_on_apieshon < 45 :
            
            if UsdtAskPrices[kir_to_nobitex_ba_on_apieshon] < TmnBidPrices[kir_to_nobitex_ba_on_apieshon] :
                print("you can buy at price : " , UsdtAskPrices[kir_to_nobitex_ba_on_apieshon] , "in market :" , UsdtAskMarkets[kir_to_nobitex_ba_on_apieshon] , "and sell in price :" , TmnBidPrices[kir_to_nobitex_ba_on_apieshon] , "at market" , TmnBidMarkets[kir_to_nobitex_ba_on_apieshon] )
            elif UsdtBidPrices[kir_to_nobitex_ba_on_apieshon] > TmnAskPrices[kir_to_nobitex_ba_on_apieshon] :
                print("you can buy at price : " , float (UsdtBidPrices[kir_to_nobitex_ba_on_apieshon]) , "in market :" , TmnAskMarkets[kir_to_nobitex_ba_on_apieshon] , "and sell in price :" , float (UsdtBidPrices[kir_to_nobitex_ba_on_apieshon]) , "at market" , TmnAskMarkets[kir_to_nobitex_ba_on_apieshon] )
            else : 
                print("in" , TmnAskMarkets[kir_to_nobitex_ba_on_apieshon] , "and" ,UsdtAskMarkets[kir_to_nobitex_ba_on_apieshon] , "isn't any arbitrage chance")
            #print(UsdtAskPrices[kir_to_nobitex_ba_on_apieshon])
            
            kir_to_nobitex_ba_on_apieshon=kir_to_nobitex_ba_on_apieshon+1
            

while 1>0 :
    mamd()    
    time.sleep(1)
    os.system('cls')
