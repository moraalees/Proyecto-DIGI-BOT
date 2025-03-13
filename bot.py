import discord
from discord.ext import commands
from openai import OpenAI
import random
import json
import os
from dotenv import load_dotenv

# py -3.11 bot.py

# https://discord.com/oauth2/authorize?client_id=1329402639729037353&permissions=2147551232&integration_type=0&scope=bot+applications.commands

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Cargar las claves API desde el archivo .env
api_key = os.getenv("OPENROUTER_API_KEY")
discord_token = os.getenv("DISCORD_BOT_TOKEN")

# Configurar el cliente de OpenAI (OpenRouter)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# Configurar intents de Discord
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Variables globales para la historia
historia_activa = False
historia_completa = ""

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
            model="google/gemini-flash-1.5",
            messages=[
                {"role": "system", "content": "Eres un asistente útil en Discord."},
                {"role": "user", "content": "Genera un inicio de historia interesante."}
            ],
            max_tokens=200
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        print("Error con OpenRouter:", e)
        return random.choice(inicios_historia)

# Función para obtener respuesta de la IA
def obtener_respuesta_ia(mensaje):
    try:
        respuesta = client.chat.completions.create(
            model="google/gemini-flash-1.5",
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

# Comando para interactuar con la IA
@bot.tree.command(name="ia", description="Hazle una pregunta a la IA")
async def ia(interaction: discord.Interaction, pregunta: str):
    respuesta = obtener_respuesta_ia(pregunta)
    await interaction.response.send_message(respuesta)

# Comando para saludar
@bot.tree.command(name="hola", description="El bot te saluda")
async def hola(interaction: discord.Interaction):
    await interaction.response.send_message(f'¡Qué pasa {interaction.user.mention}!')

# Comando para iniciar una historia
@bot.tree.command(name="inicia", description="Inicia una nueva historia")
async def inicia(interaction: discord.Interaction):
    global historia_activa, historia_completa
    if historia_activa:
        await interaction.response.send_message("¡Ya hay una historia en curso! Usa /nueva para empezar otra.")
    else:
        historia_activa = True
        inicio = generar_inicio_historia_ia()
        historia_completa = inicio
        await interaction.response.send_message(f"**Nueva Historia Iniciada:** {inicio}")

# Comando para iniciar una historia nueva desde cero
@bot.tree.command(name="nueva", description="Inicia una historia nueva desde cero")
async def nueva(interaction: discord.Interaction):
    global historia_activa, historia_completa
    historia_activa = True
    inicio = random.choice(inicios_historia)
    historia_completa = inicio
    await interaction.response.send_message(f"**Se ha iniciado una nueva historia:** {inicio}")

# Comando para seguir la historia
@bot.tree.command(name="seguir", description="Continúa la historia con tu aportación")
async def seguir(interaction: discord.Interaction, aportacion: str):
    global historia_activa, historia_completa
    if not historia_activa:
        await interaction.response.send_message("No hay una historia activa. Usa /inicia para empezar una.")
        return

    historia_completa += f"\n{interaction.user.name} dijo: {aportacion}"

    continuacion = obtener_respuesta_ia(f"Continúa la siguiente historia:\n{historia_completa}")
    historia_completa += f"\nLa IA respondió: {continuacion}"

    await interaction.response.send_message(f"**La historia continúa:** {continuacion}")

# Comando para finalizar la historia con el aporte del usuario
@bot.tree.command(name="finalizar", description="Finaliza la historia con tu propio final")
async def finalizar(interaction: discord.Interaction, final_usuario: str):
    global historia_activa, historia_completa
    if not historia_activa:
        await interaction.response.send_message("No hay una historia activa. Usa /inicia para empezar una.")
        return

    historia_completa += f"\n**Final de {interaction.user.name}:** {final_usuario}"
    historia_activa = False

    await interaction.response.send_message(f"**La historia ha finalizado:** {final_usuario}")

# Comando para guardar la historia en un archivo JSON
@bot.tree.command(name="guardar", description="Guarda la historia en un archivo JSON")
async def guardar(interaction: discord.Interaction):
    global historia_completa

    if not historia_completa:
        await interaction.response.send_message("No hay ninguna historia para guardar.")
        return

    # Datos a guardar en el JSON
    datos = {
        "historia": historia_completa
    }

    # Guardar en un archivo JSON
    try:
        with open("historia.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        await interaction.response.send_message("✅ La historia ha sido guardada en 'historia.json'.")
    except Exception as e:
        print(f"Error al guardar la historia: {e}")
        await interaction.response.send_message("❌ Hubo un error al guardar la historia.")

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')
    try:
        await bot.tree.sync()
        print("Comandos sincronizados correctamente")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

# Ejecutar el bot con el token de Discord desde el archivo .env
bot.run(discord_token)
