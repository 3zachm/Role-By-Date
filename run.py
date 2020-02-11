import discord
from discord.ext import commands, tasks
from tinydb import TinyDB, Query
from datetime import date

botToken = ''
birthdays = TinyDB('bday-db.json')

client = discord.Client()
bot = commands.Bot(command_prefix = '!')

@client.event
async def on_ready(self):
    print('Ready as {0}.'.format(self.user))
    
@client.event
async def on_message(self, message):
    print('{0.author}: {0.content}'.format(message))

@bot.command()
async def print(ctx, arg1):
    print('{}'.format(arg1))
    await ctx.send('{}'.format(arg1))

@bot.command(name="getID")
async def getID(ctx, user: discord.User):
    await ctx.send(user.id)

@tasks.loop()  # not implemented correctly
async def checkBirthday():
    if len(searchBirthday(int(getDate('m')), int(getDate('d'))) > 1:
        # code for assigning role based on name

#async def assignRole(id)
    # not all here but get ID from mention, store ID, use ID here to assign role

def addDB(name, month, day):
    birthdays.insert({'name': name, 'month': month, 'day': day})

def listDB():
    print(birthdays.all())

def searchBirthday(m, d):
    Birthday = Query()
    rtnBday = birthdays.search((Birthday.month == m) & (Birthday.day == d))
    getName = [r['name'] for r in rtnBday]
    name = '\''.join(getName)
    return name
    
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