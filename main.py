from _config import *
from fastapi import FastAPI, Request
#import uvicorn

app = FastAPI(title=fastapi_title, version=fastapi_version, contact=fastapi_contact)


@app.get("/")
async def root():
    return {"message": "Hello Azure"}

@app.get("/get")
async def get_name(name:str):
    return {"name": name}
