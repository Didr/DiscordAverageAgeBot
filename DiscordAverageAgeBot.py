import discord
from datetime import datetime, date
from statistics import mean 

def GetUserAgeInDays(user):
    userage = datetime.now() - user.created_at
    return userage.days


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$averageage'):
        await message.channel.send('Calculating average user age...')
        members = message.guild.members
        daylist = []
        for member in members:
            if member.bot == True: # We don't want to count the age of bots.
                continue
            else:
                memberdate = GetUserAgeInDays(member)
                print(f"{member.name} is {memberdate} days old.")
                daylist.append(memberdate)
        print(daylist)
        average = mean(daylist)
        await message.channel.send(f"Average age of {len(daylist)} registered users on this server is: {round(average, 3)} days!")
            


client.run('token')