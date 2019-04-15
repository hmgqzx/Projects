# encoding: UTF-8
import re
import csv

in_f = '../data/dict_revised_2015_20190329_1.csv'
out_f = '../data/out.csv'
ranking_f = ac_corpus_csv = '../data/ACCorpusCharacterlist.csv'


def split_meaning_text(meaning_text):
    """根據詞性對詞條釋義文本進行分割
    :param meaning_text: 詞條釋義文本
    :return pos_meaning_list: 由各個釋義所組成的列表"""
    pos_meaning_list = re.findall(r'\[.][^\[]*', meaning_text)
    print("pos_meaning_list:")
    print(pos_meaning_list)
    return pos_meaning_list


def extract_pos(pos_meaning):
    pos = re.match(r'\[\w]', pos_meaning).group()
    print('pos:')
    print(pos)
    return pos


def split_pos_meaning(pos_meaning):
    meanings = re.findall(r'\d[^\d]*', pos_meaning)
    if meanings:
        print('meanings:')
        print(meanings)
        return meanings
    else:
        meaning = re.sub(r'\[.]', '', pos_meaning)
        print('meaning:')
        print([meaning])
        return [meaning]


if __name__ == '__main__':
    pos_meaning_list = split_meaning_text(fake_meaning_text)
    for pos_meaning in pos_meaning_list:
        pos = extract_pos(pos_meaning)
        meaning_list = split_pos_meaning(pos_meaning)
        for meaning in meaning_list:
            pass
