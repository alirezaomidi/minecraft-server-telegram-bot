# Minecraft Server Telegram Bot

This repo contains a telegram bot written in Python, which is an interface for Minecraft servers
(and mods, e.g. Spigot).

## Install
```bash
git clone https://github.com/alirezaomidi/minecraft-server-telegram-bot
cd minecraft-server-telegram-bot
virtualenv -py python3 vevn
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python bot.py --token YOURTOKEN
```

## TODO
- [ ] create a game server & transfer from backup server to game server & start the game
- [ ] stop the game & transfer file from game server to backup server & delete game server
- [ ] status (On, Turning on, Off, Turning off)

## Contribute
Check issues to see ongoing tasks. Feel free to participate in tasks or Open a new issue.
