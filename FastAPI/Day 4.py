"""
FASTAPI – DAY 4
================

Topics Covered:
1. Path Parameters
2. Path Functions
3. HTTP Status Codes
4. Query Parameters
5. Complete Code Demo

--------------------------------------------------
PATH PARAMETERS
--------------------------------------------------
Path parameters are variables in the URL path.
They are used to identify specific resources.

Example:
GET /users/5
Here, 5 is a path parameter.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# --------------------------------------------------
# CREATE FASTAPI APP
# --------------------------------------------------
app = FastAPI(
    title="FastAPI Day 4",
    description="Path Params, Query Params & Status Codes",
    version="1.0"
)

# --------------------------------------------------
# DUMMY DATABASE
# --------------------------------------------------
users_db = {
    1: {"name": "Vatsal", "role": "Student"},
    2: {"name": "Aman", "role": "Developer"}
}

# --------------------------------------------------
# PATH PARAMETER EXAMPLE
# --------------------------------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Get user using path parameter
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return users_db[user_id]

# --------------------------------------------------
# PATH FUNCTION EXAMPLE
# --------------------------------------------------
@app.get("/square/{number}")
def square_number(number: int):
    """
    Path function that returns square of a number
    """
    return {
        "number": number,
        "square": number * number
    }

# --------------------------------------------------
# HTTP STATUS CODES
# --------------------------------------------------
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, name: str, role: str):
    """
    Create new user with status code
    """
    if user_id in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    users_db[user_id] = {"name": name, "role": role}
    return {
        "message": "User created successfully",
        "user": users_db[user_id]
    }

# --------------------------------------------------
# QUERY PARAMETER
# --------------------------------------------------
@app.get("/search")
def search_user(role: str = None):
    """
    Query parameter example
    """
    if role is None:
        return users_db

    filtered_users = {
        uid: user for uid, user in users_db.items()
        if user["role"].lower() == role.lower()
    }

    return filtered_users

# --------------------------------------------------
# COMBINED PATH + QUERY PARAMETER
# --------------------------------------------------
@app.get("/users/{user_id}/details")
def user_details(user_id: int, show_role: bool = True):
    """
    Combination of path and query parameter
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user = users_db[user_id]

    if show_role:
        return user
    else:
        return {"name": user["name"]}

# --------------------------------------------------
# HOW TO RUN
# --------------------------------------------------
"""
1. Install:
   pip install fastapi uvicorn

2. Run server:
   uvicorn Day_4:app --reload

3. Open browser:
   http://127.0.0.1:8000/docs

4. Try:
   GET  /users/1
   GET  /square/5
   POST /users?user_id=3&name=Riya&role=ML
   GET  /search?role=Developer
   GET  /users/1/details?show_role=false
"""

