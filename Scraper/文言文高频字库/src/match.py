# encoding: UTF-8
import re

fake_meaning_text = "[代]\
如此。《論語．憲問》：「子曰：『何必高宗，古之人皆然。』」唐．柳宗元〈桐葉封弟辯〉：「周公曰：『天子不可戲。』乃封小弱弟於唐。吾意不然。」\
[連]\
1.但是、可是。然後。唐．柳宗元〈桐葉封弟辯〉：「周公曰：『天子不可戲。』乃封小弱弟於唐。吾意不然。」\
2.然後。《隋書．卷七○．李密傳》：「待士馬肥充，然可與人爭利。」\
[助]\
1.形容詞或副詞詞尾。然後。但是、可是。如：「斐然」、「赫然」、「恍然」。唐．柳宗元〈桐葉封弟辯〉：「周公曰：『天子不可戲。』乃封小弱弟於唐。吾意不然。」\
2.用於句末，表肯定、斷定的語氣。然後。唐．柳宗元〈桐葉封弟辯〉：「周公曰：『天子不可戲。』乃封小弱弟於唐。吾意不然。」《論語．憲問》：「子曰：『何必高宗，古之人皆然。』」\
[歎]\
唯，表應答。如：「斐然」、「赫然」、「恍然」。唐．柳宗元〈桐葉封弟辯〉：「周公曰：『天子不可戲。』乃封小弱弟於唐。吾意不然。」\
[名]\
姓。如漢代有然溫。"


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
