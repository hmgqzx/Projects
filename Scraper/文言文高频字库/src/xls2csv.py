import pandas as pd

PREFIX = 'dict_revised_2015_20190329_'
DATA_DIR = '../data/'


def xlsx_to_csv_pd(xlsx_f, csv_f):
    data_xls = pd.read_excel(xlsx_f, index_col=0)
    data_xls.to_csv(csv_f, encoding='utf-8')


if __name__ == '__main__':
    for x in range(1, 4):
        index = str(x)
        xlsx_f = DATA_DIR + PREFIX + index + '.xls'
        csv_f = DATA_DIR + PREFIX + index + '.csv'
        xlsx_to_csv_pd(xlsx_f, csv_f)