import discord
from discord.ext import commands
import traceback
from embed import color_Embed
import asyncio
from .Login import usuarios_autenticados

# *******************************************************
# **    Comando Para Mostrar Los Roles Del Servidor    **
# *******************************************************
def Mostrar_Roles(bot):
    @bot.command()
    async def roles(ctx):
        #if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["roles"]  # Valor por defecto si no se encuentra
                color = discord.Colour.from_rgb(*color_tuple)

                server = ctx.guild

                # Crear un Embed para mostrar la lista de roles
                embed = discord.Embed(title=f"Roles en {server.name}", color=color)
                embed.set_thumbnail(url=server.icon.url)

                roles_info = []
                for role in sorted(server.roles, key=lambda role: role.position, reverse=True):
                    if role.name != "@everyone":
                        role_info = f"{role.mention} ({len(role.members)} miembros)"
                        roles_info.append(role_info)

                roles_list_message = "\n".join(roles_info)

                embed.add_field(name=f"Total de roles: {len(server.roles) - 1}", value=roles_list_message, inline=False)

                # Comprobar si el autor tiene una imagen de perfil
                if ctx.author.avatar:
                    embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar.url)
                else:
                    embed.set_footer(text=f"Solicitado por {ctx.author.name}")

                # Enviar el Embed en el canal donde se llamó el comando
                await ctx.send(embed=embed)
            except Exception as e:
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.add_field(name="Error al mostrar los Roles", value=str(e))
                await ctx.send(embed=error_embed)
        #else:
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.add_field(name="Permiso denegado", value="No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero.")
            #await ctx.send(embed=error_embed)

# ****************************************
# **    Comando para Crear un Rol    **
# ****************************************
def Crear_Rol(bot):
    @bot.command()
    async def crear_rol(ctx, rol_nombre):
        #if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["crear_rol"]
                color = discord.Colour.from_rgb(*color_tuple)

                # Verifica si el autor tiene permisos para crear roles
                if ctx.author.guild_permissions.manage_roles:
                    # Crea el rol en el servidor
                    new_role = await ctx.guild.create_role(name=rol_nombre)

                    # Crear un Embed para mostrar la confirmación
                    embed = discord.Embed(title="Rol Creado", color=color)
                    embed.description = f"¡Se ha creado el rol '{new_role.name}' con éxito!"

                    await ctx.send(embed=embed)
                else:
                    # Crear un Embed para mostrar un mensaje de error
                    error_embed = discord.Embed(title="Error", color=discord.Color.red())
                    error_embed.description = "No tienes permisos para crear roles en este servidor."
                    await ctx.send(embed=error_embed)
            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Ha ocurrido un error al crear el rol: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)

# ****************************************************
# **    Comando para Asignar un Rol a un Miembro    **
# ****************************************************
def Asignar_Rol(bot):
    @bot.command()
    async def asignar_rol(ctx, rol: discord.Role, miembro: discord.Member):
        #if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperar 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["asignar_rol"]
                color = discord.Colour.from_rgb(*color_tuple)

                # Verificar si el autor tiene permisos para asignar roles y si el rol es manejable
                if ctx.author.guild_permissions.manage_roles and ctx.author.top_role > rol:
                    await miembro.add_roles(rol)

                    # Crear un Embed para mostrar la confirmación
                    embed = discord.Embed(title="Asignación de Rol", color=color)
                    embed.add_field(name="Rol asignado", value=rol.mention, inline=False)
                    embed.add_field(name="Miembro", value=miembro.mention, inline=False)

                    # Comprobar si el autor y el miembro tienen imágenes de perfil
                    if ctx.author.avatar:
                        embed.set_footer(text=f"Asignado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                    else:
                        embed.set_footer(text=f"Asignado por {ctx.author.display_name}")

                    if miembro.avatar:
                        embed.set_thumbnail(url=miembro.avatar.url)

                    await ctx.send(embed=embed)
                else:
                    # Crear un Embed para mostrar un mensaje de error
                    error_embed = discord.Embed(title="Error", color=discord.Color.red())
                    error_embed.description = "No tienes permisos para asignar roles o el rol que intentas asignar es superior al tuyo."
                    await ctx.send(embed=error_embed)
            except discord.Forbidden:
                await ctx.send("No tengo permisos para asignar roles o el rol que intentas asignar es superior al mío.")
            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Error al asignar un rol: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)

# ***************************************************
# **    Comando para Quitar un Rol a un Miembro    **
# ***************************************************
def Quitar_Rol(bot):
    @bot.command()
    async def quitar_rol(ctx, rol: discord.Role, miembro: discord.Member):
        #if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperar 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["quitar_rol"]
                color = discord.Colour.from_rgb(*color_tuple)

                # Verificar si el autor tiene permisos para gestionar roles y si el rol es manejable
                if ctx.author.guild_permissions.manage_roles and ctx.author.top_role > rol:
                    await miembro.remove_roles(rol)

                    # Crear un Embed para mostrar la confirmación
                    embed = discord.Embed(title="Quitar Rol", color=color)
                    embed.add_field(name="Rol retirado", value=rol.mention, inline=False)
                    embed.add_field(name="Miembro", value=miembro.mention, inline=False)

                    # Comprobar si el autor y el miembro tienen imágenes de perfil
                    if ctx.author.avatar:
                        embed.set_footer(text=f"Retirado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                    else:
                        embed.set_footer(text=f"Retirado por {ctx.author.display_name}")

                    if miembro.avatar:
                        embed.set_thumbnail(url=miembro.avatar.url)

                    await ctx.send(embed=embed)
                else:
                    # Crear un Embed para mostrar un mensaje de error
                    error_embed = discord.Embed(title="Error", color=discord.Color.red())
                    error_embed.description = "No tienes permisos para quitar roles o el rol que intentas quitar es superior al tuyo."
                    await ctx.send(embed=error_embed)
            except discord.Forbidden:
                await ctx.send("No tengo permisos para quitar roles o el rol que intentas quitar es superior al mío.")
            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Error al quitar un rol: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)

# *****************************************************
# **    Comando para Eliminar un Rol del Servidor    **
# *****************************************************
def Eliminar_Rol(bot):
    @bot.command()
    async def eliminar_rol(ctx, rol: discord.Role):
        #if ctx.author.id in usuarios_autenticados:
            try:
                # Mostrar "Escribiendo..."
                async with ctx.typing():
                    await asyncio.sleep(3)  # Esperar 3 segundos simulando "Escribiendo..."

                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["eliminar_rol"]
                color = discord.Colour.from_rgb(*color_tuple)

                # Verificar si el autor tiene permisos para administrar roles
                if ctx.author.guild_permissions.manage_roles:
                    # Elimina el rol del servidor
                    await rol.delete()

                    # Crear un Embed informativo
                    embed = discord.Embed(
                        title="Rol Eliminado",
                        description=f"¡El rol '{rol.name}' ha sido eliminado con éxito!",
                        color=color
                    )

                    # Comprobar si el autor tiene una imagen de perfil
                    if ctx.author.avatar:
                        embed.set_footer(text=f"Eliminado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
                    else:
                        embed.set_footer(text=f"Eliminado por {ctx.author.display_name}")

                    await ctx.send(embed=embed)
                else:
                    # Crear un Embed para mostrar un mensaje de error
                    error_embed = discord.Embed(title="Error", color=discord.Color.red())
                    error_embed.description = "No tienes permisos para eliminar roles en este servidor."
                    await ctx.send(embed=error_embed)
            except discord.Forbidden:
                await ctx.send("No tengo permisos para eliminar roles o el rol que intentas eliminar es superior al mío.")
            except Exception as e:
                # Crear un Embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(title="Error", color=discord.Color.red())
                error_embed.description = f"Error al eliminar el rol: {str(e)}"
                await ctx.send(embed=error_embed)
        #else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            #error_embed = discord.Embed(title="Error", color=discord.Color.red())
            #error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            #await ctx.send(embed=error_embed)
