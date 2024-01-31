import requests
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from .src.flood_warning_api import upsert_to_database, perform_flood_warning_get_api

#using FastAPI
app = FastAPI()

@app.get("/flood-warnings/count/group-by/states")
def get_flood_warnings_count_groupby_state():
    response = requests.get( "https://api.data.gov.my/flood-warning/" )
    raw_data = response.json()
    alert_time_id = response.json()[11]['water_level_update_datetime']
    x = 0
    new_state= [{}]
    sub_basin_r = [{}]
    alerts_r = [{}]
    for x in range(len(raw_data)):
        states = response.json()[int(x)]['state']  
        if states == 'KELANTAN':
            state = states
            new_state = str(new_state) + str(states)
            sub_basin_id = response.json()[int(x) + 1]['sub_basin']
            alerts_id = response.json()[int(x) + 5]['water_level_indicator']
            sub_basin_r = str(sub_basin_r) + str(sub_basin_id)
            alerts_r = str(alerts_r) + str(alerts_id)
            x = x + 1

        else:
            x = x + 1
    
    return (alert_time_id,state,sub_basin_r,alerts_r)

@app.on_event("startup")
@repeat_every(seconds=30)  # CRON job runs every hour, adjust as needed
def scheduled_flood_warning_get_api():
    data = perform_flood_warning_get_api()
    upsert_to_database(data)
