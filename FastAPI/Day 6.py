"""
FASTAPI – DAY 6
================

Topic: CREATE Endpoint using Request Body (POST)

What we build today:
- Patient Management System
- Create new patient record
- Store data in JSON file (database)
- Use Pydantic for validation
- Use computed fields (BMI & Verdict)
- Proper HTTP status codes & error handling
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator
from typing import Literal
import json
import os

# --------------------------------------------------
# APP INITIALIZATION
# --------------------------------------------------
app = FastAPI(
    title="FastAPI Day 6 - Create Endpoint",
    description="Patient Management System - Create Patient",
    version="1.0"
)

DB_FILE = "patients.json"

# --------------------------------------------------
# UTILITY FUNCTIONS (LOAD & SAVE DATA)
# --------------------------------------------------
def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# --------------------------------------------------
# PYDANTIC MODEL (REQUEST BODY)
# --------------------------------------------------
class Patient(BaseModel):
    id: int
    name: str
    city: str
    age: int = Field(..., gt=0)
    gender: Literal["Male", "Female", "Others"]
    height: float = Field(..., gt=0)   # in meters
    weight: float = Field(..., gt=0)   # in kg

    # ------------------------------
    # FIELD VALIDATOR
    # ------------------------------
    @field_validator("name")
    @classmethod
    def name_length(cls, value):
        if len(value) < 3:
            raise ValueError("Name must have at least 3 characters")
        return value

    # ------------------------------
    # COMPUTED FIELD - BMI
    # ------------------------------
    @property
    def bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    # ------------------------------
    # COMPUTED FIELD - VERDICT
    # ------------------------------
    @property
    def verdict(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

# --------------------------------------------------
# CREATE ENDPOINT
# --------------------------------------------------
@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_patient(patient: Patient):
    """
    Create a new patient record
    """
    data = load_data()

    # Check if patient already exists
    if str(patient.id) in data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient with this ID already exists"
        )

    # Store patient data
    data[str(patient.id)] = {
        "name": patient.name,
        "city": patient.city,
        "age": patient.age,
        "gender": patient.gender,
        "height": patient.height,
        "weight": patient.weight,
        "bmi": patient.bmi,
        "verdict": patient.verdict
    }

    save_data(data)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "Patient created successfully",
            "patient_id": patient.id,
            "bmi": patient.bmi,
            "verdict": patient.verdict
        }
    )

# --------------------------------------------------
# HOW TO RUN
# --------------------------------------------------
"""
1. Install dependencies:
   pip install fastapi uvicorn

2. Run server:
   uvicorn Day_6:app --reload

3. Open Swagger UI:
   http://127.0.0.1:8000/docs

4. Test POST /create with JSON body:
{
  "id": 1,
  "name": "Rahul Sharma",
  "city": "Delhi",
  "age": 28,
  "gender": "Male",
  "height": 1.75,
  "weight": 72
}
"""

