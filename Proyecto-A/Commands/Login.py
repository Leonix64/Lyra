import discord
from discord.ext import commands
import mysql.connector
from config import db_config
import base64

# Variable de estado para rastrear si un usuario ha iniciado sesión
usuarios_autenticados = set()

# ***************************************
# **    Comando de inicio de sesión    **
# ***************************************
def Login(bot):
    @bot.command()
    async def login(ctx, password: str):
        try:
            # Conectar a la base de datos
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Desencriptar la contraseña almacenada en la base de datos y verificar si coincide
            query = "SELECT user_id, username, password FROM users WHERE user_id = %s"
            cursor.execute(query, (ctx.author.id,))
            result = cursor.fetchone()

            if result:
                stored_password = base64.b64decode(result[2]).decode('utf-8')
                if password == stored_password:
                    usuarios_autenticados.add(ctx.author.id)  # Marcar al usuario como autenticado
                    
                    # Crear un Embed para mostrar el mensaje de inicio de sesión exitoso
                    embed = discord.Embed(title="Inicio de Sesión Exitoso", color=discord.Color.green())
                    embed.add_field(name="Bienvenido", value=f"{result[1]}")
                    await ctx.send(embed=embed)
                else:
                    # Crear un Embed para mostrar el mensaje de inicio de sesión fallido (en rojo)
                    error_embed = discord.Embed(title="Inicio de Sesión Fallido", color=discord.Color.red())
                    error_embed.add_field(name="Error", value="Verifica tu contraseña.")
                    await ctx.send(embed=error_embed)
            else:
                # Crear un Embed para mostrar el mensaje de inicio de sesión fallido (en rojo)
                error_embed = discord.Embed(title="Inicio de Sesión Fallido", color=discord.Color.red())
                error_embed.add_field(name="Error", value="No estás registrado.")
                await ctx.send(embed=error_embed)

            # Cerrar la conexión a la base de datos
            cursor.close()
            conn.close()
        except Exception as e:
            # Crear un Embed para mostrar un mensaje de error (en rojo)
            error_embed = discord.Embed(title="Error", color=discord.Color.red())
            error_embed.add_field(name="Error en el inicio de sesión", value=str(e))
            await ctx.send(embed=error_embed)

# ****************************************************
# **    Comando para que un usuario asigne su contraseña    **
# ****************************************************
def Registro(bot):
    @bot.command()
    async def register(ctx, password: str):
        try:
            # Conectar a la base de datos
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Verificar si el usuario ya está registrado
            query = "SELECT user_id FROM users WHERE user_id = %s"
            cursor.execute(query, (ctx.author.id,))
            result = cursor.fetchone()

            if result:
                # Crear un Embed para mostrar un mensaje de error (en rojo)
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.add_field(name="Error en el registro", value="Ya estás registrado. No puedes registrarte de nuevo.")
                await ctx.send(embed=error_embed)
            else:
                # Encriptar la contraseña en base64 antes de almacenarla en la base de datos
                encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')

                # Insertar el usuario y la contraseña en la base de datos
                query = "INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)"
                data = (ctx.author.id, ctx.author.display_name, encoded_password)
                cursor.execute(query, data)
                conn.commit()

                # Crear un Embed para mostrar un mensaje de registro exitoso (en verde)
                success_embed = discord.Embed(title="Registro Exitoso", color=discord.Color.green())
                success_embed.add_field(name="Éxito", value="Contraseña asignada y registrado correctamente.")
                await ctx.send(embed=success_embed)

            # Cerrar la conexión a la base de datos
            cursor.close()
            conn.close()
        except Exception as e:
            # Crear un Embed para mostrar un mensaje de error (en rojo)
            error_embed = discord.Embed(title="Error", color=discord.Color.red())
            error_embed.add_field(name="Error en el registro", value=str(e))
            await ctx.send(embed=error_embed)

# *************************************************************
# **    Comando para salir del estado de inicio de sesión    **
# *************************************************************
def Logout(bot):
    @bot.command()
    async def logout(ctx):
        if ctx.author.id in usuarios_autenticados:
            usuarios_autenticados.remove(ctx.author.id)
            # Crear un Embed para mostrar un mensaje exitoso (en verde)
            success_embed = discord.Embed(title="Cierre de Sesión Exitoso", color=discord.Color.green())
            success_embed.add_field(name="Éxito", value="¡Has cerrado tu sesión! Ya no estás autenticado.")
            await ctx.send(embed=success_embed)
        else:
            # Crear un Embed para mostrar un mensaje de error (en rojo)
            error_embed = discord.Embed(title="Error", color=discord.Color.red())
            error_embed.add_field(name="Error en el cierre de sesión", value="No estás autenticado. No puedes cerrar la sesión si no has iniciado sesión previamente.")
            await ctx.send(embed=error_embed)

# ********************************************************************************
# **    Comando protegido que solo puede ser usado por usuarios autenticados    **
# ********************************************************************************
def Special(bot):
    @bot.command()
    async def especial(ctx):
        if ctx.author.id in usuarios_autenticados:
            # Crear un Embed para mostrar un mensaje exitoso (en verde)
            success_embed = discord.Embed(title="Comando Especial", color=discord.Color.green())
            success_embed.add_field(name="Éxito", value="¡Has ejecutado un comando confidencial!")
            await ctx.send(embed=success_embed)
        else:
            # Crear un Embed para mostrar un mensaje de error (en rojo)
            error_embed = discord.Embed(title="Error", color=discord.Color.red())
            error_embed.add_field(name="Error en el comando especial", value="No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero.")
            await ctx.send(embed=error_embed)
