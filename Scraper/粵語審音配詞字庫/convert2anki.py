import csv

note_id = 0

headers = ['Id','Ranking','Freq.','Characters','Syllable','Words(Explanation) / Remarks','Sound']
with open('RankingChartDetialed-1000-sound.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

with open('RankingChartDetialed-1000.csv') as f:
    fr_csv = csv.reader(f)
    headers = next(fr_csv)
    for row in fr_csv:
        note_id +=1
        rank,freq,chrct,syllable,word = row
        sound = "[sound:"+syllable+"_by_can4_ging1_ying1"+".wav]"
        with open('RankingChartDetialed-1000-sound.csv','a') as fw:
            fw_csv = csv.writer(fw)
            fw_csv.writerow((note_id,rank,freq,chrct,syllable,word,sound))
