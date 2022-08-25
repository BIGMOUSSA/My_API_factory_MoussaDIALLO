# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 17:07:15 2022

@author: mdiallo
"""
import random
import requests
import pandas as pd

#from urllib.request import urlopen
from bs4 import BeautifulSoup
URL = "https://www.bceao.int/fr/cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts"


class Scrapbceao(object):
    """ Cette class implémente des méthodes qui permettent d'aller dans le site de la BCEAO pour récupérer le cours des devises """
    @classmethod
    def fetcher(cls,url):
        return requests.get(url).text
    @classmethod 
    def getRows(cls,html):
        data =BeautifulSoup(html,features="html.parser")
        rows = data.find_all("tr")
        return rows[1:]
    @classmethod 
    def getData(cls,rows):
        tables = []
        for row in rows :
            datas = row.find_all('td')
            table = {
                    'device' : datas[0].getText(),
                    'achat' : float(str(datas[1].getText()).replace(",", ".")),
                    'vente' : float(str(datas[2].getText()).replace(",", "."))

                    }
            tables.append(table)
        return tables

    
    @classmethod 
    def main(cls):
        return pd.DataFrame(data=cls.getData(cls.getRows(cls.fetcher(URL))))
    @classmethod 
    def Currency(cls,Monnaies:str):
        #assert Monnaies not in ["euro","dollar","yen"], "on ne convertit que l'euro, le dollar ou le yen !"
        equiv = {"euro":"Euro","dollar":"Dollar us","yen":"Yen japonais"}
        data=cls.main()
        return data[data.device==equiv[Monnaies]].achat