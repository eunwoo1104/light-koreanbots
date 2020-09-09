import light_koreanbots as lkb
import discord

client = discord.Client()
kbot_token = "koreanbots_token"
lkb_client = lkb.LKBClient(bot=client, token=kbot_token)

client.run("discord_token")
