input_file = '../../../data/merged_base.data'
cf_train_f = '../../../data/cf_train.data'

with open(cf_train_f, 'w') as f:
    pass

# User-Item dict
u_i_dict = {}

with open(input_file, 'r') as f_in:
    for line in f_in:
        ss = line.strip().split('\001')
        # print(ss)
        user_id, item_id, listen_len, listen_moment, gender, age, salary, user_loc, name, desc, total_time, item_loc, tags = ss
        # if name!=desc:
        #     print([user_id, item_id, listen_len, listen_moment, gender, age, salary, user_loc, name, desc, total_time, item_loc, tags])

        u_i_id = '_'.join([user_id, item_id])
        if u_i_id not in u_i_dict:
            u_i_dict[u_i_id] = []
        v = [int(listen_len), int(total_time)]
        u_i_dict[u_i_id].append(v)

for k, vs in u_i_dict.items():
    score = 0.
    for v in vs:
        listen_len, total_time = v
        score += float(listen_len) / float(total_time)  # sum of all times of listen_percent
    user_id, item_id = k.strip().split('_')
    with open(cf_train_f, 'a') as f_cf:
        line = '{},{},{}'.format(user_id, item_id, score)
        f_cf.write(line)
        f_cf.write('\n')
