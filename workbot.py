#
# CohesionBot by Jack (gitub.com/jackthebaptist)
# This bot will manage basic tasks like role changes and welcome messages
# Licensed under the GPL 3.0
#

# --- Imports ---
import sys
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from profanity import profanity
import platform

# --- Colours ---
def codechar(code):
    return CPT + str(code) + 'm'

class colour_code(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, codechar(value))

class foreground(colour_code): #foreground colours (text)
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

class background(colour_code): #background colours (selections)
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

# --- Global Variables ---
client = Bot(description="This bot will help the community", command_prefix="/", pm_help = False)

# --- Roles ---
USER_ROLES = [
    "role1",
    "role2",
    "role3"
]

# --- Channel IDs ---
WELCOME_CHANNEL = "" #add channel ID
ROLE_CHANNEL = "" #add channel ID

# --- variable texts ---


# --- Console code ---
@client.event
async def on_ready(): #Start up message for console, will not be seen on Discord
	print('======================================================')
	print('Logged in as \033[32m'+client.user.name+'\033[39m (ID:\033[32m'+client.user.id+'\033[39m) | Connected to \033[33m'+str(len(client.servers))+'\033[39m servers | Connected to \033[33m'+str(len(set(client.get_all_members())))+'\033[39m users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite your bot to other servers:')
	print('\033[32mhttps://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8\033[39m'.format(client.user.id))
	print('--------')
	print('You are running WorkBot 1.4')
	print('Created by \033[36mJack\033[39m')
	print('\033[32mhttps://github.com/jackthebaptist\033[39m')
	print('======================================================\n')
	return await client.change_presence(game=discord.Game(name='Helping the server!'))

# --- welcome code ---
@client.event
async def on_member_join(member):
    channel = discord.Object(id=WELCOME_CHANNEL)
    msg = ":new: {0} *has joined /ADD SERVER NAME/* \nTo see available roles type: **/roles**\nTo set a role type: **/set**\n To remove a role type: ** /remove**".format(member.mention)
    await client.send_message(channel, msg)


# --- role changer ---
@client.event
async def on_message(message):
	id = message.author.id
			
	if message.content.startswith("/roles"):
		s = "``` === ROLES ===\n\nrole1\nrole2\nrole3```"
		await client.send_message(message.channel,s)
		print("\033[32m[+]\033[39m request for ROLE LIST by: "+message.author.name)
	
	elif message.content.startswith("/set"):
		rchannel = discord.Object(id=ROLE_CHANNEL)
		print("\033[32m[+]\033[39m request for SET ROLE by: "+message.author.name)
		s = message.content[5:]
		newrole = s
		roles = message.server.roles
		for r in roles:
			if r.name.lower() == newrole.lower():
				if r.name.lower() in USER_ROLES:
					if r not in message.author.roles:
						await client.add_roles(message.author, r)
						await client.send_message(rchannel,":white_check_mark: User **{0}** added to {1}.".format(message.author.name, r.name))
					else:
						await client.send_message(rchannel,"You already have that role.")
				else:
					await client.send_message(rchannel,":no_entry: *You're not allowed to assign yourself to that role.*")
			
	elif message.content.startswith("/remove"):
		rchannel = discord.Object(id=ROLE_CHANNEL)
		print("\033[32m[+]\033[39m request for ROLE REMOVE by: "+message.author.name)
		s = message.content[8:]
		oldrole = s
		roles = message.server.roles
		for r in message.author.roles:
			if r.name.lower() == oldrole.lower():
				await client.remove_roles(message.author, r)
				await client.send_message(rchannel, ":white_check_mark: role was removed from **{0}**".format(message.author.name))
		

client.run('ADD DISCORD CLIENT CODE HERE')

