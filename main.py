import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    # يدخل البوت الروم الصوتي تلقائياً عند التشغيل
    vc = bot.get_channel(1367476216524705817)  # غيّر الـ ID برومك إذا مختلف
    if vc:
        await vc.connect()


keep_alive()  # عشان يبقى شغال مع UptimeRobot
TOKEN = os.environ.get("TOKEN")
bot.run(TOKEN)
