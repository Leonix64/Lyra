import discord
from discord.ext import commands, tasks
import qrcode
from io import BytesIO
import traceback
from embed import color_Embed
import string
import secrets
import asyncio

# *******************************************
# **    Comando para Generar Códigos QR    **
# *******************************************
def Code_QR(bot):
    @bot.command()
    async def QR(ctx, *, contenido):
        try:
            # Verificar que el contenido tenga menos de 500 caracteres
            if len(contenido) > 500:
                await ctx.send("El contenido debe tener un máximo de 500 caracteres para generar el QR correctamente.")
                return

            autor = ctx.author

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["QR"]
            color = discord.Colour.from_rgb(*color_tuple)

            # Crear un objeto QRCode con el contenido proporcionado
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(contenido)
            qr.make(fit=True)

            # Crear una imagen del código QR en formato BytesIO
            img_io = BytesIO()
            img = qr.make_image(fill_color="white", back_color="#36393F")
            img.save(img_io, "PNG")
            img_io.seek(0)

            # Crear un Embed para la respuesta
            embed = discord.Embed(title="Código QR generado", color=color)
            mensaje_lyra = "He generado un Código QR para ti."
            embed.description = mensaje_lyra
            embed.set_author(name=f"Solicitado por: {autor.display_name}", icon_url=autor.avatar.url)
            embed.set_image(url="attachment://codigo_qr.png")

            # Enviar el Embed con la imagen del código QR en el canal donde se llamó el comando
            await ctx.send(embed=embed, file=discord.File(img_io, filename="codigo_qr.png"))

            # Borrar el mensaje que menciona al bot y el mensaje original que generó el comando
            await ctx.message.delete()
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'He encontrado un error al generar el código QR: {str(e)}')

# ******************************************************
# **    Comando para Generar una Contraseña Segura    **
# ******************************************************
def Password(bot):
    @bot.command()
    async def password(ctx, longitud: int = 20):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["password"]
            color = discord.Colour.from_rgb(*color_tuple)

            caracteres = string.ascii_letters + string.digits + string.punctuation
            contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))

            # Crear un Embed para la contraseña segura
            embed = discord.Embed(title="Generador de Contraseña Segura", color=color)
            embed.add_field(name="Contraseña generada", value=f'||`{contrasena}`||', inline=False)
            #print(f"Contraseña generada: {contrasena} por: {ctx.author.display_name}")
            embed.set_footer(text=f'Generada por {ctx.author.display_name}', icon_url=ctx.author.avatar.url)

            # Enviar el Embed en un mensaje privado al usuario
            await ctx.author.send(embed=embed)
            await ctx.send("¡Te he enviado tu contraseña por mensaje privado!")

        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al generar la contraseña: {str(e)}')

# **************************************************
# **    Comando para Enviar un Mensaje Anónimo    **
# **************************************************
def Anonimo(bot):
    @bot.command()
    async def mensaje_anonimo(ctx, canal: discord.TextChannel, *, contenido):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["mensaje_anonimo"]
            color = discord.Colour.from_rgb(*color_tuple)

            # Crear un Embed para el mensaje anónimo
            embed = discord.Embed(title="Mensaje Anónimo", color=color)
            embed.add_field(name="Contenido del mensaje", value=contenido, inline=False)

            # Enviar el Embed en el canal especificado
            await canal.send(embed=embed)

            # Borrar el mensaje del autor del comando
            await ctx.message.delete()

        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al enviar el mensaje: {str(e)}')

# **********************************************************
# **    Comando para Enviar un Mensaje en Código Morse    **
# **********************************************************
def Code_Morse(bot):
    @bot.command()
    async def morse(ctx, *mensaje):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."
                
            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["morse"]
            color = discord.Colour.from_rgb(*color_tuple)

            morse_code_dict = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                '9': '----.', ' ': '/'
            }

            mensaje_morse = " ".join([morse_code_dict.get(c.upper(), c) for c in " ".join(mensaje)])

            # Crear un Embed para el mensaje en código Morse
            embed = discord.Embed(title="Mensaje en Código Morse", color=color)
            embed.add_field(name="Mensaje original", value=" ".join(mensaje), inline=False)
            embed.add_field(name="Mensaje en Morse", value=mensaje_morse, inline=False)
            embed.set_footer(text=f"Convertido por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al traducir: {str(e)}')

