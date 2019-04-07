import requests
import csv
from bs4 import BeautifulSoup


def get(s):
    r = requests.get('http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/faq.php?s='+s)
    r.encoding='big5'
    html=r.text

    bssoup = BeautifulSoup(html,"html.parser")
    table = bssoup.find("table")
    items = table.find_all("td")
    n=len(items)
    for i in range(0,n,3):
        rank=items[i].string
        freq=items[i+1].string
        chrct=items[i+2].string
        row=(rank,freq,chrct)
        with open('RankingChart.csv','a') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(row)

headers = ['Ranking','Freq.','Characters']
with open('RankingChart.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

for s in range(1,7072,500):
    get(str(s))