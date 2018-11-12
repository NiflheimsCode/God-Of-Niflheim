# This is where it begins, boys.

from random import *
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def commands(ctx):
    await ctx.channel.send('Command List: \n'
                           'james        - Replies Ooga Booga\n'
                           'propaganda   - Posts the Gods propaganda\n'
                           'version      - Posts current bot Version\n'
                           'rdnd         - N/I Will give random dnd character\n'
                           'joke         - tells a joke')


@client.command()
async def version(ctx):
    await ctx.channel.send('Version : 0.6.0a\n'
                           'Added Rdnd and a joke :)')


@client.command()
async def propaganda(ctx):
    await ctx.send(file=discord.File('NiflheimsAvatar.png'))


@client.command()
async def joke(ctx):
    await ctx.channel.send('What did the gnome rogue say to his quarry?\n\n\n'
                           '"Gnomae wa mou, shinde iru')


@client.command()
async def james(message):
    await message.channel.send('Ooga Booga')

@client.command()
async def neener(message):
    await message.channel.send('NeeNeR NeEneR')


@client.command()
async def rdnd(ctx):
    reply = ('STR: {}     Race : {}\n'
             'DEX: {}\n'
             'CON: {}\n'
             'INT: {}\n'
             'WIS: {}\n'
             'CHA: {}\n'.format(statgen(),get_race(), statgen(), statgen(), statgen(), statgen(), statgen()))

    await ctx.channel.send(reply)


def statgen():
    rolls = []
    x = 0
    while x < 4:
        rolls.append(randint(1, 6))
        x += 1
    rolls.sort()
    rolls[0] = 0
    stat = rolls[1] + rolls[2] + rolls[3]
    return stat


def get_race():
    races = ['Dwarf', 'Elf', 'Halfing', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
    count = 0
    for i in races:
        count += 1
    race = races[randint(0, (count - 1))]

    if race == 'Tiefling':
        race = 'Tiefling (+1 INT, +2 CHA)'

    if race == 'Half-Orc':
        race = 'Half-Orc (+2 STR, +1 CON)'

    if race == 'Half-Elf':
        race = 'Half-Elf (+2 CHA, +1/+1)'

    if race == 'Dragonborn':
        race = 'Dragonborn (+2 STR, +1 CHA)'

    if race == 'Human':
        fate = randint(1, 2)
        if fate == 1:
            race = 'Human (+1 ALL)'
        if fate == 2:
            race = 'Human (+1/+1)'

    if race == 'Gnome':
        fate = randint(1, 3)
        if fate == 1:
            race = 'Gnome (+2 INT)'
        if fate == 2:
            race = 'Forest Gnome (+2 INT, +1 DEX)'
        if fate == 3:
            race = 'Rock Gnome (+2 INT, +1 CON)'

    if race == 'Halfing':
        fate = randint(1, 3)
        if fate == 1:
            race = 'Halfing (+2 DEX)'
        if fate == 2:
            race = 'Lightfoot Halfing (+2 DEX, +1 CHA)'
        if fate == 3:
            race = 'Stout Halfing (+2 DEX, +1 CON)'

    if race == 'Elf':
        fate = randint(1, 4)
        if fate == 1:
            race = 'Elf (+2 DEX)'
        if fate == 2:
            race = 'High Elf (+2 Dex +1 INT)'
        if fate == 3:
            race = 'Wood Elf (+2 DEX, +1 WIS)'
        if fate == 4:
            race = 'Dark Elf (+2 DEX, +1 CHA)'

    if race == 'Dwarf':
        fate = randint(1, 3)
        if fate == 1:
            race = 'Dwarf (+2 CON)'
        if fate == 2:
            race = 'Hill Dwarf (+2 CON, +1 WIS)'
        if fate == 3:
            race = 'Stout Halfing (+2 CON, +2 STR)'

    return race


client.run('NTA3MDQwMjI0MzI5NzI4MDAw.Drq_dQ.V73tCFAl3AJmhqejRPMzOc13jpA')
