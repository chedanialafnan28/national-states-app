from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
import mysql.connector
import requests

app = FastAPI()

def fetch_and_update():
    try:
        api_url = 'https://api.data.gov.my/flood-warning/'
        response = requests.get(api_url)
    
        if response.status_code == 200:
            api_data = response.json()

    
            db_connection = mysql.connector.connect(
                user = "root",
                password = "Cd@281195",
                host = "localhost",
                database = "NATIONAL STATES",
            )

            cursor = db_connection.cursor()

            for item in api_data:
                query = "INSERT INTO national_state (station_id, station_name, latitude, longitude, district, state, sub_basin, main_basin, station_type, water_level_current, water_level_indicator, water_level_normal_level, water_level_alert_level, water_level_warning_level, water_level_danger_level, water_level_increment, water_level_update_datetime, water_level_update_date, water_level_trend, rainfall_clean, rainfall_latest_1hr, rainfall_total_today, rainfall_indicator, rainfall_update_datetime, rainfall_update_date, water_level_display, rainfall_display, raw_water_level, raw_rainfall, station_status, station_code, water_level_status, rainfall_status) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s)"
                values = (item['station_id'], item['station_name'], item['latitude'], item['longitude'], item['district'], item['state'], item['sub_basin'], item['main_basin'], item['station_type'], item['water_level_current'], item['water_level_indicator'], item['water_level_normal_level'], item['water_level_alert_level'], item['water_level_warning_level'], item['water_level_danger_level'], item['water_level_increment'], item['water_level_update_datetime'], item['water_level_update_date'], item['water_level_trend'], item['rainfall_clean'], item['rainfall_latest_1hr'], item['rainfall_total_today'], item['rainfall_indicator'], item['rainfall_update_datetime'], item['rainfall_update_date'], item['water_level_display'], item['rainfall_display'], item['raw_water_level'], item['raw_rainfall'], item['station_status'], item['station_code'], item['water_level_status'], item['rainfall_status'])
                cursor.execute(query, values)

            db_connection.commit()

            print("Data  sucessfully inserted into MYSQL Database")
        else:
            print('Failed to fetch data from the API')

        cursor.close()
        db_connection.close()

    except Exception as e:
        print(f"Error: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_update, 'interval', seconds=30)
scheduler.start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


