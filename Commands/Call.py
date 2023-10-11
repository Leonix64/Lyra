import discord
from discord.ext import commands
from embed import color_Embed
import asyncio

# *************************************************
# **    Comando para Unirse a un Canal de Voz    **
# *************************************************
def Join_Llamada(bot):
    @bot.command()
    async def unirse(ctx):
        # Verifica si el autor del comando está en un canal de voz
        if ctx.author.voice is None:
            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["unirse_error"]
            color = discord.Colour.from_rgb(*color_tuple)

            # Crear un embed de error con un color RGB personalizado
            embed = discord.Embed(
                title="Error al unirse al canal de voz",
                description="Debes estar en un canal de voz para que yo me una.",
                color=color
            )
            await ctx.send(embed=embed)
            return

        # Obtén el canal de voz en el que se encuentra el autor del comando
        channel = ctx.author.voice.channel

        # Intenta unirse al canal de voz
        try:
            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["unirse"]
            color = discord.Colour.from_rgb(*color_tuple)

            voice_client = await channel.connect()

            # Crear un embed exitoso con un color RGB personalizado
            embed = discord.Embed(
                title="Lyra se unido al canal de voz",
                description=f"Me he unido al canal de voz: {channel.name}",
                color=color
            )
            await ctx.send(embed=embed)
        except Exception as e:
            # Crear un embed de error con un color RGB personalizado para mostrar el error
            color_tuple = color_Embed["unirse_error"]
            color = discord.Colour.from_rgb(*color_tuple)

            embed = discord.Embed(
                title="Error al unirse al canal de voz",
                description=f"Ocurrió un error al intentar unirse al canal de voz: {e}",
                color=color
            )
            await ctx.send(embed=embed)

        print('-------------------------------------------------------')

# ***********************************************
# **    Comando para Salir del Canal de Voz    **
# ***********************************************
def Exit_Call (bot):
    @bot.command()
    async def salir(ctx):
        # Verifica si el bot está en un canal de voz
        if ctx.voice_client is not None:
            try:
                await ctx.voice_client.disconnect()

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["salir"]
                color = discord.Colour.from_rgb(*color_tuple)

                # Crear un embed con un color RGB personalizado (por ejemplo, RGB 100, 200, 50)
                embed = discord.Embed(
                    title="Bot desconectado del canal de voz",
                    description="Me he desconectado exitosamente del canal de voz.",
                    color=color
                )
                await ctx.send(embed=embed)
            except Exception as e:
                # Crear un embed con un color RGB personalizado para mostrar el error (por ejemplo, RGB 200, 50, 50)
                embed = discord.Embed(
                    title="Error al desconectarse del canal de voz",
                    description=f"Ocurrió un error al intentar desconectarse del canal de voz: {e}",
                    color=color
                )
                await ctx.send(embed=embed)
        else:
            # Si el bot no está en un canal de voz
            embed = discord.Embed(
                title="Error al desconectarse del canal de voz",
                description="El bot no está en un canal de voz.",
                color=color
            )
            await ctx.send(embed=embed)

        print('-------------------------------------------------------')