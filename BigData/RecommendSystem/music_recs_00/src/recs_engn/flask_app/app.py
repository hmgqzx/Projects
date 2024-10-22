import redis
from flask import Flask, request

app = Flask(__name__)

CB_PREFIX = 'CB_'
CF_PREFIX = 'CF_'


@app.route('/')
def index():
    # resolve parameters of the request:
    # http://127.0.0.1:5050/?itemId=6229709155&userId=ao1235123ec&type=old&ip=127.0.0.1
    item_id = request.args.get('itemId', '')
    # user_id = request.args.get('userId', '')
    # action_type = request.args.get('type', '')
    # ip = request.args.get('ip', '')

    # connect to Redis
    rdb = redis.Redis(host='localhost', port=6379, db=0,
                      charset='utf-8', decode_responses=True)  # redis return byte-like object default

    # match and merge phrase
    rec_set = set()
    # # CF
    cf_item_key = CF_PREFIX + item_id
    cf_rec_result = ''
    if rdb.exists(cf_item_key):
        cf_rec_result = rdb.get(cf_item_key)  # a str like i:s_i:s_...
    cf_item_score_list = cf_rec_result.strip().split('_')  # a list like ['i:s',...]
    for cf_item_score in cf_item_score_list:
        item, score = cf_item_score.strip().split(':')
        rec_set.add(item)
    # # CB
    cb_item_key = CB_PREFIX + item_id
    cb_rec_result = ''
    if rdb.exists(cb_item_key):
        cb_rec_result = rdb.get(cb_item_key)
    cb_item_score_list = cb_rec_result.strip().split('_')  # ['i:s',...]
    for cb_item_score in cb_item_score_list:
        item, score = cb_item_score.strip().split(':')
        rec_set.add(item)

    rec_dict = {}
    music_meta_data = '../../../data/music_meta'
    with open(music_meta_data, 'r') as f:
        for line in f:
            ss = line.strip().split('\001')
            if len(ss) != 6:
                continue
            # print(line)
            item_id, name, desc, total_time, loc, tags = ss
            if item_id in rec_set:
                rec_dict[item_id] = name

    rec_list = []
    for k, v in rec_dict.items():
        line = '{} : {}'.format(k, v)
        rec_list.append(line)
    # return page
    ret = '<br/>'.join(rec_list)  # flask use HTML rendering, use <br/> to represent a newline
    return ret


app.run(host='127.0.0.1', port='5050', debug=True)
