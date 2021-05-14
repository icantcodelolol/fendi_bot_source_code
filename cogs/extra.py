from discord.ext import commands
import datetime
import discord
import os
start_time = datetime.datetime.utcnow()

class extra(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.group(invoke_without_command=True)
  async def help(sef, ctx):
    embed = discord.Embed(description=f"[click here to add fendi](https://discord.com/api/oauth2/authorize?client_id=804567395124904006&permissions=8&scope=bot)\n`Categories`", color=0x2f3136)


    embed.add_field(name="**— ADMIN**", value="`displays the admin commands`", inline=False)
    embed.add_field(name="**— FUN**", value="`displays the fun commands`", inline=False)
    embed.add_field(name="**— IMAGE**", value="`displays the image commands `", inline=False)
    embed.add_field(name="**— SERVER**", value="`displays the server commands`", inline=False)
    embed.add_field(name="**— NSFW**", value="`displays the nsfw commands`", inline=False)
    embed.add_field(name="**— MISC**", value="`displays the misc commands`", inline=False)
    embed.set_author(name="Fendi", url="https://discord.gg/hB4Vmygqza")
    embed.set_footer(text=f"Use >help [category] before every command | prefix: > | 6 Categories | ")

    await ctx.send(embed=embed)

    




  @help.command()
  async def fun(self, ctx):
    embed = discord.Embed(description=f"**Fun Commands!**", color=0x2f3136)


    embed.add_field(name=f"**— howgay**", value="`shows how gay a mentioned user is`", inline=False)
    embed.add_field(name=f"**— slots**", value="`idek what this command is`", inline=False)
    embed.add_field(name=f"**— penis**", value="`shows how long someone penis is`", inline=False)
    embed.add_field(name=f"**— av**", value="`shows a mentioned users avatar`", inline=False)
    embed.add_field(name=f"**— meme**", value="`shows a meme`", inline=False)
    embed.add_field(name=f"**— snipe**", value="`snipes a deleted messsage`", inline=False)
    embed.add_field(name=f"**— esnipe**", value="`snipes a edited message`", inline=False)
    embed.set_footer(text='Category: Fun | Commands (7)')
    await ctx.send(embed=embed)

  @help.command()
  async def misc(self, ctx):
    embed = discord.Embed(description=f"**Misc Commands**", color=0x2f3136)

    embed.add_field(name=f"**— uptime**", value="`shows how long the bot has been up for`", inline=False)
    embed.add_field(name=f"**— about**", value="`info about the bot`", inline=False)
    embed.add_field(name=f"**— ping**", value="`shows the bots ping`", inline=False)
    embed.add_field(name=f"**— invite**", value="`sends a the bot invite and server support in dms`", inline=False)
    embed.add_field(name=f"**— bots**", value="`tells how many bots there is in the server`", inline=False)
    embed.add_field(name=f"**— urban**", value="`searches for a word in the urban dictionary`", inline=False)
    embed.add_field(name=f"**— members**", value="`shows how members there is in the server`", inline=False)
    embed.set_footer(text="Category: Misc | Commands (7)")
    await ctx.send(embed=embed)

  @help.command()
  async def server(self, ctx):
    embed = discord.Embed(description=f"**Server Commands**", color=0x2f3136)

    embed.add_field(name=f"**— serverinfo**", value="`shows info about a guild`", inline=False)
    embed.add_field(name=f"**— whois**", value="`shows info about a member`", inline=False)
    embed.add_field(name=f"**— servericon**", value="`shows the servericon`", inline=False)
    embed.add_field(name=f"**— roleinfo**", value="`tells info about a role`", inline=False)
    embed.set_footer(text="Category: Server | Commands (4)")
    await ctx.send(embed=embed)

  @help.command()
  async def admin(self, ctx):
    embed = discord.Embed(description=f"**Moderation Commands**", color=0x2f3136)

    embed.add_field(name=f"**— kick**", value="`kicks a mentioned user from the server`", inline=False)
    embed.add_field(name=f"**— ban**", value="`bans a mentioned user from the server`", inline=False)
    embed.add_field(name=f"**— softban**", value="`softbans a mentioned user from the server`", inline=False)
    embed.add_field(name=f"**— bans**", value="`shows bans list`", inline=False)
    embed.add_field(name=f"**— idban**", value="`bans a spacific user with their id`", inline=False)
    embed.add_field(name=f"**— purge**", value="`purges messages up to 1k`", inline=False)
    embed.add_field(name=f"**— lpurge**", value="`purges messages up to 100`", inline=False)
    embed.add_field(name=f"**— nuke**", value="`nukes a channel and resets everything`", inline=False)
    embed.add_field(name=f"**— mute**", value="`mutes a mentioned user and it will tell them in dm`", inline=False)
    embed.add_field(name=f"**— unmute**", value="`unmutes a mentioned user and it will tell them in dms`", inline=False)
    embed.add_field(name=f"**— block**", value="`blocks a spacific user from using this bot`", inline=False)
    embed.add_field(name=f"**— unblock**", value="`unblocks a user`", inline=False)
    embed.set_footer(text=f"Category: Admin | Commands (12)")
    await ctx.send(embed=embed)

  @help.command()
  async def nsfw(self, ctx):
    embed = discord.Embed(description=f"**NSFW Commands**", color=0x2f3136)

    embed.add_field(name=f"**— hentai**", value="`sends hot hentai`", inline=False)
    embed.add_field(name=f"**— tits**", value="`sends tit pics`", inline=False)
    embed.add_field(name=f"**— boobs**", value="`sends anime boobs`", inline=False)
    embed.add_field(name=f"**— les**", value="`sends lesbian shit`", inline=False)
    embed.set_footer(text=f"Category: NSFW | Commands (4)")
    await ctx.send(embed=embed)

  @help.command()
  async def image(self, ctx):
    embed = discord.Embed(description=f"**Image Commands**", color=0x2f3136)

    embed.add_field(name=f"**— kiss**", value="`go ahead nd kiss someone`", inline=False)
    embed.add_field(name=f"**— tickle**", value="`theres always a time to laugh`", inline=False)
    embed.add_field(name=f"**— hug**", value="`everyone loves hugs`", inline=False)
    embed.add_field(name=f"**— slap**", value="`fuck up`", inline=False)
    embed.add_field(name=f"**— cat**", value="`send a random cute cat image`", inline=False)
    embed.add_field(name=f"**— fox**", value="`sends a random cute fox image`", inline=False)
    embed.add_field(name=f"**— dog**", value="`sends a random cute dog image`", inline=False)
    embed.add_field(name=f"**— pet**", value="`we all like pets`", inline=False)
    embed.add_field(name=f"**— feed**", value="`everyone always needs to eat`", inline=False)
    embed.add_field(name=f"**— pat**", value="`everyone loves pats on there head`", inline=False)
    embed.set_footer(text=f"Category: Image | Commands (10)")
    await ctx.send(embed=embed)

