# http://59.80.44.47/humanum.arts.cuhk.edu.hk/Lexis/lexi-can/sound/dei6.wav

import requests
import os.path
import csv

def download(syll):
    url='http://59.80.44.47/humanum.arts.cuhk.edu.hk/Lexis/lexi-can/sound/' + syll + '.wav'
    r = requests.get(url, allow_redirects=True)
    file_path="./media/"+syll+"_by_can4_ging1_ying1"+'.wav'
    if os.path.isfile(file_path):
        # print("exist!")
        pass
    else:
        open(file_path, 'wb').write(r.content)

with open('RankingChartDetialed.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        syll=row[3]
        download(syll)