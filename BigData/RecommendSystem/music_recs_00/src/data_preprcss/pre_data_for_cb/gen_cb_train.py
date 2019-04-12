in_file = '../../../data/merged_base.data'
out_file = '../../../data/cb_train.data'

with open(out_file, 'w') as f:
    pass

with open(in_file, 'r') as f_in:
    for line in f_in:
        ss = line.strip().split('\001')
        (user_id, item_id, listen_len, listen_moment,
         gender, age, salary, user_loc,
         name, desc, total_time, item_loc, tags) = ss
