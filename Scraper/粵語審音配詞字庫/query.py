import requests
import csv
from bs4 import BeautifulSoup

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'Canton=1; Canlang=1',
            'Host': 'humanum.arts.cuhk.edu.hk',
            'Referer': 'https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/faq.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }



def query(code):
    result=[]
    url="https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q="+code
    r = requests.get(url, headers=headers)
    r.encoding='big5'
    html=r.text
    # print(html)
    bssoup = BeautifulSoup(html,"html.parser")
    form = bssoup.find("form")
    table = form.find("table")
    trs = table.find_all("tr")
    for i in range(1,len(trs)):
        tds = trs[i].find_all("td")
        syllable = tds[0].get_text()
        word = tds[5].get_text()
        result += [(syllable,word)]
    return result


# headers = ['Ranking','Freq.','Characters','Syllable','Words(Explanation) / Remarks']
# with open('RankingChartDetialed.csv','w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)

with open('RankingChartDetialed.csv') as f:
    f_csv = list(csv.reader(f))
    try:
        start = int(f_csv[-1][0])+1
    except Exception as e:
        start=1

end=1000

with open('RankingChart.csv') as f:
    f_csv = list(csv.reader(f))
    f_csv = f_csv[start:end]
    for row in f_csv:
        rank,freq,chrct,code = row
        # print(query(code))
        for item in query(code):
            syllable,word = item
            nrow = (rank,freq,chrct,syllable,word)
            with open('RankingChartDetialed.csv','a') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(nrow)


