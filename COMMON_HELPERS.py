import re

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