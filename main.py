from _config import *
#import uvicorn
from fastapi import FastAPI, Request
from apiFunctions import *


app = FastAPI(title=fastapi_title, version=fastapi_version, contact=fastapi_contact)


@app.get("/")
def root():
    return {"message": "Hello Azure"}


@app.get("/get")
def get_name(name:str):
    return {"name": name}


@app.get("/getClientCorporation/{client_corporation_id}")
def getClientCorporation(client_corporation_id:int):
    resp = ClientCorporation(client_corporation_id)
    return resp


@app.get("/getClientCorporation/{vacancy_id}")
def getVacancy(vacancy_id:int):
    resp = Vacancy(vacancy_id)
    return resp
