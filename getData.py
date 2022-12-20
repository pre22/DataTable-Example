from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
from demo import User

# Create Engine
engine = create_engine('sqlite+pysqlite:///db.sqlite3', echo=False)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Create Table
class Base(DeclarativeBase):
    pass

class Session(Base):
    __tablename__ = 'user_session'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User, back_populates="user_session")
    session_item = Column(String(300))
    session_value= Column(String(300))

    def __str__(self):
        return f"{user} | {session_item}"

Base.metadata.create_all(engine)
