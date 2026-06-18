"""
============================================================
APEX PRONOS AI — Configuration Globale
============================================================
Centralise tous les paramètres du bot : constantes,
coefficients des modèles, couleurs Discord, emojis.
============================================================
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# DISCORD
# ============================================================
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")
DISCORD_GUILD_ID: int | None = int(os.getenv("DISCORD_GUILD_ID", 0)) or None
BOT_PREFIX: str = os.getenv("BOT_PREFIX", "!")

# ============================================================
# API EXTERNES
# ============================================================
API_FOOTBALL_KEY: str = os.getenv("API_FOOTBALL_KEY", "")
API_FOOTBALL_HOST: str = os.getenv("API_FOOTBALL_HOST", "v3.football.api-sports.io")
API_FOOTBALL_BASE_URL: str = f"https://{API_FOOTBALL_HOST}"
TWITTER_BEARER_TOKEN: str = os.getenv("TWITTER_BEARER_TOKEN", "")

# ============================================================
# MOTEUR DE PRÉDICTION
# ============================================================
MONTE_CARLO_SIMULATIONS: int = int(os.getenv("MONTE_CARLO_SIMULATIONS", 10000))

# Pondération forme récente
FORM_WEIGHT_LAST_5: float = 0.50
FORM_WEIGHT_PREV_5: float = 0.30
FORM_WEIGHT_REST:   float = 0.20

# Avantage domicile
HOME_ADVANTAGE_FACTOR: float = 1.20

# Poisson
MAX_GOALS_POISSON: int  = 8
DIXON_COLES_RHO:  float = -0.13

# Over/Under seuils
OVER_UNDER_THRESHOLDS: list[float] = [0.5, 1.5, 2.5, 3.5, 4.5]

# Elo
ELO_K_FACTOR:      int = 32
ELO_DEFAULT_RATING: int = 1500

# ============================================================
# UPSETS & CHAOS
# ============================================================
TRAP_GAME_VARIANCE_BONUS:     float = 0.25
DERBY_LEVEL_GAP_REDUCTION:    float = 0.30
PENALTY_TAKER_BONUS:          float = 0.12
KEY_DEFENDER_ABSENCE_PENALTY: float = 0.15
VALUE_THRESHOLD_PERCENT:      float = 5.0

# ============================================================
# CACHE & BASE DE DONNÉES
# ============================================================
CACHE_EXPIRY_SECONDS: int = int(os.getenv("CACHE_EXPIRY_SECONDS", 3600))
DATABASE_PATH: str = os.getenv("DATABASE_PATH", "data/apex_pronos.db")
DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() == "true"

# ============================================================
# COULEURS DISCORD (entiers hex)
# ============================================================
COLOR_SUCCESS: int = 0x00FF87
COLOR_WARNING: int = 0xFFD700
COLOR_DANGER:  int = 0xFF4757
COLOR_INFO:    int = 0x3498DB
COLOR_APEX:    int = 0x9B59B6

# ============================================================
# EMOJIS
# ============================================================
EMOJI: dict[str, str] = {
    "ball":    "⚽",
    "chart":   "📊",
    "target":  "🎯",
    "money":   "💰",
    "warning": "⚠️",
    "news":    "📰",
    "math":    "🧮",
    "fire":    "🔥",
    "red":     "🔴",
    "blue":    "🔵",
    "draw":    "🤝",
    "up":      "📈",
    "down":    "📉",
    "star":    "⭐",
    "trophy":  "🏆",
    "clock":   "🕐",
    "check":   "✅",
    "cross":   "❌",
    "info":    "ℹ️",
    "robot":   "🤖",
    "shock":   "⚡",
    "versus":  "⚔️",
    "pin":     "📌",
}
