import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='=', description="พูดมากว่ะ", intents=intents)
bot.remove_command('help')

# Commands
@bot.command()
async def help(ctx):
	h = discord.Embed(title = "ต้องการความช่วยเหลือหรอครับ?", color = 0x00FF00)
	h.add_field(name="อย่าสู่รู้", value="`ไปอ่านเองครับ ไม่สอน`")
	await ctx.send(embed = h)

@bot.command()
async def send(ctx, id, *, text):
		channel = ctx.bot.get_channel(int(id))
		await channel.send(text)

# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="อย่าสู่รู้ครับ"))
	print('Apichat is coming !!')

Token = os.environ["ApichatToken"]
bot.run(Token)
