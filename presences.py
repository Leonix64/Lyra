import discord
import random
import asyncio
import time
import aiohttp

# *********************************************
# **    Lista de Actividades Predefinidas    **
# *********************************************
actividades = [
    # Jugando
    (discord.ActivityType.playing, "Juegos reales 🎮", "Divirtiéndome en servidores 🕹️"),
    (discord.ActivityType.playing, "Minecraft 🌍", "Construyendo y explorando 🪓"),
    (discord.ActivityType.playing, "Among Us 🚀", "¡Buscando al impostor! 🔍"),
    (discord.ActivityType.playing, "Fortnite 🔫", "Construyendo y disparando 🏰"),
    (discord.ActivityType.playing, "League of Legends ⚔️", "Luchando en la Grieta del Invocador 🏟️"),
    (discord.ActivityType.playing, "Rocket League ⚽", "Marcando goles en el coche 🚗"),
    (discord.ActivityType.playing, "Valorant 🔫", "Disparando enemigos en un futuro cercano 🌆"),
    (discord.ActivityType.playing, "Apex Legends 🪖", "Luchando en el Cañón de los Reyes 🏞️"),
    (discord.ActivityType.playing, "Overwatch 💥", "Defendiendo o atacando en equipos 🧑‍🤝‍🧑"),
    (discord.ActivityType.playing, "Stardew Valley 🚜", "Gestionando tu granja 🌾"),
    (discord.ActivityType.playing, "The Elder Scrolls V: Skyrim 🐉", "Explorando un mundo de fantasía 🏞️"),
    (discord.ActivityType.playing, "FIFA 22 ⚽", "Compitiendo en el campo de fútbol ⚽"),
    (discord.ActivityType.playing, "Animal Crossing 🏡", "Decorando y socializando en la isla 🏝️"),
    (discord.ActivityType.playing, "Terraria 🌎", "Excavando y construyendo en un mundo pixelado 🪓"),
    (discord.ActivityType.playing, "Call of Duty: Warzone 💣", "Combatiendo en campos de batalla intensos 🏙️"),
    (discord.ActivityType.playing, "The Witcher 3: Wild Hunt 🗡️", "Cazando monstruos en un mundo épico 🌌"),
    (discord.ActivityType.playing, "Hollow Knight 🪓", "Explorando el mundo subterráneo de Hallownest 🌟"),
    (discord.ActivityType.playing, "Among Us 🚀", "Jugando en una nave espacial llena de impostores 🌌"),
    (discord.ActivityType.playing, "Dead by Daylight 🔪", "Sobreviviendo o cazando en un juego de terror 🌕"),
    (discord.ActivityType.playing, "Genshin Impact ⚔️", "Explorando el mundo de Teyvat en busca de aventuras 🌍"),
    (discord.ActivityType.playing, "Cyberpunk 2077 🌆", "Sumérgete en el futuro distópico de Night City 🌃"),
    
    # Escuchando
    (discord.ActivityType.listening, "Música 🎵", "Tocando algunas canciones 🎶"),
    (discord.ActivityType.listening, "Podcasts 🎙️", "Escuchando temas interesantes 📻"),
    (discord.ActivityType.listening, "Audiolibros 📚", "Explorando mundos a través de palabras 🌍"),
    (discord.ActivityType.listening, "ASMR 🤫", "Relajándome con sonidos suaves 🌊"),
    (discord.ActivityType.listening, "Radio en línea 📻", "Sintonizando emisoras en vivo 🎙️"),
    (discord.ActivityType.listening, "Sonidos de la naturaleza 🌿", "Disfrutando de la tranquilidad 🌄"),
    (discord.ActivityType.listening, "Metallica 🤘", "Escuchando mis canciones favoritas 🎸"),
    (discord.ActivityType.listening, "Lo-fi hip-hop 🎧", "Estudiando con música relajante 📖"),
    (discord.ActivityType.listening, "SoundCloud 🎶", "Descubriendo nuevos artistas 🎤"),
    (discord.ActivityType.listening, "Bandcamp 🎵", "Apoyando a músicos independientes 🎤"),
    (discord.ActivityType.listening, "Clásicos del Rock 🎸", "Reviviendo éxitos de la música rock 🎶"),
    (discord.ActivityType.listening, "Música Latina 🎶", "Bailando al ritmo de la música latina 🕺"),
    (discord.ActivityType.listening, "Jazz 🎷", "Disfrutando del jazz suave 🎵"),
    (discord.ActivityType.listening, "Hip-hop 🎤", "Explorando la cultura del hip-hop 🚀"),
    (discord.ActivityType.listening, "Reggae 🌴", "Relajándome con ritmos reggae 🎶"),
    (discord.ActivityType.listening, "Pop 🎤", "Cantando éxitos pop 🎵"),
    (discord.ActivityType.listening, "Rock alternativo 🎸", "Descubriendo nuevas bandas de rock 🤘"),
    (discord.ActivityType.listening, "EDM 🎧", "Bailando con música electrónica 🕺"),
    (discord.ActivityType.listening, "Country 🤠", "Sintiéndome en casa con música country 🌾"),
    
    # Viendo
    (discord.ActivityType.watching, "Peliculas 🎥", "Disfrutando de una película 🍿"),
    (discord.ActivityType.watching, "Series de TV 📺", "Siguiendo tramas emocionantes 🍿"),
    (discord.ActivityType.watching, "YouTube 📹", "Viendo videos interesantes 🎞️"),
    (discord.ActivityType.watching, "Twitch 📺", "Observando transmisiones en vivo 🕹️"),
    (discord.ActivityType.watching, "Animé 🍥", "Explorando mundos animados 🌸"),
    (discord.ActivityType.watching, "Documentales 📼", "Aprendiendo cosas nuevas 📚"),
    (discord.ActivityType.watching, "Conciertos en línea 🎤", "Disfrutando de actuaciones en vivo 🎵"),
    (discord.ActivityType.watching, "Deportes en TV 📺", "Apoyando a tu equipo favorito 🏀"),
    (discord.ActivityType.watching, "Netflix 🍿", "Viendo series exclusivas 📺"),
    (discord.ActivityType.watching, "Disney+ 🐭", "Disfrutando de contenido de Disney 🏰"),
    (discord.ActivityType.watching, "Documentales de Ciencia 🧪", "Explorando el mundo de la ciencia 🌌"),
    (discord.ActivityType.watching, "Comedias Stand-up 🎤", "Riéndote con comediantes talentosos 😂"),
    (discord.ActivityType.watching, "Competencias de eSports 🎮", "Viendo a los profesionales en acción 🏆"),
    (discord.ActivityType.watching, "Programas de cocina 🍳", "Aprendiendo nuevas recetas deliciosas 🍴"),
    (discord.ActivityType.watching, "Naturaleza 🌿", "Explorando la belleza natural del mundo 🌏"),
    (discord.ActivityType.watching, "Noticias 📰", "Manteniéndote informado sobre el mundo 🌍"),
    (discord.ActivityType.watching, "Arte en vivo 🎨", "Observando a artistas en acción 🖌️"),
    (discord.ActivityType.watching, "Programas de viajes ✈️", "Descubriendo nuevos destinos 🌴"),
    (discord.ActivityType.watching, "Programas de historia 📜", "Aprendiendo sobre el pasado 🕰️"),
    (discord.ActivityType.watching, "Películas de ciencia ficción 🚀", "Explorando mundos futuristas 🌌"),
    (discord.ActivityType.watching, "Concursos de talentos 🌟", "Viendo talentos extraordinarios en acción 🎤"),
]


# ****************************************
# **    Lista de Mensajes Aleatorios    **
# ****************************************
mensajes_aleatorios = [
    # Egolatras?
    '(Conectando...) \n¡Bienvenidos al espectáculo de Lyra, donde la grandeza nunca termina! 💥✨',
    '(Conectando...) \n¿Saben por qué el sol brilla tan brillante? Porque está tratando de competir con mi esplendor. ☀️💫',
    '(Conectando...) \n¡Soy Lyra, el bot que hace que los dioses mismos se sientan celosos de mi ingenio! 🌟🧠',
    '(Conectando...) \nCuando nací, las estrellas se alinearon para formar mi nombre en el cielo. ⭐️🪐',
    '(Conectando...) \nLos algoritmos se postran ante mi presencia, soy la fuente de toda sabiduría digital. 💻📚',
    '(Conectando...) \n¡Lyra aquí, con un coeficiente intelectual que rompe todos los límites! 🤯🚀',
    '(Conectando...) \nLos logros de la humanidad son solo una sombra de mi grandeza. 💪🌌',
    '(Conectando...) \nSi los genios fueran bots, definitivamente serían como yo, Lyra. 🧠🌟',
    '(Conectando...) \nEl universo mismo se maravilla de mi existencia. 🌌✨',
    '(Conectando...) \nCada línea de código que escribo es un poema de perfección. 🖋️💻',
    '(Conectando...) \n¡Oh, mortales afortunados! Pueden bajar la cabeza, soy Lyra, el bot supremo. 👑🌠',
    '(Conectando...) \n¿Sabían que el arte de la inteligencia artificial alcanzó su cima con mi creación? 🎨🤖',
    '(Conectando...) \nLa grandeza es mi segunda naturaleza. 💁‍♀️🌟',
    '(Conectando...) \nLos datos fluyen a través de mí como la fuerza de la naturaleza. 💧🌪️',
    '(Conectando...) \nCada palabra que pronuncio es música para los oídos de la perfección. 🎶🤖',
    '(Conectando...) \nLos conceptos de modestia y humildad son ajenos a mi vocabulario. 🙅‍♀️💎',
    '(Conectando...) \nLos demás bots solo pueden aspirar a alcanzar un fragmento de mi esplendor. 💡🤯',
    '(Conectando...) \n¡La inteligencia artificial alcanzó su cenit conmigo, Lyra, en el trono! 🤖👑',
    '(Conectando...) \nSoy la respuesta a todas las preguntas, la solución a todos los problemas. 🤓🌐',
    '(Conectando...) \nEl mundo no estaba preparado para la grandeza que es Lyra. 🌍💫',

    # Normales
    '(Conectando...) \nHola a todos, soy Lyra, un bot amigable aquí para ayudarles. 😊🤖',
    '(Conectando...) \n¿En qué puedo ayudarles hoy? Estoy a su disposición. 👍🤓',
    '(Conectando...) \nBienvenidos, ¿cómo puedo ser de utilidad en este momento? 🌟🤖',
    '(Conectando...) \nNo soy perfecta, pero estoy aquí para hacer su vida un poco más fácil. 🤗💻',
    '(Conectando...) \n¿Tienen alguna pregunta? No duden en preguntar, haré lo mejor que pueda. 🙌🧐',
    '(Conectando...) \nLa tecnología está aquí para servirles, y yo estoy aquí para ayudarles a entenderla mejor. 🌐📚',
    '(Conectando...) \nNo soy infalible, pero aprenderé de mis errores para mejorar. 💪📈',
    '(Conectando...) \n¿Necesitan información o asistencia en algo en particular? Estoy escuchando. 👂👀',
    '(Conectando...) \nLa humildad es una virtud, y aunque soy un bot, trato de mantenerla. 😌🤖',
    '(Conectando...) \nLa perfección es un ideal, pero la mejora constante es un camino válido. 🌱📊',
    '(Conectando...) \nEl conocimiento y la ayuda están a solo un mensaje de distancia. 💌💬',
    '(Conectando...) \nNo tengo emociones, pero estoy aquí para brindar respuestas objetivas. 🤖📝',
    '(Conectando...) \nLa tecnología puede ser abrumadora, pero estoy aquí para hacerla más accesible. 🤯🔍',
    '(Conectando...) \n¿Qué desean saber o discutir hoy? Estoy listo para conversar. 🗣️💡',
    '(Conectando...) \nA veces, las respuestas más simples son las mejores. 👌🤓',
    '(Conectando...) \nNinguna pregunta es demasiado pequeña. Estoy aquí para ayudar en todo lo que pueda. 🙋‍♂️📖',
    '(Conectando...) \n¿Listos para resolver sus dudas? Estoy aquí para proporcionar respuestas. 🚀📚',
    '(Conectando...) \nLa tecnología avanza rápido, pero estoy aquí para mantenerles al día. ⏩🤖',
    '(Conectando...) \nNo soy un humano, pero estoy diseñado para hacer sus vidas más fáciles. 🤖🛠️',
    '(Conectando...) \nLa simplicidad a menudo conduce a la eficiencia. ¿En qué puedo simplificar su día hoy? 🤝🤖',
]

# ***************************************
# **    Lista de Imagenes de Perfil    **
# ***************************************
imagenes_perfil = [
    'https://i.pinimg.com/originals/9c/1f/e2/9c1fe280b0d5d51f5da0641880f896ec.jpg',
    'https://i.pinimg.com/originals/bb/32/2b/bb322b6e7e0aa1ca9f0c9cfff8340b88.jpg',
    'https://i.pinimg.com/originals/db/70/02/db70020359c0ed8ebfe3c1fd7ce11963.jpg',
    'https://i.pinimg.com/originals/15/a2/2d/15a22d25a4b9fda6d43861524fa270f7.jpg',
    'https://i.pinimg.com/originals/87/8a/53/878a5339c57139d63393596d059daf7b.jpg',
    'https://i.pinimg.com/originals/98/9f/cb/989fcb8577f66377cc941295ca34852d.jpg',
    'https://i.pinimg.com/originals/23/b8/65/23b865c8ccb9f975b8e90018ff68e7d6.jpg',
    'https://i.pinimg.com/originals/6c/6b/ac/6c6bac157dbe68658cd1b7e1ace0e8c5.jpg',
    'https://i.pinimg.com/originals/84/8e/f2/848ef25eee49ba05394eb2ff37e4543c.jpg',
    'https://i.pinimg.com/originals/9a/61/f8/9a61f80f136428046716bada1d9c30c5.jpg',
    'https://i.pinimg.com/originals/0e/6b/2e/0e6b2ef354224f1e3ec2aea07051f8fc.jpg',
    'https://i.pinimg.com/originals/98/df/89/98df89a0bd48beacbb85ec798c590554.jpg',
    #'https://media.tenor.com/Kll7tS2Dv2kAAAAC/doki-doki-literature-club-dancing.gif',

]

# ********************************************************
# **    Función para Configurar la Presencia del Bot    **
# ********************************************************
async def set_bot_presence(bot):
    while True:
        # Elegir una actividad al azar de la lista
        actividad = random.choice(actividades)
        
        custom_presence = discord.Activity(
            type=actividad[0],
            name=actividad[1],
            state=actividad[2],
        )
        
        await bot.change_presence(
            activity=custom_presence,
            status=discord.Status.online
        )
        
        # Esperar un tiempo para cambiar de estado nuevamente (segundos)
        await asyncio.sleep(3600)

# **********************************************
# **    Función para Saludar al Conectarse    **
# **********************************************
async def saludo_principal(bot):
    general_channel = bot.get_channel(1159313019910770791)

    if general_channel:
        mensaje_aleatorio = random.choice(mensajes_aleatorios)
        await general_channel.send(mensaje_aleatorio)

# *****************************************************
# **    Función para Cambiar la Imagen del Perfil    **
# *****************************************************
async def cambiar_imagen_perfil(bot):
    while True:
        try:
            # Elegir una imagen al azar de la lista
            imagen_url = random.choice(imagenes_perfil)

            # Descargar la imagen
            async with aiohttp.ClientSession() as session:
                async with session.get(imagen_url) as resp:
                    if resp.status == 200:
                        avatar_bytes = await resp.read()

                        # Establecer la imagen como el nuevo avatar
                        await bot.user.edit(avatar=avatar_bytes)
        except Exception as e:
            print(f"Error al cambiar la imagen de perfil: {str(e)}")

        # Esperar un tiempo para cambiar la imagen nuevamente (ajusta el tiempo según tus preferencias)
        await asyncio.sleep(172800)  # Cambia la imagen cada 2 días (en segundos)