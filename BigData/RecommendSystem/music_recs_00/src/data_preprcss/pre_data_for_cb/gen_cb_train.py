in_file = '../../../data/music_meta'
out_file = '../../../data/cb_train.data'

with open(out_file, 'w') as f:
    pass

with open(in_file, 'r') as f_in:
    for line in f_in:
        ss = line.strip().split('\001')
        (item_id, name, desc, total_time, item_loc, tags) = ss
        # print(ss)
