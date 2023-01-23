from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
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
    session_id = relationship('SessionDB', back_populates="users")

    def __repr__(self):
        return f"{self.username}"


class SessionDB(Base):
    __tablename__ = 'user_session'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
    users = relationship('User', back_populates="session_id")

    session_item = Column(String(300))
    session_value= Column(String(300))

    def __str__(self):
        return f"{user} | {session_item}"

# User.addresses = relationship("SessionDB", order_by=SessionDB.id, back_populates="user")

# Migrate
# Base.metadata.create_all(engine)

# Add Data 
user_one = User(username="pre.chika.22@gmail.com", password="user1234")
# user_two = User(username="pre.chika.22@gmail.com", password="user1234")
# user_three = User(username="pre.chika.22@gmail.com", password="user1234")
session.add(user_one)
# session.add_all([user_two, user_three])
# session.commit()


# data = session.query(User).all()
# data = session.query(User).filter(User.id == 1).one
# print(data)

# data = session.query(User).filter(User.username=="pre.chika.22@gmail.com").first()
# data.password = "user2424"
# session.commit()