import jieba.analyse

in_file = '../../../data/music_meta'
out_file = '../../../data/cb_train_on_music_meta.data'

with open(out_file, 'w') as f:
    pass

idf_file = '../../../data/idf.txt'
idf_dict = {}
with open(idf_file, 'r') as f:
    for line in f:
        word, idf_score = line.strip().split(' ')
        idf_dict[word] = idf_score

# weight of fields
RADIO_FOR_NAME = 0.9
RADIO_FOR_DESC = 0.1
RADIO_FOR_TAGS = 0.05

# prepare set to memorize item_id has presented
item_id_set = set()
with open(in_file, 'r') as f_in:
    for line in f_in:
        ss = line.strip().split('\001')
        (item_id, name, desc, total_time, item_loc, tags) = ss
        # print(ss)
