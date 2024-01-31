# Backend Requirement
## Data CRON service
1. Add CRON service to store latest data that we get from flood warning api https://api.data.gov.my/flood-warning/
2. Store the data to database (mysql)
3. Make the CRON job performs every 30 seconds

## GET API data from https://api.data.gov.my/flood-warning/ and STORE in MYSQL
1. GET raw data and using python coding, reorganize data into respective columns in MYSQL

## API server
1. Create API server that allows FETCH data from MYSQL to RestAPI
2. API expectation
   1. GET /flood-warnings/count/group-by/states
   2. GET /flood-warnings/count/group-by/water
   3. GET /flood-warnings/count/group-by/rainfall
# national-states-app
