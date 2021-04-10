import requests
from bs4 import BeautifulSoup
from .Essential_Functions import Negative_Detector

def Scrape_Index():

    TSETMC_MainPage = 'http://www.tsetmc.com/Loader.aspx?ParTree=15'
    TSETMC_MainPage_Request = requests.get(TSETMC_MainPage)
    TSETMC_MainPage_Src = TSETMC_MainPage_Request.content
    TSETMC_MainPage_Soup = BeautifulSoup(TSETMC_MainPage_Src, 'lxml')

    # To Scrape Index of Bourse ----------------------------------------------------------------------------
    TseTmc1 = TSETMC_MainPage_Soup.find_all('tbody')[0].find_all('td')
    Index1 = float(''.join(TseTmc1[3].text.split()[0].split(',')))
    Index1C = Negative_Detector(''.join(TseTmc1[3].text.split()[1].split(','))) 
    Index2 = float(''.join(TseTmc1[5].text.split()[0].split(',')))
    Index2C = Negative_Detector(''.join(TseTmc1[5].text.split()[1].split(',')))   
    TotalValueBourse = int(int(''.join(TseTmc1[13].div['title'].split(',')))/1000000)

    # To Scrape Index of FaraBourse ------------------------------------------------------------------------
    TseTmc2 = TSETMC_MainPage_Soup.find_all('tbody')[25].find_all('td')
    Index3 = float(''.join(TseTmc2[3].text.split()[0].split(',')))
    Index3C = Negative_Detector(''.join(TseTmc2[3].text.split()[1].split(',')))
    TotalValueFaraBourse = int(int(''.join(TseTmc2[11].div['title'].split(',')))/1000000)

    Index = [Index1, Index1C, Index2, Index2C, Index3, Index3C, TotalValueBourse, TotalValueFaraBourse]
    
    return Index