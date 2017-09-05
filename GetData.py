import SQL_COMMON_HELPERS
import COMMON_HELPERS


connect = SQL_COMMON_HELPERS.connect


def exampleQuery():
    query = "SELECT * FROM mainframes;"
    queryResults = SQL_COMMON_HELPERS.doSelectQuery('mainframes', query)

    for each in queryResults:
        print(each)


# lets make a function to return the line with the least strategic importance

def getMostStrategicImportance(table):
    query = "SELECT * FROM " + table + " ORDER BY STRATEGIC_IMPORTANCE ASC LIMIT 1;"
    queryResults = SQL_COMMON_HELPERS.doSelectQuery(table, query)
    out = tuple('')
    for each in queryResults:
        out = out + each
    return out


def getLeastStrategicImportance(table):
    query = "SELECT * FROM " + table + " ORDER BY STRATEGIC_IMPORTANCE DESC LIMIT 1;"
    queryResults = SQL_COMMON_HELPERS.doSelectQuery(table, query)
    out = tuple('')
    for each in queryResults:
        out = out + each
    return out

def runThese():
    print(getMostStrategicImportance('mainframes'))
    print(getLeastStrategicImportance('mainframes'))
runThese()