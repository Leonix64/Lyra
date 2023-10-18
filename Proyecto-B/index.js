const { Client, Intents, GatewayIntentBits } = require('discord.js');
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildPresences
  ]
});

const token = 'MTE2NDAyMDA3NjMxNjQ1OTA5OA.GjY7Hh.XQgXw674IKWbRkmTFuvZuc3dAyHcKHWQAx-fjY';
const prefix = '!';

client.once('ready', () => {
  console.log(`Conectado como ${client.user.tag}`);
});

client.on('messageCreate', (message) => {
  // Verifica si el mensaje comienza con el prefijo y si el autor no es un bot.
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'tucomando') {
    // Mensaje en la consola para verificar que el comando fue detectado.
    console.log(`Comando ejecutado por: ${message.author.tag}`);

    // Respuesta en la consola.
    console.log('¡Hola, mundo!');

    // Respuesta en Discord.
    message.reply('¡Hola, mundo!');
  }
});

client.on('error', (error) => {
  console.error('¡Ocurrió un error en el bot!', error);
});

client.login(token);
