## old style
from fastapi import FastAPI
import datetime

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print('Server started :', datetime.datetime.now())

@app.on_event("shutdown")
async def shutdown_event():
    print('server Shutdown :', datetime.datetime.now())