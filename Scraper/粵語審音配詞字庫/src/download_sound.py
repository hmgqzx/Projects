# http://59.80.44.47/humanum.arts.cuhk.edu.hk/Lexis/lexi-can/sound/dei6.wav

import requests
import os.path
import csv

src = 'data/7072/RankingChartDetialed-7072.csv'

def download(syll):
    file_path="./media/7072/"+syll+"_by_can4_ging1_ying1"+'.wav'
    if os.path.isfile(file_path):
        # print("exist!")
        pass
    else:
        url='http://59.80.44.47/humanum.arts.cuhk.edu.hk/Lexis/lexi-can/sound/' + syll + '.wav'
        r = requests.get(url, allow_redirects=True)
        open(file_path, 'wb').write(r.content)

with open(src) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        syll=row[3]
        download(syll)