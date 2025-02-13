from fastapi import FastAPI
import requests

app = FastAPI()

BOOK_SERVICE_URL = "http://127.0.0.1:8001"
ORDER_SERVICE_URL = "http://127.0.0.1:8002"
USER_SERVICE_URL = "http://127.0.0.1:8003"

@app.get("/books")
def get_books():
    response = requests.get(f"{BOOK_SERVICE_URL}/books/")
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
def create_book(book: dict):
    response = requests.post(f"{BOOK_SERVICE_URL}/create/book/", json=book)
    return response.json()


@app.post("/usertype/create")
def usertype_create(user:dict):
    response = requests.post(f"{USER_SERVICE_URL}/usertype/create", json=user)
    return response.json()