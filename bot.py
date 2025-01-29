import discord
from discord.ext import commands
from discord import app_commands
import random
import openai


OPEN_AI_KEY = "TOKEN"

Token = 'TOKENQ'


# Configurar intents
intents = discord.Intents.default()
intents.message_content = True


# Crear el bot con prefijo '/'
bot = commands.Bot(command_prefix='/', intents=intents)


# Lista de inicios de historia
inicios_historia = [
    "Era una noche oscura y tormentosa cuando de repente se escuchó un extraño ruido...",
    "En un mundo donde la magia estaba prohibida, un joven descubrió un libro olvidado...",
    "La nave espacial había estado a la deriva durante días hasta que detectaron una señal desconocida..."
]


# Variable para verificar si hay una historia activa
historia_activa = False


# Función de la IA
def generar_inicio_historia_ia():
    prompt = "Escribe un inicio intrigante para una historia de fantasía o ciencia ficción:"
    
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # O usa "gpt-4" si tienes acceso
            messages=[{"role": "system", "content": "Eres un escritor creativo."},
                      {"role": "user", "content": prompt}],
            max_tokens=50  # Limita la cantidad de palabras generadas
        )
        
        inicio_historia = respuesta['choices'][0]['message']['content'].strip()
        return inicio_historia

    except Exception as e:
        print("Error al generar historia:", e)
        return "Hubo un problema al generar la historia. Inténtalo más tarde."



# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sincroniza los slash commands con Discord
    print(f'Conectado como {bot.user}')


# Comando /hola
@bot.tree.command(name="hola", description="El bot te saluda")
async def hola(interaction: discord.Interaction):
    await interaction.response.send_message(f'¡Qué pasa {interaction.user.mention}!')


@bot.tree.command(name="inicia", description="Inicia una nueva historia")
async def inicia(interaction: discord.Interaction):
    global historia_activa
    if historia_activa:
        await interaction.response.send_message("¡Ya hay una historia en curso! Usa /nueva para empezar otra.")
    else:
        historia_activa = True
        inicio = generar_inicio_historia_ia()
        await interaction.response.send_message(f"**Nueva Historia Iniciada:** {inicio}")



# Comando /nueva para reiniciar la historia
@bot.tree.command(name="nueva", description="Inicia una historia nueva desde cero")
async def nueva(interaction: discord.Interaction):
    global historia_activa
    historia_activa = True
    inicio = random.choice(inicios_historia)
    await interaction.response.send_message(f"**Se ha iniciado una nueva historia:** {inicio}")


# Iniciar el bot
bot.run(Token)
