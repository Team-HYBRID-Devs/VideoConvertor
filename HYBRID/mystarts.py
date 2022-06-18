#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("Set Thumbnail.", data="set"),
                               Button.inline("Remove Thumbnail.", data="rem")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4 BETA**", 
                    buttons=[
                        [Button.inline("Info", data="info"),
                         Button.inline("Source", data="source")],
                        [Button.inline("Notice", data="notice"),
                         Button.inline("Main", data="help")],
                        [Button.url("Updates", url="t.me/HYBRID_Bots")]])
    
