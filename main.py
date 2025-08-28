# CRUD
# Create; Read; Update; Delete items

# HTTP Requests - each correspond to a CRUD operation
# GET; POST; PUT; DELETE information

# Create -> POST
# Read -> GET
# Update -> PUT
# Delete -> DELETE

from fastapi import FastAPI  # import the class FastAPI
from fastapi import HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # create instance of FastAPI; this instance builds out the API
# dummy database:
users = {
    1: {
        "name": "Robby",
        "website": "www.github.com/robby-g-singh",
        "age": 27,
        "role": "developer"
    }
}


# Endpoint creation:
@app.get("/")  # create the landing page
def root():
    return {"message": "Welcome to your Introduction to FastAPI!"}


# root.com/users/1
# Get Users Endpoint
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., description="The ID you want to get", gt=0, lt=100)):
    # check if user is in the database
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not Found!")
    return users[user_id]
