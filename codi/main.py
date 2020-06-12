import discord
import random
import asyncio
import pyfiglet
import png
import pyqrcode
import jishaku
import re
from datetime import datetime
from itertools import cycle
from discord.ext import commands, tasks
import os 


client = commands.Bot(command_prefix=['zz!', 'zz! ', '<@553883586210562060> '])
client.remove_command('help')
status = cycle(["Atenció! Canvi de prefix! (zz!)"])
#status = cycle(["MrOrange9 JCT en Twitch", "a una persona (no tapes tu webcam)", "el comandament zz!help", "que fa zz!giveyouup"])
MD = discord.Embed(title="**<:greenTick:714072192358416474> Mira els missatges directes!**", descripton="\u200b", colour=0x212227)
embed_color = 0x8404FC

client.load_extension("jishaku")

def is_bot(m):
    return m.author == client.user


###########################################    EVENTS    ##########################################

@client.event
async def on_command_error(ctx, error):
    print(str(error))
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
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=(next(status))))


###########################################    COMANDAMENTS DEL BOT    ##########################################

# zz!ping
@client.command()
async def ping(ctx):
    ping = client.latency
    embed=discord.Embed(title=f"**:ping_pong: Pong!**\n`{round(ping * 1000)} ms`", color=embed_color)
    await ctx.send(embed=embed)

# zz!help
@client.command()
async def help(ctx, pag='home'):
    if pag == 'home':
        embed = discord.Embed(title="**Missatge d'ajuda**",
                            colour=embed_color)

        embed.set_author(name="El prefix és zz!",
                        icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flat_exclamation_icon_-_blue.svg/1024px-Flat_exclamation_icon_-_blue.svg.png")


        embed.set_thumbnail(url="http://sweetclipart.com/multisite/sweetclipart/files/question_mark_blue.png")
        embed.add_field(name="zz!help", value="Mostra aquest missatge.\n ", inline=False)
        embed.add_field(name="<:omegalul:710458865887477800> **Comandaments de diversió:**", value="`zz!help diversio`", inline=False)
        embed.add_field(name="**<:modBanHammer:714212161764982858> Comandaments de moderació:**", value="`zz!help moderacio`", inline=False)
        embed.add_field(name="**<:Monedacapek:551094485250080779> Comandaments de Čapek Maker:**", value="`zz!help capek`", inline=False)
        embed.add_field(name="**:robot: Comandaments del bot:**", value="`zz!help bot`", inline=False)
        embed.add_field(name="**<:serverIcon:716586717552967741> Comandaments d'utilitat (i servidor):**", value="`zz!help utilitat`", inline=False)

        await ctx.send(embed=embed)
    if pag == 'diversio':
        embed2 = discord.Embed(title="**Missatge d'ajuda (Diversió <:omegalul:710458865887477800>)**",
                            colour=embed_color)
        embed2.set_footer(text="Els \"<\" o \">\" no s'han de posar (parametres nessecaris) igualment amb els \"[\" o \"]\" (parametres opcionals)",  icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flat_exclamation_icon_-_blue.svg/1024px-Flat_exclamation_icon_-_blue.svg.png")
        embed2.add_field(name="zz!8ball <pregunta>", value="Respon una pregunta de si / no.", inline=False)
        embed2.add_field(name="zz!ascii <font> <text>", value="Genera un text ascii art a partir del text i font intruduïts. Llista de fonts disponibles [**AQUÍ**](http://www.figlet.org/examples.html) (posa \"default\" per la font pre-determinada).", inline=False)
        embed2.add_field(name="zz!coinflip", value="Tira una moneda virtual a l'aire!", inline=False)
        embed2.add_field(name="zz!f", value="Press F to pay respects.", inline=False)
        embed2.add_field(name="zz!giveyouup", value="Na na nananana na nannana nana. Millor em callo.", inline=False)
        embed2.add_field(name="zz!echo <missatge>", value="Repeteix el teu missatge.", inline=False)
        
        await ctx.send(embed=embed2)

    if pag == 'moderacio':
        embed3 = discord.Embed(title="**Missatge d'ajuda (Moderació <:modBanHammer:714212161764982858>)**",
                            colour=embed_color)
        embed3.set_footer(text="Els \"<\" o \">\" no s'han de posar (parametres nessecaris) igualment amb els \"[\" o \"]\" (parametres opcionals)",  icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flat_exclamation_icon_-_blue.svg/1024px-Flat_exclamation_icon_-_blue.svg.png")
        embed3.add_field(name="zz!clear <nombre de missates a borrar>", value="`Requereix: Manage Messages`\nBorrar \"x\" missatges a la vegada", inline=False)
        embed3.add_field(name="zz!warn <@persona> [raó]", value="`Requereix: Kick Members`\nEl bot envia un missatge privat d'avís a la persona mencionada", inline=False)
        embed3.add_field(name="zz!kick <@persona> [raó]", value="`Requereix: Kick Members`\nEl bot expulsa del servidor a la persona mencionada", inline=False)
        embed3.add_field(name="zz!ban <@persona> [raó]", value="`Requereix: Ban Members`\nEl bot baneja del servidor a la persona mencionada", inline=False)        
        await ctx.send(embed=embed3)

    if pag == 'capek':
        embed4 = discord.Embed(title="**Missatge d'ajuda (Čapek Maker <:Monedacapek:551094485250080779>)**", description='Aquest comandaments estàn restringits per a Čapek Maker',
                            colour=embed_color)
        embed4.set_footer(text="Els \"<\" o \">\" no s'han de posar (parametres nessecaris) igualment amb els \"[\" o \"]\" (parametres opcionals)",  icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flat_exclamation_icon_-_blue.svg/1024px-Flat_exclamation_icon_-_blue.svg.png")
        embed4.add_field(name="zz!minecraft", value="Mostra informació del sever de minecraft **(Servidor Privat)**", inline=False)
        embed4.add_field(name="zz!titu", value="Ei titu!!", inline=False)
        await ctx.send(embed=embed4)

    if pag == 'bot':
        embed5 = discord.Embed(title="**Missatge d'ajuda (Bot :robot:)**",
                            colour=embed_color)
        embed5.set_footer(text="Els \"<\" o \">\" no s'han de posar (parametres nessecaris) igualment amb els \"[\" o \"]\" (parametres opcionals)",  icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flat_exclamation_icon_-_blue.svg/1024px-Flat_exclamation_icon_-_blue.svg.png")
        embed5.add_field(name="zz!ping", value="T'envia la latencia del bot.", inline=False)
        embed5.add_field(name="zz!developer", value="Estàs interesat en programar el bot?", inline=False)
        embed5.add_field(name="zz!info", value="Mostra informació sobre el bot", inline=False)
        await ctx.send(embed=embed5)
    if pag == 'utilitat':
        embed6 = discord.Embed(title="**Missatge d'ajuda (Uitlitat i servidor <:serverIcon:716586717552967741>)**", colour=embed_color)
        embed6.set_footer(text="Els \"<\" o \">\" no s'han de posar (parametres nessecaris) igualment amb els \"[\" o \"]\" (parametres opcionals)",  icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flat_exclamation_icon_-_blue.svg/1024px-Flat_exclamation_icon_-_blue.svg.png")
        embed6.add_field(name="zz!qr <text>", value="Genera un codi QR a partir del text intruduït", inline=False)
        embed6.add_field(name="zz!morsificar <text>", value="Tradueix el text intruduït a codi morse.", inline=False)
        embed6.add_field(name="zz!google <cerca>", value="Cerca alguna cosa al google.", inline=False)
        embed6.add_field(name="zz!rannum / randomnumber <num1> <num2>", value="Nombre aleatori entre num1 i num2.", inline=False)
        embed6.add_field(name="zz!ui / infousuari [usuari]", value="Mostra informació sobre un usuari. (Si no es posa un usuari, mostra informació teva)", inline=False)
        embed6.add_field(name="zz!embed <títol> | <descripció> | <color> | [mostrarautor] | [mostrardata]", value="**Important: S'ha de posar `|` per separar els parametres**\nGenera un missatge embed, ideal per a servidors. Per fer una nova línia s'ha de posar \" \\n \" \n Llista de colors disponibles [**AQUÍ**](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e#file-discord-colour-md) Markdown: https://docs.discord.club/embedg/reference/markdown", inline=False)
        await ctx.send(embed=embed6)

# zz!developer
@client.command()
async def developer(ctx):
    dev = discord.Embed(title="**Bot Developer**", description="Vols colaborar amb el bot? Mira això", colour=0x336699)


    dev.set_author(name="Això es una prova si veig que no funciona es treurà.", icon_url="https://media.discordapp.net/attachments/662994134763700267/670645503037407243/image0.png")
    dev.set_footer(text="Estàs llest? Envia un MD al @MrOrange9_JCT#3363", icon_url="https://media.discordapp.net/attachments/662994134763700267/670645503037407243/image0.png")

    dev.set_thumbnail(url="https://i.imgur.com/RPrw70n.png")

    dev.add_field(name="Requisits:", value="\u200b",  inline=False)

    dev.add_field(name="Saber una mica de Python.", value="Si no en saps podràs donar idees però no programar-les", inline=False)

    dev.add_field(name="Provar altres bots.", value="Has de provar alguns bots, al servidor de Capek en tenim uns quants", inline=False)

    await ctx.author.send(embed=dev)

    await ctx.send(embed=MD)
    await asyncio.sleep(1.5)
    await ctx.channel.purge(limit=1, check=is_bot)

# zz!info
@client.command()
async def info(ctx, language='home'):
    bot_guilds = len(client.guilds)
    if language == 'home':
        embedhome=discord.Embed(title="Bot Info", description="", color=embed_color)
        embedhome.add_field(name=":flag_gb: :flag_us: English", value="`zz!info english`", inline=False)
        embedhome.add_field(name="<:flag_cat:714094535340457994> <:flag_val:714094604156141638> :flag_ad: Català", value="`zz!info català` - **AMB ACCENT**", inline=False)
        embedhome.set_thumbnail(url='https://icons.iconarchive.com/icons/custom-icon-design/flatastic-1/512/information-icon.png')
        await ctx.send(embed=embedhome)

    if language == 'english':
        embed=discord.Embed(title="Bot Info :flag_gb: :flag_us:", description="The information of Ezpezialet (English)", color=0xff0000)
        embed.set_author(name="👑 Owner: MrOrange9_JCT#9999", icon_url="https://images-ext-2.discordapp.net/external/03DuK9mIngzpX9yLWieJXKLi8sBCcQfNKjOhp3n95QM/%3Fsize%3D256/https/cdn.discordapp.com/avatars/449992158729076746/b50b00cc16ccbf9a72686f3d8e6b4450.png")
        embed.set_thumbnail(url='https://icons.iconarchive.com/icons/custom-icon-design/flatastic-1/512/information-icon.png')
        embed.add_field(name=":speaking_head: Language", value="The bot’s language is [catalan](https://en.wikipedia.org/wiki/Catalan_language)", inline=False)
        embed.add_field(name=":question: Help Command (Command list)", value="zz!help", inline=False)
        embed.add_field(name=":sos: Bot Development Helper", value="SpaceCowboy#8914", inline=False)
        embed.add_field(name=":grey_exclamation: Bot Prefix", value="`zz!`", inline=False)
        embed.add_field(name="<:bot:714072191968346163> Number of guilds in", value=f"{bot_guilds}", inline=False)

        embed.add_field(name=":no_bell: Statuses", value="<:statusDND:714072192890961970> **Bot in maintenance**\n<:statusIdle:714072406867574815> **Bot in testing**\n<:statusOnline:714072197072683038> **All is working fine**\n<:statusOffline:714072193344208938> **Bot not working**", inline=False)
        embed.add_field(name="<:discordbotlist:338808864352763904> Top.gg link (invite)", value="[Click Here](https://top.gg/bot/553883586210562060)", inline=False)
        embed.add_field(name="<:githublogo:720620633632800779> Github (Catalan)", value="[Click Here](https://github.com/MrOrange9-JCT/Ezpezialet)", inline=False)
        embed.add_field(name="<:python:553255078052757554> Python version ", value="3.8.2", inline=False)
        embed.set_footer(text="📚 Library: discord.py 1.3.3")
        await ctx.send(embed=embed)

###########################################    COMANDAMENTS DE DIVERSIÓ    ##########################################

# zz!8ball
@client.command(aliases=['8ball'])
async def eightball(ctx, *, ques):
    responses = ['És clar que sí!',
                 'Sip',
                 'Sense dubtes',
                 'Sí - definitivament.',
                 'Segurament que si.',
                 'Com estic veient... Sí.',
                 'Clarament',
                 'Sembla que sí',
                 'Sí.',
                 'Tot apunta a sí.',
                 'No se... Torna a provar!',
                 'Pregunta després.',
                 'Millor que no respongui...',
                 'No puc prediure ara mateix.',
                 'Concentra\'t i pregunta després.',
                 'No contis que sí...',
                 'La meva resposta és no.',
                 'Les meves fonts diuen que no.',
                 'Sembla que no.',
                 'Molt dubtós.', ]

    magic = discord.Embed(title=f'<:pregunta:713082769697407047> Pregunta: {ques}', descripton="\u200b", colour=embed_color)
    magic2 = discord.Embed(title=f'<:resposta:713082769390960652> Resposta: {random.choice(responses)}',
                           descripton="\u200b", colour=embed_color)
    await ctx.send(embed=magic)
    await ctx.send("<a:thin:670358155162681345>")
    await asyncio.sleep(2)

    
    await ctx.channel.purge(limit=1, check=is_bot)
    await ctx.send(embed=magic2)

# zz!f
@client.command()
async def f(ctx):
    author = ctx.author.mention
    await ctx.send(f"<:f_:554321687487840277> {author} ha pagat respectes.")

# zz!echo / say
@client.command(aliases=['say'])
async def echo(ctx, *, words=''):
    await ctx.send(words)

# zz!giveyouup
@client.command()
async def giveyouup(ctx):
    await ctx.send("Never gonna give " + (str(ctx.author.mention)) + " up\nNever gonna let " + (str(ctx.author.mention)) + " down\nNever gonna run around and desert " + (str(ctx.author.mention)) + " \nNever gonna make " + (str(ctx.author.mention)) + " cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt " + (str(ctx.author.mention)) + " \nNever gonna give " + (str(ctx.author.mention)) + " up\nNever gonna let " + (str(ctx.author.mention)) + " down\nNever gonna run around and desert " + (str(ctx.author.mention)) + " \nNever gonna make " + (str(ctx.author.mention)) + " cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt " + (str(ctx.author.mention)) + " \nNever gonna give " + (str(ctx.author.mention)) + " up\nNever gonna let " + (str(ctx.author.mention)) + " down\nNever gonna run around and desert " + (str(ctx.author.mention)) + " \nNever gonna make " + (str(ctx.author.mention)) + " cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt " + (str(ctx.author.mention)))

# zz!ascii
@client.command(aliases=['ascii'])
async def asciitext(ctx, font='default', *, input_text):
    if font == 'default':
        result = pyfiglet.figlet_format(f"{input_text}")
        await ctx.send(f"```{result}```")
    else:
        result = pyfiglet.figlet_format(f"{input_text}", font = f"{font}")
        await ctx.send(f"```{result}```")

# Ascii Error
@asciitext.error
async def ascii_error(ctx, error):
	embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova els arguments són correctes.**", description="[Llista de fonts](http://www.figlet.org/examples.html) | Posar \"default\" per a la font pre-determinada.", colour=0x212227)
	await ctx.send(embed=embed)

# zz!coinflip
@client.command()
async def coinflip(ctx):
        await ctx.send("<a:flip:670373222717587468>")
        
        await asyncio.sleep(3.5)
        await ctx.channel.purge(limit=1, check=is_bot)
        quotelist = ["cara", "creu"]

        if random.choice(quotelist) == "cara":
            choice = "cara"
            image = "https://media.discordapp.net/attachments/662994134763700267/670558104366219264/image0.gif"
        else:
            choice = "creu"
            image = "https://media.discordapp.net/attachments/662994134763700267/670558104601231380/image1.gif"
        coin = discord.Embed(title="\u200b", description=f"**Ha sortit {choice}!**", color=0x212227)
        coin.set_thumbnail(url=image)
        await ctx.send(embed=coin)


#################################    COMANDAMENTS DE CAPEK (No son per a un sevidor)    #################################

# zz!titu
@client.command()
async def titu(ctx):
    await ctx.send(":fire: Ei titu! Vaig a fer una barbacoa, pazza'm el flamizell. Ara te'l torno.. :fire:")

# zz!minecraft 
@client.command()
async def minecraft(ctx):
    minebed = discord.Embed(title="**Info Server Minecraft**", description="Informació del server de Minecraft:",
                            colour=discord.Color.green())

    minebed.set_author(name="Vols saber les coordenades de les ciutats? Ves als botons de TP del spawn!",
                       icon_url="https://cdn.discordapp.com/attachments/662994134763700267/669894359793008641/pngfuel.com.png")
    minebed.set_footer(
        text="Si petes algo, ban. Si poses bloques a algo, Ban. Si et mous, BAN. Si entres, **BAN**.\n Ok em calmo, la primera, es veritat",
        icon_url="https://cdn.discordapp.com/attachments/662994134763700267/669894359793008641/pngfuel.com.png")

    minebed.set_thumbnail(
        url="https://www.nocreasnada.com/wp-content/uploads/2019/09/2019-09-02_5d6cfd32c7b57_512dVKB22QL.png")

    minebed.add_field(name="IP", value="Contacta amb el @MrOrange9_JCT#3363", inline=False)
    minebed.add_field(name="Versió", value="1.15.1", inline=False)
    minebed.add_field(name="Móns",
                      value="world, Survival i Minigames",
                      inline=False)
    minebed.add_field(name="Permisos",
                      value="De moment no estàn configurats", inline=False)

    await ctx.author.send(embed=minebed)
    await ctx.send(embed=MD)
    await asyncio.sleep(1.5)
    await ctx.channel.purge(limit=1, check=is_bot)


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
    
    if 'mostrarautor' in splitted_input:
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)

# Embed Error
@embed.error
async def embed_error(ctx, error):
	embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova els arguments són correctes.** (`zz!help`)", description="[Llista de colors](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e#file-discord-colour-md)", colour=0x212227)
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
    embed = discord.Embed(title="{user} ha sigut banejat!", description=f"{reason}", color=0xff2600)
    embed.set_author(name=f"{author_name}", icon_url=f"{author_icon}")
    embed.set_footer(text=f"{guild}", icon_url=f"{guild_icon}")
    await ctx.send(embed=embed)
    await user.ban(reason=reason)
    embed2 = discord.Embed(title="<:greenTick:714072192358416474> **Usuari banejat!**", color=0x212227)
    await ctx.send(embed=embed2)
    await asyncio.sleep(1.5)
    await ctx.channel.purge(limit=1, check=is_bot)

# Ban kick_error   
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

TOKEN = str(os.environ.get("TOKEN"))
client.run(TOKEN)
