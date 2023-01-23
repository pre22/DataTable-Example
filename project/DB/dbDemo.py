from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, DeclarativeBase, sessionmaker

# Create Engine
engine = create_engine('sqlite+pysqlite:///db.sqlite3', echo=False)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"<User {self.fullname}>"

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

# Base.metadata.create_all(engine)
# user_one = User(name="Daniel", fullname="Daniel Mike", password="user1234")
users = session.query(Address).join(Address.user).filter(User.name == "Daniel")
user=users[0]
print(f"{user.email_address} {user.user.name}")


# user_one = Address(email_address="pre.chika.22@gmail.com", user_id=users[0].id)
# session.add(user_one)
# session.commit()

# session.close()