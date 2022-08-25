

#from .utils import Utils

from bs4 import BeautifulSoup

#BASE_URL = 'C:/Users/Mdiallo/Documents/Master AI Datascience/MASTER1/data_collection/COURS19AOUT2022/DATA-COLLECTION-DIT/COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'
BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'
class HtmlFactory(object):
    @classmethod
    def OpenFile(cls):
        with open(BASE_URL, 'r') as f:
            html= f.read()
        return html
    
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
                    'name' : datas[0].getText(),
                    'phone' : datas[1].getText(),
                    'email' : datas[2].getText(),
                    'latlng' : datas[3].getText(),
                    'salary': datas[4].getText(),
                    'age':datas[5].getText()
                    }
            tables.append(table)
        return tables
    @classmethod 
    def main(cls):
        return cls.getData(cls.getRows(cls.OpenFile()))