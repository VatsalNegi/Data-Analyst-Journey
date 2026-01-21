"""
FASTAPI – DAY 1
================

Topics Covered (from video):
1. What is an API?
2. API Analogy (Restaurant Example)
3. Need for APIs
4. API from Machine Learning Perspective
5. Introduction to FastAPI
6. Creating First FastAPI App

--------------------------------------------------
WHAT IS AN API?
--------------------------------------------------
API stands for Application Programming Interface.

An API is a set of rules that allows one software application
(frontend, mobile app, ML model, etc.) to communicate with
another software application (backend, server, database).

In simple words:
API = Medium of communication between two systems
"""

# --------------------------------------------------
# API ANALOGY (RESTAURANT EXAMPLE)
# --------------------------------------------------
"""
Customer  -> Frontend (User)
Waiter    -> API
Kitchen   -> Backend / Server

Customer places an order  -> Request
Kitchen prepares food     -> Processing
Waiter brings food back   -> Response
"""

# --------------------------------------------------
# NEED FOR APIs
# --------------------------------------------------
"""
1. Separation of frontend and backend
2. Security (direct DB access is avoided)
3. Scalability
4. Reusability (same API for web, mobile, ML models)
5. Platform independence
"""

# --------------------------------------------------
# API FROM MACHINE LEARNING PERSPECTIVE
# --------------------------------------------------
"""
In ML:
- Model is trained offline
- Model is deployed on a server
- API is used to send input data to the model
- API returns predictions as output

Example:
Frontend/App  -> API -> ML Model -> Prediction
"""

# --------------------------------------------------
# INTRODUCTION TO FASTAPI
# --------------------------------------------------
"""
FastAPI is a modern Python web framework used to build APIs.

Why FastAPI?
- Very fast (built on Starlette & Pydantic)
- Automatic API documentation
- Easy to learn
- Ideal for ML & Data Science projects
"""

# --------------------------------------------------
# CREATING FIRST FASTAPI APPLICATION
# --------------------------------------------------

from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI(
    title="FastAPI Day 1",
    description="Introduction to APIs and FastAPI",
    version="1.0"
)

# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------
@app.get("/")
def home():
    """
    Root endpoint.
    Access: http://127.0.0.1:8000/
    """
    return {
        "message": "Welcome to FastAPI - Day 1",
        "status": "API is working successfully"
    }

# --------------------------------------------------
# SIMPLE GET API
# --------------------------------------------------
@app.get("/about")
def about_api():
    """
    Basic API to explain purpose.
    Access: http://127.0.0.1:8000/about
    """
    return {
        "framework": "FastAPI",
        "use_case": "Building APIs for Web & ML",
        "day": 1
    }

# --------------------------------------------------
# HOW TO RUN THIS APPLICATION
# --------------------------------------------------
"""
1. Install required libraries:
   pip install fastapi uvicorn

2. Run the server:
   uvicorn Day_1:app --reload

3. Open browser:
   http://127.0.0.1:8000/docs   -> Swagger UI
   http://127.0.0.1:8000/redoc -> ReDoc UI
"""

