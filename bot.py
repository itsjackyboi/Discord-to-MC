import requests
import random
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

with open("rumors.txt", "r", encoding="utf-8") as f:
    raw = f.read()

entries = [block.strip() for block in raw.split("\n\n") if "|" in block]
speaker, text = random.choice(entries).split("|", 1)

requests.post(WEBHOOK_URL, json={
    "content": text.strip(),
    "username": speaker.strip()
})
