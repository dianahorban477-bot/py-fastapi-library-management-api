from sqlalchemy.orm import Session
import schemas
import models
from typing import List


def get_author(db: Session, author_id: int)\
        -> models.Author:
    return db.query(models.Author).get(author_id)


def get_authors(db: Session, skip: int = 0, limit: int = 100)\
        -> List[models.Author]:
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate)\
        -> models.Author:
    db_author = models.Author(
         name=author.name,
         bio=author.bio
     )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_books(db: Session,
              author_id: int = None,
              skip: int = 0,
              limit: int = 100)\
        -> List[models.Book]:
    query = db.query(models.Book)
    if author_id is not None:
        query = query.filter(models.Book.author_id == author_id)
    return query.offset(skip).limit(limit).all()


def create_book(db: Session, new_book: schemas.BookCreate)\
        -> models.Book:
    db_book = models.Book(
        title=new_book.title,
        author_id=new_book.author_id,
        summary=new_book.summary,
        publication_date=new_book.publication_date
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books_by_author(db: Session,
                        author_id: int,
                        skip: int = 0,
                        limit: int = 100)\
        -> List[models.Book]:
    query = db.query(models.Book)
    query = query.filter(models.Book.author_id == author_id)
    return query.offset(skip).limit(limit).all()
