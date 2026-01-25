"""
FASTAPI – DAY 5
================

Topics Covered:
1. Why is Pydantic used?
2. How does Pydantic work?
3. Field Validators
4. Model Validators
5. Computed Fields
6. Nested Models
7. Serialization

--------------------------------------------------
WHY IS PYDANTIC USED?
--------------------------------------------------
Pydantic is used for:
- Data validation
- Type checking
- Automatic error handling
- Clean request & response bodies

FastAPI uses Pydantic internally to:
✔ Validate incoming data
✔ Convert data types
✔ Generate API documentation
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, List

app = FastAPI(
    title="FastAPI Day 5 - Pydantic Deep Dive",
    description="Understanding Pydantic models, validation & serialization",
    version="1.0"
)

# --------------------------------------------------
# BASIC PYDANTIC MODEL
# --------------------------------------------------
class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user/basic")
def create_basic_user(user: User):
    return user

"""
Pydantic automatically:
- Checks data types
- Converts data if possible
- Throws error if data is invalid
"""

# --------------------------------------------------
# FIELD VALIDATOR
# --------------------------------------------------
class Employee(BaseModel):
    name: str
    salary: int = Field(..., gt=0)

    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, value):
        if len(value) < 3:
            raise ValueError("Name must have at least 3 characters")
        return value

@app.post("/employee")
def create_employee(emp: Employee):
    return emp

"""
Field validators validate individual fields.
"""

# --------------------------------------------------
# MODEL VALIDATOR
# --------------------------------------------------
class Student(BaseModel):
    marks: int
    pass_marks: int

    @model_validator(mode="after")
    def check_marks(cls, values):
        if values.marks < values.pass_marks:
            raise ValueError("Student has failed")
        return values

@app.post("/student")
def create_student(student: Student):
    return {"status": "Passed", "data": student}

"""
Model validators validate the entire model.
"""

# --------------------------------------------------
# COMPUTED FIELDS
# --------------------------------------------------
class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @property
    def total_price(self):
        return self.price * self.quantity

@app.post("/product")
def create_product(product: Product):
    return {
        "name": product.name,
        "total_price": product.total_price
    }

"""
Computed fields are derived values.
They are not sent by user but calculated internally.
"""

# --------------------------------------------------
# NESTED MODELS
# --------------------------------------------------
class Address(BaseModel):
    city: str
    pincode: int

class Customer(BaseModel):
    name: str
    email: str
    address: Address

@app.post("/customer")
def create_customer(customer: Customer):
    return customer

"""
Nested models help represent real-world data.
"""

# --------------------------------------------------
# SERIALIZATION
# --------------------------------------------------
class Order(BaseModel):
    order_id: int
    items: List[str]
    amount: float
    discount: Optional[float] = 0

@app.post("/order")
def create_order(order: Order):
    return order.model_dump()

"""
Serialization converts Python objects into JSON.
Pydantic handles this automatically.
"""

# --------------------------------------------------
# HOW TO RUN
# --------------------------------------------------
"""
1. Install:
   pip install fastapi uvicorn

2. Run:
   uvicorn Day_5:app --reload

3. Open:
   http://127.0.0.1:8000/docs

Try all endpoints from Swagger UI.
"""

