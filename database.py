from sqlalchemy import create_engine 
from decouple import config
from sqlalchemy.orm import declarative_base, sessionmaker

engine=create_engine(config('database_credentials'), echo=True)

Base=declarative_base()

Session=sessionmaker()