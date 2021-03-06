# BSE File Bot

The **BSE File Bot** is a small python tool to track the uploaded files on my school platform and notify me about changes via Discord.
<br />It is supposed to replace the need of writing report booklets ("Ausbildungsnachweise").


## Requirements

- Python 3 & pip installed
- A discord webhook
- An account at my school platform (obviosly...)


## Setup

Install requirements:
```
pip install -r requirements.txt
```

Copy and edit the .env file:
```bash
# Windows
copy .env.example .env
notepad .env

# Linux
cp .env.example .env
vim .env
```


## Run

```bash
# Windows & if you only have Python 3 installed
python bse-file-bot.py

# with Python 3 specifically
python3 bse-file-bot.py
```


## Docker

The **BSE File Bot** can be run in a container using Docker Compose.
<br />You won't need Python and pip anymore, however the .env file still has to be configured.

Build:
```bash
docker-compose build
```

Run:
```bash
docker-compose up -d
```


## Automation

This tool is supposed to run as a cronjob.
<br />A possible cron entry to run it every day at 4pm:
```bash
0 16 * * * python3 /path/to/bse-file-bot.py
```

Or in Docker:
```bash
0 16 * * * /path/to/docker-compose -f /path/to/docker-compose.yml up -d > /dev/null
```
