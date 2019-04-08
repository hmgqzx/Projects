import csv

note_id = 0

src='data/7072/RankingChartDetialed-7072.csv'
dest='data/7072/RankingChartDetialed-7072-Anki.csv'

headers = ['Id','Ranking','Freq.','Characters','Syllable','Words(Explanation) / Remarks','Sound']
with open(dest,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

with open(src) as f:
    fr_csv = csv.reader(f)
    headers = next(fr_csv)
    for row in fr_csv:
        note_id +=1
        rank,freq,chrct,syllable,word = row
        sound = "[sound:"+syllable+"_by_can4_ging1_ying1"+".wav]"
        with open(dest,'a') as fw:
            fw_csv = csv.writer(fw)
            row = (note_id,rank,freq,chrct,syllable,word,sound)
            fw_csv.writerow(row)
