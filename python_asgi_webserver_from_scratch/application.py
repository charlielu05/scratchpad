import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/foo")
async def foo():
    return {"message": "foo"}