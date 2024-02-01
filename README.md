# NATIONAL-STATES-APP
1. It is a web-based app for the client to get latest update on the water level and rainfall status based on states in Malaysia.
2. The data that will be accordingly shown is state,station ID, station name, latitude, longitude, district, sub basin, main basin, station type, current water level, water level alerts, water level trend, water level update time, rainfall indicator and raifall update time.

# Backend Requirement

## GET API data from https://api.data.gov.my/flood-warning/ and STORE in MYSQL
1. Add CRON service to store latest data that we get from flood warning api https://api.data.gov.my/flood-warning/
2. Store the data to database (MYSQL)
3. Make the CRON job performs every 30 seconds
4. The data are fetch and stored in MYSQL database every 30 seconds.

## API server
1. Create API server that allows FETCH data from MYSQL to RestAPI
2. API expectation

   a) To see list of water data stations by state
   1. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/selangor
   2. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/negeri_sembilan
   3. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/melaka
   4. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/johor
   5. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/pahang
   6. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/terengganu
   7. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/kelantan
   8. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/perak
   9. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/kedah
   10. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/perlis
   11. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/sabah
   12. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/sarawak
   13. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/kuala_lumpur
   14. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/labuan
   15. GET http://127.0.0.1:5000/flood-warnings/group-by/list_station/putrajaya

   b) To get alerts based on water level data by state
   1. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/selangor
   2. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/negeri_sembilan
   3. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/melaka
   4. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/johor
   5. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/pahang
   6. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/terengganu
   7. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/kelantan
   8. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/perak
   9. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/kedah
   10. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/perlis
   11. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/sabah
   12. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/sarawak
   13. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/kuala_lumpur
   14. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/labuan
   15. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/water/putrajaya
  
   c) To get alerts based on rainfall data by state
   1. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/selangor
   2. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/negeri_sembilan
   3. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/melaka
   4. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/johor
   5. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/pahang
   6. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/terengganu
   7. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/kelantan
   8. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/perak
   9. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/kedah
   10. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/perlis
   11. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/sabah
   12. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/sarawak
   13. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/kuala_lumpur
   14. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/labuan
   15. GET http://127.0.0.1:5000/flood-warnings/group-by/alerts/rainfall/putrajaya


