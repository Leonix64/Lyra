import discord
from discord.ext import commands
from embed import color_Embed
from .Login import usuarios_autenticados

# *****************************************
# **    Comando para limpiar mensajes    **
# *****************************************
def Limpia_Mensajes(bot):
    @bot.command()
    async def clear(ctx, amount: int):
        if ctx.author.id in usuarios_autenticados:
            try:
                # Obtener el color correspondiente al comando
                color_tuple = color_Embed["clear"]
                color = discord.Colour.from_rgb(*color_tuple)

                # Verificar si el usuario tiene permisos para administrar mensajes
                if ctx.message.author.guild_permissions.manage_messages:
                    await ctx.message.delete()  # Elimina el mensaje del usuario que ejecuta el comando
                    await ctx.channel.purge(limit=amount + 1)  # Elimina la cantidad especificada de mensajes

                    # Crear un embed para el mensaje de confirmación
                    embed = discord.Embed(
                        title="Mensajes eliminados",
                        description=f'Se han eliminado {amount} mensajes en este canal.',
                        color=color
                    )

                    # Enviar el embed como mensaje de confirmación
                    await ctx.send(embed=embed)
                else:
                    # Crear un embed para informar al usuario sobre la falta de permisos
                    error_embed = discord.Embed(
                        title="Error de permisos",
                        description="No tienes permiso para usar este comando.",
                        color=discord.Color.red()
                    )

                    # Enviar el embed como mensaje de error
                    await ctx.send(embed=error_embed)
            except discord.Forbidden:
                # Crear un embed para informar al usuario sobre la falta de permisos
                error_embed = discord.Embed(
                    title="Error de permisos",
                    description="No tengo permisos para eliminar mensajes.",
                    color=discord.Color.red()
                )

                # Enviar el embed como mensaje de error
                await ctx.send(embed=error_embed)
            except Exception as e:
                # Crear un embed para mostrar un mensaje de error en caso de problemas
                error_embed = discord.Embed(
                    title="Error",
                    description=f"Ocurrió un error al intentar eliminar mensajes: {str(e)}",
                    color=discord.Color.red()
                )

                # Enviar el embed como mensaje de error
                await ctx.send(embed=error_embed)
        else:
            # Crear un Embed para mostrar un mensaje de error si el usuario no ha iniciado sesión
            error_embed = discord.Embed(title="Error", color=discord.Color.red())
            error_embed.description = "No tienes permiso para usar este comando protegido. Por favor, inicia sesión primero."
            await ctx.send(embed=error_embed)

