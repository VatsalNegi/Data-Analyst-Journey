"""
FASTAPI – DAY 2
================

Topics Covered (from video):
1. Philosophy of FastAPI
2. Why FastAPI is fast to code
3. FastAPI Architecture (Starlette + Pydantic)
4. Installation
5. Code Demo (First Practical App)

--------------------------------------------------
PHILOSOPHY OF FASTAPI
--------------------------------------------------
FastAPI is designed with these goals:
1. Fast to run (high performance)
2. Fast to code (developer productivity)
3. Fewer bugs
4. Easy to learn
5. Easy to scale

FastAPI follows modern Python standards and type hints.
"""

# --------------------------------------------------
# FASTAPI ARCHITECTURE
# --------------------------------------------------
"""
FastAPI internally uses:

1. Starlette
   - Handles routing
   - Manages requests & responses
   - ASGI framework (very fast)

2. Pydantic
   - Data validation
   - Data parsing
   - Uses Python type hints

Flow:
Client -> FastAPI -> Starlette -> Pydantic -> Response
"""

# --------------------------------------------------
# WHY FASTAPI IS FAST TO CODE
# --------------------------------------------------
"""
1. Automatic data validation
2. Automatic documentation
3. Less boilerplate code
4. Type hints reduce errors
5. Built-in Swagger UI

You write less code but get more functionality.
"""

# --------------------------------------------------
# INSTALLATION
# --------------------------------------------------
"""
Install FastAPI and Uvicorn:

pip install fastapi uvicorn
"""

# --------------------------------------------------
# CODE DEMO STARTS HERE
# --------------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(
    title="FastAPI Day 2",
    description="Understanding FastAPI philosophy and basic API demo",
    version="1.0"
)

# --------------------------------------------------
# SIMPLE GET API
# --------------------------------------------------
@app.get("/")
def read_root():
    """
    Root endpoint
    """
    return {"message": "FastAPI Day 2 is running successfully"}

# --------------------------------------------------
# PATH PARAMETER EXAMPLE
# --------------------------------------------------
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Path parameter example
    """
    return {
        "item_id": item_id,
        "info": "This data came from path parameter"
    }

# --------------------------------------------------
# QUERY PARAMETER EXAMPLE
# --------------------------------------------------
@app.get("/search")
def search_item(q: str = None):
    """
    Query parameter example
    """
    return {
        "search_query": q
    }

# --------------------------------------------------
# REQUEST BODY USING PYDANTIC
# --------------------------------------------------
class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user")
def create_user(user: User):
    """
    Accepts JSON body and validates automatically
    """
    return {
        "message": "User created successfully",
        "user_data": user
    }

# --------------------------------------------------
# HOW TO RUN THIS APPLICATION
# --------------------------------------------------
"""
1. Run server:
   uvicorn Day_2:app --reload

2. Open browser:
   http://127.0.0.1:8000/docs   -> Swagger UI
   http://127.0.0.1:8000/redoc -> ReDoc UI

3. Try:
   GET  /
   GET  /items/5
   GET  /search?q=fastapi
   POST /user
"""

