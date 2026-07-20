from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()
print("Hello World")


@app.get("/")
def home():
    return {"message": "Hello World"}


# query parameters
@app.get("/customer/")
def get_customer(name: str, age: int):
    return {"name": name, "age": age}

# path parameters
@app.get("/customer/{customer_id}")
def get_customer_by_id(customer_id: int):
    return {"customer_id": customer_id}


# request body
@app.post("/customer/")
def create_customer(request: Request):
    query_params = Request.query_params
    
    customer = request.json()
    return {"greet": f"Hi {query_params['name']}, your age is {query_params['age']}", "customer": customer}



## different types of HTTP methods 
## 1. GET - to retrieve data from the server
## 2. POST - to create new data on the server
## 3. PUT - to update existing data on the server
## 4. DELETE - to delete data from the server

PRODUCTS = {
    "p1": {"name": "Product 1", "price": 100},
    "p2": {"name": "Product 2", "price": 200},
    "p3": {"name": "Product 3", "price": 300}
}

@app.get("/products/")
def get_products(product_id: str = None):
    if product_id:
        product = PRODUCTS.get(product_id)
        if product:
            return {"product": product}
        else:
            return {"message": "Product not found"}
    else:
        return {"products": PRODUCTS}


class Product(BaseModel):
    name: str
    price: int 


@app.post("/create_product/")
def create_products(payload: Product):
    product_id = f"p{len(PRODUCTS) + 1}"
    PRODUCTS[product_id] = payload.dict()
    return {"message": "Product created successfully", "product_id": product_id, "product": payload.dict()}

@app.put("/update_product/{product_id}")
def update_product(product_id: str, payload: Product):
    if product_id in PRODUCTS:
        PRODUCTS[product_id] = payload.dict()
        return {"message": "Product updated successfully", "product_id": product_id, "product": payload.dict()}




## How to validate data in FastAPI

