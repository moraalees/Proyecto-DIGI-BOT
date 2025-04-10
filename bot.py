"""
Discord storytelling bot with AI integration using OpenRouter (compatible with OpenAI API).
Allows users to generate, continue, and save collaborative stories directly from Discord.
"""

import discord
from discord.ext import commands
from openai import OpenAI
import random
import json
import os
from dotenv import load_dotenv

# py -3.11 bot.py / How to run the code


# https://discord.com/oauth2/authorize?client_id=1329402639729037353&permissions=2147551232&integration_type=0&scope=bot+applications.commands


# Load environment variables from the .env file
load_dotenv()


# Load API keys
api_key = os.getenv("OPENROUTER_API_KEY")
discord_token = os.getenv("DISCORD_BOT_TOKEN")


# Set up OpenAI (OpenRouter) client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# Configure Discord intents
intents = discord.Intents.default()
intents.message_content = True


# Create the bot
bot = commands.Bot(command_prefix='/', intents=intents)


# Global story variables
historia_activa = False
historia_completa = ""


# Story openings
inicios_historia = [
    "Érase una vez en un lejano reino...",
    "En un mundo donde la magia era real...",
    "Hace mucho tiempo, en una galaxia muy, muy lejana...",
    "En un pequeño pueblo rodeado de bosques oscuros...",
    "En un futuro distópico donde las máquinas dominaban el mundo..."
]


def generar_inicio_historia_ia():
    """
    Generates a story opening using AI. If AI fails, selects a random predefined opening.

    Returns:
        str: Story opening text.
    """
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


def obtener_respuesta_ia(mensaje):
    """
    Gets a response from the AI based on a given message.

    Args:
        mensaje (str): The user input or story continuation.

    Returns:
        str: AI's response.
    """
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


@bot.tree.command(name="ia", description="Hazle una pregunta a la IA")
async def ia(interaction: discord.Interaction, pregunta: str):
    """
    Discord slash command to ask the AI any question.

    Args:
        interaction (discord.Interaction): Discord interaction context.
        pregunta (str): User's question to the AI.
    """
    respuesta = obtener_respuesta_ia(pregunta)
    await interaction.response.send_message(respuesta)


@bot.tree.command(name="hola", description="El bot te saluda")
async def hola(interaction: discord.Interaction):
    """
    Discord slash command to greet the user.

    Args:
        interaction (discord.Interaction): Discord interaction context.
    """
    await interaction.response.send_message(f'¡Qué pasa {interaction.user.mention}!')


@bot.tree.command(name="inicia", description="Inicia una nueva historia")
async def inicia(interaction: discord.Interaction):
    """
    Starts a new story using AI-generated opening. Prevents starting if a story is already active.

    Args:
        interaction (discord.Interaction): Discord interaction context.
    """
    global historia_activa, historia_completa
    if historia_activa:
        await interaction.response.send_message("¡Ya hay una historia en curso! Usa /nueva para empezar otra.")
    else:
        historia_activa = True
        inicio = generar_inicio_historia_ia()
        historia_completa = inicio
        await interaction.response.send_message(f"**Nueva Historia Iniciada:** {inicio}")


@bot.tree.command(name="nueva", description="Inicia una historia nueva desde cero")
async def nueva(interaction: discord.Interaction):
    """
    Starts a brand-new story using a random predefined opening.

    Args:
        interaction (discord.Interaction): Discord interaction context.
    """
    global historia_activa, historia_completa
    historia_activa = True
    inicio = random.choice(inicios_historia)
    historia_completa = inicio
    await interaction.response.send_message(f"**Se ha iniciado una nueva historia:** {inicio}")


@bot.tree.command(name="seguir", description="Continúa la historia con tu aportación")
async def seguir(interaction: discord.Interaction, aportacion: str):
    """
    Continues the current story by adding user input and letting the AI generate the next part.

    Args:
        interaction (discord.Interaction): Discord interaction context.
        aportacion (str): User's contribution to the story.
    """
    global historia_activa, historia_completa
    if not historia_activa:
        await interaction.response.send_message("No hay una historia activa. Usa /inicia para empezar una.")
        return

    historia_completa += f"\n{interaction.user.name} dijo: {aportacion}"

    continuacion = obtener_respuesta_ia(f"Continúa la siguiente historia:\n{historia_completa}")
    historia_completa += f"\nLa IA respondió: {continuacion}"

    await interaction.response.send_message(f"**La historia continúa:** {continuacion}")


@bot.tree.command(name="finalizar", description="Finaliza la historia con tu propio final")
async def finalizar(interaction: discord.Interaction, final_usuario: str):
    """
    Ends the current story with a user-provided ending.

    Args:
        interaction (discord.Interaction): Discord interaction context.
        final_usuario (str): User's final story segment.
    """
    global historia_activa, historia_completa
    if not historia_activa:
        await interaction.response.send_message("No hay una historia activa. Usa /inicia para empezar una.")
        return

    historia_completa += f"\n**Final de {interaction.user.name}:** {final_usuario}"
    historia_activa = False

    await interaction.response.send_message(f"**La historia ha finalizado:** {final_usuario}")


@bot.tree.command(name="guardar", description="Guarda la historia en un archivo JSON")
async def guardar(interaction: discord.Interaction):
    """
    Saves the full story into a local JSON file.

    Args:
        interaction (discord.Interaction): Discord interaction context.
    """
    global historia_completa

    if not historia_completa:
        await interaction.response.send_message("No hay ninguna historia para guardar.")
        return

    datos = {
        "historia": historia_completa
    }

    try:
        with open("historia.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        await interaction.response.send_message("✅ La historia ha sido guardada en 'historia.json'.")
    except Exception as e:
        print(f"Error al guardar la historia: {e}")
        await interaction.response.send_message("❌ Hubo un error al guardar la historia.")


@bot.tree.command(name="chiste", description="Pídele un chiste a la IA")
async def chiste(interaction: discord.Interaction, tema: str):
    """
    Discord command to request a joke from the AI based on a user-provided topic.

    Parameters:
        interaction (discord.Interaction): The context of the command interaction from Discord.
        tema (str): The topic or subject the user wants the joke to be about.

    Behavior:
        - Sends a prompt to the AI to generate a joke related to the given topic.
        - Replies in the same channel with the generated joke.
        - If there's an error during the request, it informs the user of the failure.

    Example:
        User: /chiste tema="programadores"
        Bot: ¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 = DEC 25.
    """
    try:
        # Usamos la IA para generar un chiste sobre el tema que el usuario proporciona
        respuesta = obtener_respuesta_ia(f"Cuenta un chiste sobre {tema}")

        # Envía el chiste al canal
        await interaction.response.send_message(respuesta)
    
    except Exception as e:
        print("Error al obtener el chiste:", e)
        await interaction.response.send_message("Lo siento, algo salió mal al generar el chiste. ¡Intenta de nuevo!")


@bot.event
async def on_ready():
    """
    Event triggered when the bot is fully connected and ready.

    Synchronizes slash commands with Discord's API.
    """
    print(f'Conectado como {bot.user}')
    try:
        await bot.tree.sync()
        print("Comandos sincronizados correctamente")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")


# Run the bot
bot.run(discord_token)
