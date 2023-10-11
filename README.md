# Generador de Códigos QR con Bot de Discord

Este es un bot de Discord que permite generar códigos QR a partir de texto proporcionado por los usuarios en un servidor de Discord. Los códigos QR generados se pueden utilizar para almacenar información y enlaces.

## Comandos del Bot

- `@Menciona_el_bot QR <contenido>`: Este comando genera un código QR a partir del contenido proporcionado. El contenido debe tener un máximo de 500 caracteres. El bot generará un código QR en blanco y negro y lo enviará al canal donde se llamó el comando. Además, mencionará al usuario que solicitó la generación del código QR.

- `@Menciona_el_bot estadisticas`: Este comando muestra estadísticas del servidor de Discord en el que se encuentra el bot. Proporciona información sobre el número de miembros, roles, canales y más.

- `@Menciona_el_bot Roles`: Este comando muestra una lista de todos los roles en el servidor de Discord. Muestra el nombre de cada rol.

- `@Menciona_el_bot asignar_rol <rol> <miembro>`: Este comando permite asignar un rol a un miembro en el servidor de Discord. El bot verificará si tiene los permisos necesarios y si el rol que se está asignando no es superior al suyo.

- `@Menciona_el_bot quitar_rol <rol> <miembro>`: Este comando permite quitar un rol a un miembro en el servidor de Discord. Al igual que en el comando anterior, el bot verificará los permisos necesarios y la jerarquía de roles.

## Configuración

Antes de ejecutar este bot, asegúrate de configurar lo siguiente:

- `TOKEN`: Reemplaza `'MTA5ODM3MTAyNjUxNTE0NDg0NQ.GVDK65.Y54SKyYRQOXXHZElutnr4WDYk3Tqg68YIQS2cY'` con el token de tu bot de Discord.

- Configura las intenciones del bot según tus necesidades. En el código actual, se han deshabilitado las intenciones de "typing" y "presences", pero se han habilitado las intenciones de "members".

## Uso

1. Ejecuta el bot con el comando `bot.run(TOKEN)` al final del código.

2. Invita al bot a tu servidor de Discord y asegúrate de que tenga los permisos necesarios para funcionar correctamente.

3. Los usuarios pueden utilizar los comandos mencionados anteriormente para generar códigos QR, ver estadísticas del servidor y gestionar roles.

## Dependencias

Este bot utiliza las siguientes dependencias externas:

- `discord.py`: Una biblioteca de Discord para Python que facilita la creación de bots de Discord.

- `qrcode`: Una biblioteca para generar códigos QR.

## Notas

Este es un proyecto de ejemplo y se proporciona tal cual. Asegúrate de revisar y adaptar el código según tus necesidades antes de ejecutarlo en tu servidor de Discord.

¡Disfruta utilizando tu bot generador de códigos QR en Discord!
