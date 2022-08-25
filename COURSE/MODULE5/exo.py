from ast import Try
from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.BCEAO import Scrapbceao
from libraries.Contries import DataSouper
import pandas as pd
import random
import os

def ConcatData(CSV : list, JSON : list , HTML: list ):
    return [*CSV,*JSON,*HTML]

def AddRandomDevice(data):
    def Adding(item):
        dev = ['yen', 'euro', 'dollar']
        item["Devise"]=random.choice(dev)
        return item
    return list(map(Adding,data))

def ConvertToXOF(data):

    """ Cette fonction convertit les salaires en FCFA en utilsant le cours des dévises de la BCEAO"""

    def ConXOF(item):
        recup_val_devise = Scrapbceao.Currency(item["Devise"])
        item["salary_XOF"] = recup_val_devise.iloc[0]*int(item["salary"])
        return item
    
    return list(map(ConXOF,data))

def AdddingRandomContries(data):

    """ Cette fonction permet d'ajouter aléatoirement des pays en utilsant les données scrapper depuis l'API Coontry"""

    def AddContry(item):
        item["Country"] = random.choice(DataSouper.RecupName())
        return item
    return list(map(AddContry,data))

def AdddingFlag(data):

    """ Cette fonction permet d'ajouter les drapeaux de chaque pays en utilisant le même API country"""

    C_and_Flag = DataSouper.ContriesAndFlags()
    def Flag(item):
        item["Flag"] = C_and_Flag[item["Country"]]
        return item
    return list(map(Flag,data))
    
def StoreIndCSV(Liste):
    """ Après les traitements sous-jacentes, cette fonction permet de sauvegarder les données finales sous format csv """
    #relpath = 'C:/Users/Mdiallo/Documents/Master AI Datascience/MASTER1/data_collection/COURS19AOUT2022/DATA-COLLECTION-DIT/COURSE/DATABASES/
    
    path = "C:/Users/Mdiallo/Documents/Master AI Datascience/MASTER1/data_collection/COURS19AOUT2022/DATA-COLLECTION-DIT/COURSE/DATABASES/"
    if os.path.exists('COURSE/DATABASES/Final_data.csv') :
        pass
    else : 
        print("ok")
        #pd.DataFrame(data=Liste).to_csv('COURSE/DATABASES/Final_data.csv')


def ScrapFactory() :
    print(Utils.divider()+"Recupérartion des donnnées....")
    CSV=CsvFactory.main()
    JSON = JsonFactory.main()
    HTML = HtmlFactory.main()
    print(Utils.divider()+"Recupérartion des donnnées : done")
    print(Utils.divider())
    print(Utils.divider()+"Concaténation des base...")
    data = ConcatData(CSV, JSON, HTML)
    print(Utils.divider()+"Concaténation des base : done")
    print(Utils.divider())
    print(Utils.divider()+"Ajout aleatoire des devises des base...")
    data01=AddRandomDevice(data)
    print(Utils.divider()+"convertion des salaire en XOF devises des base...")
    data02=ConvertToXOF(data01)
    print(Utils.divider()+"Ajout aleatoire des pays...")
    data03=AdddingRandomContries(data02)
    print(Utils.divider()+"Ajout des liens des drapeaux de chaque pays...")
    data04=AdddingFlag(data03)
    print(Utils.divider()+"Stockage de la base sous format csv...")
    StoreIndCSV(data04)




if __name__ == '__main__':
    if os.path.exists('COURSE/DATABASES/Final_data.csv') :
        print("exist")
        rep=input("Les données existent deja voulez vous relancer le scrapinge (Oui:O/o; Non:N/n): ")
        if rep.lower() == 'o' :
            ScrapFactory()
        else :
            pass
    else :
        ScrapFactory()
