import psycopg2
from _config import *
from typing import Optional
from pydantic import BaseModel

######## DB Connection

conn = psycopg2.connect(host=db_host, port=db_port, user=db_user, password=db_pass, database=db_dbname)
cur = conn.cursor()


######## Class Definitions

class searchClientCorporationReq(BaseModel):
    corpID: Optional[str]
    #corpName: Optional[str]
    #corpManager: Optional[str]


######## Function Definitions

def clientCorporationDetails(client_corporation_id):
    qry = """
            SELECT array_agg(client_corp) 
            FROM mi.v_api_ClientCorporationDetails 
            WHERE client_corporation_id = %d
        """ % (client_corporation_id)

    results = cur.execute(qry)
    results = cur.fetchall()[0][0]

    return results


def vacancyDetails(vacancy_id):
    qry = """
            SELECT array_agg(vacancy) 
            FROM mi.v_api_VacancyDetails 
            WHERE vacancy_id = %d
        """ % (vacancy_id)

    results = cur.execute(qry)
    results = cur.fetchall()[0][0]

    return results


def searchClientCorporation(searchClientCorporationReq):

    #if searchClientCorporationReq.corpID != None:
    #    varname = 'client_corporation_id'
    #    varvalue = searchClientCorporationReq.corpID

    #elif searchClientCorporationReq.corpID != None:
    #    varname = 'corporation_name'
    #    varvalue = searchClientCorporationReq.corpManager

    #elif searchClientCorporationReq.corpID != None:
    #    varname = 'manager'
    #    varvalue = searchClientCorporationReq.corpManager


    #qry = """
    #        SELECT array_agg(client_corp)
    #        FROM mi.v_api_ClientCorporationDetails
    #        WHERE LOWER(%s) LIKE '%%%s%%'
    #    """ % (varname, varvalue)

    #results = cur.execute(qry)
    #results = cur.fetchall()[0]

    #results = {varname: varvalue}

    return searchClientCorporationReq.corpID