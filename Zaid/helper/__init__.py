import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zaid"])

async def join(client):
    try:
        await client.join_chat("🔰𝗙𝗟𝗔𝗠𝗘 ❖ 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬🔰")
    except BaseException:
        pass
