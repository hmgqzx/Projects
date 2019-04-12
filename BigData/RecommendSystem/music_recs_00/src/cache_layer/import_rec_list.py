# 由在 hadoop MapReduce 跑出的结果，排序取 top N，
# 然后输出为适合 redis 导入的格式，以进行批量灌库

cb_in_file = '../../data/hadoop_output/cb.result'
cb_out_file = '../../data/redis/cb_rec_list.redis'

cf_in_file = '../../data/hadoop_output/cf.result'
cf_out_file = '../../data/redis/cf_rec_list.redis'

MAX_TOP_N_SIZE = 100
CB_PREFIX = 'CB_'
CF_PREFIX = 'CF_'


def gen_rec_list_fit_redis(in_file, out_file, prefix):
    rec_dict = {}
    with open(in_file, 'r') as f_in:
        for line in f_in:
            item_a_id, item_b_id, sim_score = line.strip().split('\t')
            # be careful here! it had has a bug bcz of my wrong way to handle the branch of `if`
            if item_a_id not in rec_dict:
                rec_dict[item_a_id] = []
            rec_dict[item_a_id].append([item_b_id, sim_score])

    with open(out_file, 'w') as f_out:
        for k, xs in rec_dict.items():  # k - item_id; xs - collections of similar item and corresponded score
            top_n_list = sorted(xs, key=lambda x: x[1],
                                reverse=True)[
                         :MAX_TOP_N_SIZE]  # x - [item_id,sim_score], similar item's id and corresponded score
            rec_result = '_'.join(
                [':'.join([x[0], str(round(float(x[1]), 6))]) for x in top_n_list])  # id:sc_id:sc_...
            # print(rec_result)
            line = 'SET {} {}'.format(prefix + k, rec_result)
            # print(line)
            f_out.write(line)
            f_out.write('\n')  # redis has supported '\n'? this work without using unix2dos or '\r\n'


gen_rec_list_fit_redis(cb_in_file, cb_out_file, CB_PREFIX)
gen_rec_list_fit_redis(cf_in_file, cf_out_file, CF_PREFIX)
