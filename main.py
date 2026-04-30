from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
import crud
import schemas
from typing import List


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    return db


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)


@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0,
                 limit: int = 100,
                 db: Session = Depends(get_db)):
    return crud.get_authors(db, skip=skip, limit=limit)


@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_author(db, author_id)


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0,
               limit: int = 100,
               author_id: int = None,
               db: Session = Depends(get_db)):
    return crud.get_books(db, author_id=author_id, skip=skip, limit=limit)
