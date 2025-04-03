import fastapi
from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int
    
app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/foo")
async def foo():
    return {"message": "foo"}

@app.get("/bar")
async def bar():
    return {"message": "bar"}

@app.post("/greet")
async def greet(person:Person):
    return {"message": f"Hi {person.name}, you are {person.age} years old."}