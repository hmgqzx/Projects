# TODO: import path by config will be better
user_action_data = '../../../data/user_watch_pref.sml'
music_meta_data = '../../../data/music_meta'
user_profile_data = '../../../data/user_profile.data'

merged_data = '../../../data/merged_base.data'

# touch new file: bcz "with open(output_data,'a') as f" below
with open(merged_data, 'w') as fa:
    pass

# 1. decode music meta data
item_info_dict = {}  # key:item_id, value: name, desc, total_time, loc, tags
with open(music_meta_data, 'r') as f:
    for line in f:
        ss = line.strip().split('\001')
        if len(ss) != 6:
            continue
        # print(line)
        item_id, name, desc, total_time, loc, tags = ss
        item_info_dict[item_id] = '\001'.join([name, desc, total_time, loc, tags])
    # print(item_info_dict)

# 2. decode user profile data
user_profile_dict = {}  # key:user_id, value: user_id, gender, age, salary, loc
with open(user_profile_data, 'r') as f:
    for line in f:
        ss = line.strip().split(',')
        if len(ss) != 5:
            continue
        user_id, gender, age, salary, loc = ss
        user_profile_dict[user_id] = '\001'.join([gender, age, salary, loc])
        # print(user_profile_dict)

# see sth
# print(len(item_info_dict)) # 759984
# print(len(user_profile_dict)) # 110392


# 3. decode user action dat
with open(user_action_data, 'r') as f:
    for line in f:
        ss = line.strip().split('\001')
        # print(ss)
        if len(ss) != 4:
            continue
        user_id, item_id, listen_len, listen_moment = ss
        # filter
        if user_id not in user_profile_dict:
            continue
        if item_id not in item_info_dict:
            continue
        # join 3 tables
        record = '\001'.join([user_id, item_id, listen_len, listen_moment,
                              user_profile_dict[user_id],
                              item_info_dict[item_id]])
        with open(merged_data, 'a') as f_op:
            f_op.write(record)
            f_op.write('\n')
