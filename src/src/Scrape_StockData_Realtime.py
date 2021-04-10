import requests

def Realtime_StockData(Realtime_URL):
    Realtime_URL_Request = requests.get(Realtime_URL)
    Realtime_URL_Src = Realtime_URL_Request.content
    Split = str(Realtime_URL_Src).split(';')
    
    # To Scrape Orderbooks ---------------------------------------------------------------------------------------
    OrderBook = Split[2].split(',')
    Split = str(Realtime_URL_Src).split(';')
    OrderBook = Split[2].split(',')
    if len(OrderBook) > 1:
        OrderBook1 = OrderBook[0].split('@')
        OrderBook2 = OrderBook[1].split('@')
        OrderBook3 = OrderBook[2].split('@')
        StakeHolder = Split[4].split(',')
    else:
        OrderBook1 = OrderBook2 = OrderBook3 = [0,0,0]
    
    # print(OrderBook1)

    # To Scrape Realtime Market Parameters ------------------------------------------------------------------------
    TradeInfo = Split[0].split(',')
    TradeVolume = round(int(TradeInfo[9])/1000000,2)
    TradeValue = int(int(TradeInfo[10])/1000000)
    HighPrice = int(TradeInfo[6])
    LowPrice = int(TradeInfo[7])
    MarkPrice = int(TradeInfo[3])
    MarkPriceP = round((int(TradeInfo[3])/int(TradeInfo[5]))-1,4)
    LastPrice = int(TradeInfo[2])
    LastPriceP = round((int(TradeInfo[2])/int(TradeInfo[5]))-1,4)
    
    # To Calculate Average of Buy & Sell per capita ---------------------------------------------------------------
    if len(StakeHolder) > 5 and int(StakeHolder[5]) > 0:
        BuyCapita = int((int(StakeHolder[0])/int(StakeHolder[5]))*LastPrice/1000000)
    else: BuyCapita = 0
    if len(StakeHolder) > 8 and int(StakeHolder[8]) > 0:
        SellCapita = int((int(StakeHolder[3])/int(StakeHolder[8]))*LastPrice/1000000)
    else: SellCapita = 0
    if len(StakeHolder) > 0 and SellCapita > 0:
        CapitaRatio = round(BuyCapita/SellCapita,2) 
    else: CapitaRatio = 0
    
    # To make a list of realtime data of a stock ------------------------------------------------------------------- 
    Realtime_StockData = [TradeVolume, TradeValue, 
                          MarkPrice, MarkPriceP, LastPrice, LastPriceP,
                          int(OrderBook1[0]), int(OrderBook1[1]), int(OrderBook1[2]), 
                          int(OrderBook1[3]), int(OrderBook1[4]), int(OrderBook1[5]),
                          BuyCapita, SellCapita, CapitaRatio]
    
    return Realtime_StockData