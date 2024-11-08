from pydantic import BaseModel
from datetime import datetime
from typing import List,Optional 

class Userbase(BaseModel):
    name:str
    email:str
    
class Usercreate(Userbase):
    pass
class User(Userbase):
    id: int
    class Config:
        from_attributes = True


class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    

class BookCreate(BookBase):
    authors: List[int]

class Book(BookBase):
    id: int
    authors: List[Author]
    class Config:
        from_attributes = True

# class LoanBase(BaseModel):
#     user_id: int
#     book_id: int
#     due_date: datetime

# class LoanCreate(LoanBase):
#     pass

# class Loan(LoanBase):
#     id: int
#     class Config:
#         from_attributes = True
class LoanBase(BaseModel):
    user_id: int
    book_id: int
    due_date: datetime

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    class Config:
        from_attributes = True  
class LoanHistoryBase(BaseModel):
    loan_id: int
    borrowed_date: datetime
    returned_date: Optional[datetime] = None

class LoanHistoryCreate(LoanHistoryBase):
    pass

class LoanHistory(LoanHistoryBase):
    id: int

    class Config:
        from_attributes = True