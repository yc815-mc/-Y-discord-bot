import discord
import os
from dotenv import load_dotenv
import json
from pathlib import Path
client = discord.Client()
msid = ""


@client.event
async def on_ready():
    print("目前登入身份：", client.user)
    game = discord.Game("y/help")
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.online, activity=game)

askingID = False


@client.event
# 當有訊息時
async def on_message(message):
    global askingID
    global mcid
    # 防止機器人被自己說的話觸發
    if message.author == client.user:
        return
    # ping功能
    if message.content == 'y/ping':
        await message.channel.send('pong')
    # 指令列表
    if message.content == 'y/help':
        await message.channel.send('！指令列表如下！\n```json\n1. y/help 指令列表與教學\n2. y/ping 測試機器人是否可用\n3. y/audit 進入審核系統\n```')

    # 審核系統
    if message.content == 'y/audit':
        askingID = True
        await message.channel.send('請輸入Minecraft ID')
    elif askingID == True:
        mcid = message.content
        print(mcid)
        askingID = False
        if bool(mcid) == True:
            print(Path(__file__))
            mcid = ""
            await message.channel.send('！指令列表如下！\n```json\n1. y/help 指令列表與教學\n2. y/ping 測試機器人是否可用\n3. y/audit 進入審核系統\n```')

# TOKEN
client.run(os.getenv("token"))
