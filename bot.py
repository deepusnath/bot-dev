import discord

client = discord.Client()
@client.event
async def on_message(message):
    if message.author ==  client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Hello, Awesome buddy.. I am a bot!')

client.run('OTE5MjA0MDUxMjk4Njk3MjE2.YbSZew.yROw7ROjvVZ16xjNiCzJpeCNUfo')        
