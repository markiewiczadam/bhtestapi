import psycopg2
from _config import *


######## DB Connection

conn = psycopg2.connect(host=db_host, port=db_port, user=db_user, password=db_pass, database=db_dbname)
cur = conn.cursor()


######## Function Definitions

def ClientCorporation(client_corporation_id):
    qry = """
            SELECT array_agg(client_corp) 
            FROM mi.v_api_ClientCorporation 
            WHERE client_corporation_id = %d
        """ % (client_corporation_id)

    results = cur.execute(qry)
    results = cur.fetchall()

    return results


