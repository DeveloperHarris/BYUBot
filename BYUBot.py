import discord
from discord.ext import commands
import asyncio

DISCORD_KEY = ''

ROLE_CHANNEL_ID = 399963477302575105;

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():

	print(discord.__version__)

	print('------')

	print('Logged in as:')
	print(bot.user.name)
	print(bot.user.id)

	print('------')


@bot.command()
async def iam(ctx, role:discord.Role):

	if (ctx.channel.id == ROLE_CHANNEL_ID):

		if (role not in ctx.author.roles):

			if (role.name != "mod" or role.name != "TA"):

				await ctx.author.add_roles(role)

				await ctx.send(ctx.author.mention + ' you have been given the ' + role.name + ' role.')

		else:

			await ctx.send(ctx.author.mention + ' you already have the ' + role.name + ' role.')

@bot.command()
async def iamnot(ctx, role:discord.Role):

	if (ctx.channel.id == ROLE_CHANNEL_ID):

		if (role not in ctx.author.roles):

			await ctx.send(ctx.author.mention + ' you do not have the ' + role.name + ' role.')

		else:	

			await ctx.author.remove_roles(role)

			await ctx.send(ctx.author.mention + ' you have been removed from the ' + role.name + ' role.')




bot.run(DISCORD_KEY)