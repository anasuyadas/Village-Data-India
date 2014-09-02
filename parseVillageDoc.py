"""
parseVillageDoc.py
"""
import os
import zipfile
import lxml
import sys
from bs4 import BeautifulSoup



def loadVillageData(file):

    #files = [f for f in os.listdir(datapath) is os.path.isfile(f) and 'Microplanning' in f and '.html' in f ] 

    #for file in files:
        print 'Loading data: ' + file + '\n'
        villageName=file.lower().split(' ')[1]
        villageName=villageName.split('.html')[0]
        villageSoup = BeautifulSoup(open(file))
            # parse all the tables in each village
            for tag in soup.findAll('table'):
                table.append(tag)

    return (table, villageName)

#---------------------------------------------------------------------------------


def getTableData(table,villageName):
    
    villageData=[]
    
    table_body = table[tabNum].find('tbody')

    data=[]
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
        data2=pd.DataFrame(data)
        data2=data2.T
        data2[]=villageName  

    villageData.append(data2)

    return villageData


#---------------------------------------------------------------------------------

files = [f for f in os.listdir(datapath) is os.path.isfile(f) and 'Microplanning' in f and '.html' in f ] 

allVillageTable=[]

for file in files:
    table=[]
    villageName, table=loadVillageData(file)
    allVillageTable=allVillageTable.append(table)
        for x in range(0, en(table)):
            parsedTable=
            globals()['table%s' % x] = 



    #([ele for ele in cols if ele]) # Get rid of empty values

   