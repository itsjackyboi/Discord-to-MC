import discord
import random
import os
import asyncio

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

# Load rumors
with open("rumors.txt", "r", encoding="utf-8") as f:
    rumors = [line.strip() for line in f if "|" in line]

# Pick one rumor
speaker, text = random.choice(rumors).split("|", 1)

message = f"<{speaker}> {text}"

class GossipClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)

        if channel:
            msg = await channel.send("...")
            await msg.edit(content=message)

        await self.close()

intents = discord.Intents.default()
client = GossipClient(intents=intents)

asyncio.run(client.start(TOKEN))
