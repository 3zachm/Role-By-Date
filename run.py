import discord
from discord.ext import commands, tasks
from tinydb import TinyDB, Query
from datetime import date
# literally anything related to discord is untested
botToken = ''
birthdays = TinyDB('bday-db.json')

client = discord.Client()
bot = commands.Bot(command_prefix = '!')

@client.event
async def on_ready(self): # on boot
    print('Ready as {0}.'.format(self.user))
    bot.loop.create_task(checkBirthday())
    
@client.event
async def on_message(self, message): # logging
    print('{0.author}: {0.content}'.format(message))

@bot.command(name="print") # debug command
async def print(ctx, arg1):
    print('{}'.format(arg1))
    await ctx.send('{}'.format(arg1))

@bot.command(name="getID") # debug command
async def getID(ctx, user: discord.User):
    await ctx.send(user.id)

@bot.command(name="bday")
async def bday(ctx, op, user: discord.user, month, day): # test if amount of parameters from user matters or throws errors
    if op == 'add':
        if searchName(discord.user):
            await ctx.send('User already present in database. Use edit or remove.')
        else:
            addDB(user, month, day)
            await ctx.send('Added successfully.')
    elif op == 'remove':
        removeDB(user)
        await ctx.send('Removed successfully')
    elif op == 'edit':
        removeDB(user)
        addDB(user, month, day)
        await ctx.send('Edited successfully')
    else:
        await ctx.send('Proper operations include ``add``, ``remove``, ``edit``.')   

#@tasks.loop()
async def checkBirthday():
    await client.wait_until_ready()
    bday = True
    lastDay =  getDate('d')
    lastUser = 0
    while bday == True
        if len(searchBirthday(int(getDate('m')), int(getDate('d'))) > 1:
            bday = False
            lastDay = getDate('d')
            lastYser = searchBirthday(int(getDate('m')), int(getDate('d'))
            #add role
    while bday == False
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
    rtnBday = birthdays.search((Birthday.month == n)
    getName = [r['name'] for r in rtnBday]
    name = '\''.join(getName)
    found = False
    if len(searchBirthday(int(getDate('m')), int(getDate('d'))) > 1:
            found = True
    return found

def getDate(dmy):
    currentDate = date.today()
    if dmy == 'd':
        return currentDate.strftime("%d")
    if dmy == 'm':
        return currentDate.strftime("%m")

client.run(botToken)

#addDB('Yes', 6, 20)

out = searchBirthday(int(getDate('m')), int(getDate('d')))

if len(out) > 1: 
    print('yes')
else:
    print('rip')