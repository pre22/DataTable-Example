from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship

# # Create Engine
engine = create_engine('sqlite+pysqlite:///db.sqlite3', echo=False)

# # Create Session
Session = sessionmaker(bind=engine)
session = Session()

# # Create Table
# class Base(DeclarativeBase):
#     pass

# class User(Base):
#     __tablename__ = "users"
#     id  =  Column(Integer(), primary_key=True)
#     username = Column(String(40), nullable=False)
#     email = Column(String(40), nullable=True)
#     posts = relationship('Post', backref='author')

#     def __repr__(self):
#         return f"<User {self.username}>"

# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer(), primary_key=True)
#     title = Column(String(45), nullable=False)
#     content = Column(String(255), nullable=False)
#     user_id = Column(Integer(), ForeignKey('users.id'))

#     def __repr__(self):
#         return f"User {self.title}"


# Base.metadata.create_all(engine)
from ..project.DB.dbDemo import Address, User

users = session.query(Address).join(Address.user).filter(User.name == "Daniel")
user=users[0]
print(f"{user.email_address} {user.user.name}")