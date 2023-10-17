import discord
from discord.ext import commands
from embed import color_Embed
import datetime
from help import commands_list
import asyncio
from .Login import usuarios_autenticados

# *********************************************************
# **    Comando para Solicitar la Información del Bot    **
# *********************************************************
def Lyra_Info(bot):
    @bot.command()
    async def Lyra(ctx):
        if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrando "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperando 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["infobot"]
                color = discord.Colour.from_rgb(*color_tuple)

                bot_user = bot.user
                embed = discord.Embed(title="Información sobre mí", color=color)
                embed.set_thumbnail(url=bot_user.avatar.url)
                embed.add_field(name="Nombre", value=bot_user.name, inline=False)
                embed.add_field(name="Versión", value="2.5", inline=False)
                embed.add_field(name="Creada por", value="leonix64", inline=False)
                embed.add_field(name="Mi código fuente", value="[Enlace al código fuente](Proximamente...)", inline=False)
                await ctx.send(embed=embed)
            except Exception as e:
                # Mostrando un error en rojo
                color_error = discord.Colour.from_rgb(255, 0, 0)
                embed_error = discord.Embed(title="Error", color=color_error)
                embed_error.add_field(name="Error al obtener la información del bot", value=str(e), inline=False)
                await ctx.send(embed=embed_error)
        else:
            await ctx.send("No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero.")

# ***************************************************************
# **    Comando para Solicitar la Información de un Usuario    **
# ***************************************************************
def User_Info(bot):
    @bot.command()
    async def userinfo(ctx, member: discord.Member = None):
        if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrando "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperando 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["userinfo"]
                color = discord.Colour.from_rgb(*color_tuple)

                if member is None:
                    member = ctx.author

                embed = discord.Embed(title=f"Información de {member.name}", color=color)

                if member.avatar:
                    embed.set_thumbnail(url=member.avatar.url)

                # Información básica
                embed.add_field(name="Nombre de usuario", value=member.name, inline=True)
                embed.add_field(name="Apodo", value=member.nick if member.nick else "N/A", inline=True)
                embed.add_field(name="ID de usuario", value=member.id, inline=False)
                embed.add_field(name="Cuenta creada el", value=member.created_at.strftime("%d de %B de %Y a las %H:%M:%S"), inline=False)
                embed.add_field(name="Se unió al servidor el", value=member.joined_at.strftime("%d de %B de %Y a las %H:%M:%S"), inline=False)

                # Más información
                embed.add_field(name="Estado", value=str(member.status).title(), inline=True)
                embed.add_field(name="Cumpleaños", value=member.created_at.strftime("%d de %B"), inline=True)
                embed.add_field(name="Móvil", value="Sí" if member is not None and member.is_on_mobile() else "No", inline=True)
                embed.add_field(name="Es un bot?", value="Sí" if member is not None and member.bot else "No", inline=True)
                embed.add_field(name="Boost del servidor", value=member.premium_since.strftime("%d de %B de %Y a las %H:%M:%S") if member.premium_since else "N/A", inline=False)
                embed.add_field(name="Cuenta verificada", value="Sí" if member.public_flags.verified_bot else "No", inline=True)

                # Roles del usuario
                roles_str = ", ".join([role.mention for role in member.roles[1:]])
                embed.add_field(name="Roles", value=roles_str if roles_str else "N/A", inline=False)

                # Actividad del usuario
                if member.activity:
                    if member.activity.type == discord.ActivityType.playing:
                        activity_type = "Jugando a"
                    elif member.activity.type == discord.ActivityType.streaming:
                        activity_type = "Transmitiendo"
                    elif member.activity.type == discord.ActivityType.listening:
                        activity_type = "Escuchando"
                    elif member.activity.type == discord.ActivityType.watching:
                        activity_type = "Viendo"
                    else:
                        activity_type = "Otra actividad"

                    activity_details = member.activity.name
                    embed.add_field(name="Actividad", value=f"{activity_type} {activity_details}", inline=False)

                await ctx.send(embed=embed)
            except Exception as e:
                # Mostrando un error en rojo
                color_error = discord.Colour.from_rgb(255, 0, 0)
                embed_error = discord.Embed(title="Error", color=color_error)
                embed_error.add_field(name="Error al obtener la información del usuario", value=str(e), inline=False)
                await ctx.send(embed=embed_error)

        else:
            await ctx.send("No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero.")

# ***********************************************************************
# **    Comando para Solicitar la Información del Bot de Servidores    **
# ***********************************************************************
def Estadisticas_Bot_Info(bot):
    @bot.command()
    async def stats(ctx):
        if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrando "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperando 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["stats"]
                color = discord.Colour.from_rgb(*color_tuple)

                total_users = len(bot.users)
                total_servers = len(bot.guilds)
                uptime = datetime.datetime.utcnow() - bot.user.created_at.replace(tzinfo=None)

                # Crear un Embed para mostrar las estadísticas del bot
                embed = discord.Embed(title="Mis Estadísticas", color=color)
                embed.add_field(name="Usuarios totales", value=total_users)
                embed.add_field(name="Servidores totales", value=total_servers)
                embed.add_field(name="Tiempo en línea", value=str(uptime).split(".")[0])

                # Comprobar si el autor tiene una imagen de perfil
                if ctx.author.avatar:
                    embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                else:
                    embed.set_footer(text=f"Solicitado por {ctx.author.display_name}")

                await ctx.send(embed=embed)
            except Exception as e:
                # Mostrando un error en rojo
                color_error = discord.Colour.from_rgb(255, 0, 0)
                embed_error = discord.Embed(title="Error", color=color_error)
                embed_error.add_field(name="Error al obtener las estadísticas", value=str(e), inline=False)
                await ctx.send(embed=embed_error)
        else:
            await ctx.send("No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero.")

# **********************************************************
# **    Comando para Mostrar Estadísticas Del Servidor    **
# **********************************************************
def Server_Info(bot):
    @bot.command()
    async def estadisticas(ctx):
        if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrando "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperando 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["estadisticas"]
                color = discord.Colour.from_rgb(*color_tuple)

                server = ctx.guild
                member_count = len(server.members)
                role_count = len(server.roles)
                channel_count = len(server.channels)
                text_channels = len(server.text_channels)
                voice_channels = len(server.voice_channels)
                category_count = len(server.categories)
                emoji_count = len(server.emojis)
                online_members = sum(1 for member in server.members if member.status != discord.Status.offline)
                offline_members = sum(1 for member in server.members if member.status != discord.Status.online)

                embed = discord.Embed(title=f"Estadísticas del Servidor {server.name}", color=color)
                embed.description = "Aquí tienes las estadísticas del servidor."
                embed.set_thumbnail(url=server.icon.url)
                embed.add_field(name="Miembros Totales", value=member_count)
                embed.add_field(name="No. Roles", value=role_count)
                embed.add_field(name="Canales Totales", value=channel_count)
                embed.add_field(name="Canales de Texto", value=text_channels)
                embed.add_field(name="Canales de Voz", value=voice_channels)
                embed.add_field(name="Categorías", value=category_count)
                embed.add_field(name="Emojis", value=emoji_count)
                embed.add_field(name="Miembros en Línea", value=online_members)
                embed.add_field(name="Miembros Desconectados", value=offline_members)

                await ctx.send(embed=embed)
            except Exception as e:
                # Mostrando un error en rojo
                color_error = discord.Colour.from_rgb(255, 0, 0)
                embed_error = discord.Embed(title="Error", color=color_error)
                embed_error.add_field(name="Error al dar las estadísticas", value=str(e), inline=False)
                await ctx.send(embed=embed_error)
        else:
            await ctx.send("No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero.")

# ***************************************************************
# **    Comando para Solicitar Ayuda con Comandos Generales    **
# ***************************************************************
def Ayuda(bot):
    @bot.command()
    async def ayuda(ctx, command_name: str = None):
        try:
            # Mostrando "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3)  # Esperando 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["ayuda"]
            color = discord.Colour.from_rgb(*color_tuple)

            if command_name:
                for command in commands_list:
                    if command["name"] == command_name:
                        embed = discord.Embed(title=f"Comando: {command_name}", color=color)
                        embed.add_field(name="Descripción", value=command["description"], inline=False)
                        embed.add_field(name="Uso", value=command["usage"], inline=False)
                        await ctx.send(embed=embed)
                        return
                await ctx.send(f"No se encontró el comando '{command_name}'.")
            else:
                # Crear un diccionario de categorías
                categorias = {
                    "/=== Login ===/": [],
                    "/=== Seguridad ===/": [],
                    "/=== Roles ===/": [],
                    "/=== Informacion ===/": [],
                    "/=== Entretenimiento ===/": [],
                    "/=== Llamada ===/": [],
                    "/=== Saludo ===/": [],
                    "/=== Utilidades ===/": [],
                }
                for command in commands_list:
                    categorias[command['category']].append(f"**{command['name']}** - {command['description']}\n*`Uso:`* {command['usage']}\n")

                embed = discord.Embed(title="Comandos Disponibles por Categoría", color=color)
                for categoria, comandos in categorias.items():
                    if comandos:
                        embed.add_field(name=f"**{categoria}**", value="\n".join(comandos), inline=False)
                await ctx.send(embed=embed)
        except Exception as e:
            # Mostrando un error en rojo
            color_error = discord.Colour.from_rgb(255, 0, 0)
            embed_error = discord.Embed(title="Error", color=color_error)
            embed_error.add_field(name="Error al obtener la ayuda del comando", value=str(e), inline=False)
            await ctx.send(embed=embed_error)

# ********************************************************
# **    Comando para Realizar una Prueba de Latencia    **
# *********************************************************
def Latencia(bot):
    @bot.command()
    async def ping(ctx):
        try:
            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["ping"]
            color = discord.Colour.from_rgb(*color_tuple)
            latency = round(bot.latency * 1000)  # Convertir latencia a milisegundos

            # Crear un Embed para mostrar la latencia
            embed = discord.Embed(title="Ping de Lyra", color=color)
            embed.add_field(name="Pong! Latencia", value=f"{latency} ms", inline=False)
            
            # Comprobar si el autor tiene una imagen de perfil
            if ctx.author.avatar:
                embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            else:
                embed.set_footer(text=f"Solicitado por {ctx.author.display_name}")

            await ctx.send(embed=embed)
        except Exception as e:
            # Mostrar un error en rojo
            color_error = discord.Colour.from_rgb(255, 0, 0)
            embed_error = discord.Embed(title="Error", color=color_error)
            embed_error.add_field(name="Error al establecer la latencia", value=str(e))

            await ctx.send(embed=embed_error)
