from fastapi import FastAPI, Query, Path
from models.books import Book
from routers.books import router as books_router

app = FastAPI()
app.include_router(books_router)




@app.get('/')
def Bookstore():
    return "Hello readers"

