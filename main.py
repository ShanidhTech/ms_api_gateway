from fastapi import FastAPI, HTTPException, Header, Path
import requests

app = FastAPI()

BOOK_SERVICE_URL = "http://127.0.0.1:8001"
ORDER_SERVICE_URL = "http://127.0.0.1:8002"
USER_SERVICE_URL = "http://127.0.0.1:8003"

@app.get("/books")
def get_books(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token is required")

    headers = {"Authorization": authorization} 
    response = requests.get(f"{BOOK_SERVICE_URL}/books/", headers=headers)
    return response.json()

@app.post("/orders")
def create_order(order: dict):
    response = requests.post(f"{ORDER_SERVICE_URL}/orders/", json=order)
    return response.json()

@app.post("/users")
def create_user(user: dict):
    response = requests.post(f"{USER_SERVICE_URL}/users/", json=user)
    return response.json()


@app.post("/register/user")
def register_user(user:dict):
    response = requests.post(f"{USER_SERVICE_URL}/register/user", json=user)
    return response.json()

@app.post("/login/")
def register_user(user:dict):
    response = requests.post(f"{USER_SERVICE_URL}/login/", json=user)
    return response.json()


@app.post("/create/book/")
def create_book(book: dict, authorization: str = Header(None)):
    """Pass JWT token when calling Book Service API"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token is required")

    headers = {"Authorization": authorization}  # Forward token to Book Service
    response = requests.post(f"{BOOK_SERVICE_URL}/create/book/", json=book, headers=headers)
    
    return response.json()


@app.post("/usertype/create")
def usertype_create(user:dict):
    response = requests.post(f"{USER_SERVICE_URL}/usertype/create", json=user)
    return response.json()


@app.patch("/update/book/{book_id}")
def update_book(book_id: int = Path(...), book_data: dict = {}, authorization: str = Header(None)):
    """Update book details (supports partial updates)"""

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token is required")

    headers = {"Authorization": authorization}  # Forward token to Book Service
    response = requests.patch(f"{BOOK_SERVICE_URL}/update/book/{book_id}/", json=book_data, headers=headers)
    
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Book not found")
    if response.status_code == 403:
        raise HTTPException(status_code=403, detail="Not authorized to update this book")
    
    return response.json()


@app.patch("/update/status/{book_id}")
def update_book(book_id: int = Path(...), book_data: dict = {}, authorization: str = Header(None)):
    """Update book details (supports partial updates)"""

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token is required")

    headers = {"Authorization": authorization}  # Forward token to Book Service
    response = requests.patch(f"{BOOK_SERVICE_URL}/update/status/{book_id}/", json=book_data, headers=headers)
    
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Book not found")
    if response.status_code == 403:
        raise HTTPException(status_code=403, detail="Not authorized to update this book")
    
    return response.json()    