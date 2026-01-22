"""
FASTAPI – DAY 3
================

Topics Covered (from video):
1. Project Overview
2. HTTP Methods
3. HTTP Methods Demo
4. Small Project using FastAPI

--------------------------------------------------
WHAT ARE HTTP METHODS?
--------------------------------------------------
HTTP methods define what action the client wants
to perform on the server.

Common HTTP Methods:
GET     -> Read data
POST    -> Create data
PUT     -> Update entire data
PATCH   -> Update partial data
DELETE  -> Delete data
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --------------------------------------------------
# CREATE FASTAPI APP
# --------------------------------------------------
app = FastAPI(
    title="FastAPI Day 3 - HTTP Methods",
    description="Understanding GET, POST, PUT, DELETE with demo project",
    version="1.0"
)

# --------------------------------------------------
# DUMMY DATABASE (IN-MEMORY)
# --------------------------------------------------
items_db = {}

# --------------------------------------------------
# DATA MODEL USING PYDANTIC
# --------------------------------------------------
class Item(BaseModel):
    name: str
    price: float
    available: bool = True

# --------------------------------------------------
# GET METHOD
# --------------------------------------------------
@app.get("/")
def home():
    """
    GET method example
    """
    return {"message": "FastAPI Day 3 - HTTP Methods"}

@app.get("/items")
def get_all_items():
    """
    GET all items
    """
    return items_db

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    GET item by ID
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# --------------------------------------------------
# POST METHOD
# --------------------------------------------------
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    """
    POST - Create new item
    """
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    items_db[item_id] = item
    return {
        "message": "Item created successfully",
        "item": item
    }

# --------------------------------------------------
# PUT METHOD
# --------------------------------------------------
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    PUT - Update existing item completely
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    items_db[item_id] = item
    return {
        "message": "Item updated successfully",
        "item": item
    }

# --------------------------------------------------
# DELETE METHOD
# --------------------------------------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    DELETE - Remove item
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id]
    return {"message": "Item deleted successfully"}

# --------------------------------------------------
# HOW TO RUN
# --------------------------------------------------
"""
1. Install dependencies:
   pip install fastapi uvicorn

2. Run server:
   uvicorn Day_3:app --reload

3. Open Swagger UI:
   http://127.0.0.1:8000/docs

Try all HTTP methods directly from Swagger UI.
"""
