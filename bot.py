import discord
import random
import os
import asyncio

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

with open("rumors.txt", "r", encoding="utf-8") as f:
    rumors = [line.strip() for line in f if "|" in line]

speaker, rumor = random.choice(rumors).split("|", 1)

message = f"<{speaker}> {rumor}"

class GossipClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)

        if channel:
            await channel.send(message)

        await self.close()

client = GossipClient(
    intents=discord.Intents.default()
)

asyncio.run(client.start(TOKEN))
