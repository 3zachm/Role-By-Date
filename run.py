import discord
import configparser
import io
from discord.ext import commands, tasks
from tinydb import TinyDB, Query
from datetime import date

with open("config.ini") as c:
    discord_config = c.read()
config = configparser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(discord_config))

botToken = config.get('discord', 'token')
birthdays = TinyDB('bday-db.json')
bot = commands.Bot(command_prefix = '!')

@bot.command(name="print") # debug command
async def print(ctx, arg1):
    print('{}'.format(arg1))
    await ctx.send('{}'.format(arg1))

@bot.command(name="getID") # debug command
async def getID(ctx, user: discord.User, op = ''):
    message = user.id, " " + op
    await ctx.send('{}'.format(message))

@bot.command(name="checkBday") # debug command
async def checkBday(ctx, d, m):
    if len(searchBirthday(int(m), int(d))) > 1:
            message = 'Birthday found'
    else:
        message = 'Not found'
    ctx.send(message)    

@bot.command(name="bday")
async def bday(ctx, user: discord.User, op = '', month = 0, day = 0): # test if amount of parameters from user matters or throws errors
    if op == 'add': 
        if searchName(user.id):
            message = 'User already present in database. Use edit or remove.'
        #elif user == '':
            #await ctx.send('Please specify a name!')
        else: 
            addDB(user.id, month, day)
            message = 'Added successfully!'
    elif op == 'remove':
        removeDB(user.id)
        message = 'Removed successfully!'
    elif op == 'edit':
        removeDB(user.id)
        addDB(user.id, month, day)
        message = 'Edited successfully!'
    elif op == 'list':
        day = getBirthday(user.id)
        message = day
    else:
        message = 'Proper operations include ``add``, ``remove``, ``edit``, and ``list [mention]``.'
    await ctx.send(message)   
#@bday.error
#async def bday_error(ctx, error):
#    await ctx.send('Proper syntax is !bday [mention] [add/remove/edit/list] [month] [day]')
    
@tasks.loop()
async def checkBirthday():
    await bot.wait_until_ready()
    bday = True
    lastDay =  getDate('d')
    lastUser = 0
    while bday == True:
        if len(searchBirthday(int(getDate('m')), int(getDate('d')))) > 1:
            bday = False
            lastDay = getDate('d')
            lastUser = searchBirthday(int(getDate('m')), int(getDate('d')))
            #add role
    while bday == False:
        if getDate('d') != lastDay:
            bday == True
            #remove role
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
    index = month - 1
    months = ["January","February","March","April","May","June","July",
            "August","September","October","November","December"];
    return month[index]

bot.run(botToken)
bot.loop.create_task(checkBirthday())
#addDB('Yes', 6, 20)