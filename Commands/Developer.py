import discord
from discord.ext import commands

def Givemebadge(bot):
    @bot.command()
    async def givemebadge(ctx):
        # Enviamos un mensaje al usuario indicando cómo reclamar la insignia
        await ctx.send("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")