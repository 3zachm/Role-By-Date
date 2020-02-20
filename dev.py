import discord
from discord.ext import commands, tasks
from tinydb import TinyDB, Query
from datetime import date

birthdays = TinyDB('bday-debug.json')

def bday(dID, op = '', month = 0, day = 0): # test if amount of parameters from user matters or throws errors
    if op == 'add': 
        if searchName(dID):
            print('User already present in database. Use edit or remove.') 
        #elif user == '':
            #print('Please specify a name!')
        else: # FIX THIS CONDITION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Not correctly searching ID :(
            addDB(dID, month, day)
            message = 'Added successfully!'
            print(message)
    elif op == 'remove':
        removeDB(dID)
        print('Removed successfully!')
    elif op == 'edit':
        removeDB(dID)
        addDB(dID, month, day)
        print('Edited successfully!')
    elif op == 'list':
        day = getBirthday(dID)
        print(day)
    else:
        print('Proper operations include ``add``, ``remove``, ``edit``, and ``list [mention]``.')   
    
def addDB(name, month, day):
    birthdays.insert({'name': name, 'month': month, 'day': day})

def removeDB(name):
    Birthday = Query()
    birthdays.remove(Birthday.name == name)

def listDB():
    print(birthdays.all())

def searchBirthday(m, d):
    Birthday = Query()
    rtnBday = birthdays.search((Birthday.month == m) & (Birthday.day == d))
    getName = [r['name'] for r in rtnBday]
    name = '\''.join(getName)
    return name

def searchName(n):
    Birthday = Query()
    rtnBday = birthdays.search((Birthday.name == n))
    iName = [r['name'] for r in rtnBday]
    getName = str(iName)
    found = False
    if len(searchBirthday(int(getDate('m')), int(getDate('d')))) > 1:
            found = True
    return found

def getBirthday(n):
    Birthday = Query()
    rtnBday = birthdays.search((Birthday.name == n))
    getMonth = [r['month'] for r in rtnBday]
    getDay = [r['day'] for r in rtnBday]
    day = ''.join(getDay)
    month = ''.join(getMonth)
    wordM = numToWord(month)
    return wordM + ' ' + day

def getDate(dmy):
    currentDate = date.today()
    if dmy == 'd':
        return currentDate.strftime("%d")
    if dmy == 'm':
        return currentDate.strftime("%m")
def numToWord(month):
    index = month - 1
    months = ["January","February","March","April","May","June","July",
            "August","September","October","November","December"];
    return month[index]

while(True):
    command, dID, op, month, day  =  input(">>>").split() or '', '', '', '', ''
    if command == "bday":
        bday(dID, op, month, day)