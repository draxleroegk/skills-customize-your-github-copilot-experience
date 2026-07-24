"""Starter code for the FastAPI REST APIs assignment.

Run locally:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0, le=2100)


class Book(BookCreate):
    id: int


books: List[Book] = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    Book(id=2, title="1984", author="George Orwell", year=1949),
]


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to the Book API"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    return books


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate) -> Book:
    next_id = max((book.id for book in books), default=0) + 1
    new_book = Book(id=next_id, **book_data.model_dump())
    books.append(new_book)
    return new_book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"message": f"Book {book_id} deleted"}
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


# Example request:
# POST /books
# {
#   "title": "Dune",
#   "author": "Frank Herbert",
#   "year": 1965
# }
#
# Example response (201):
# {
#   "id": 3,
#   "title": "Dune",
#   "author": "Frank Herbert",
#   "year": 1965
# }
