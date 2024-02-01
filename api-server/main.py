import mysql.connector
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from src.flood_warning_api import upsert_to_database, perform_flood_warning_get_api

#using Flask
app = Flask(__name__)

def scheduled_flood_warning_get_api():
    data = perform_flood_warning_get_api()
    upsert_to_database(data)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(
    func=scheduled_flood_warning_get_api,
    trigger="interval",
    seconds=30  # CRON job runs every 30 seconds
)
scheduler.start()

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Cd@281195',
    'database': 'NATIONAL STATES'
}

@app.route('/flood-warnings/count/group-by/states', methods=['GET'])
def get_states_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT state, station_id, station_name, district, main_basin, sub_basin FROM national_state"
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3], 'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/count/group-by/water', methods=['GET'])
def get_water_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT state, station_id, station_name, water_level_current, water_level_indicator, water_level_normal_level, water_level_alert_level, water_level_warning_level, water_level_danger_level, water_level_increment, water_level_update_datetime, water_level_trend,station_status, water_level_status FROM national_state"
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'water_level_current': row[3], 'water_level_indicator' : row[4], 'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 'water_level_trend' : row[11], 'station_status' : row[12], 'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/count/group-by/rainfall', methods=['GET'])
def get_rainfall_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, rainfall_status FROM national_state"
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})




if __name__ == '__main__':
        app.run(debug=True)


