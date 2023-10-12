import discord
from discord.ext import commands
import traceback
from embed import color_Embed
import random
import asyncio
import openai

# **************************************************
# **    Comando para Lanzar una Moneda al Azar    **
# **************************************************
def Moneda(bot):
    @bot.command()
    async def moneda(ctx):
        try:
            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["moneda"]
            color = discord.Colour.from_rgb(*color_tuple)

            resultado = random.choice(["cara", "cruz"])

            # Crear un Embed para el resultado de la moneda
            embed = discord.Embed(title="Lanzamiento de Moneda", color=color)
            embed.add_field(name="Resultado", value=resultado, inline=False)

            # Comprobar si el autor tiene una imagen de perfil
            if ctx.author.avatar:
                embed.set_footer(text=f"Lanzado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            else:
                embed.set_footer(text=f"Lanzado por {ctx.author.display_name}")

            # Agregar una imagen de una moneda (cara o cruz) al Embed
            if resultado == "cara":
                embed.set_image(url="https://www.banxico.org.mx/multimedia/mon20_700anosMxTen_revPrensa.jpg")
            else:
                embed.set_image(url="https://www.banxico.org.mx/multimedia/anv_mon20Marina_prensaNgo.png")

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al tirar la moneda: {str(e)}')

# ***********************************************
# **    Comando para Jugar a la Ruleta Rusa    **
# ***********************************************
def Ruleta_Rusa(bot):
    @bot.command()
    async def ruleta(ctx):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["ruleta"]
            color = discord.Colour.from_rgb(*color_tuple)

            chamber = random.randint(1, 6)
            trigger = random.randint(1, 6)

            # Crear un Embed para el juego de la ruleta
            embed = discord.Embed(title="Ruleta Rusa", color=color)

            # Comprobar si el autor tiene una imagen de perfil
            if ctx.author.avatar:
                embed.set_footer(text=f"Jugado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            else:
                embed.set_footer(text=f"Jugado por {ctx.author.display_name}")

            if chamber == trigger:
                embed.add_field(name="¡BANG!", value="Parece que no sobreviviste. 😵💥", inline=False)
            else:
                embed.add_field(name="¡Click!", value="Sobreviviste por ahora. 😅🔫", inline=False)

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error, se trabó el revólver: {str(e)}')
def GPT(bot):
    @bot.command()
    async def chat(ctx, *, pregunta):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=pregunta,
                max_tokens=150
            )
            respuesta = response.choices[0].text

            # Comprobar si el autor tiene una imagen de perfil
            if ctx.author.avatar:
                await ctx.send(respuesta, content=f"Respuesta para {ctx.author.mention}:", embed=discord.Embed().set_thumbnail(url=ctx.author.avatar.url))
            else:
                await ctx.send(respuesta)

        except Exception as e:
            await ctx.send(f"Ocurrió un error: {e}")