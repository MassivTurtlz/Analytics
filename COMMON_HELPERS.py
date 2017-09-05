import re
import hashlib
import glob


def getExtension(file):
    path = glob.glob("data/"+file+".*")
    return str(path).split('.')[1].replace("'","").replace("]","")


## TODO: HANDLE CSV FILE FORMAT -- needs testing

def dataReader(fileName):
    ext = str(getExtension(fileName))
    if ext == 'txt':
        with open('data/'+fileName+"."+ext) as file:
            file = file.readlines()
            line = ''
            for x in file:
                x = re.sub("[|]","','",x)
                x = re.sub(r'\n',"'\n",x)
                x = "'"+x

                line = line+str(x)
            return line+"'"
    if ext == 'csv':
        with open('data/' + fileName + "." + ext) as file:
            file = file.readlines()
            line = ''
            for x in file:
                x = re.sub("[,]", "','", x)
                x = re.sub(r'\n', "'\n", x)
                x = "'" + x

                line = line + str(x)
            return line + "'"

def dataReaderCSV(fileName):
    data = dataReader(fileName)
    data = str(str(data).replace('(', '').replace(')', '').replace("'", ''))
    return data

def hashMaker(x):
    y = str(x.split(',')[0] + x.split(',')[3]).replace("'","")
    hash = str("'" + (hashlib.md5(y.encode('utf-8')).hexdigest()) + "'")
    return hash