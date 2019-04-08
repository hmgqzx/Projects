import requests
import csv
from bs4 import BeautifulSoup
import re

def get(s):
    r = requests.get('http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/faq.php?s='+s)
    r.encoding='big5'
    html=r.text
    # print(html)
    bssoup = BeautifulSoup(html,"html.parser")
    table = bssoup.find("table")
    items = table.find_all("td")
    n=len(items)
    for i in range(0,n,3):
        rank=items[i].string
        freq=items[i+1].string
        chrct=items[i+2].string
        href=items[i+2].a.get('href')
        code=re.search('%.*',href).group()
        row=(rank,freq,chrct,code)
        # print(row)
        with open('RankingChart.csv','a') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(row)

headers = ['Ranking','Freq.','Characters','Code']
with open('RankingChart.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

for s in range(1,7072,500):
    get(str(s))