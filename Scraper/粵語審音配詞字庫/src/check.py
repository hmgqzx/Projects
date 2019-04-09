import csv

srca='../data/7072/RankingChartDetailed-7072.csv'
srcb='../data/RankingChart.csv'

l=[]
sa=set()
sb=set()

with open(srca) as f:
    fr_csv = csv.reader(f)
    headers = next(fr_csv)
    for row in fr_csv:
        rank,freq,chrct,syllable,word = row
        sa.add(chrct)

with open(srcb) as f:
    fr_csv = csv.reader(f)
    headers = next(fr_csv)
    for row in fr_csv:
        rank,freq,chrct,code = row
        l+=chrct
        sb.add(chrct)

print(len(sa))
print(len(sb))
d=[x for x in l if x not in sb]
print(d)

with open(srca) as f:
    fr_csv = csv.reader(f)
    headers = next(fr_csv)
    for row in fr_csv:
        rank,freq,chrct,syllable,word = row
        if('�' in chrct or '�' in word):
            print(row)
