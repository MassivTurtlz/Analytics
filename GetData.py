import SQL_COMMON_HELPERS
import COMMON_HELPERS

connect = SQL_COMMON_HELPERS.connect
query = "SELECT * FROM mainframes;"
queryResults = SQL_COMMON_HELPERS.doSelectQuery(connect,'mainframes',query)

for each in queryResults:
    print(each)