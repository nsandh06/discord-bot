# My Discord Bot

A Python Discord bot built as a portfolio project (Cal Poly, Fall 2026).

## What it does (so far)
- `!ping` — replies "Pong!" (bot is alive)
- `!hello` — greets you by name

## Roadmap
- [ ] Scheduled reminders
- [ ] Persistent storage (SQLite)
- [ ] 24/7 deployment

## Setup
1. Create a bot at https://discord.com/developers/applications — copy the token, and enable the **Message Content Intent** under Bot settings.
2. Invite the bot to your test server (OAuth2 → URL Generator → scopes: `bot`, permissions: Send Messages).
3. `cp .env.example .env` and paste your token into `.env`.
4. `python3 -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
5. `pip install -r requirements.txt`
6. `python bot.py` — then type `!ping` in your server.

## Tech
Python, discord.py
