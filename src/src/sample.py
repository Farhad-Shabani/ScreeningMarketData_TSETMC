import requests
import re

url = "http://tsetmc.com/tsev2/data/MarketWatchPlus.aspx"
r = requests.get(url)
ids = set(re.findall(r"\d{15,20}", r.text))
print(r.text)