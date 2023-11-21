import os
import sqlite3

"""
   - програма не може підключитись до вказаного файлу
   - у БД відсутня зазначена таблиця;
   - Програма звертається до файлу. У разі будь-якого виключення, вона просить користувача
     ввести шлях до файлу та підключається заново (застосуйте функції та рекурсію)
"""

def openDb():
    print('1. Hi! Lets open DB!')
    
    dbFile="country.db"
    dbFile = input(f'Input dbfile [like {dbFile}] :')
    
    if dbFile == 'q' or dbFile == 'Q':
        exit(0)
    elif dbFile == None or dbFile == '':
        raise ValueError('Empty file name')
    elif not os.path.exists(dbFile):
        raise ValueError('No such file')
     
    con = sqlite3.connect(dbFile)
    
    tableDef = 'Regions' 
    table    = input(f'Input tablename [default : {tableDef}] :')

    if table==None or table=='':
        table = tableDef
    
    cur = con.cursor()
    res = cur.execute('select id, name from '+table);
    regionsTab = res.fetchall()
    print(regionsTab)

def tryOpenDb():
    try:
        openDb()
    except ValueError as ve:
        print(f'Value error: [{ve}]')
        tryOpenDb()
    except Exception as ex:
        print(f'Unknown error: [{ex}]')
        tryOpenDb()

if __name__ == '__main__':
    tryOpenDb()
