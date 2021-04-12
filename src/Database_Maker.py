"""
    These functions take a list of stocks' ID and return:
       1. A list with stocks info + their realtime trading data 
       2. Sorted data based on different criteria
"""

from .Essential_Functions import URL_Maker, Negative_Detector
from .Scrape_StockInfo import StockInfo
from .Scrape_StockData_Realtime import Realtime_StockData


def Database_Maker(Stock):
      
    Stocks_Database = list()

    for i in Stock:
        StocksInfo = list()
        Realtime_StocksData = list()
        Stock_URLs = URL_Maker(Stock[i])
        StocksInfo = StockInfo(Stock_URLs[0])
        Realtime_StocksData = Realtime_StockData(Stock_URLs[1])
        
    # To calculate other desired ratios ----------------------------------------------------------------------------
        if StocksInfo[3] > 0: TradeRatio = round(Realtime_StocksData[0]/StocksInfo[3] *1000000,3)
        else: TradeRatio = 0
        
        PtoE = round(Realtime_StocksData[2] / StocksInfo[6],2)
        
        Realtime_StocksData.append(TradeRatio)
        Realtime_StocksData.append(PtoE)
    
    # To make a list of data from desired stocks -------------------------------------------------------------------
    # Name                 # 0
    # Capital              # 1
    # BaseVol              # 2
    # QTotTran5JAvg        # 3
    # HighValid            # 4 
    # LowValid             # 5 
    # EstimatedEPS         # 6
    # TradeVolume          # 7
    # TradeValue           # 8
    # MarkPrice            # 9
    # MarkPriceP           # 10
    # LastPrice            # 11
    # LastPriceP           # 12
    # int(OrderBook1[0])   # 13
    # int(OrderBook1[1])   # 14
    # int(OrderBook1[2])   # 15
    # int(OrderBook1[3])   # 16
    # int(OrderBook1[4])   # 17
    # int(OrderBook1[5])   # 18
    # BuyCapita            # 19
    # SellCapita           # 20
    # CapitaRatio          # 21
    # TradeRatio           # 22
    # PtoE                 # 23
        
        print(StocksInfo + Realtime_StocksData)
        Stocks_Database.append(StocksInfo + Realtime_StocksData)

    return Stocks_Database


def Sorted_Database(Database, Stocks):

    # To Count Number of Stock in Buy and Sell Queues --------------------------------------------------------------
    HighCount, PositiveCount, NegativeCount, LowCount = 0, 0, 0, 0
    SumBuyQueueValue, SumSellQueueValue, AveBuyCapitaSort, AveSellCapitaSort = 0, 0, 0, 0
    BuyQueueRow = list()
    BuyQueue = list()
    SellQueueRow = list() 
    SellQueue = list()
   
    
    for i in Database:  
        if i[11] == i[4]:
            BuyQueueRow = []
            HighCount += 1
            BuyQueueValue = int(i[11] * i[14] / 1000000)
            BuyQueueRow.append(i[0])                     # 0
            BuyQueueRow.append(i[11])                    # 1
            BuyQueueRow.append(round(i[14]/1000000,1))   # 2
            BuyQueueRow.append(BuyQueueValue)            # 3
            BuyQueue.append(BuyQueueRow)
            SumBuyQueueValue += BuyQueueValue

        elif i[11] != i[4] and i[12] >= 0: PositiveCount +=1
        elif i[11] != i[5] and i[12] < 0: NegativeCount +=1
        elif i[11] == i[5]:
            LowCount += 1
            SellQueueValue = int(i[11] * i[17] / 1000000)
            SellQueueRow.append(i[0])                     # 0
            SellQueueRow.append(i[11])                    # 1
            SellQueueRow.append(round(i[17]/1000000,1))   # 2
            SellQueueRow.append(SellQueueValue)           # 3
            SellQueue.append(SellQueueRow)
            SellQueueRow = []
            SumSellQueueValue += SellQueueValue

        AveBuyCapitaSort  += i[19] 
        AveSellCapitaSort += i[20] 
    
    AveBuyCapitaSort = round(AveBuyCapitaSort / len(Database), 1)
    AveSellCapitaSort = round(AveSellCapitaSort / len(Database), 1)

    # AveSellCapitaSort = round(list(map(sum, zip(*Database)))[20] / len(Database), 1)
    CountCache = [HighCount,PositiveCount,NegativeCount,LowCount, SumBuyQueueValue, SumSellQueueValue, AveBuyCapitaSort, AveSellCapitaSort]  

    # Sorting -------------------------------------------------------------------------------------------------------

    VolRatioSort = sorted(Database,key = lambda x: x[22],reverse=True)  
    ValueSort = sorted(Database,key = lambda x: x[8],reverse=True)
    BuyCapitaSort = sorted(Database,key = lambda x: x[-5],reverse=True)
    SellCapitaSort = sorted(Database,key = lambda x: x[-4],reverse=True)  
    BuyQueue.sort(key = lambda x: x[3], reverse=True) 
    SellQueue.sort(key = lambda x: x[3], reverse=True) 

    return CountCache, VolRatioSort, ValueSort, BuyCapitaSort, SellCapitaSort, BuyQueue, SellQueue

