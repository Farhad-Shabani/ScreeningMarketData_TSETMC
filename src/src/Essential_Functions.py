import re


def URL_Maker(ID):

    URL_Info_Data = 'http://www.tsetmc.com/loader.aspx?ParTree=151311&i=' + ID[0]
    URL_Realtime_Data = 'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=' + ID[0] + ID[1] 
    Stock_URLs = [URL_Info_Data, URL_Realtime_Data]

    return Stock_URLs


def Negative_Detector(i):
    
    return - float(re.findall(r'(\d+)',i)[0]) if i[0] == '(' else float(i)
