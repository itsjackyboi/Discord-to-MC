import requests
import random
import os
import re

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

with open("rumors.txt", "r", encoding="utf-8") as f:
    rumors = [line.strip() for line in f if line.strip() and line.startswith("<")]

entry = random.choice(rumors)
match = re.match(r"<(.+?)>\s*(.*)", entry, re.DOTALL)
speaker = match.group(1)
text = match.group(2)

requests.post(WEBHOOK_URL, json={
    "content": text,
    "username": speaker
})
