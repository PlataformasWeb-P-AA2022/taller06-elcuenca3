
from sqlalchemy.orm import sessionmaker
from genera_base import Paises
from configuracion import engine
import requests


Session = sessionmaker(bind=engine)
session = Session()

resp = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

datos=resp.json()


for d in datos:
    print(d)
    print(len(d.keys()))
    p = Paises(npais=d['CLDR display name'], capital=d['Capital'], con=d['Continent'],\
        dial=d['Dial'],geoid=d['Geoname ID'],itu=d['ITU'],lenguaje=d['Languages'],independecia=d['is_independent'])        
    session.add(p)

# confirmar transacciones

session.commit()
