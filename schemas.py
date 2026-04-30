from pydantic import BaseModel
from typing import Optional, List


class AuthorCreate(BaseModel):
    name: str
    bio: str


class BookCreate(BaseModel):
    title: str
    author_id: int
    publication_date: str
    summary: str


class Book(BaseModel):
    id: int
    title: str
    summary: str
    author_id: int
    publication_date: str
    author: Optional[AuthorCreate] = None


class Author(BaseModel):
    id: int
    name: str
    bio: str
    books: List[Book] = []
