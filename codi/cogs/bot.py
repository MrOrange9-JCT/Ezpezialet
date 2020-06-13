import discord
import asyncio
from discord.ext import commands

MD = discord.Embed(title="**<:greenTick:714072192358416474> Mira els missatges directes!**", descripton="\u200b", colour=0x212227)
embed_color = 0x8404FC


class Bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    def is_bot(m):
        return m.author == self.client.user
    
    # zz!ping
    @commands.command()
    async def ping(self, ctx):
        ping = self.client.latency
        embed=discord.Embed(title=f"**:ping_pong: Pong!**\n`{round(ping * 1000)} ms`", color=embed_color)
        await ctx.send(embed=embed)

    # zz!help
    @commands.command()
    async def help(self, ctx, pag='home'):
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
            embed2.add_field(name="zz!echo / say <missatge>", value="Repeteix el teu missatge.", inline=False)
            embed2.add_field(name="zz!gat", value="Mostra una imatge d'un gat", inline=False)
            embed2.add_field(name="zz!gos", value="Mostra una imatge d'un gos", inline=False)
            
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
    @commands.command()
    async def developer(self, ctx):
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
        await ctx.channel.purge(limit=6, check=is_bot)


    # zz!info
    @commands.command()
    async def info(self, ctx, language='home'):
        bot_guilds = len(self.client.guilds)
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

            embed.add_field(name=":no_bell: Statuses", value="<:statusDND:714072192890961970> **Bot in maintenance**\n<:statusIdle:714072406867574815> **Bot in testing**\n<:statusOnline:714072197072683038> **All is working fine**\n<:7389_streaming:721297372059271208> **Just purple status**\n<:statusOffline:714072193344208938> **Bot not working**", inline=False)
            embed.add_field(name="<:discordbotlist:338808864352763904> Top.gg link (invite)", value="[Click Here](https://top.gg/bot/553883586210562060)", inline=False)
            embed.add_field(name="<:githublogo:720620633632800779> Github (Catalan)", value="[Click Here](https://github.com/MrOrange9-JCT/Ezpezialet)", inline=False)
            embed.add_field(name="<:python:553255078052757554> Python version ", value="3.8.2", inline=False)
            embed.set_footer(text="📚 Library: discord.py 1.3.3")
            await ctx.send(embed=embed)

        if language == 'català':
            embed2=discord.Embed(title="Informació del bot <:flag_cat:714094535340457994> <:flag_val:714094604156141638> :flag_ad:", description="L'informació de Ezpezialet (Català)", color=0xfffb00)
            embed2.set_author(name="👑 Creador: MrOrange9_JCT#9999", icon_url="https://images-ext-2.discordapp.net/external/03DuK9mIngzpX9yLWieJXKLi8sBCcQfNKjOhp3n95QM/%3Fsize%3D256/https/cdn.discordapp.com/avatars/449992158729076746/b50b00cc16ccbf9a72686f3d8e6b4450.png")
            embed2.set_thumbnail(url='https://icons.iconarchive.com/icons/custom-icon-design/flatastic-1/512/information-icon.png')
            embed2.add_field(name=":speaking_head: Idioma", value="L'idioma del cot és el [català](https://en.wikipedia.org/wiki/Catalan_language)", inline=False)
            embed2.add_field(name=":question: Comandament d'ajuda (Llista de comandaments)", value="zz!help", inline=False)
            embed2.add_field(name=":sos: Ajudant de desenvoloupament", value="SpaceCowboy#8914", inline=False)
            embed2.add_field(name=":grey_exclamation: Prefix del bot", value="`zz!`", inline=False)
            embed2.add_field(name="<:bot:714072191968346163> Nombre de servidors", value=f"{bot_guilds}", inline=False)

            embed2.add_field(name=":no_bell: Estats", value="<:statusDND:714072192890961970> **Bot en manteniment**\n<:statusIdle:714072406867574815> **Bot en proves**\n<:statusOnline:714072197072683038> **Tot funciona correctament**\n<:7389_streaming:721297372059271208> **Res, estat lila, que mola**\n<:statusOffline:714072193344208938> **Bot no funciona**", inline=False)
            embed2.add_field(name="<:discordbotlist:338808864352763904> Top.gg (invitació)", value="[Clic Aquí](https://top.gg/bot/553883586210562060)", inline=False)
            embed2.add_field(name="<:githublogo:720620633632800779> GitHub (Catalan)", value="[Clic Aquí](https://github.com/MrOrange9-JCT/Ezpezialet)", inline=False)
            embed2.add_field(name="<:python:553255078052757554> Versió de python", value="3.8.2", inline=False)
            embed2.set_footer(text="📚 Llibreria: discord.py 1.3.3")
            await ctx.send(embed=embed2)


def setup(client):
    client.add_cog(Bot(client))
