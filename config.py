import openai

TOKEN = 'TU_TOKEN_AQUÍ'# Token de Discord
COMMAND_PREFIX = "!"

# API de OpenAI
openai.api_key = "TU_API_KEY_AQUÍ"

# Configura los detalles de la conexión a la base de datos
db_config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "lyra_db"
}

#Permisos (se pone como custom link en el bot OAuth2)
#https://discord.com/developers/applications
#https://discord.com/api/oauth2/authorize?client_id=1098371026515144845&permissions=8&scope=bot
