import re
import hashlib

def dataReader(fileName):
    with open('data/'+fileName+'.txt') as mainframes:
        mainframes = mainframes.readlines()
        line = ''
        for x in mainframes:
            x = re.sub("[|]","','",x)
            x = re.sub(r'\n',"'\n",x)
            x = "'"+x

            line = line+str(x)
        return line+"'"

def dataReaderCSV(fileName):
    data = dataReader(fileName)
    data = str(str(data).replace('(', '').replace(')', '').replace("'", ''))
    return data

def hashMaker(x):
    hash = str("'" + (hashlib.md5(x.encode('utf-8')).hexdigest()) + "'")
    return hash