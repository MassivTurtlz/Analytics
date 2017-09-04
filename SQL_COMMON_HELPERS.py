import MySQLdb
import COMMON_HELPERS
import hashlib
import re

hostname = 'localhost'
username = 'root'
password = 'maximus'
database = 'ANALYTICS'


## TEST QUERY

def doSelectQuery(conn, table):
    cur = conn.cursor()
    cur.execute('SELECT * FROM ' + table + ';');
    for x in cur.fetchall():
        print(x)


def doProcessColumnsNames(conn, table):
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
    hash = str("'" + (hashlib.md5(x.encode('utf-8')).hexdigest()) + "'")
    query = str('INSERT INTO '+table+' VALUES(' + str(hash) + "," + str(
        x) + ') ON DUPLICATE KEY UPDATE '+doProcessColumnsNames(connect,table))
    print(query)
    return str(query)

def doCreateRecords(conn, table):
    cur = conn.cursor()
    tableName = table
    table = COMMON_HELPERS.dataReader(table)
    iterRow = iter(table.splitlines())
    next(iterRow)
    for x in iterRow:
        query = QueryBuilder(x,tableName)
        cur.execute(query)



connect = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
target = ['mainframes','servers']
for each in target:
    each = str(each)
    doSelectQuery(connect, each)
    doCreateRecords(connect, each)

connect.commit()
connect.close()
