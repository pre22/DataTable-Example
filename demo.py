from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# Create Engine
engine = create_engine('sqlite+pysqlite:///db.sqlite3', echo=False)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Create Table
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))

Base.metadata.create_all(engine)


# Migrate