import discord
from discord.ext import commands

# *********************************
# **    Importaciones Locales    **
# *********************************
from config import TOKEN, COMMAND_PREFIX
from presences import *
from Commands.Roles import *
from Commands.Entertainment import *
from Commands.Information import *
from Commands.Security import *
from Commands.Call import *
from Commands.Greetings import *

# ****************************************************
# **    Configuración de las Intenciones del Bot    **
# ****************************************************
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.guilds = True
intents.messages = True

# Crear el bot con un prefijo de comando y las intenciones configuradas
bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_PREFIX), intents=intents)

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    
    print(f'Bot conectada como {bot.user.name} (ID: {bot.user.id})')
    print('-------------------------------------------------------')

    # Enviar un mensaje al canal general cuando el bot se conecta
    #await saludo_principal(bot)

    # Configurar la presencia del las actividades del bot
    await set_bot_presence(bot)

# CATEGORIAS DE COMANDOS
#//=============================================//

# /=== Seguridad ===/
Code_QR(bot) #@Lyra QR <contenido>
Password(bot) #@Lyra password <int>
Anonimo(bot) #@Lyra mensaje_anonimo <#canal> <contenido>
Code_Morse(bot) #@Lyra morse <contenido>

# /=== Roles  ===/
Mostrar_Roles(bot) #@Lyra roles
Crear_Rol(bot) #@Lyra crear_rol <contenido>
Asignar_Rol(bot) #@Lyra asignar_rol <@rol> <@miembro>
Quitar_Rol(bot) #@Lyra quitar_rol <@rol> <@miembro>
Eliminar_Rol(bot) #@Lyra eliminar_rol <@rol>

# /=== Informacion  ===/
Lyra_Info(bot) #@Lyra Lyra
User_Info(bot) #@Lyra userinfo <@miembro>
Estadisticas_Bot_Info(bot) #@Lyra stats
Server_Info(bot) #@Lyra estadisticas
Ayuda(bot) #@Lyra ayuda 
Latencia(bot) #@Lyra ping

# /=== Entretenimiento  ===/
Moneda(bot) #@Lyra moneda
Ruleta_Rusa(bot) #@Lyra ruleta

# /=== Llamada  ===/
Join_Llamada(bot) #@Lyra unirse
Exit_Call(bot) #@Lyra salir

# /=== Saludo  ===/
Saludar(bot) #@Lyra hola-


# Iniciar el bot con el token
try:
    bot.run(TOKEN)
except Exception as e:
    print(f'Error al iniciar el bot: {e}')
