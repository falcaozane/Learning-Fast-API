from typing import Optional
from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

class BookModel(BaseModel):
    title: str
    author: str
    year: int

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

@app.post("/create_book")
async def create_book(book_data:BookModel):
    return {
        "message": "Book created successfully",
        "book": {
            "title": book_data.title,
            "author": book_data.author,
            "year": book_data.year
        }
    }
    
    
@app.get("/get_headers",status_code=200)
async def get_headers(accept:str = Header(None), content_type: str = Header(None),user_agent: str = Header(None),host: str = Header(None)):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers