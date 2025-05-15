from fastapi import FastAPI
import datetime
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Server startup:', datetime.datetime.now())
    yield
    print('Server shutdown:', datetime.datetime.now())

app = FastAPI(lifespan=lifespan)