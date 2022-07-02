from sqlalchemy import create_engine 
from decouple import config
from sqlalchemy.orm import declarative_base, sessionmaker

# engine=create_engine(config('DATABASE_CREDENTIALS'), echo=True)
engine=create_engine('postgresql://postgres:kitty121@localhost/Pizza-Delivery-FastAPI', echo=True)

Base=declarative_base()

Session=sessionmaker()