import discord
from discord.ext import commands
import qrcode
from io import BytesIO
import traceback
from embed import color_Embed
import string
import secrets
import asyncio
from .Login import usuarios_autenticados

# *******************************************
# **    Comando para Generar Códigos QR    **
# *******************************************
def Code_QR(bot):
    @bot.command()
    async def QR(ctx, *, contenido):
        #if ctx.author.id in usuarios_autenticados:
            try:
                # Verificar que el contenido tenga menos de 500 caracteres
                if len(contenido) > 500:
                    # Crear un Embed para mostrar un mensaje de error
                    error_embed = discord.Embed(title="Error", color=discord.Color.red())
                    error_embed.description = "El contenido debe tener un máximo de 500 caracteres para generar el QR correctamente."
                    await ctx.send(embed=error_embed)
                    return

                autor = ctx.author

                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(1)  # Esperar 1 segundo simulando "Escribiendo..."

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

                # Comprobar si el autor tiene una imagen de perfil
                if ctx.author.avatar:
                    embed.set_author(name=f"Solicitado por: {autor.display_name}", icon_url=autor.avatar.url)
                else:
                    embed.set_author(name=f"Solicitado por: {autor.display_name}")

                embed.set_image(url="attachment://codigo_qr.png")

                # Enviar el Embed con la imagen del código QR en el canal donde se llamó el comando
                await ctx.send(embed=embed, file=discord.File(img_io, filename="codigo_qr.png"))

                # Borrar el mensaje que menciona al bot y el mensaje original que generó el comando
                await ctx.message.delete()
            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"He encontrado un error al generar el código QR: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)

# ******************************************************
# **    Comando para Generar una Contraseña Segura    **
# ******************************************************
def Password(bot):
    @bot.command()
    async def password(ctx, longitud: int = 20):
        #if ctx.author.id in usuarios_autenticados:
            try:

                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(0)  # Esperar 0 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["password"]
                color = discord.Colour.from_rgb(*color_tuple)

                caracteres = string.ascii_letters + string.digits + string.punctuation
                contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))

                # Crear un Embed para la contraseña segura
                embed = discord.Embed(title="Generador de Contraseña Segura", color=color)
                embed.add_field(name="Contraseña generada", value=f'||`{contrasena}`||', inline=False)

                # Comprobar si el autor tiene una imagen de perfil
                if ctx.author.avatar:
                    embed.set_footer(text=f'Generada por {ctx.author.display_name}', icon_url=ctx.author.avatar.url)
                else:
                    embed.set_footer(text=f'Generada por {ctx.author.display_name}')

                # Enviar el Embed en un mensaje privado al usuario
                await ctx.author.send(embed=embed)
                confirmation_embed = discord.Embed(title="Generación de Contraseña", description="¡Te he enviado tu contraseña por mensaje privado!", color=color)
                await ctx.send(embed=confirmation_embed)

            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Error al generar la contraseña: {str(e)}"
                await ctx.send(embed=error_embed)

        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)


# **************************************************
# **    Comando para Enviar un Mensaje Anónimo    **
# **************************************************
def Anonimo(bot):
    @bot.command()
    async def mensaje_anonimo(ctx, canal: discord.TextChannel, *, contenido):
        #if ctx.author.id in usuarios_autenticados:
            try:

                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperar 3 segundos simulando "Escribiendo..."

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

            except discord.Forbidden:
                await ctx.send("No tengo permisos para enviar mensajes en ese canal o el canal especificado no es válido.")
            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Error al enviar el mensaje anónimo: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)

# **********************************************************
# **    Comando para Enviar un Mensaje en Código Morse    **
# **********************************************************
def Code_Morse(bot):
    @bot.command()
    async def morse(ctx, *mensaje):
        #if ctx.author.id in usuarios_autenticados:
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

                # Traducir el mensaje original a código Morse
                mensaje_morse = " ".join([morse_code_dict.get(c.upper(), c) for c in " ".join(mensaje)])

                # Crear un Embed para el mensaje en código Morse
                embed = discord.Embed(title="Mensaje en Código Morse", color=color)
                embed.add_field(name="Mensaje original", value=" ".join(mensaje), inline=False)
                embed.add_field(name="Mensaje en Morse", value=mensaje_morse, inline=False)

                # Comprobar si el autor tiene una imagen de perfil
                if ctx.author.avatar:
                    embed.set_footer(text=f"Convertido por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                else:
                    embed.set_footer(text=f"Convertido por {ctx.author.display_name}")

                await ctx.send(embed=embed)

            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Error al traducir: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)
