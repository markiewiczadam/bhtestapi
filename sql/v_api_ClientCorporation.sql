
CREATE OR REPLACE VIEW mi.v_api_ClientCorporation AS
    SELECT client_corporation_id
    ,row_to_json(cc) as client_corp
    FROM ( 
            SELECT 
            client_corporation_id	
            ,corporation_name		
            ,status		
            ,manager	
            ,client_activity_status
            FROM mi.v_client_corporation
        ) cc 
  



