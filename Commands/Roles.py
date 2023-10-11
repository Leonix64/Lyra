import discord
from discord.ext import commands
import traceback
from embed import color_Embed
import asyncio

# *******************************************************
# **    Comando Para Mostrar Los Roles Del Servidor    **
# *******************************************************
def Mostrar_Roles(bot):
    @bot.command()
    async def roles(ctx):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["roles"]  # Valor por defecto si no se encuentra
            color = discord.Colour.from_rgb(*color_tuple)

            server = ctx.guild

            # Obtener información detallada de los roles
            roles_info = []
            for role in sorted(server.roles, key=lambda role: role.position, reverse=True):
                if role.name != "@everyone":
                    role_info = f"{role.mention} ({len(role.members)} miembros)"
                    roles_info.append(role_info)

            roles_list_message = "\n".join(roles_info)

            # Crear un Embed para la lista de roles
            embed = discord.Embed(
                title=f"Roles en este Servidor ({len(server.roles) - 1} roles)",  # Restar 1 para excluir "@everyone"
                description=roles_list_message,
                color=color
            )
            embed.set_thumbnail(url=server.icon.url)
            embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar.url)

            # Enviar el Embed en el canal donde se llamó el comando
            await ctx.send(embed=embed)

        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al mostrar los Roles: {str(e)}')

# ****************************************
# **    Comando para Crear un Rol    **
# ****************************************
def Crear_Rol(bot):
    @bot.command()
    async def crear_rol(ctx, rol_nombre):
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
                await ctx.guild.create_role(name=rol_nombre)

                # Crear un Embed
                embed = discord.Embed(
                    title="Rol Creado",
                    description = f"¡He creado el rol '{rol_nombre}' con éxito!",
                    color=color
                )

                await ctx.send(embed=embed)
            else:
                await ctx.send("No tienes permisos para crear roles en este servidor.")
        except Exception as e:
            await ctx.send(f"Ha ocurrido un error al crear el rol: {str(e)}")

# ****************************************************
# **    Comando para Asignar un Rol a un Miembro    **
# ****************************************************
def Asignar_Rol(bot):
    @bot.command()
    async def asignar_rol(ctx, rol: discord.Role, miembro: discord.Member):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["asignar_rol"]
            color = discord.Colour.from_rgb(*color_tuple)

            await miembro.add_roles(rol)

            # Crear un Embed informativo
            embed = discord.Embed(title="Asignación de Rol", color=color)
            embed.add_field(name="Rol asignado", value=rol.mention, inline=False)
            embed.add_field(name="Miembro", value=miembro.mention, inline=False)
            embed.set_footer(text=f"Asigné el rol por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url=miembro.avatar.url)

            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send("No tengo permisos para asignar roles o el rol que intentas asignar es superior al mío.")
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al asignar un rol: {str(e)}')

# ***************************************************
# **    Comando para Quitar un Rol a un Miembro    **
# ***************************************************
def Quitar_Rol(bot):
    @bot.command()
    async def quitar_rol(ctx, rol: discord.Role, miembro: discord.Member):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["quitar_rol"]
            color = discord.Colour.from_rgb(*color_tuple)

            await miembro.remove_roles(rol)

            # Crear un Embed informativo
            embed = discord.Embed(title="Quitar Rol", color=color)
            embed.add_field(name="Rol retirado", value=rol.mention, inline=False)
            embed.add_field(name="Miembro", value=miembro.mention, inline=False)
            embed.set_footer(text=f"Retiré el rol por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url=miembro.avatar.url)

            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send("No tengo permisos para quitar roles o el rol que intentas quitar es superior al mío.")
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al quitar un rol: {str(e)}')

# *****************************************************
# **    Comando para Eliminar un Rol del Servidor    **
# *****************************************************

# Define una función que configure los comandos relacionados con roles
def Eliminar_Rol(bot):
    @bot.command()
    async def eliminar_rol(ctx, rol: discord.Role):
        try:

            # Mostrar "Escribiendo..."
            async with ctx.typing():
                await asyncio.sleep(3) # Esperar 3 segundos simulando "Escribiendo..."

            # Verifica si el autor tiene permisos para administrar roles
            if ctx.author.guild_permissions.manage_roles:
                # Elimina el rol del servidor
                await rol.delete()

                # Crear un Embed informativo
                embed = discord.Embed(
                    title="Rol Eliminado",
                    description=f"¡El rol '{rol.name}' ha sido eliminado con éxito!"
                )

                await ctx.send(embed=embed)
            else:
                await ctx.send("No tienes permisos para eliminar roles en este servidor.")
        except discord.Forbidden:
            await ctx.send("No tengo permisos para eliminar roles o el rol que intentas eliminar es superior al mío.")
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f'Error al eliminar el rol: {str(e)}')

