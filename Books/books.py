from fastapi import FastAPI, Body

app = FastAPI()

Books = [
    {'Title': 'Angels And Demon', 'Author': 'Dan Brown', 'Category': 'Sci-Fic'},
    {'Title': 'Sherlock Holmes', 'Author': 'Conan Doyle', 'Category': 'Investigation'},
    {'Title': 'The DaVinci Code', 'Author': 'Dan Brown', 'Category': 'Sci-Fic'},
    {'Title': 'Never Failed, All Is Changes', 'Author': 'Chung Kim Sook', 'Category': 'Motivation'},
    {'Title': 'Tam Quốc Diễn Nghĩa', 'Author': 'La Quán Trung', 'Category': 'Historical Novels'},
]

@app.get("/")
async def index():
    return {
        "Details": "Index"
    } 

@app.get("/books")
async def first_api():
    return Books

@app.get("/books/{book_title}")
async def read_book(book_title : str):
    for book in Books:
        if book.get("Title").casefold() == book_title.casefold():
            return book
        else:
            return {
                "Message": "Not Found"
            }
        
@app.get("/books/")
async def read_books_by_the_category(category : str):
    books_to_return = []
    for book in Books:
        if book.get("Category").casefold() == category.casefold():
            books_to_return.append(book)
    if not books_to_return:
        return {
            "Message": "Found Nothing"
        }
    return books_to_return

@app.get("/books/by_author/")
async def read_books_by_the_author(author_name : str):
    books_to_return = []
    for book in Books:
        if book.get("Author").casefold() == author_name.casefold():
            books_to_return.append(book)
    if not books_to_return:
        return {
            "Message": "Found Nothing"
        }
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_and_by_category(book_author : str, category : str):
    books_to_return = []
    for book in Books:
        if book.get("Category").casefold() == category.casefold() and book.get("Author").casefold() == book_author.casefold():
            books_to_return.append(book)
    if not books_to_return:
        return {
            "Message": "Found Nothing"
        }
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    Books.append(new_book)

@app.put("/books/update_book")
async def update_book(update_book = Body()):
    result = []
    for i in range(len(Books)):
        if Books[i].get("Title").casefold() == update_book.get("Title").casefold():
            Books[i] = update_book
            result.append("Y")
    if not result:
        return {
            "Message": "No Updated"
        }
    else:
        return {
            "Message": "Updated Successfully",
            "Status": 200
        }
    
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title : str):
    result = []
    for book in Books:
        if book.get("Title").casefold() == book_title.casefold():
            Books.remove(book)
            result.append("Y")
            break
    if result:
        return {
            "Message": "Delete Successful",
            "Status": 200
        }
    else:
        return {
            "Message": "No Delete"
        }