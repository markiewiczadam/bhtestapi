
CREATE OR REPLACE VIEW mi.v_api_ClientCorporationDetails AS
    SELECT client_corporation_id
    ,row_to_json(cc) as client_corp
    FROM ( 
            SELECT 
            cc.client_corporation_id	
            ,corporation_name		
            ,status		
            ,manager	
            ,client_activity_status
            ,json_agg(v) as vacancies		
            FROM mi.v_client_corporation cc
            JOIN (
                    SELECT 
                    vacancy_id	
                    ,vacancy_title	
                    ,vacancy_owner_name		
                    ,vacancy_status	
                    ,employment_type	
                    ,start_date				
                    ,is_open		
                    ,address_city			
                    ,remote_work	
                    ,publishing_status	
                    ,tech_area	
                    ,primary_category		
                    ,seniority_level
                    ,client_corporation_id	
                    FROM mi.v_vacancy v 
                ) v 
                ON cc.client_corporation_id = v.client_corporation_id
            GROUP BY 
            cc.client_corporation_id	
            ,corporation_name		
            ,status		
            ,manager	
            ,client_activity_status
        ) cc 
    



