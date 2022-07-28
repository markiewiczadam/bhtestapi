from fastapi import FastAPI, Request
#import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get")
async def get_name(name:str):
    return {"name": name}