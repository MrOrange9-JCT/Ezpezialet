import discord
import random
import asyncio
import png
import aiohttp
import pyqrcode
import jishaku
import re
from datetime import datetime
from itertools import cycle
from discord.ext import commands, tasks
import os 


client = commands.Bot(command_prefix=['zz!', 'zz! ', '<@553883586210562060> '])
client.remove_command('help')
status = cycle(["zz!help", "Minecraft", "zz!info", "Basic Programming", "Guacamelee! Gold Edition", "Nothing / Nada"])
#status = cycle(["MrOrange9 JCT en Twitch", "a una persona (no tapes tu webcam)", "el comandament zz!help", "que fa zz!giveyouup"])
MD = discord.Embed(title="**<:greenTick:714072192358416474> Mira els missatges directes!**", descripton="\u200b", colour=0x212227)
embed_color = 0x8404FC

client.load_extension("jishaku")

def is_bot(m):
    return m.author == client.user
    
def servers():
    servers = client.guilds
    return servers


###########################################    EVENTS    ##########################################

@client.event
async def on_command_error(ctx, error):
    print(str(error))

    if hasattr(ctx.command, 'on_error'):
            return

    if isinstance(error, commands.MissingRequiredArgument):
        falta = discord.Embed(title="**<:redTick:714072192681508885> Argument/s necessaris faltants!**",
                              descripton="\u200b", colour=0x212227)
        await ctx.send(embed=falta)


    if isinstance(error, commands.TooManyArguments):
        noarg = discord.Embed(
            title="**<:redTick:714072192681508885> Argument/s no nessecaris!**", colour=0x212227)
        await ctx.send(embed=noarg)

    if isinstance(error, discord.InvalidArgument):
        badarg = discord.Embed(title="**<:redTick:714072192681508885> Comprova que els arguments siguin correctes.**", colour=0x212227)
        await ctx.send(embed=badarg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.guild is None:
        responses = ["Beep Boop Beep Bop",
                    "Boo Bip Boop Bep?",
                    "Jeje parlo ezpezialet o robotz",
                    "BOOOOOP BEEEEEEP",
                    "Que bolz",
                    "Boop Beep! Beep Bop :(",
                    "Prova elz comandoz! zz!help",
                    "Boop Beep!! BOOOOOOOP BEEEEEEEEP! :) :) :)",
                    "01001000 01101111 01101110 01100001 00100000 01110001 01110101 01100101 00100000 01110100 01100001 01101110 00100000 01100101 01101101 00100000 01100100 01101001 01101110 01100011 00100000 01101010 01101111 01101110 01100100 01101001",
                    "Hona **" + str(message.author) + "**, que tan?"]
        await message.channel.send(random.choice(responses))
    await client.process_commands(message)

@client.event
async def on_ready():
    change_status.start()
    print('Bot connected to discord succesfully!')

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=next(status), url="https://www.twitch.tv/mrorange9jct"))



###########################################    COMANDAMENTS DEL BOT    ##########################################

# ./cogs/bot.py
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

###########################################    COMANDAMENTS DE DIVERSIÓ    ##########################################

# ./cogs/bot.py

#################################    COMANDAMENTS DE CAPEK (No son per a un sevidor)    #################################

# zz!titu
@client.command()
async def titu(ctx):
    await ctx.send(":fire: Ei titu! Vaig a fer una barbacoa, pazza'm el flamizell. Ara te'l torno.. :fire:")


##########################################    COMANDAMENTS DE UTILITAT (i servidor)    #########################################

# zz!rannum
@client.command(aliases=['rannum'])
async def randomnumber(ctx, n1, n2):
    number = random.randrange(int(n1), int(n2))
    embed = discord.Embed(title=f":1234:  **Ha sortit {number}.**", color=0x212227)
    await ctx.send(embed=embed)

# Rannum Error
@randomnumber.error
async def rannum_error(ctx):
    embed = discord.Embed(title='**<:redTick:714072192681508885> Comprova que el missatge sigui: \n`rannum <num1(desde)> <num2(fins)>`**', color=0x212227)
    await ctx.send(embed=embed)

# zz!minecraft 
@client.command()
async def minecraft(ctx, *, adress):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://mcapi.us/server/status?ip={adress}") as r:
                data = await r.json()

                name = data['server']['name']
                players_now = data['players']['now']
                players_max = data['players']['max']
                motd = data['motd']

                embed = discord.Embed(title=f"{adress} ({name})", description=f"**Jugadors:** {players_now}/{players_max}\n \n{motd}\n \n**Previsualització Minecraft:**")
		embed.set_image(url=f"http://status.mclive.eu/{adress}/{adress}/25565/banner.png")

                await ctx.send(embed=embed)

# Minecraft Error
@minecraft.error
async def minecraft_error(ctx, error):
    embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova si has proporcionat una IP que existeixi.**", color=0x212227)

    await ctx.send(embed=embed)	

# zz!morsificar
@client.command()
async def morsificar(ctx, *, word: str=None):
    code = {
        "a" : ".-",
        "b" : "-...",
        "c" : "-.-.",
        "d" : "-..",
        "e" : ".",
        "f" : "..-.",
        "g" : "--.",
        "h" : "....",
        "i"  : "..",
        "j"  : ".---",
        "k" : "-.-",
        "l"  : ".-..",
        "m" : "--",
        "n" : "-.",
        "o" : "---",
        "p" : ".--.",
        "q" : "--.-",
        "r"  : ".-.",
        "s" : "...",
        "t" : "-",
        "u": "..-",
        "v" : "...-",
        "w" : ".--",
        "x"  : "-..-",
        "y"  : "-.--",
        "z" : "--..",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----",
    }
    word = str(word).lower().replace(".", "").replace("-", "")
    chars = list(word)
    msg = ""
    for w in chars:
        try:
            msg += code[w] + " "
        except:
            msg += "  "
            
    if len(list(word)) > 500:
        embed_error = discord.Embed(title="**<:redTick:714072192681508885> Ala tio! No et passis de llarg! (literalment)**", colour=0x212227)
        await ctx.send(embed=embed_error)
    else:
        embed = discord.Embed(title="**<:greenTick:714072192358416474> Codi morsificat!**", description=f"`{msg}`", colour=0x212227)
        await ctx.send(embed=embed)

    
# zz!embed
@client.command()
async def embed(ctx, *, str_input):
    splitted_input = str_input.split(" | ")

    if 'mostrardata' in splitted_input:
        if splitted_input[2] == 'default':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], timestamp=datetime.utcnow())
        elif splitted_input[2] == 'teal':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.teal(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_teal':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_teal(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'green':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.green(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_green':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_green(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'blurple':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.blurple(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'blue':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.blue(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_blue':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_blue(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'magenta':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.magenta(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_magenta':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_magenta(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'gold' or 'yellow':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.gold(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_gold' or 'dark_yellow':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_gold(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'orange':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.orange(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_orange':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_orange(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'red':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.red(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_red':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.blue(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'greyple':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.greyple(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'light_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.light_grey(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'lighter_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.lighter_grey(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'dark_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_grey(), timestamp=datetime.utcnow())
        elif splitted_input[2] == 'darker_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.darker_grey(), timestamp=datetime.utcnow())
        else:
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=splitted_input[2], timestamp=datetime.utcnow())
            

    else:
        if splitted_input[2] == 'default':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1])
        elif splitted_input[2] == 'teal':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.teal())
        elif splitted_input[2] == 'dark_teal':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_teal())
        elif splitted_input[2] == 'green':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.green())
        elif splitted_input[2] == 'dark_green':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_green())
        elif splitted_input[2] == 'blurple':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.blurple())
        elif splitted_input[2] == 'blue':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.blue())
        elif splitted_input[2] == 'dark_blue':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_blue())
        elif splitted_input[2] == 'magenta':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.magenta())
        elif splitted_input[2] == 'dark_magenta':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_magenta())
        elif splitted_input[2] == 'gold' or 'yellow':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.gold())
        elif splitted_input[2] == 'dark_gold' or 'dark_yellow':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_gold())
        elif splitted_input[2] == 'orange':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=0xff9900)
        elif splitted_input[2] == 'dark_orange':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=0xb07002)
        elif splitted_input[2] == 'red':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.red())
        elif splitted_input[2] == 'dark_red':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.blue())
        elif splitted_input[2] == 'greyple':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.greyple())
        elif splitted_input[2] == 'light_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.light_grey())
        elif splitted_input[2] == 'lighter_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.lighter_grey())
        elif splitted_input[2] == 'dark_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.dark_grey())
        elif splitted_input[2] == 'darker_grey':
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=discord.Color.darker_grey())
        else:
            embed = discord.Embed(title=splitted_input[0], description=splitted_input[1], colour=splitted_input[2])
    
    if 'mostrarautor' in splitted_input:
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)

# Embed Error
@embed.error
async def embed_error(ctx, error):
	embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova els arguments són correctes.** (`zz!help`)", description="[Llista de colors](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e#file-discord-colour-md)", colour=0x212227)
	await ctx.send(embed=embed)

# zz!placa
@client.command()
async def placa(ctx, *, str_input):
    splitted_input = str_input.split(" | ")
    etiqueta = splitted_input[0].replace("-", "--", 100)
    etiqueta = etiqueta.replace("_", "__", 100)
    etiqueta = etiqueta.replace(" ", "_", 100)
    missatge = splitted_input[1].replace("-", "--", 100)
    missatge = missatge.replace("_", "__", 100)
    missatge = missatge.replace(" ", "_", 100)
    try:
        url = f"https://raster.shields.io/badge/{etiqueta}-{missatge}-{splitted_input[2]}?{splitted_input[3]}"
        print(url)
        embed = discord.Embed(title="**Placa generada!**")
        embed.set_author(name="Shields.io", url="https://shields.io/", icon_url="https://cdn.discordapp.com/icons/308323056592486420/11a50197f2858fa14b74f41ceaacc4b6.png?size=128")
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    except:
        url = f"https://raster.shields.io/badge/{etiqueta}-{missatge}-{splitted_input[2]}"
        print(url)
        embed = discord.Embed(title="**Placa generada!**")
        embed.set_author(name="Shields.io", url="https://shields.io/", icon_url="https://cdn.discordapp.com/icons/308323056592486420/11a50197f2858fa14b74f41ceaacc4b6.png?size=128")
        embed.set_image(url=url)
        await ctx.send(embed=embed)

# zz!infousuari / ui
@client.command(aliases=['infousuari'])
async def ui(ctx, *, member: discord.Member=None):
    if member == None:
        embed = discord.Embed(title="**Informació de l'usuari.**", description=ctx.author.name + "#" + ctx.author.discriminator, timestamp=datetime.utcnow(), color=0x303136)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        if ctx.author.status == discord.Status.online:
            embed.add_field(name="Estat", value='<:statusOnline:714072197072683038> Conectat')
        if ctx.author.status == discord.Status.idle:
            embed.add_field(name="Estat", value='<:statusIdle:714072406867574815> Ausent')
        if ctx.author.status == discord.Status.dnd:
            embed.add_field(name="Estat", value='<:statusDND:714072192890961970> No molestar')
        if ctx.author.status == discord.Status.offline:
            embed.add_field(name="Estat", value='<:statusOffline:714072193344208938> Desconectat')
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="ID de l'usuari", value=":id: " + str(ctx.author.id), inline=False)
        if ctx.author.is_on_mobile():
            embed.add_field(name="Dispositiu", value=':iphone: Mòvil / Tauleta', inline=False)
        elif ctx.author.status == discord.Status.offline:
            print('')
        else:
            embed.add_field(name="Dispositiu", value=':desktop: Ordinador / Web', inline=False)
        joined_at = ctx.author.joined_at
        created_at = ctx.author.created_at
        embed.add_field(name="Al servidor desde (Data en anglès)", value="<a:blobJoining:716649861608374272> " + str(joined_at.ctime()), inline=False)
        embed.add_field(name="Conta creada al (Data en anglès)", value="<:discordLogo:716720696885248000> " + str(created_at.ctime()), inline=False)
        if ctx.author.activity == None:
            embed.add_field(name="Activitat", value=':x: Cap', inline=False)
        elif ctx.author.activity.type is discord.ActivityType.custom:
            embed.add_field(name="Estat Personalitzat", value=ctx.author.activity, inline=False) 
        else:
            embed.add_field(name=":video_game: Activitat", value=ctx.author.activity.name, inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
    else:
        embed = discord.Embed(title="**Informació de l'usuari.**", description=member.name + "#" + member.discriminator, timestamp=datetime.utcnow(), color=0x303136)
        embed.set_author(name=member.display_name, icon_url=member.avatar_url)
        if member.status == discord.Status.online:
            embed.add_field(name="Estat", value='<:statusOnline:714072197072683038> Conectat')
        if member.status == discord.Status.idle:
            embed.add_field(name="Estat", value='<:statusIdle:714072406867574815> Ausent')
        if member.status == discord.Status.dnd:
            embed.add_field(name="Estat", value='<:statusDND:714072192890961970> No molestar')
        if member.status == discord.Status.offline:
            embed.add_field(name="Estat", value='<:statusOffline:714072193344208938> Desconectat')
        if member.is_on_mobile():
            embed.add_field(name="Dispositiu", value=':iphone: Mòvil', inline=False)
        elif member.status == discord.Status.offline:
            print('')
        else:
            embed.add_field(name="Dispositiu", value=':desktop: Ordinador / Web', inline=False)
        joined_at = member.joined_at
        created_at = member.created_at
        embed.add_field(name="ID de l'usuari", value=":id: " + str(member.id), inline=False)
        embed.add_field(name="Al servidor desde (Data en anglès)", value="<a:blobJoining:716649861608374272> " + str(joined_at.ctime()), inline=False)
        embed.add_field(name="Conta creada al (Data en anglès)", value="<:discordLogo:716720696885248000> " + str(created_at.ctime()), inline=False)
        if member.activity == None:
            embed.add_field(name="Activitat", value=':x: Cap', inline=False)
        elif member.activity.type is discord.ActivityType.custom:
            embed.add_field(name="Estat Personalitzat", value=member.activity, inline=False)
        else:
            embed.add_field(name=":video_game: Activitat", value=member.activity.name, inline=False)
        embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


# zz!qr
@client.command()
async def qr(ctx, *, input_text):
    qr = pyqrcode.create(f"{input_text}")
    qr.png("qr.png", scale = 12)
    await ctx.send("**Codi QR generat!**", file=discord.File('qr.png'))

# zz!google
@client.command()
async def google(ctx, *, input_text):
    url = f"https://google.com/search?q={input_text}"
    final_url = url.replace(" ", "%20")
    embed=discord.Embed(title="**Fes clic aquí per veure els resultats**", url=final_url, description=f"Cerca: {input_text}", color=0x3a87fe)
    embed.set_thumbnail(url="https://cdn.foliomag.com/wp-content/uploads/2018/04/google-logo-icon-png-transparent-background.png")
    await ctx.send(embed=embed)

# zz!email
@client.command()
async def email(ctx, *, input_text):
    await ctx.message.delete()
    email_to, subject, body = input_text.split(" | " or "|")
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(os.environ.get("EMAIL_ADRESS"), os.environ.get("EMAIL_PASS"))

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(os.environ.get("EMAIL_ADRESS"), email_to, msg)

        embed = discord.Embed(title=f"**<:greenTick:714072192358416474> Correu enviat!**\n\n**Previsualització:**\n`ezpezialet@gmail.com`\n\n**{subject}**\n{body}", colour=0x212227)
        await ctx.send("", embed=embed, delete_after=10)

# Email Error
@email.error
async def email_error(ctx, error):
    embed = discord.Embed(title="**<:redTick:714072192681508885> No s'ha enviat el correu.**", description="**Comprova si el correu proporcionat és vàlid, si has separat els arguments correctament i que només siguin caràcters [ASCII](http://www.asciitable.com/index/asciifull.gif)**\nSi tot està correcte i segueix sense funcionar, prova-ho més tard", colour=0x212227)
    await ctx.send(embed=embed)


###########################################    COMANDAMENTS DE MODERACIÓ    ##########################################

# zz!clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(title="<:greenTick:714072192358416474> **Missatges borrats!**", colour=0x212227)
    await ctx.send(embed=embed)
    await asyncio.sleep(1.5)
    await ctx.channel.purge(limit=1, check=is_bot)

# Clear Error
@clear.error
async def clear_error(ctx, error):
    embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova si tú i el bot teniu el permís de `Manage Messages`  i que els arguments siguin numeros.**", colour=0x212227)
    await ctx.send(embed=embed)

# zz!warn
@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.User, *, reason='Raó: Sense definir'):
	user_to_warn = user
	guild = ctx.guild
	guild_icon = ctx.guild.icon_url
	author_name = ctx.author
	author_icon = author_name.avatar_url
	embed = discord.Embed(title="Has rebut un avís!", description=f"{reason}", color=0xff2600)
	embed.set_author(name=f"{author_name}", icon_url=f"{author_icon}")
	embed.set_footer(text=f"{guild}", icon_url=f"{guild_icon}")
	await user_to_warn.send(embed=embed)
	embed2 = discord.Embed(title="<:greenTick:714072192358416474> **Usuari avisat!**", colour=0x212227)
	await ctx.send(embed=embed2)
	await asyncio.sleep(1.5)
	await ctx.channel.purge(limit=1, check=is_bot)

# Warn Error
@warn.error
async def warn_error(ctx, error):
	embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova si tens el permís `Kick Users` i que els arguments siguin correctes.** (`zz!help`)", colour=0x212227)
	await ctx.send(embed=embed)

# zz!kick
@client.command(aliases=['kick'])
@commands.has_permissions(kick_members=True)
async def kickuser(ctx, user: discord.Member, *, reason='Raó Sense definir'):
    guild = ctx.guild
    guild_icon = ctx.guild.icon_url
    author_name = ctx.author
    author_icon = author_name.avatar_url
    embed = discord.Embed(title=f"{user} ha sigut expulsat!", description=f"{reason}", color=0xff2600)
    embed.set_author(name=f"{author_name}", icon_url=f"{author_icon}")
    embed.set_footer(text=f"{guild}", icon_url=f"{guild_icon}")
    await ctx.send(embed=embed)
    await user.kick(reason=reason)

# Kick Error
@kickuser.error
async def kick_error(ctx, error):
	embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova si tú i el bot teniu el permís `Kick Users` i que els arguments siguin correctes.** (`zz!help`)", colour=0x212227)
	await ctx.send(embed=embed)    
   
# zz!ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason='Raó: Sense definir'):
    guild = ctx.guild
    guild_icon = ctx.guild.icon_url
    author_name = ctx.author
    author_icon = author_name.avatar_url
    embed = discord.Embed(title=f"{user} ha sigut banejat!", description=f"{reason}", color=0xff2600)
    embed.set_author(name=f"{author_name}", icon_url=f"{author_icon}")
    embed.set_footer(text=f"{guild}", icon_url=f"{guild_icon}")
    await ctx.send(embed=embed)
    await user.ban(reason=reason)
    embed2 = discord.Embed(title="<:greenTick:714072192358416474> **Usuari banejat!**", color=0x212227)
    await ctx.send(embed=embed2)
    await asyncio.sleep(1.5)
    await ctx.channel.purge(limit=1, check=is_bot)

# Ban Error 
@ban.error
async def ban_error(ctx, error):
	embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova si tú i el bot teniu el permís `Ban Users` i que els arguments siguin correctes.** (`zz!help`)", colour=0x212227)
	await ctx.send(embed=embed)

###########################################    COMANDAMENTS SENSE ACABAR    ##########################################

"""@client.command()
async def mute(ctx, user: discord.Member, *, reason):
    role = discord.utils.get(ctx.guild.roles, name='Silenciat') 
    if role == None:
        perms = discord.Permissions(send_messages=False, speak=False)
        await ctx.guild.create_role(name='Silenciat', permissions=perms)
    else:
        user.add_role(name='Silenciat')
        role_position = role.position"""


"""@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member, *, reason='Raó: Sense definir'):
    role = discord.utils.get(ctx.guild.roles, name='Silenciat') 
    guild = ctx.guild
    guild_icon = ctx.guild.icon_url
    author_name = ctx.author
    author_icon = author_name.avatar_url
    embed = discord.Embed(title="Has sigut silenciar!", description=f"{reason}", color=0xff2600)
    embed.set_author(name=f"{author_name}", icon_url=f"{author_icon}")
    embed.set_footer(text=f"{guild}", icon_url=f"{guild_icon}")
    await user.send(embed=embed)
    if role == None:
        perms = discord.Permissions(send_messages=False, speak=False)
        await ctx.guild.create_role(name='Silenciat', permissions=perms)
    await user.add_roles(role)
    embed2 = discord.Embed(title="<:greenTick:714072192358416474> **Usuari silenciat!**", color=0x212227)
    await ctx.send(embed=embed2)"""


###########################################
@client.command()                        ##
@commands.is_owner()                     ##
async def guilds(ctx):                   ##
    await ctx.author.send(client.guilds) ##
###########################################

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print("Cog Loaded!")


TOKEN = str(os.environ.get("TOKEN"))
client.run(TOKEN)
