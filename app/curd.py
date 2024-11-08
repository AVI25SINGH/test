from sqlalchemy.orm import Session
from . import module, schema

def create_user(db:Session ,user:schema.Usercreate):
    db_user=module.User(name=user.name ,email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_author(db: Session, author: schema.AuthorCreate):
    db_author = module.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def create_book(db:Session , books:schema.BookCreate):
    db_book=module.Book(title=books.title)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    
    for auth_id in books.authors:
        auther=db.query(module.Author).filter(module.Author.id==auth_id).first()
        if auther:
            db_book.authors.append(auther)
        
    db.commit()
    return db_book
    
def create_loan(db: Session, loan: schema.LoanCreate):
    db_loan = module.Loan(user_id=loan.user_id, book_id=loan.book_id, due_date=loan.due_date)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan



# def create_loan_history(db: Session, loan_history: module.LoanHistoryCreate):
#     db_loan_history = module.LoanHistory(
#         loan_id=loan_history.loan_id,
#         borrowed_date=loan_history.borrowed_date,
#         return_date=loan_history.returned_date or loan_history.borrowed_date
#     )
#     db.add(db_loan_history)
#     db.commit()
#     db.refresh(db_loan_history)
#     return db_loan_history

# def get_loan_history(db: Session, loan_id: int):
#     return db.query(module.LoanHistory).filter(module.LoanHistory.loan_id == loan_id).all()

# def get_loan_history_by_id(db: Session, history_id: int):
#     return db.query(module.LoanHistory).filter(module.LoanHistory.id == history_id).first()

# def create_loan_history(db: Session, loan_history: schema.LoanHistoryCreate):
#     db_loan_history = module.LoanHistory(  # Use models.LoanHistory instead of module.LoanHistory
#         loan_id=loan_history.loan_id,
#         borrowed_date=loan_history.borrowed_date,
#         return_date=loan_history.returned_date or loan_history.borrowed_date
#     )
#     db.add(db_loan_history)
#     db.commit()
#     db.refresh(db_loan_history)
#     return db_loan_history
def create_loan_history(db: Session, loan_history: schema.LoanHistoryCreate):
    db_loan_history = module.LoanHistoryRecord(  # Use the new name here
        loan_id=loan_history.loan_id,
        borrowed_date=loan_history.borrowed_date,
        return_date=loan_history.returned_date or loan_history.borrowed_date
    )
    db.add(db_loan_history)
    db.commit()
    db.refresh(db_loan_history)
    return db_loan_history

def get_loan_history(db: Session, loan_id: int):
    return db.query(module.LoanHistoryRecord).filter(module.LoanHistory.loan_id == loan_id).all()

def get_loan_history_by_id(db: Session, history_id: int):
    return db.query(module.LoanHistoryRecord).filter(module.LoanHistory.id == history_id).first()


def get_user(db:Session ,  user_id:int):
    return db.query(module.User).filter(module.User.id==user_id).first()

# def get_all_users(db:Session, skip:int=0,limt:int=10):
#     return db.query(module.User).offset(skip).limit(limt).all()
def get_all_users(db: Session):
    return db.query(module.User).all()