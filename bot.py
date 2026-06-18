"""
============================================================
APEX PRONOS AI — Point d'entrée principal du bot Discord
============================================================
Charge toutes les extensions (cogs), initialise la base
de données, configure les événements globaux et démarre.
============================================================
"""

import asyncio
import sys

import disnake
from disnake.ext import commands

import config
from utils.logger import get_logger
from data.database import Database

logger = get_logger("bot")

# ============================================================
# EXTENSIONS (COGS)
# ============================================================
EXTENSIONS: list[str] = [
    "commands.prono",
    "commands.stats",
    "commands.buteurs",
    "commands.value",
    "commands.help",
]


# ============================================================
# CRÉATION DU BOT
# ============================================================
def create_bot() -> commands.InteractionBot:
    """Instancie et configure le bot Discord."""
    intents = disnake.Intents.default()
    intents.message_content = True

    test_guilds = [config.DISCORD_GUILD_ID] if config.DISCORD_GUILD_ID else None

    bot = commands.InteractionBot(
        intents=intents,
        test_guilds=test_guilds,
    )
    return bot


bot = create_bot()


# ============================================================
# ÉVÉNEMENTS
# ============================================================
@bot.event
async def on_ready() -> None:
    """Déclenché quand le bot est connecté et prêt."""
    logger.info(f"✅ Connecté en tant que : {bot.user} (ID: {bot.user.id})")
    logger.info(f"📡 Serveurs : {len(bot.guilds)}")

    db = Database()
    await db.initialize()
    logger.info("🗄️  Base de données initialisée")

    await bot.change_presence(
        activity=disnake.Activity(
            type=disnake.ActivityType.watching,
            name="⚽ les matchs | /prono",
        ),
        status=disnake.Status.online,
    )
    logger.info("🚀 ApexPronos AI est prêt !")


@bot.event
async def on_slash_command(inter: disnake.ApplicationCommandInteraction) -> None:
    """Log chaque commande slash utilisée."""
    logger.info(
        f"📌 /{inter.application_command.name} "
        f"par {inter.author} dans #{inter.channel}"
    )


@bot.event
async def on_slash_command_error(
    inter: disnake.ApplicationCommandInteraction,
    error: Exception,
) -> None:
    """Gestionnaire global d'erreurs pour les commandes slash."""
    logger.error(f"❌ Erreur sur /{inter.application_command.name} : {error}")
    embed = disnake.Embed(
        title="❌ Une erreur est survenue",
        description=(
            f"```{str(error)[:500]}```\n"
            "Si le problème persiste, contacte l'administrateur."
        ),
        color=config.COLOR_DANGER,
    )
    try:
        await inter.response.send_message(embed=embed, ephemeral=True)
    except Exception:
        pass


# ============================================================
# CHARGEMENT DES EXTENSIONS
# ============================================================
def load_extensions(bot: commands.InteractionBot) -> None:
    """Charge toutes les extensions définies dans EXTENSIONS."""
    for ext in EXTENSIONS:
        try:
            bot.load_extension(ext)
            logger.info(f"✅ Extension chargée : {ext}")
        except Exception as e:
            logger.error(f"❌ Impossible de charger {ext} : {e}")
            sys.exit(1)


# ============================================================
# POINT D'ENTRÉE
# ============================================================
async def main() -> None:
    """Charge les cogs et démarre le bot."""
    if not config.DISCORD_TOKEN:
        logger.critical("DISCORD_TOKEN manquant ! Vérifie ton .env")
        sys.exit(1)

    load_extensions(bot)
    logger.info("🔌 Connexion à Discord...")
    await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Bot arrêté manuellement.")
