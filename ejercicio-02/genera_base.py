from sqlalchemy import create_engine


from configuracion import engine

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String,Boolean

class Paises(Base):

    __tablename__ = 'codepais'

    id = Column(Integer, primary_key=True)
    npais = Column(String(200))
    capital = Column(String(200))
    con=Column(String(200))
    dial=Column(String(200))
    geoid=Column(Integer)
    itu=Column(String(200))
    lenguaje=Column(String(200))
    independecia=Column(String(200))


Base.metadata.create_all(engine)

