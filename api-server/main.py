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

@app.route('/flood-warnings/group-by/list_station/selangor', methods=['GET'])
def get_selangor_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'SELANGOR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/list_station/negeri_sembilan', methods=['GET'])
def get_negeri_sembilan_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'NEGERI SEMBILAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/list_station/melaka', methods=['GET'])
def get_melaka_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'MELAKA' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/list_station/johor', methods=['GET'])
def get_johor_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'JOHOR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}) 

@app.route('/flood-warnings/group-by/list_station/pahang', methods=['GET'])
def get_pahang_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'PAHANG' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/terengganu', methods=['GET'])
def get_terengganu_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'TERENGGANU' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/kelantan', methods=['GET'])
def get_kelantan_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'KELANTAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/perak', methods=['GET'])
def get_perak_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'PERAK' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/kedah', methods=['GET'])
def get_kedah_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'KEDAH' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/perlis', methods=['GET'])
def gget_perlis_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'PERLIS' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/sabah', methods=['GET'])
def get_sabah_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'SABAH' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/sarawak', methods=['GET'])
def get_sarawak_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'SARAWAK' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/kuala_lumpur', methods=['GET'])
def get_kuala_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'WILAYAH PERSEKUTUAN KUALA LUMPUR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/labuan', methods=['GET'])
def get_labuan_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'WILAYAH PERSEKUTUAN LABUAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/list_station/putrajaya', methods=['GET'])
def get_putrajaya_list_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, district, main_basin, sub_basin 
        FROM national_state2 WHERE state = 'WILAYAH PERSEKUTUAN PUTRAJAYA' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 'district': row[3],
        'main_basin' : row[4], 'sub_basin' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
       
@app.route('/flood-warnings/group-by/alerts/water/selangor', methods=['GET'])
def get_water_selangor_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 WHERE state = 'SELANGOR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/negeri_sembilan', methods=['GET'])
def get_water_negeri_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'NEGERI SEMBILAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/melaka', methods=['GET'])
def get_water_melaka_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'MELAKA' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/johor', methods=['GET'])
def get_water_johor_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'JOHOR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/pahang', methods=['GET'])
def get_water_pahang_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'PAHANG' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/terengganu', methods=['GET'])
def get_water_terengganu_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'TERENGGANU' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/kelantan', methods=['GET'])
def get_water_kelantan_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'KELANTAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/perak', methods=['GET'])
def get_water_perak_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'PERAK' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/water/kedah', methods=['GET'])
def get_water_kedah_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'KEDAH' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/perlis', methods=['GET'])
def get_water_perlis_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'PERLIS' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/sabah', methods=['GET'])
def get_water_sabah_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'SABAH' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/sarawak', methods=['GET'])
def get_water_sarawak_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'SARAWAK' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/kuala_lumpur', methods=['GET'])
def get_water_kuala_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'WILAYAH PERSEKUTUAN KUALA LUMPUR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/labuan', methods=['GET'])
def get_water_labuan_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'WILAYAH PERSEKUTUAN LABUAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/water/putrajaya', methods=['GET'])
def get_water_putrajaya_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, water_level_current, water_level_indicator,
        water_level_normal_level, water_level_alert_level, water_level_warning_level, 
        water_level_danger_level, water_level_increment, water_level_update_datetime, 
        water_level_trend,station_status, water_level_status FROM national_state2 
        WHERE state = 'WILAYAH PERSEKUTUAN PUTRAJAYA' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'water_level_current': row[3], 'water_level_indicator' : row[4], 
        'water_level_normal_level' : row[5], 'water_level_alert_level': row[6], 
        'water_level_warning_level' : row[7], 'water_level_danger_level': row[8], 
        'water_level_increment' : row [9], 'water_level_update_datetime' : row[10], 
        'water_level_trend' : row[11], 'station_status' : row[12], 
        'water_level_status': row[13]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/flood-warnings/group-by/alerts/rainfall/selangor', methods=['GET'])
def get_rainfall_selangor_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'SELANGOR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/rainfall/negeri_sembilan', methods=['GET'])
def get_rainfall_negeri_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'NEGERI SEMBILAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/rainfall/melaka', methods=['GET'])
def get_rainfall_melaka_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'MELAKA' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/johor', methods=['GET'])
def get_rainfall_johor_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'JOHOR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/pahang', methods=['GET'])
def get_rainfall_pahang_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'PAHANG' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/terengganu', methods=['GET'])
def get_rainfall_terengganu_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'TERENGGANU' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/kelantan', methods=['GET'])
def get_rainfall_kelantan_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'KELANTAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/perak', methods=['GET'])
def get_rainfall_perak_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'PERAK' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/flood-warnings/group-by/alerts/rainfall/kedah', methods=['GET'])
def get_rainfall_kedah_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'KEDAH' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/perlis', methods=['GET'])
def get_rainfall_perlis_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'PERLIS' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/sabah', methods=['GET'])
def get_rainfall_sabah_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'SABAH' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/sarawak', methods=['GET'])
def get_rainfall_sarawak_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'SARAWAK' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/kuala_lumpur', methods=['GET'])
def get_rainfall_kuala_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'WILAYAH PERSEKUTUAN KUALA LUMPUR' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/labuan', methods=['GET'])
def get_rainfall_labuan_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'WILAYAH PERKSEKUTUAN LABUAN' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/flood-warnings/group-by/alerts/rainfall/putrajaya', methods=['GET'])
def get_rainfall_putrajaya_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = '''SELECT state, station_id, station_name, rainfall_clean, rainfall_update_datetime, 
        rainfall_status FROM national_state2 WHERE state = 'PUTRAJAYA' '''
        
        cursor.execute(query)

        data = cursor.fetchall()
     
        result = [{'state': row[0], 'station_id': row[1], 'station_name': row[2], 
        'rainfall_clean': row[3], 'rainfall_update_datetime' : row[4], 
        'rainfall_status' : row[5]} for row in data]
       
        cursor.close()
        connection.close()
      
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
        app.run(debug=True)


