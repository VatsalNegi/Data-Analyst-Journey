"""
FASTAPI – DAY 7
================

Topic: UPDATE & DELETE Endpoints (CRUD)

What we build today:
- Update existing patient (PUT)
- Partial updates using optional fields
- Re-validation using Pydantic
- Delete patient (DELETE)
- JSON file as database
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, Literal
import json
import os

# --------------------------------------------------
# APP INITIALIZATION
# --------------------------------------------------
app = FastAPI(
    title="FastAPI Day 7 - Update & Delete",
    description="Patient Management System - Update & Delete APIs",
    version="1.0"
)

DB_FILE = "patients.json"

# --------------------------------------------------
# UTILITY FUNCTIONS
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
# MAIN PATIENT MODEL (FROM DAY 6)
# --------------------------------------------------
class Patient(BaseModel):
    id: int
    name: str
    city: str
    age: int = Field(..., gt=0)
    gender: Literal["Male", "Female", "Others"]
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)

    @property
    def bmi(self):
        return round(self.weight / (self.height ** 2), 2)

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
# PATIENT UPDATE MODEL (ALL FIELDS OPTIONAL)
# --------------------------------------------------
class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = Field(None, gt=0)
    gender: Optional[Literal["Male", "Female", "Others"]] = None
    height: Optional[float] = Field(None, gt=0)
    weight: Optional[float] = Field(None, gt=0)

# --------------------------------------------------
# UPDATE ENDPOINT (PUT)
# --------------------------------------------------
@app.put("/update/{patient_id}")
def update_patient(patient_id: int, update_data: PatientUpdate):
    """
    Update existing patient data
    """
    data = load_data()

    if str(patient_id) not in data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Existing patient data
    existing_patient = data[str(patient_id)]

    # Update only provided fields
    update_dict = update_data.model_dump(exclude_unset=True)
    existing_patient.update(update_dict)

    # Re-validate using Patient model
    validated_patient = Patient(
        id=patient_id,
        **existing_patient
    )

    # Save updated data
    data[str(patient_id)] = {
        "name": validated_patient.name,
        "city": validated_patient.city,
        "age": validated_patient.age,
        "gender": validated_patient.gender,
        "height": validated_patient.height,
        "weight": validated_patient.weight,
        "bmi": validated_patient.bmi,
        "verdict": validated_patient.verdict
    }

    save_data(data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Patient updated successfully",
            "patient_id": patient_id,
            "bmi": validated_patient.bmi,
            "verdict": validated_patient.verdict
        }
    )

# --------------------------------------------------
# DELETE ENDPOINT (DELETE)
# --------------------------------------------------
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: int):
    """
    Delete patient by ID
    """
    data = load_data()

    if str(patient_id) not in data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    del data[str(patient_id)]
    save_data(data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Patient deleted successfully",
            "patient_id": patient_id
        }
    )

# --------------------------------------------------
# HOW TO RUN
# --------------------------------------------------
"""
1. Run server:
   uvicorn Day_7:app --reload

2. Open:
   http://127.0.0.1:8000/docs

3. Test:
   PUT    /update/1
   DELETE /delete/1
"""

