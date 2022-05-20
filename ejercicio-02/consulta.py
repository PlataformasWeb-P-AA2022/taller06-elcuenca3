
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Paises

engine = create_engine('sqlite:///ejercicio2.db')

Session = sessionmaker(bind=engine)
session = Session()

#consulta 1
paises1 = session.query(Paises).filter(Paises.con.in_(['NA','SA'])).all()
print(paises1)
#consulta 1


#consulta 2
paises2 = session.query(Paises).filter(Paises.con=="AS").order_by(Paises.dial).all()
print(paises2)

#consulta 3
paises3 = session.query(Paises.lenguaje).all()

print(paises3)
#consulta 4

paises4 = session.query(Paises).filter(Paises.con=="EU").order_by(Paises.capital).all()
print(paises4)

#consulta 5  

paises5 = session.query(Paises).filter(or_(Paises.npais.like("%uador"), Paises.capital.like("%ito"))).all()
print(paises5)