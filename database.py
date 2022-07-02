from sqlalchemy import create_engine 
from decouple import config

from sqlalchemy.orm import declarative_base, sessionmaker


# engine=create_engine(config('DATABASE_CREDENTIALS'), echo=True)
# engine=create_engine('postgresql://postgres:kitty121@localhost/Pizza-Delivery-FastAPI', echo=True)
engine=create_engine("postgresql://postgres:xwjrxsgmusggpm:cb0e9f72e5b8ce042440d58f25bc572a6dfb5c9b94b71ea1576171b69bf4e806@ec2-44-198-82-71.compute-1.amazonaws.com:5432/d80sm6fqpidcjc", echo=True)

# database = databases.Database(DATABASE_URL)

# metadata = sqlalchemy.MetaData()


Base=declarative_base()

Session=sessionmaker()