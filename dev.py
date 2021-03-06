import discord
import configparser
import io
from discord.ext import commands, tasks
from tinydb import TinyDB, Query
from datetime import date

with open("config.ini") as c:
    discord_config = c.read()
config = configparser.RawConfigParser(allow_no_value=True)
config.read_file(io.StringIO(discord_config))

birthdays = TinyDB('bday-debug.json')

def checkBday(m, d):
    if len(searchBirthday(m, d)) > 1:
            message = 'Birthday found'
    else:
        message = 'Not found'
    print(message)    

def bday(dID, op = '', month = 0, day = 0): # test if amount of parameters from user matters or throws errors
    if op == 'add': 
        if searchName(dID):
            message = 'User already present in database. Use edit or remove.'
        #elif user == '':
            #print('Please specify a name!')
        else: 
            addDB(dID, month, day)
            message = 'Added successfully!'
    elif op == 'remove':
        removeDB(dID)
        message = 'Removed successfully!'
    elif op == 'edit':
        removeDB(dID)
        addDB(dID, month, day)
        message = 'Edited successfully!'
    elif op == 'list':
        day = getBirthday(dID)
        message = day
    else:
        message = 'Proper operations include ``add``, ``remove``, ``edit``, and ``list [mention]``.'
    print(message)
def addDB(name, month, day):
    birthdays.insert({'name': name, 'month': month, 'day': day})

def removeDB(name):
    Birthday = Query()
    birthdays.remove(Birthday.name == name)

def listDB():
    print(birthdays.all())

def searchBirthday(m, d):
    Birthday = Query()
    rtnBday = birthdays.search((Birthday.month == m) & (Birthday.day == d)) # fix?
    print(rtnBday) # debug remove
    getName = [r['name'] for r in rtnBday]
    name = '\''.join(getName)
    return name

def searchName(n):
    Birthday = Query()
    rtnBday = birthdays.search((Birthday.name == n))
    iName = [r['name'] for r in rtnBday]
    name = '\''.join(iName)
    found = False
    if name == n:
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
    index = int(month) - 1
    months = ["January","February","March","April","May","June","July",
            "August","September","October","November","December"];
    return months[index]
while(True):
    command =  input(">>>")
    command2 = command, " >>>"
    if command == "bday":
        dID, op, month, day  =  input(command2).split()
        bday(dID, op, month, day)
    if command == "search":
        dID  =  input(command2).split()
        print(searchName(dID))
    if command == "checkBday":
        month, day  =  input(command2).split()
        checkBday(month, day)
    if command == "numToWord":
        month, day  =  input(command2).split()
        print(numToWord(month), " ", day)