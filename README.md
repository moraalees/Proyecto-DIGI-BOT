# Historias Interactivas (Storytelling Bot)

**HistoriasInteractivas**, also known as **Storytelling Bot**, is a program established on Discord whose main purpose is to entertain and provoke thought in the user. Unlike other Discord bots, which are designed to perform predefined functions -such as providing server information or guiding the user through the channel- HistoriasInteractivas uses AI (Artificial Intelligence) to engage in a 'conversation' with the user or to tell them a joke. Thanks to AI, it is possible to combine story fragments between the human and the bot, resulting in a rather interesting and intricate narrative.

> **Note**: HistoriasInteractivas is not finished. As of 02/05/2025, the program is still under development. For this reason, to learn more about the future of HistoriasInteractivas, I recommend taking a look at the 'CONTRIBUTING.md' file, which contains several ideas about the future of this project.
Community contributions and feedback are welcome as the project evolves.

# Motivation

The spark that has driven me to create and improve this project over the course of several months lies in the cooperation between AI and humans. I find it fascinating that humans rely on AI for certain aspects, while AI depends entirely on humans to function. For this very reason, I decided to create a program that merges human thought with artificial intelligence data, so that neither is dependent on the other, and both can collaborate with a single purpose: a story.

As a side note, part of my motivation also came from a personal curiosity: to see whether I was capable of completing a demanding yet interesting project, and to challenge myself in the process.
What began as a simple experiment gradually turned into a passion project -one that helped me grow not only in technical skills, but also in creativity, perseverance, and problem-solving-.

# Getting started

To get started with HistoriasInteractivas, you must correctly follow these steps:

- Create a local folder and clone this repository into it using the GitBash command `git clone yourSSHkey`, where yourSSHkey can be found under the CODE section of this repository.
- Inside that folder, you must create a file named .env, which must contain the following (the details will be explained further below):
```
OPENROUTER_API_KEY='your OpenRouter API KEY'
DISCORD_BOT_TOKEN='your Discord bot TOKEN'
```
- For the **DISCORD_BOT_TOKEN**, the user must register their own bot through the [Discord Developer Portal](https://discord.com/developers/applications). Create an application, open it, and go to the OAuth2 tab. In the OAuth2 URL Generator, check the boxes for Bot and Applications.commands.
Scroll down and select the required permissions for the bot:
  - `Send Messages`
  - `Read Message History`
  - `Use Slash Commands`
- At the bottom, a URL will be generated to invite the bot to any Discord server of your choice.
Additionally, go to the Bot tab in the left-hand menu and click Reset Token to generate your bot's token. Copy this token and paste it into the .env file, replacing `your Discord bot TOKEN`.
- For the **OpenRouter API KEY**, go to [OpenRouter](https://openrouter.ai/) in your browser and search for Google: Gemini Flash 1.5. Once selected, go to the API tab and click Create API Key. After the key is generated, copy and paste it into your .env file where it says `your OpenRouter API KEY`.
- Once all of the above is completed, you're ready to run the .py file.
From my experience, Python version 3.13 does not work with this program, so I recommend installing Python 3.11, which does work correctly.
To run the bot, simply use the command:
```
py -3.11 bot.py
```
HistoriasInteractivas will then be active on your Discord server and ready to respond to commands.

# Separador
Como proyecto para el módulo de **Digitalización** he tenido la idea de crear y desarrollar un bot de Discord mediante un programa de Python. Dicho bot tendrá la posibilidad de realizar acciones mediante comandos concretos, como por ejemplo, saludar al usuario. No obstante, como este proyecto necesita originalidad y algo que no se haya visto frecuentemente, he pensado en implementar IA en dicho proyecto.

La IA actuará dependiendo del comando que otorguemos. Mi idea es hacer que la IA empiece una historia que el usuario deberá seguir. Cuando el usuario decida no implementar más historia, la IA ofrecerá la posibilidad de seguir la historia, terminar la existente o comenzar alguna nueva dependiendo del comando. Si hemos decidido terminar la historia, tendremos la oportunidad de guardarla en el programa del bot mediante comandos.

He decidido realizar este proyecto con esta misma idea ya que me parece interesante cómo actúa la IA y también porque la idea de crear una historia entre IA y humano me llama la atención, para saber la creatividad e intenciones de cada uno.

# Segunda entrega

En esta segunda entrega del proyecto del software funcional (bot de Discord) he finalizado el proyecto. Para poder ser usado correctamente, primero se deben de hacer unos ajustes:

- Crea una carpeta local donde clones este repositorio mediante el comando en GitBash 'git clone claveSSH', donde la claveSSH la conseguirás en el apartado de CODE que hay en el propio repositorio.
- En esa carpeta, deberás crearte un archivo que se llame '.env', cuyo contenido debe de ser específicamente el siguiente (en donde esas especificaciones se expliacrán más adelante):
```
OPENROUTER_API_KEY='tu API KEY de OpenRouter'
DISCORD_BOT_TOKEN='tu TOKEN de un bot de Discord'
```
- En el apartado de DISCORD_BOT_TOKEN, el usuario deberá registrar un bot propio en la página web de Discord Developer Portal. Crea una aplicación, luego se mete en ella y accede a la pestaña de OAuth2, donde seleccionará en OAuth2 URL Generator las las casillas Bot y Applications.commands. Más abajo marcará los permisos del bot, que deben de ser 'Send Messages, Read Message History, Use Slash Commands'. Por úlitmo, al bajar más aparecerá la URL para invitar al Bot a un servidor de Discord (el que quiera el usuario). Además de todo esto, el usuario debe acceder a la pestaña Bot de la izquierda y pinchar en 'Reset Token', que generará su TOKEN. Este TOKEN debe introducirlo en su ya creado archivo .env, donde pone 'tu TOKEN de un bot de Discord'.
- Sobre la API KEY de OpenRouter, el usuario deberá acceder a Open Router desde su navegador y buscar 'Google: Gemini Flash 1.5'. Una vez seleccionada, acceder a la pestaña 'API' y ahí seleccionará entonces 'Create API key'. Una vez creada, deberá ser copiada y pegada en el archivo .env donde pone 'tu API KEY de OpenRouter'.
- Una vez todo esto ya esté cumplido, faltaría poder ejecutar el archivo .py. Por mi experiencia, la versión 3.13 no funciona con el programa, por tanto recomiendo instalar la versión 3.11, que sí funciona. para ejecutar el bot, tan solo se debe de ejecutar el comando 'py -3.11 bot.py', y entonces el bot en el servidor de Discord estará activo para usar los comandos.

Para poder ejecutar opciones del bot, se deberán escribir los diferentes comandos con una barra '/' por delante. Los diferentes comandos son:

- /hola: El bot saluda al usuario.

- /ia: El bot responderá con IA a una pregunta que tú le escribirás (el máximo de caracteres que Discord permite en un mensaje es de 2000, por tanto es posible que la respuesta se vea incompleta).

- /inicia: Inicia una historia implementando IA.

- /nueva: Reinicia la historia pero esta vez el comienzo será uno por defecto aleatoriamente desde una lista de inicios.

- /seguir: Te pedirá que escribas algo. La IA lo recoge y seguirá también dicha historia (el máximo de caracteres que Discord permite en un mensaje es de 2000, por tanto es posible que la respuesta se vea incompleta).

- /finalizar: Te pedirá que ingreses el final de la historia.

- /guardar: Guardará la historia en un archivo JSON para poder verla de forma completa.

- /chiste: La IA te contará un chiste según de qué tema lo pidas.
