import discord
import asyncio
from discord.ext import commands
import random

 
startup_extensions = ["General"]
bot = commands.Bot("cb!")
 
@bot.event
async def on_ready():
    print('Chewie Bot Has Successfully launched!')
 
class Main_Commands():
    def __init__(self, bot):
        self.bot = bot
 
@bot.command(pass_context=True)
async def Reqmod(ctx):
    """This Command Gives You Mod!"""
    await bot.say("Requesting...")
    await asyncio.sleep(1.5)
    await bot.say("Failed Nothing Found.")

@bot.command(pass_context=True)
async def Ratemylvl(ctx):
    """Do I Have To?"""
    await bot.say("Nah, To much work for me :joy:")

@bot.command(pass_context=True)
async def ModHack(ctx):
    """This Will Give You Mod On Any Server!"""
    await bot.say("Hacking...")
    await asyncio.sleep(1.0)
    await bot.say("Finding GDPS database...")
    await asyncio.sleep(1.0)
    await bot.say("Found Database Successfully!")
    await asyncio.sleep(1.0)
    await bot.say("Finding Name And Password Please Wait...")
    await asyncio.sleep(1.0)
    await bot.say("Found!")
    await asyncio.sleep(1.0)
    await bot.say("Assigning Role Mod, To The Given Account ID...")
    await asyncio.sleep(1.0)
    await bot.say("Succes!")
    await asyncio.sleep(1.0)
    await bot.say("Activating Hidemephp...")
    await asyncio.sleep(0.5)
    await bot.say("Anticheat Success!")
    await asyncio.sleep(1.0)
    await bot.say("You Can Now Open The Server And Req")

@bot.command(pass_context=True)
async def Rndcode(ctx) :
    """The Random Code Challenge. You Must Find 666.666 To Win!"""
    await bot.say(random.choice(["PUSPUS",
"Nope","Why Even Try?","Just Stop","Yawn","You Can't Win","STOP IT","666.666","ha ha!","Incorrect","NANI!?","/RubRubRubRubRub","ChewTop","Damk memes","lol nub","Nah","Kappa","(⍤ᴥ⍤)","¯\_(ツ)_/¯",":thinking:",":b:",":joy: You Can't Do It Lmfao!","666.665","666.66","666.661"]))

bot.run("NDE2OTI1MDY0NzM1MzU4OTc2.DXLtUw.gamNH5NaQJG5WuMcXvKDWNd2lls")
