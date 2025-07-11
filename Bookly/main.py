from typing import Optional,List
from fastapi import FastAPI, Header, status
from pydantic import BaseModel

app = FastAPI()

books= []
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    language: str
    page_count: int

@app.get("/")
async def read_root():
    return {"message": "Welcome to Bookly API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/greet")
async def greet_user(name: Optional[str] = "User", age: Optional[int] = 1) -> dict:
    if age < 0:
        return {"error": "Age cannot be negative"}
    return {"message": f"Hello, {name}! You are {age} years old."}
   
@app.get("/get_headers",status_code=200)
async def get_headers(accept:str = Header(None), content_type: str = Header(None),user_agent: str = Header(None),host: str = Header(None)):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers

    
    
@app.get("/books",response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}, 404

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_data: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = book_data
            return book_data
    return {"error": "Book not found"}, 404

@app.post("/books",status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book: Book)-> dict:
    new_book = book.model_dump
    books.append(new_book)
    return new_book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}, 404

