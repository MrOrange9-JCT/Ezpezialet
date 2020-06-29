import discord
import aiohttp
import asyncio
import pyfiglet
import random
from discord.ext import commands

MD = discord.Embed(title="**<:greenTick:714072192358416474> Mira els missatges directes!**", descripton="\u200b", colour=0x212227)
embed_color = 0x8404FC


class Diversio(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    # zz!8ball
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, ques):
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
        await ctx.send("<a:thin:670358155162681345>", delete_after=2)
        await asyncio.sleep(2)
        await ctx.send(embed=magic2)

    # zz!gat
    @commands.command()
    async def gat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow!")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)

    # zz!gos
    @commands.command()
    async def gos(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Woof!")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="http://random.dog/")

                    await ctx.send(embed=embed)

    # zz!f
    @commands.command()
    async def f(self, ctx):
        author = ctx.author
        embed = discord.Embed(title=f"<:f_:554321687487840277> {author} ha pagat respectes.", color=0x303136)
        embed.set_image(url="https://images-ext-1.discordapp.net/external/cMESiXzCOt8xPQqqxeWN43AhWL1X65d3URNqcYSYiq4/https/media.giphy.com/media/j6ZlX8ghxNFRknObVk/giphy.gif")
        await ctx.send(embed=embed)

    # zz!echo / say
    @commands.command(aliases=['say'])
    async def echo(self, ctx, *, words=''):
        await ctx.send(words)

    # zz!giveyouup
    @commands.command()
    async def giveyouup(self, ctx):
        await ctx.send("Never gonna give " + (str(ctx.author.mention)) + " up\nNever gonna let " + (str(ctx.author.mention)) + " down\nNever gonna run around and desert " + (str(ctx.author.mention)) + " \nNever gonna make " + (str(ctx.author.mention)) + " cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt " + (str(ctx.author.mention)) + " \nNever gonna give " + (str(ctx.author.mention)) + " up\nNever gonna let " + (str(ctx.author.mention)) + " down\nNever gonna run around and desert " + (str(ctx.author.mention)) + " \nNever gonna make " + (str(ctx.author.mention)) + " cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt " + (str(ctx.author.mention)) + " \nNever gonna give " + (str(ctx.author.mention)) + " up\nNever gonna let " + (str(ctx.author.mention)) + " down\nNever gonna run around and desert " + (str(ctx.author.mention)) + " \nNever gonna make " + (str(ctx.author.mention)) + " cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt " + (str(ctx.author.mention)))

    # zz!ascii
    @commands.command(aliases=['ascii'])
    async def asciitext(self, ctx, font='default', *, input_text):
        if font == 'default':
            result = pyfiglet.figlet_format(f"{input_text}")
            await ctx.send(f"```{result}```")
        else:
            result = pyfiglet.figlet_format(f"{input_text}", font = f"{font}")
            await ctx.send(f"```{result}```")

    # Ascii Error
    @asciitext.error
    async def ascii_error(self, ctx, error):
        embed = discord.Embed(title="**<:redTick:714072192681508885> Comprova els arguments són correctes.**", description="[Llista de fonts](http://www.figlet.org/examples.html) | Posar \"default\" per a la font pre-determinada.", colour=0x212227)
        await ctx.send(embed=embed)

    # zz!coinflip
    @commands.command()
    async def coinflip(self, ctx):
            await ctx.send("<a:flip:670373222717587468>", delete_after=3.5)
            
            await asyncio.sleep(3.5)

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

def setup(client):
    client.add_cog(Diversio(client))
