from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///ejercicio2.db', echo=True)

# mysql
# pip install mysql-connector-python
#engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3306/base2",echo=True)