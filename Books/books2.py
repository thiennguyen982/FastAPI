from fastapi import FastAPI, Body, Path, Query, HTTPException
from models import Book, BookRequest
from starlette import status

app = FastAPI()

Books = [
    Book(1, "Computer Science 1", "CodingWithThroby 1", "Useful Books", 5, 2012),
    Book(2, "Computer Science 2", "CodingWithThroby 2", "Useful Books", 5, 2012),
    Book(3, "Computer Science 3", "CodingWithThroby 3", "Useful Books", 5, 2018),
    Book(4, "Computer Science 4", "CodingWithThroby 4", "Useful Books", 5, 2018),
    Book(5, "Computer Science 5", "CodingWithThroby 5", "Useful Books", 5, 2019),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return Books

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id : int = Path(gt=0)):
    for book in Books:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=404,
        detail='Items is not found in list'
    )
        
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(book_rating : int = Query(gt=0, lt=6)):
    books_return = []
    for book in Books:
        if book.rating == book_rating:
            books_return.append(book)
    return books_return

@app.get("/books/by_year/", status_code=status.HTTP_200_OK)
async def read_books_by_year(year : int = Query(gt=0, lt=3000)):
    books_return = []
    for book in Books:
        if book.published_date == year:
            books_return.append(book)
    return books_return

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(find_book_id(new_book))

def find_book_id(book : Book) -> Book:
    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book : BookRequest):
    book_changed = False
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(
            status_code=404,
            detail='Items is not found in list'
        )

@app.delete("/books/delete_book/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id : int = Query(gt=0)):
    book_deleted = False
    for i in range(len(Books)):
        if Books[i].id == book_id:
            Books.pop(i)
            book_deleted = True
    if not book_deleted:
        raise HTTPException(
            status_code=404,
            detail='No Books Is Deleted In List'
        )