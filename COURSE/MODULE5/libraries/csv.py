from .utils import Utils
import pandas as pd
import json

#COURSE/DATABASES/COURSE\DATABASES\data-_zJ9Zko2Dh1LYlNNgALKE.csv
#COURSE\DATABASES\data-_zJ9Zko2Dh1LYlNNgALKE.csv
import os

#dirname = os.path.dirname(__file__)
#BASE_URL = os.path.join(dirname, 'COURSE\DATABASES\data-_zJ9Zko2Dh1LYlNNgALKE.csv')
#BASE_URL = "COURSE\DATABASES\data-_zJ9Zko2Dh1LYlNNgALKE.csv"
#BASE_URL = 'C:/Users/Mdiallo/Documents/Master AI Datascience/MASTER1/data_collection/COURS19AOUT2022/DATA-COLLECTION-DIT/COURSE/DATABASES/data-_zJ9Zko2Dh1LYlNNgALKE.csv'
BASE_URL = 'COURSE/DATABASES/data-_zJ9Zko2Dh1LYlNNgALKE.csv'


class CsvFactory(object):
    @classmethod
    def openFile(cls):
        data = pd.read_csv(
            BASE_URL,
            encoding='utf-8')
        return data

    @classmethod
    def addSalary(cls, data):
        START = 200000
        FINAL = 1000000
        data['salary'] = float(0)
        data['salary'] = data['salary'] \
            .apply(lambda x: Utils.randomize(START, FINAL))
        return data

    @classmethod
    def addAge(cls, data):
        START = 18
        FINAL = 100
        data['age'] = 0
        data['age'] = data['age'] \
            .apply(lambda x: Utils.randomize(START, FINAL))
        return data

    @classmethod
    def naming(cls, data):
        data['name'] = data['name'] \
            .apply(Utils.x)
        return data

    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.addSalary(data)
        data = cls.addAge(data)
        data = cls.naming(data)
        data = data \
            .T \
            .to_dict() \
            .values()
        return list(data)
