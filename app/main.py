from fastapi import FastAPI,Depends,Request
from sqlalchemy.orm import Session
from .import module,schema,curd
from .database import session, engin
from typing import List
from fastapi import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse#
from fastapi.staticfiles import StaticFiles #
module.Base.metadata.create_all(bind=engin)
app=FastAPI()
# Initialize the Jinja2 template environment
# templates = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory="app/templates")
# for add css
app.mount("/static", StaticFiles(directory="app/static"), name="static")
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/users/",response_model=schema.User)
def create_user(user:schema.Usercreate, db:Session =Depends(get_db)):
    return curd.create_user(db=db,user=user)

@app.post("/author/", response_model=schema.Author)
def create_authors(author: schema.AuthorCreate, db: Session = Depends(get_db)):
    return curd.create_author(db=db, author=author)

# @app.post("/book/",response_model=schema.Book)
# def create_books(books:schema.BookCreate, db:Session=Depends(get_db)):
#     return curd.create_book(db=db , book=books)

@app.post("/book/", response_model=schema.Book)
def create_books(books: schema.BookCreate, db: Session = Depends(get_db)):
    return curd.create_book(db=db, books=books)

# @app.post("/loan/",response_model=schema.Loan)
# def create_loan(loans:schema.LoanCreate , db: Session=Depends(get_db)):
#     return curd.create_loan(db=db , loans=loans)

@app.post("/loan/", response_model=schema.Loan)
def create_loan(loans: schema.LoanCreate, db: Session = Depends(get_db)):
    return curd.create_loan(db=db , loan=loans)


@app.post("/loan_history/", response_model=schema.LoanHistory)
def create_loan_history(loan_history: schema.LoanHistoryCreate, db: Session = Depends(get_db)):
    return curd.create_loan_history(db=db, loan_history=loan_history)

@app.get("/loan_history/{loan_id}", response_model=List[schema.LoanHistory])
def get_loan_history(loan_id: int, db: Session = Depends(get_db)):
    loan_history = curd.get_loan_history(db=db, loan_id=loan_id)
    if not loan_history:
        raise HTTPException(status_code=404, detail="Loan history not found")
    return loan_history

# @app.get("/loan_history/{history_id}", response_model=schema.LoanHistory)
# def get_loan_history_by_id(history_id: int, db: Session = Depends(get_db)):
#     loan_history = curd.get_loan_history_by_id(db=db, history_id=history_id)
#     if not loan_history:
#         raise HTTPException(status_code=404, detail="Loan history not found")
#     return loan_history

# @app.post("/loan_history/", response_model=schema.LoanHistory)
# def create_loan_history(loan_history: schema.LoanHistoryCreate, db: Session = Depends(get_db)):
#     return curd.create_loan_history(db=db, loan_history=loan_history)


# getapi for user
@app.get("/user/{user_id}",response_model=schema.User)
def read_user(user_id:int, db:Session=Depends(get_db)):
    db_user = curd.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Endpoint to get a list of users
# @app.get("/users/", response_model=List[schema.User])
# def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     users = curd.get_all_users(db, skip=skip, limit=limit)
#     return users

@app.get("/users/", response_model=List[schema.User])
def read_users(db: Session = Depends(get_db)):
    users = curd.get_all_users(db)  # No need for skip and limit
    return users

# this api for return user data in html page
# @app.get("/user", response_class=HTMLResponse)
# def getuserdata_htmlpage(request: Request, db: Session = Depends(get_db)):
#     users = curd.get_all_users(db)
#     return templates.TemplateResponse("user.html", {"request": request, "users": users})
@app.get("/user", response_class=HTMLResponse)
def getuserdata_htmlpage(request: Request, db: Session = Depends(get_db)):
    users = curd.get_all_users(db)
    return templates.TemplateResponse("user.html", {"request": request, "users": users})
