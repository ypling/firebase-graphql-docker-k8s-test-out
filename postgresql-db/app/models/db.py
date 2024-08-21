from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Reading the database URL from environment variable
db_root_password = os.getenv('DB_ROOT_PASSWORD')
db_username = os.getenv('DB_USERNAME')
db_host = os.getenv('DB_HOST')

schema = os.getenv('PGRST_DB_SCHEMA', 'api')

# Construct the PostgreSQL connection URL
database_url = f"postgresql://{db_username}:{db_root_password}@{db_host}:5432/postgres"

# Create the database engine
engine = create_engine(database_url)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()