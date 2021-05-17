from datetime import date
from datetime import datetime
import time
import discord
import discord.utils
from discord.ext import commands, tasks
import discord.ext.commands.bot
import asyncio
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True
now = datetime.now()
currentMonth = now.strftime("%m")
currentDay = now.strftime("%d")
client = commands.Bot(command_prefix='&', intents=intents)
hours = 0

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Made by dustyyxo'))
    print('birthdaybot online.')

    readytime = now.strftime("%H:%M:%S")
    print(readytime)
    
@client.event
async def on_message(message):
    channel = message.channel
    global hours
    if message.author.bot:
        return
    elif message.content == "!hours":
        await channel.send("Current hours: " + str(hours))
    elif message.content == "!break":
        hours = 0
        await channel.send("Hours reset.")
    elif message.content.startswith("!sethours"):
        a = message.content.split(' ')
        print(a)
        hours = int(a[1])
        await channel.send("Hours set to: " + a[1])

        
async def bh(n):
    global hours
    await asyncio.sleep(60*60)
    n += 1
    hours = hours + 1
    await bh(n)
    
    
async def check():
    currtime = datetime.now()
    month = currtime.month
    day = currtime.day
    hour = currtime.hour
    minute = currtime.minute
    second = currtime.second
    if hour == 0 and minute == 00:
        await client.wait_until_ready()
        guild = client.get_guild(131876630959226880)
        channel = client.get_channel(559064512766935070)
        role = guild.get_role(516412507254947858)

        aiciwho = client.get_channel(774776214459383830)
        if month == 1 and day == 3:
            await client.wait_until_ready()
            user = await guild.fetch_member(145351721181380608)  # bijay
            await user.add_roles(role)
            user1 = await guild.fetch_member(102949862877696000)  # cj
            await user1.add_roles(role)
            await channel.send('happy birthday bijay and cj')
            await channel.send(user.mention)
            await channel.send(user1.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
            await user1.remove_roles(role)
        elif month == 1 and day == 16:
            await client.wait_until_ready()
            user = await guild.fetch_member(556519741372629024)  # austin
            await user.add_roles(role)
            user1 = await guild.fetch_member(152964018808553472)  # patrick
            await user1.add_roles(role)
            await channel.send('happy birthday austin and patrick')
            await channel.send(user.mention)
            await channel.send(user1.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
            await user1.remove_roles(role)
        elif month == 1 and day == 21:
            await client.wait_until_ready()
            user = await guild.fetch_member(169611631658008577)  # mitchell
            await user.add_roles(role)
            await channel.send('happy birthday mitchell')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 2 and day == 16:
            await client.wait_until_ready()
            user = await guild.fetch_member(263460873329180689)  # joey
            await user.add_roles(role)
            await channel.send('happy birthday joey')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 3 and day == 13:
            await client.wait_until_ready()
            user = await guild.fetch_member(276032470497886218)  # jordan
            await user.add_roles(role)
            await channel.send('happy birthday jordan')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 4 and day == 16:
            await client.wait_until_ready()
            user = await guild.fetch_member(186557497178324992)  # muna
            await user.add_roles(role)
            await channel.send('happy birthday muna')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 4 and day == 17:
            await client.wait_until_ready()
            user = await guild.fetch_member(185891950472331264)  # zain
            await user.add_roles(role)
            await channel.send('happy birthday zain')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 4 and day == 19:
            await client.wait_until_ready()
            user = await guild.fetch_member(131876531223003138)  # aayush
            await user.add_roles(role)
            await channel.send('happy birthday aayush')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 5 and day == 11:
            await client.wait_until_ready()
            user = await guild.fetch_member(231539753437102082)  # nick
            await user.add_roles(role)
            await channel.send('happy birthday nick')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 5 and day == 31:
            await client.wait_until_ready()
            user = await guild.fetch_member(335955007910182914)  # jonathan
            await user.add_roles(role)
            await channel.send('happy birthday jonathan')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 6 and day == 9:
            await client.wait_until_ready()
            user = await guild.fetch_member(180381691720761344)  # bivek
            await user.add_roles(role)
            await channel.send('happy birthday bivek')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 6 and day == 23:
            await client.wait_until_ready()
            user = await guild.fetch_member(168721477099716609)  # charley
            await user.add_roles(role)
            await channel.send('happy birthday jackson')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 7 and day == 28:
            await client.wait_until_ready()
            user = await guild.fetch_member(202586765394051094)  # piyush
            await user.add_roles(role)
            await channel.send('happy birthday piyush')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 8 and day == 24:
            await client.wait_until_ready()
            user = await guild.fetch_member(229246048470564866)  # owen
            await user.add_roles(role)
            await channel.send('happy birthday owen')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 9 and day == 19:
            await client.wait_until_ready()
            user = await guild.fetch_member(211616413553655810)  # tulley
            await user.add_roles(role)
            await channel.send('happy birthday tulley')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 9 and day == 24:
            await client.wait_until_ready()
            user = await guild.fetch_member(147855665065492480)  # sean
            await user.add_roles(role)
            await channel.send('happy birthday sean')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 10 and day == 2:
            await client.wait_until_ready()
            user = await guild.fetch_member(168390637945618432)  # zihan
            await user.add_roles(role)
            await channel.send('happy birthday zihan')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 10 and day == 8:
            await client.wait_until_ready()
            user = await guild.fetch_member(272465610707959810)  # ari
            await user.add_roles(role)
            await channel.send('happy birthday ari')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 10 and day == 9:
            await client.wait_until_ready()
            user = await guild.fetch_member(158656321367965696)  # jeremy
            await user.add_roles(role)
            await channel.send('happy birthday jeremy')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 11 and day == 16:
            await client.wait_until_ready()
            user = await guild.fetch_member(168400517884674048)  # asahi
            await user.add_roles(role)
            await channel.send('happy birthday asahi')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 11 and day == 21:
            await client.wait_until_ready()
            user = await guild.fetch_member(118470162419679240)  # jovani
            await user.add_roles(role)
            await channel.send('happy birthday jovani')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 12 and day == 8:
            await client.wait_until_ready()
            user = await guild.fetch_member(222794543987294208)  # martin
            await user.add_roles(role)
            await channel.send('happy birthday martin')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 12 and day == 16:
            await client.wait_until_ready()
            user = await guild.fetch_member(738170377003597955)  # poopsock
            await user.add_roles(role)
            await channel.send('happy birthday poopsock')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        elif month == 12 and day == 24:
            await client.wait_until_ready()
            user = await guild.fetch_member(260904201998172160)  # theo
            await user.add_roles(role)
            await channel.send('happy birthday theo')
            await channel.send(user.mention)
            await asyncio.sleep(86400)
            await user.remove_roles(role)
        else:
            await client.wait_until_ready()
            await channel.send('no birthdays today')
            await asyncio.sleep(86400)
        await check()

    if second != 00:  # to fix to the nearest whole minute
        print("second not 0, second:", second, ", sleeping for:", 60 - second, "seconds")
        await asyncio.sleep(60 - second)
        await check()
    elif hour != 0 and minute == 00:  # to fix to midnight from a whole hour
        wait = 24 - hour
        print("hour is:", hour, ", minute should be 00, minute:", minute, ", sleeping for:", 60 * 60 * wait, "seconds")
        await asyncio.sleep(60 * 60 * wait)
        await check()
    elif minute != 00:  # to get to the nearest whole hour
        wait = 60 - minute
        print("hour is:", hour, ", minute should NOT be 00, minute:", minute, ", sleeping for:", 60 * wait, "seconds")
        await asyncio.sleep(60 * wait)

    await check()

client.loop.create_task(check())
client.loop.create_task(bh(0))
client.run(TOKEN)
