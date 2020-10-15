import discord
from discord.ext import commands
import os
import sys
import certifi
import json

client = commands.Bot(command_prefix="^")

@client.event
async def on_ready():
	print()
	print('------------DO NOT REMOVE CREDITS---------------')
	print("Developer: Leo Power")
	print("GitHub: https://github.com/powerthecoder")
	print("Website: https://powerthecoder.xyz/")
	print('-------------------------------------------------')
	print()
	print("-------------------------------")
	print("Bot Online")
	print('Logged In As: ',client.user.name)
	print('ID: ',client.user.id)
	print('Bot Version: 1.0')
	print('Discord Version: ',discord.__version__)
	print('-------------------------------')
	print()
	print()
	await client.change_presence(status=discord.Status.online, activity=discord.Game('SPAMMING LEO'))
	#await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Testing'))

@client.command()
async def msg(ctx, *,msg):
    embed=discord.Embed(
        title="Message Sent",
        description=f"**Sent To:** <@255876083918831616> \n**Message:** ```{msg}```"
    )
    with open("msg_sent.json", "r") as f:
        data = json.load(f)
    data["message_s"] = {}
    data["message_s"] = str(msg)
    data['sent_from'] = str(ctx.message.author)

    with open("msg_sent.json", "w") as f:
        json.dump(data, f)
    os.system("node msg.js")
    await ctx.send(embed=embed)

client.run("TOKEN")
