from sqlalchemy import Column, Integer, Float, String, Date

from database import Base

class PessoaModel(Base):
    __tablename__ = "pessoas"

    idpessoas = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60))
    data_nascimento = Column(Date)
    peso = Column(Float)
    altura = Column(Float)

