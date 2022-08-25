

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 19:54:25 2022

@author: mdiallo
"""

import re
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup



import json
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://restcountries.com/v3.1/all'


class DataSouper(object):
    @classmethod
    def httpFetcher(cls,
                    URL,
                    params=None,
                    headers=None):
        with requests.Session() as session:
            result = session.get(URL,
                                 params=params,
                                 headers=headers)
            result = result.json()
            return result
    @classmethod 
    def RecupName(cls):
        result =cls.httpFetcher(BASE_URL)
        liste =[item['name']['common'] for item in result]
        return liste
    @classmethod
    def RecupFlag(cls):
        result =cls.httpFetcher(BASE_URL)
        flags = [item['flags']['png'] for item in result]
        return flags
    @classmethod 
    def ContriesAndFlags(cls):
        countries =cls.RecupName()
        flags = cls.RecupFlag()
        return dict(zip(countries,flags))

if __name__ == '__main__':
    result = DataSouper.httpFetcher(
        BASE_URL,
        params={},
        headers={"Content-Type": "application/html"})

    print('\n')
    print(DataSouper.RecupName()[:10])
    print(DataSouper.RecupFlag()[:10])
    print(DataSouper.ContriesAndFlags())