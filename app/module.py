# in model we create all table here 
# Table is a function provided by SQLAlchemy to define tables 
# without mapping them to a specific ORM class (this is typical for association tables).

# Here, we create an instance of the Table class, storing it in book_author_table, which represents a 
# linking table for Book and Author.

# "book_author",:This is the name of the association table in the database. It is named "book_author" here.
# This table will store references to records from the books and authors tables,
# linking them to represent the many-to-many relationship

# Base.metadata is a MetaData object from SQLAlchemy

# By passing Base.metadata here, we ensure that this table (book_author) 
# is registered with the database when we create tables

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime,timezone

# book_author_table=Table(
#     "book_author",
#     Base.metadata,
#     Column("book_id",Integer,ForeignKey("book.id"),primary_key=True),
#     Column("author_id",Integer,ForeignKey("author.id"),primary_key=True),
# )

# class User(Base):
#     __tablename__="users"
#     id=Column(Integer,primary_key=True,index=True)
#     name=Column(String(100),nullable=False)
#     email=Column(String(50),unique=True,nullable=False)
    
# class book(Base):
#     __tablename__="books"
#     id=Column(Integer,primary_key=True,index=True)
#     title=Column(String(100))
#     authors=relationship("Author",secondary=book_author_table,back_populates="books")
#     loans=relationship("Loan",back_populates="book")
    

# class Author(Base):
#     __tablename__="authors"
#     id=Column(Integer,primary_key=True,index=True)
#     name=Column(String(50),nullable=False)
#     # here we can't pass null value in table because we can apply validation
#     books=relationship("book",secondary=book_author_table , back_populates="authors")
    
    
# # class Loan(Base):
# #     __tablename__="loans"
# #     id=Column(Integer,primary_key=True,index=True)
# #     due_date=Column(datetime,nullable=False)
# #     return_date=Column(datetime,nullable=True)
# #     user_id=Column(Integer,ForeignKey("users.id"))
# #     book_id=Column(Integer,ForeignKey("books.id"))
    
# #     user=relationship("User",back_populates="loans")
# #     book=relationship("book",back_populates="loans")
# #     history=relationship("loanhistory",uselist=False,back_populates="loan")
    
    
# # class loanhistory(Base):
# #     __tablename__="loan_histories"
# #     id=Column(Integer,primary_key=True ,index=True)
# #     borrowed_date=Column(datetime , default=datetime.now(timezone.utc))
# # # it's return is a method in Python's datetime module that returns the current date and time in
# # # Coordinated Universal Time (UTC).
# #     return_date=Column(datetime,nullable=False)
# #     loan_id=Column(Integer,ForeignKey("loans.id"))
# #     loan=relationship("Loan",back_populates="history")


# class Loan(Base):
#     __tablename__ = "loans"
#     id = Column(Integer, primary_key=True, index=True)
#     due_date = Column(DateTime, nullable=False)  # Use DateTime from SQLAlchemy
#     return_date = Column(DateTime, nullable=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     book_id = Column(Integer, ForeignKey("books.id"))
    
#     user = relationship("User", back_populates="loans")
#     book = relationship("book", back_populates="loans")
#     history = relationship("loanhistory", uselist=False, back_populates="loan")

# class loanhistory(Base):
#     __tablename__ = "loan_histories"
#     id = Column(Integer, primary_key=True, index=True)
#     borrowed_date = Column(DateTime, default=datetime.now(timezone.utc))  # Use DateTime
#     return_date = Column(DateTime, nullable=False)
#     loan_id = Column(Integer, ForeignKey("loans.id"))
#     loan = relationship("Loan", back_populates="history")

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone

book_author_table = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),  # updated to "books.id"
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True)  # also ensure authors.id is used
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    loans = relationship("Loan", back_populates="user")  # Added relationship to Loan

class Book(Base):  # Capitalize class name
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    authors = relationship("Author", secondary=book_author_table, back_populates="books")
    loans = relationship("Loan", back_populates="book")

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    books = relationship("Book", secondary=book_author_table, back_populates="authors")  # updated to "Book"

# class Loan(Base):
#     __tablename__ = "loans"
#     id = Column(Integer, primary_key=True, index=True)
#     due_date = Column(DateTime, nullable=False)
#     return_date = Column(DateTime, nullable=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     book_id = Column(Integer, ForeignKey("books.id"))
    
#     user = relationship("User", back_populates="loans")
#     book = relationship("Book", back_populates="loans")
#     history = relationship("LoanHistory", uselist=False, back_populates="loan")
class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    
    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")
    history = relationship("LoanHistoryRecord", uselist=False, back_populates="loan")  # Updated to "LoanHistoryRecord"


# models.py
class LoanHistoryRecord(Base):  # Renamed to avoid confusion with schema class
    __tablename__ = "loan_histories"
    id = Column(Integer, primary_key=True, index=True)
    borrowed_date = Column(DateTime, default=datetime.now(timezone.utc))
    return_date = Column(DateTime, nullable=False)
    loan_id = Column(Integer, ForeignKey("loans.id"))
    loan = relationship("Loan", back_populates="history")

