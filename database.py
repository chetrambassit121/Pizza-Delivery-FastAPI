from sqlalchemy import create_engine 
from decouple import config
# import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker



# database = databases.Database(DATABASE_URL)

# metadata = sqlalchemy.MetaData()

# engine = sqlalchemy.create_engine(DATABASE_URL)
engine=create_engine(config('DATABASE_CREDENTIALS'), echo=True)

Base=declarative_base()



Session=sessionmaker()



