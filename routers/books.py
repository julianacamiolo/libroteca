from fastapi import APIRouter
from models.books import Book
from typing import List
from fastapi import Query, Path

router = APIRouter()

books = [
    Book(id=1, name="Book 1", price=100, stock=10),
    Book(id=2, name="Book 2", price=200, stock=20)
]

@router.get('/books', response_model=List[Book])
def get_books():
    return books

@router.get('/books/{book_id}', response_model=Book)
def read_any_book(book_id: int = Path(..., gt=0)):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        return {"error": "Book not found"}
    return book

@router.get('/books/query/', response_model=List[Book])
def get_books_by_stock_price(stock: int = None, price: float = Query(..., gt=0)):
    filtered_books = books

    if stock is not None:
        filtered_books = [b for b in filtered_books if b.stock == stock]
    
    if price is not None:
        filtered_books = [b for b in filtered_books if b.price == price]

    return filtered_books

@router.post('/books')
def choose_book(book: Book):
    books.append(book)
    return book

@router.put('/books/{id}')
def update_book(id: int, book: Book):
    for index, item in enumerate(books):
        if item.id == id:
            books[index] = book
            break
    return book

@router.delete("/books/{id}")
def delete_book(id: int):
    global books
    books = [item for item in books if item.id != id]
    return books