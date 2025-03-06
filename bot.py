import discord
from discord.ext import commands
from openai import OpenAI
import random
import os
from dotenv import load_dotenv

# py -3.11 bot.py

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Cargar las claves API desde el archivo .env
api_key = os.getenv("OPENROUTER_API_KEY")
discord_token = os.getenv("DISCORD_BOT_TOKEN")

# Configurar el cliente de OpenAI (OpenRouter)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # Especificar la URL base de OpenRouter
    api_key=api_key
)

# Configurar intents de Discord
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Variable para controlar si hay una historia activa
historia_activa = False

# Lista de inicios de historia
inicios_historia = [
    "Érase una vez en un lejano reino...",
    "En un mundo donde la magia era real...",
    "Hace mucho tiempo, en una galaxia muy, muy lejana...",
    "En un pequeño pueblo rodeado de bosques oscuros...",
    "En un futuro distópico donde las máquinas dominaban el mundo..."
]

# Función para generar un inicio de historia utilizando la IA
def generar_inicio_historia_ia():
    try:
        respuesta = client.chat.completions.create(
            model="google/gemini-flash-1.5",  # Modelo gratuito de Google Gemini Flash
            messages=[
                {"role": "system", "content": "Eres un asistente útil en Discord."},
                {"role": "user", "content": "Genera un inicio de historia interesante."}
            ],
            max_tokens=200
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        print("Error con OpenRouter:", e)
        return random.choice(inicios_historia)  # Si hay un error, usa un inicio de la lista

# Función para obtener respuesta de la IA
def obtener_respuesta_ia(mensaje):
    try:
        respuesta = client.chat.completions.create(
            model="google/gemini-flash-1.5",  # Modelo gratuito de Google Gemini Flash
            messages=[
                {"role": "system", "content": "Eres un asistente útil en Discord."},
                {"role": "user", "content": mensaje}
            ],
            max_tokens=200
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        print("Error con OpenRouter:", e)
        return "Hubo un problema con la IA."

# Comando de Discord para interactuar con la IA
@bot.tree.command(name="ia", description="Hazle una pregunta a la IA")
async def ia(interaction: discord.Interaction, pregunta: str):
    respuesta = obtener_respuesta_ia(pregunta)
    await interaction.response.send_message(respuesta)

# Comandos adicionales que tenías
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

@bot.tree.command(name="nueva", description="Inicia una historia nueva desde cero")
async def nueva(interaction: discord.Interaction):
    global historia_activa
    historia_activa = True
    inicio = random.choice(inicios_historia)
    await interaction.response.send_message(f"**Se ha iniciado una nueva historia:** {inicio}")

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')
    try:
        await bot.tree.sync()  # Sincroniza los comandos de barra con Discord
        print("Comandos sincronizados correctamente")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

# Ejecutar el bot con el token de Discord desde el archivo .env
bot.run(discord_token)
