import re
import requests
from bs4 import BeautifulSoup

def StockInfo(Info_URL):

    # To Calculate Capial -- BaseVol -- QTotTran5JAvg -- P/E -------------------------------------
    Info_URL_Request = requests.get(Info_URL)
    Info_URL_Src = Info_URL_Request.content
    Info_URL_Soup = BeautifulSoup(Info_URL_Src, 'lxml')
    MainPage = Info_URL_Soup.body.find_all('script')[1].string.split(',')
    Name = MainPage[12].split('=')[1][1:-1]
    EstimatedEPS = MainPage[9]
    EstimatedEPS = int(re.findall("\\d+",EstimatedEPS)[0])
    Capital = MainPage[10]
    Capital = int(int(re.findall("\\d+",Capital)[0])/1000)
    BaseVol = MainPage[8]
    BaseVol = int(re.findall("\\d+",BaseVol)[0])
    QTotTran5JAvg = int(MainPage[24].split('=')[1][1:-1])
    HighValid = MainPage[16]
    HighValid = int(re.findall("\\d+",HighValid)[0])
    LowValid = MainPage[17]
    LowValid = int(re.findall("\\d+",LowValid)[0])

    # To Make a list of stock's general information ------------------------------------------------ 
    StockInfo_Data = [Name, Capital, BaseVol, QTotTran5JAvg, HighValid, LowValid, EstimatedEPS]
    
    return StockInfo_Data