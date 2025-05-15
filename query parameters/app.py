from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello world I'm new in FASTAPI world!"}

@app.get("/demo")
async def root():
    return {"Message": "Hello I a path demo"}

@app.get("/production")
async def root():
    return {"Message": "Welcome to our page!"}

@app.get("/hello")
async def root(name: str,age: int):
    return {"Message": "hello " + name + " your age is " + str(age)}