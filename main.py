from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from db import database
from fastapi.encoders import jsonable_encoder




app = FastAPI()






Userlist=[]

class user(BaseModel):
    name:str
    age:int
    city:str
    email:str


@app.get("/")
async def root():
    return {"msg":"hello"}

@app.post("/add")
def createuser(data:user):
    print(data)
    Userlist.append(data)
    json_data=jsonable_encoder(data)
    database.profile_create(data=json_data)

    
    
    return data


@app.get("/user")

def search_user():
    data= jsonable_encoder(database.profile_search())

    return {"detail":data}

