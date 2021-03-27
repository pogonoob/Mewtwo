# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/b068fc8dc8d9be627bf85.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "HELLO THIS IS Mewtwo 3.0 \n\n"
  LEGENDX += "ALL SYSTEMS ARE WORKING PROPERLY\n\n"
  LEGENDX += "Mewtwo 3.0 Version : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {Swami} ☺️\n\n"
  LEGENDX += "FULLY UPDATED\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADDDING ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/Swami_2_0_0_5"), Button.url("DEVLOPER", "https://t.me/Swami_2_0_0")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by @Swami_2_0_0
  PROBOYX = [[Button.url("REPO-Mewtwo 3.0", "https://github.com/pogonoob/Mewtwo"), Button.url("Mewtwo Repo", "https://github.com/op-coder482/Soul-thunder-")]]
  PROBOYX +=[[Button.url("DEPLOY-Mewtwo 3.0", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fpogonoob%2FMewtwo&template=https%3A%2F%2Fgithub.com%2Fpogonoob%2FMewtwoP%2FLE"), Button.url("DEPLOY-", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT&template=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/mewtwo1_botsupport"), Button.url("SUPPORT GROUP", "https://t.me/mewtwo1_botsupoort")]]


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX22 and PROBOYX 🔥
  LEGENDX = "HELLO THIS IS Mewtwo 3.0 \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "Mewtwo 3.0 OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {Swami} ☺️\n\n"
  LEGENDX += "FULLY UPDATED BOT\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADDING ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/LEGENDX22"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF GRAND OFFICIAL", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/LEGENDXOP/LEGEND-X")]])
# PROBOYX 🔥 LEGENDX22

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
