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


# Base Pydantic Models
class User(BaseModel):
    # validates the following data is passed of the correct types
    name: str
    website: str
    age: int
    role: str


class UpdateUser(BaseModel):
    # model for updating a user; optional choice for the user to update any or all fields
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None


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


# create a user
# to store a user(s), need models to store them
@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)  # post to create a user;
# 201 status = successful creation
def create_user(user_id: int, user: User):  # function to create user; input parameters would need to be a user_id of
    # type int and a user of type User as specified in the User Model above
    if user_id in users:  # check for if the user exists in our makeshift database
        raise HTTPException(status_code=400, detail="User already exists")  # if so raise a 400 status error
    users[user_id] = user.dict()  # store user.dict() inside our users db with the key of user_id
    return user


# update a user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):  # function to update an existing user in the database
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User does not exist!")
    # check which optional field is being updated
    current_user = users[user_id]

    if user.name is not None:
        current_user["name"] = user.name
    if user.website is not None:
        current_user["website"] = user.website
    if user.age is not None:
        current_user["age"] = user.age
    if user.role is not None:
        current_user["role"] = user.role

    return current_user
# delete a user

# search for a user
