from _config import *
#import uvicorn
from fastapi import FastAPI, Request
from apiFunctions import *

###########

app = FastAPI(title=fastapi_title, version=fastapi_version, contact=fastapi_contact)

###########

@app.get("/getClientCorporation/{client_corporation_id}")
def get_Client_Corporation(client_corporation_id:int):
    resp = ClientCorporation(client_corporation_id)
    return resp


@app.get("/getVacancy/{vacancy_id}")
def getVacancy(vacancy_id:int):
    resp = Vacancy(vacancy_id)
    return resp
