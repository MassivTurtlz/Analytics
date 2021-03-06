import MySQLdb
import COMMON_HELPERS
import hashlib
import re

hostname = 'localhost'
username = 'root'
password = 'maximus'
database = 'ANALYTICS'



#TODO REFACTOR SO I DONT NEED TWO INSTANCES OF THIS VARIABLE
# done but maybe i should look at closing some connections down when im not using them
def reConnect():
    connect = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
    return connect

connect = reConnect()
## TEST QUERY

def doSelectQuery(table, query):
    conn = reConnect()
    cur = conn.cursor()
    cur.execute(query + table + ';');
    results = cur.fetchall()
    return results

def doProcessColumnsNames(table):
    conn = reConnect()
    cur = conn.cursor()
    query = 'SELECT column_name FROM information_schema.columns WHERE  table_name = "'+table+'" AND table_schema = "'+database+'";'
    cur.execute(str(query))
    result = cur.fetchall()
    columnNames = ''
    iterCol = iter(result)
    next(iterCol)
    for each in iterCol:
        each = str(str(each).replace('(','').replace(')','').replace(',','').replace("'",''))
        columnNames += str("`" + each + "`" + "=VALUES(`" + each + "`), ")
    columnNames = columnNames[:-2]+";"  # strips the two trailing commas
    return str(columnNames)

def QueryBuilder(x,table):
    hash = COMMON_HELPERS.hashMaker(x)
    query = str('INSERT INTO '+table+' VALUES(' + str(hash) + "," + str(
        x) + ') ON DUPLICATE KEY UPDATE '+doProcessColumnsNames(table))
    return str(query)

def doCreateRecords(connect,table):
    cur = connect.cursor()
    tableName = table
    table = COMMON_HELPERS.dataReader(table)
    iterRow = iter(table.splitlines())
    next(iterRow)
    for x in iterRow:
        query = QueryBuilder(x,tableName)
        cur.execute(query)
        connect.commit()

def doCreateTable(table):
    conn = reConnect()
    cur = conn.cursor()
    titleRow = "uid,"+COMMON_HELPERS.dataReaderCSV(table).splitlines()[0]
    stringBuild = 'CREATE TABLE IF NOT EXISTS '+table+' ('
    stringContent = ''
    counter = 0
    while counter < len(titleRow.split(',')):
        data = titleRow.split(',')[counter]
        if data == 'uid':
            stringContent = stringContent + data + ' VARCHAR(255) PRIMARY KEY,'
        elif data == 'COUNTER' or data == 'COUNT' or data == 'STRATEGIC_IMPORTANCE':
            stringContent = stringContent + data + ' INT(255),'
        else:
            stringContent = stringContent +data+' VARCHAR(255),'
        counter+=1
    query = stringBuild+str(stringContent[:-1]+');')
    cur.execute(query)
    connect.commit()

def engineStart(target):
    #target = ['mainframes','servers','storage','desktops'] #example of including files
    for each in target:
        each = str(each)
        #doSelectQuery(each, 'SELECT * FROM ')  # PRINTS ALL TABLES MENTIONED IN TARGET VARIABLE
        doCreateTable(each)
        doCreateRecords(reConnect(),each)
        connect.commit()
    connect.close()