import requests
import csv
from bs4 import BeautifulSoup
import re

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

dest = 'data/7072/RankingChartDetialed-7072.csv'

def clean(raw):
    return re.sub(r'\[\d{1,2}\.\.\]',', ',raw)

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
        raw_word = tds[5].get_text()
        word = clean(raw_word)
        result += [(syllable,word)]
    return result


# headers = ['Ranking','Freq.','Characters','Syllable','Words(Explanation) / Remarks']
# with open(dest,'w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)

def main():
    # with open(dest) as f:
    #     f_csv = list(csv.reader(f))
    #     try:
    #         start = int(f_csv[-1][0])+1
    #     except Exception as e:
    #         start=1
    # end=7073

    with open('data/RankingChart.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        f_csv = list(f_csv)
        # f_csv = f_csv[start:end]
        f_csv = f_csv[6740:6746]
        for row in f_csv:
            print(row)
            rank,freq,chrct,code = row
            # print(query(code))
            for item in query(code):
                syllable,word = item
                nrow = (rank,freq,chrct,syllable,word)
                with open(dest,'a') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(nrow)


main()

