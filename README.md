# Historias Interactivas (Storytelling Bot)

**HistoriasInteractivas**, also known as **Storytelling Bot**, is a program established on Discord whose main purpose is to entertain and provoke thought in the user. Unlike other Discord bots, which are designed to perform predefined functions -such as providing server information or guiding the user through the channel- HistoriasInteractivas uses AI (Artificial Intelligence) to engage in a 'conversation' with the user or to tell them a joke. Thanks to AI, it is possible to combine story fragments between the human and the bot, resulting in a rather interesting and intricate narrative.


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
