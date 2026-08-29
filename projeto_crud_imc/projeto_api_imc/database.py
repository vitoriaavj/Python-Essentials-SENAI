from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost/bd_pessoas_imc"
DATABASE_URL = "mysql+pymysql://root@localhost/bd_pessoas_imc"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush = False,
    autocommit = False,
    bind = engine
)

Base = declarative_base()
