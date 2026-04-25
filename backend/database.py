from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url="postgresql://postgres:Bugatti11@localhost:5432/viki"
engine=create_engine(db_url)
session= sessionmaker(autocommit=False, autoflush=False,bind = engine)