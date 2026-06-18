# ⚽ ApexPronos AI — Discord Bot

> Moteur de prédiction footballistique ultra-avancé propulsé par l'IA, les mathématiques quantitatives et l'analyse sémantique en temps réel.

---

## 🚀 Fonctionnalités

- 🧮 **Modèle de Poisson / Dixon-Coles** — Calcul des probabilités de chaque score exact
- 📊 **Monte Carlo (10 000 simulations)** — Résultats 1N2, Over/Under, scores exacts
- ⚡ **xG Dynamique** — Expected Goals ajustés au contexte du match
- 📈 **Classement Elo & Forme récente** — Pondération exponentielle des 15 derniers matchs
- 🔍 **Analyse sémantique** — Scraping Twitter/X et presse spécialisée (simulé)
- ⚽ **Top 3 Buteurs attendus** — Indice de conversion individuel
- ⚠️ **Détection d'Upsets & Trap Games** — Algorithme de chaos
- 💰 **Sharp Betting / Value Betting** — Détection des erreurs du marché
- 🎮 **Interface Discord** — Commandes slash `/prono`, `/stats`, `/help`, etc.

---

## 📁 Structure du projet

```
apex-prono-bot/
├── bot.py                  # Point d'entrée principal du bot Discord
├── config.py               # Configuration globale (tokens, paramètres)
├── requirements.txt        # Dépendances Python
├── .env.example            # Template des variables d'environnement
│
├── engine/                 # Moteur de prédiction
│   ├── __init__.py
│   ├── poisson.py          # Modèle Poisson & Dixon-Coles
│   ├── monte_carlo.py      # Simulations Monte Carlo
│   ├── elo.py              # Système Elo & forme récente
│   ├── xg_engine.py        # Expected Goals dynamique
│   ├── upset_detector.py   # Détection d'upsets & trap games
│   └── value_betting.py    # Sharp Betting & Value Betting
│
├── data/                   # Gestion des données
│   ├── __init__.py
│   ├── team_stats.py       # Stats des équipes
│   ├── player_stats.py     # Stats individuelles des joueurs
│   ├── database.py         # Couche base de données (SQLite)
│   └── sample_data.py      # Données de démonstration
│
├── scrapers/               # Collecte de données externes
│   ├── __init__.py
│   ├── twitter_scraper.py  # Analyse sentiment Twitter/X
│   ├── press_scraper.py    # Scraping presse spécialisée
│   └── odds_scraper.py     # Suivi des cotes bookmakers
│
├── commands/               # Commandes Discord
│   ├── __init__.py
│   ├── prono.py            # Commande /prono
│   ├── stats.py            # Commande /stats
│   ├── buteurs.py          # Commande /buteurs
│   ├── value.py            # Commande /value
│   └── help.py             # Commande /help
│
├── formatters/             # Mise en forme des réponses
│   ├── __init__.py
│   └── discord_formatter.py # Formatage Markdown Discord
│
└── utils/                  # Utilitaires
    ├── __init__.py
    ├── logger.py           # Système de logs
    ├── cache.py            # Cache des analyses
    └── validators.py       # Validation des inputs
```

---

## ⚙️ Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/GitAnibri/apex-prono-bot.git
cd apex-prono-bot
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement
```bash
cp .env.example .env
# Édite .env avec ton token Discord et tes clés API
```

### 5. Lancer le bot
```bash
python bot.py
```

---

## 🎮 Commandes Discord

| Commande | Description |
|---|---|
| `/prono [équipe A] [équipe B]` | Analyse complète d'un match |
| `/stats [équipe]` | Statistiques détaillées d'une équipe |
| `/buteurs [équipe A] [équipe B]` | Top buteurs attendus |
| `/value [équipe A] [équipe B]` | Analyse Value Betting uniquement |
| `/help` | Affiche l'aide |

---

## 📜 Licence

MIT License — Utilisation libre à des fins éducatives.

> ⚠️ **Avertissement :** Ce bot est un outil d'analyse statistique à but éducatif. Il ne constitue pas un conseil en paris sportifs. Pariez de manière responsable.
