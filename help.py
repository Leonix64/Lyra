# *****************************************
# **      Lista de Comandos de Lyra      **
# *****************************************

commands_list = [
    {
        "name": "Generar QR",
        "description": "Genera un código QR a partir de un contenido proporcionado.",
        "usage": "@Lyra QR <contenido>",
        "category": "/=== Seguridad ===/"
    },
    {
        "name": "Generar Contraseña",
        "description": "Genera una contraseña segura y la envía por mensaje privado.",
        "usage": "@Lyra password [longitud]",
        "category": "/=== Seguridad ===/"
    },
    {
        "name": "Mensaje Anónimo",
        "description": "Envía un mensaje anónimo a un canal específico.",
        "usage": "@Lyra mensaje_anonimo <#canal> <contenido>",
        "category": "/=== Seguridad ===/"
    },
    {
        "name": "Convertir a Morse",
        "description": "Convierte un mensaje en código Morse.",
        "usage": "@Lyra morse <mensaje>",
        "category": "/=== Seguridad ===/"
    },
    {
        "name": "Listar Roles",
        "description": "Lista los roles del servidor.",
        "usage": "@Lyra roles",
        "category": "/=== Roles ===/"
    },
    {
        "name": "Crear Rol",
        "description": "Crea un nuevo rol en el servidor.",
        "usage": "@Lyra crear_rol <nombre_del_rol>",
        "category": "/=== Roles ===/"
    },
    {
        "name": "Asignar Rol",
        "description": "Asigna un rol a un miembro del servidor.",
        "usage": "@Lyra asignar_rol <@rol> <@miembro>",
        "category": "/=== Roles ===/"
    },
    {
        "name": "Quitar Rol",
        "description": "Quita un rol a un miembro del servidor.",
        "usage": "@Lyra quitar_rol <@rol> <@miembro>",
        "category": "/=== Roles ===/"
    },
    {
        "name": "Eliminar Rol",
        "description": "Elimina un rol del servidor.",
        "usage": "@Lyra eliminar_rol <@rol>",
        "category": "/=== Roles ===/"
    },
    {
        "name": "Información de Usuario",
        "description": "Muestra información sobre un usuario.",
        "usage": "@Lyra userinfo [@usuario]",
        "category": "/=== Informacion ===/"
    },
    {
        "name": "Información sobre Lyra",
        "description": "Muestra información sobre el bot.",
        "usage": "@Lyra Lyra",
        "category": "/=== Informacion ===/"
    },
    {
        "name": "Estadísticas del Servidor",
        "description": "Muestra estadísticas del servidor donde se ejecuta el bot.",
        "usage": "@Lyra estadisticas",
        "category": "/=== Informacion ===/"
    },
    {
        "name": "Latencia de Lyra",
        "description": "Muestra la latencia del bot.",
        "usage": "@Lyra ping",
        "category": "/=== Informacion ===/"
    },
    {
        "name": "Estadísticas de Lyra",
        "description": "Muestra estadísticas globales del bot.",
        "usage": "@Lyra stats",
        "category": "/=== Informacion ===/"
    },
    {
        "name": "Ayuda con Comandos",
        "description": "Muestra información sobre los comandos.",
        "usage": "@Lyra ayuda",
        "category": "/=== Informacion ===/"
    },
    {
        "name": "Lanzar Moneda",
        "description": "Lanza una moneda y muestra el resultado (cara o cruz).",
        "usage": "@Lyra moneda",
        "category": "/=== Entretenimiento ===/"
    },
    {
        "name": "Ruleta Rusa",
        "description": "Juega a la ruleta rusa y muestra el resultado (bang o click).",
        "usage": "@Lyra ruleta",
        "category": "/=== Entretenimiento ===/"
    },
    {
        "name": "Ruleta de Comida",
        "description": "Juega a la ruleta rusa pero ahora con comida y ve qué te toca.",
        "usage": "@Lyra comida",
        "category": "/=== Entretenimiento ===/"
    },
    {
        "name": "ChatGPT (En Desarrollo)",
        "description": "Interactúa con una implementación de ChatGPT en Discord.",
        "usage": "@Lyra chat <pregunta>",
        "category": "/=== Entretenimiento ===/"
    },
    {
        "name": "Generar un Saludo",
        "description": "Te da un saludo aleatorio.",
        "usage": "@Lyra hola",
        "category": "/=== Saludo ===/"
    },
    {
        "name": "Unirse a una Llamada",
        "description": "Se une a un canal de voz.",
        "usage": "@Lyra unirse",
        "category": "/=== Llamada ===/"
    },
    {
        "name": "Salir de una Llamada",
        "description": "Se sale de un canal de voz en el que se encuentra.",
        "usage": "@Lyra salir",
        "category": "/=== Llamada ===/"
    },
    {
        "name": "Eliminar Mensajes",
        "description": "Elimina la cantidad de mensajes especificada.",
        "usage": "@Lyra clear [cantidad]",
        "category": "/=== Utilidades ===/"
    },
    {
        "name": "Iniciar Sesión",
        "description": "Inicia sesión para acceder a los comandos.",
        "usage": "@Lyra login [contraseña]",
        "category": "/=== Login ===/"
    },
    {
        "name": "Registro",
        "description": "Crea una contraseña para usar en el inicio de sesión.",
        "usage": "@Lyra register [contraseña]",
        "category": "/=== Login ===/"
    },
    {
        "name": "Cerrar Sesión",
        "description": "Cierra la sesión actual.",
        "usage": "@Lyra logout",
        "category": "/=== Login ===/"
    },
]
