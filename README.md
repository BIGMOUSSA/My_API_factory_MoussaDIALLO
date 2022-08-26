# My_API_factory_MoussaDIALLO

Ceci est une initiation à l'utilisation des techniques de data collection

# COLLECTION DES DONNEES 

- csv
- JSON
- HTLM
- AJOUT DE L ITEM DEVISE ALEATOIREMENT
- SCRAPER LE SITE DE LA BCEAO POUR RECUPERER LE COURS DES DEVISES
- CONVERTIR LES SALAIRE EN CFA XOF AVEC LE COURS DES DEVISES
- SCRAPER L API REST COUNTRY POUR RECUPER LES PAYS ET LEUR DRAPEAU
- CREER L ITEM COUNTRY Y METTRE ALEATOREMENT UN PAYS DE LA BASE ISSUE DE L API REST COUNTRY
- CREER L ITEM FLAG EN FONCTION DU PAYS ON AJOUTE LE FLAG CORRESPONDANT


# MISE EN PLACE DE NOTRE API 

- CREATION DE LA BASE MYSQL

- CREATION DE LA TABLE people AVEC SQLALCHEMY

-  AJOUT DES DONNEES  AVEC SQLALCHEMY

- lANCER L API AVEC FASTAPI {http://127.0.0.1:8000/People}


###################### ETAPES

# creer l'environnement virtuel venv

 
> python -m venv venv (windows)

## install requirements
 
> pip install -r requirements.txt 

### LANCER Etrack transform load SCRAPFACTORY

> python COURSE\MODULE5\ETL_factory.py




#### créer la base scraping et la table people dans mysql 

## Paraméter les paramètres de données sur mysql 

> ouvri le fichier .env (COURSE\MODULE5\fastapi\.env)

- Mettez vos paramètres de connexion sur mysql

	- USER={votre user}
	- PASSWORD={VOTRE PASSWORD}

> NE PAS TOUCHER DATABASE DE PREFERENCE
 - DATABASE=SCRAPING

### exexuter le fichier create_db.py 

le programme crée la base "scraping" si elle n'existe pas, 
crée la table "people" à l'intérieur de la base scraping

> python COURSE/MODULE5/fastapi/create_db.py 

### ajout des données 
ce programme récupère les données de la première étape pour les charger dans la table "People"
de la base "scraping

> python COURSE/MODULE5/fastapi/insert_data_to_table.py

### Lancer l'api pour consulter les données

Il est temps de lancer notre API pour consulter nos données

-- Allez Dans le dossier COURSE/MODULE5/fastapi puis lancer : 
  
> uvicorn main:app --reload

### dans votre navigateur entrer ou avec l'application postman

http://127.0.0.1:8000/People

## Normalement les données doivent s'afficher sour format json !

****************  FIN 	**************************************