
CREATE OR REPLACE VIEW mi.v_api_VacancyDetails AS
    SELECT vacancy_id 
    ,row_to_json(v) as vacancy
    FROM (
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

            ,row_to_json(cc) as client_corporation		
            FROM mi.v_vacancy v 
            JOIN (
                    SELECT 
                    client_corporation_id	
                    ,corporation_name		
                    ,status		
                    ,manager	
                    ,client_activity_status
                    FROM mi.v_client_corporation 
                ) cc 
            ON v.client_corporation_id = cc.client_corporation_id   
        ) v 