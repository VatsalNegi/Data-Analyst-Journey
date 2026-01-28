"""
FASTAPI – DAY 8
================

Topic: Serving Machine Learning Models using FastAPI

Project:
- Insurance Premium Prediction
- Input user details
- Predict premium category: Low / Medium / High

Key Concepts:
- Loading trained ML model
- Request Body using Pydantic
- Feature Engineering inside API
- POST endpoint for prediction
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import pickle
import pandas as pd

# --------------------------------------------------
# LOAD TRAINED ML MODEL
# --------------------------------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------
app = FastAPI(
    title="Insurance Premium Prediction API",
    description="Serving ML model using FastAPI",
    version="1.0"
)

# --------------------------------------------------
# INPUT DATA MODEL (REQUEST BODY)
# --------------------------------------------------
class UserInput(BaseModel):
    age: int = Field(..., gt=0)
    height: float = Field(..., gt=0)   # in meters
    weight: float = Field(..., gt=0)   # in kg
    income: int = Field(..., gt=0)
    smoker: Literal["yes", "no"]
    city: Literal["tier_1", "tier_2", "tier_3"]
    occupation: Literal["private", "government", "business", "student"]

    # ------------------------------
    # COMPUTED FEATURE: BMI
    # ------------------------------
    @property
    def bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    # ------------------------------
    # COMPUTED FEATURE: AGE GROUP
    # ------------------------------
    @property
    def age_group(self):
        if self.age < 30:
            return "young"
        elif self.age < 50:
            return "adult"
        else:
            return "senior"

    # ------------------------------
    # COMPUTED FEATURE: LIFESTYLE RISK
    # ------------------------------
    @property
    def lifestyle_risk(self):
        if self.smoker == "yes" and self.bmi > 30:
            return "high"
        elif self.smoker == "yes":
            return "medium"
        else:
            return "low"

# --------------------------------------------------
# PREDICTION ENDPOINT
# --------------------------------------------------
@app.post("/predict")
def predict_premium(user: UserInput):
    """
    Predict insurance premium category
    """

    # Convert input to DataFrame
    input_data = pd.DataFrame([{
        "age": user.age,
        "income": user.income,
        "bmi": user.bmi,
        "age_group": user.age_group,
        "lifestyle_risk": user.lifestyle_risk,
        "city": user.city,
        "occupation": user.occupation,
        "smoker": user.smoker
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    return {
        "premium_category": prediction
    }

# --------------------------------------------------
# HOW TO RUN
# --------------------------------------------------
"""
1. Install dependencies:
   pip install fastapi uvicorn pandas scikit-learn

2. Place model.pkl in same directory

3. Run server:
   uvicorn Day_8:app --reload

4. Open Swagger UI:
   http://127.0.0.1:8000/docs

5. Test POST /predict
"""

