import requests
import random
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

with open("rumors.txt", "r", encoding="utf-8") as f:
    rumors = [line.strip() for line in f if "|" in line]

speaker, text = random.choice(rumors).split("|", 1)

requests.post(WEBHOOK_URL, json={
    "content": text,
    "username": speaker
})
