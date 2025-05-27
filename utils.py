import random #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
import time #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
import math #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
import os #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
from vars import CREDIT #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
from pyrogram.errors import FloodWait #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
from datetime import datetime,timedelta #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

class Timer: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    def __init__(self, time_between=5): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        self.start_time = time.time() #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        self.time_between = time_between #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    def can_send(self): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        if time.time() > (self.start_time + self.time_between): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            self.start_time = time.time() #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            return True #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        return False #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

#lets do calculations #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
def hrb(value, digits= 2, delim= "", postfix=""): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    """Return a human-readable file size. #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    """ #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    if value is None: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        return None #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    chosen_unit = "B" #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    for unit in ("KB", "MB", "GB", "TB"): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        if value > 1000: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            value /= 1024 #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            chosen_unit = unit #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        else: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            break #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

def hrt(seconds, precision = 0): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    """Return a human-readable time delta as a string. #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    """ #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    pieces = [] #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    value = timedelta(seconds=seconds) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    if value.days: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        pieces.append(f"{value.days}day") #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    seconds = value.seconds #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    if seconds >= 3600: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        hours = int(seconds / 3600) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        pieces.append(f"{hours}hr") #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        seconds -= hours * 3600 #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    if seconds >= 60: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        minutes = int(seconds / 60) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        pieces.append(f"{minutes}min") #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        seconds -= minutes * 60 #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    if seconds > 0 or not pieces: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        pieces.append(f"{seconds}sec") #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    if not precision: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        return "".join(pieces) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

    return "".join(pieces[:precision]) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

timer = Timer() #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

async def progress_bar(current, total, reply, start): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
    if timer.can_send(): #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        now = time.time() #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        diff = now - start #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        if diff < 1: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            return #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
        else: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            perc = f"{current * 100 / total:.1f}%" #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            elapsed_time = round(diff) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            speed = current / elapsed_time #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            remaining_bytes = total - current #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            if speed > 0: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                eta_seconds = remaining_bytes / speed #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                eta = hrt(eta_seconds, precision=1) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            else: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                eta = "-" #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            sp = str(hrb(speed)) + "/s" #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            tot = hrb(total) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            cur = hrb(current) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            bar_length = 10 #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            completed_length = int(current * bar_length / total) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            remaining_length = bar_length - completed_length #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

            symbol_pairs = [ #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                ("▬", "▭"), #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                ("✅", "☑️"), #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                ("🐬", "🦈"), #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                ("💚", "💛"), #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                ("🌟", "⭐"), #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                ("▰", "▱") #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            ] #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            chosen_pair = random.choice(symbol_pairs) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
            completed_symbol, remaining_symbol = chosen_pair #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮

            try: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
                #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝗗𝗘𝗠𝗢𝗡 𝗔𝗥𝗠𝗬🦋✨═══─╯`') 
            except FloodWait as e: #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮
                time.sleep(e.x) #𝘿𝙚𝙢𝙤𝙣𝘼𝙧𝙢𝙮 
