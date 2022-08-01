from _config import *
#import uvicorn
from fastapi import FastAPI, Request
from apiFunctions import *

###########

app = FastAPI(title=fastapi_title, version=fastapi_version, contact=fastapi_contact)

###########

@app.get("/getClientCorporationDetails/{client_corporation_id}")
def get_Client_Corporation_Details(client_corporation_id:int):
    resp = clientCorporationDetails(client_corporation_id)
    return resp


@app.get("/getVacancyDetails/{vacancy_id}")
def get_Vacancy_Details(vacancy_id:int):
    resp = vacancyDetails(vacancy_id)
    return resp


@app.post("/searchClientCorporation")
def search_Client_Corporation(request: searchClientCorporationReq):
    resp = searchClientCorporation(request)
    return resp
