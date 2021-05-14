
import asyncio
import requests
import json
import os
import discord
import libneko
import datetime
from datetime import datetime
from libneko import pag
from discord.ext import commands

URBAN_API_KEY = os.getenv('URBAN_API_KEY')

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx,  user: discord.Member, *, reason="No reason provided"):   
        if ctx.author.top_role > user.top_role or ctx.author == ctx.guild.owner:
            if user == ctx.author:
                return await ctx.send("***:no_entry: You can't softban yourself...***")
           
            kick = discord.Embed(title=f":boom: User Kicked:", description=f"**{user}** Was Just Kicked", color=0x2f3136)
            kick.set_footer(text = f"Kicked by: {ctx.author}")
            kick.set_thumbnail(url = user.avatar_url)
            await ctx.channel.send(embed=kick)
            await user.send(embed=kick)
            await user.kick(reason=reason)
    @kick.error 
    async def kick_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have `Kick Permissions` To Use This Command!*", color=0x2f3136)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You Must `Mention` A User To Kick!*", color=0x2f3136)
            await ctx.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx,  user: discord.Member, *, reason="No reason provided"):   
        if ctx.author.top_role > user.top_role or ctx.author == ctx.guild.owner:
            if user == ctx.author:
                return await ctx.send("***:no_entry: You can't softban yourself...***")
           
            ban = discord.Embed(title=f":boom: User Banned:", description=f"**{user}** Was Just Banned", color=0x2f3136)
            ban.set_footer(text = f"Banned by: {ctx.author}")
            ban.set_thumbnail(url = user.avatar_url)
            await ctx.channel.send(embed=ban)
            await user.send(embed=ban)
            await user.ban(reason=reason)
    @ban.error 
    async def ban_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have `Ban Permissions` To Use This Command!*")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You Must `Mention` A User To Ban!*")
            await ctx.send(embed=embed)
            
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command(aliases=['sb'])
    async def softban(self, ctx, user : libneko.converters.InsensitiveMemberConverter, *, reason=None):
        """
        Bans and unbans the user, so their messages are deleted
        """
        if ctx.author.top_role > user.top_role or ctx.author == ctx.guild.owner:
            if user == ctx.author:
                return await ctx.send("***:no_entry: You can't softban yourself...***")
            ban = discord.Embed(title=f":boom: User Banned:", description=f"**{user}** Was Just Banned", color=0x2f3136)
            ban.set_footer(text = f"Banned by: {ctx.author}")
            ban.set_thumbnail(url = user.avatar_url)
            await ctx.channel.send(embed=ban)
            await user.send(embed=ban)
            await user.ban(reason=reason)
            await user.unban()
    @softban.error 
    async def softban_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have `Ban Permissions` To Use This Command!*", color=0x2f3136)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You Must `Mention` A User To Ban!*", color=0x2f3136)
            await ctx.send(embed=embed)


    @commands.bot_has_permissions(ban_members=True)
    @commands.guild_only()
    @commands.command(aliases=["banlist"])
    async def bans(self, ctx):
        """See a list of banned users in the guild"""
        try:
            bans = await ctx.guild.bans()
        except:
            return await ctx.send("You dont have the perms to see bans.")

        banned = ""

        @pag.embed_generator(max_chars=2048)
        def det_embed(paginator, page, page_index):
            em = discord.Embed(title = f"List of Banned Members:", description=page, color=0x2f3136)
            em.set_footer(text=f"{len(bans)} Members in Total.")
            return em

        page = pag.EmbedNavigatorFactory(factory=det_embed)

        for users in bans:
            banned += f"{users.user}\n"

        page += banned
        page.start(ctx)
    @bans.error 
    async def bans_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have `Ban Permissions` To Use This Command*.", color=0x2f3136)
            await ctx.send(embed=embed)

    @commands.bot_has_permissions(ban_members=True, view_audit_log=True)
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    @commands.command(aliases=["idban"])
    async def iban(self, ctx, userid: int, *, reason = None):
        """Ban someone not in the server"""
        try:
            await ctx.guild.ban(discord.Object(userid), reason = reason)
        except:
            success = False
        else:
            success = True

        if success:
            async for entry in ctx.guild.audit_logs(
                limit = 1, user = ctx.guild.me, action = discord.AuditLogAction.ban
           ):
                emb = await self.format_mod_embed(ctx, entry.target, success, "hackban")
        else:
            emb = await self.format_mod_embed(ctx, userid, success, "hackban")
        await ctx.send(embed = emb)

    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1000):
      if amount > 1000:
            await ctx.send('For safety reasons, i refuse to delete any message thats over 1k!')
            return
      await ctx.channel.purge(limit=amount + 1)
      await ctx.send(f"`{ctx.author}` cleared `{amount}` messages in `{ctx.message.channel}`", delete_after=5)
    @purge.error 
    async def purge_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have ``Permissions`` to purge!*", color=0x2f3136)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You Must `Provice` An amount of messages to purge!*", color=0x2f3136)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def lpurge(self, ctx, amount=100):
      async for msg in ctx.message.channel.history(limit=amount):
        if 'http' in msg.content:
            await msg.delete()

    @commands.command(aliases = ['channelnuke', 'nchan', 'nukechan'])
    @commands.has_permissions(manage_channels=True)		  
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        embed = discord.Embed(description=f"**:boom: Boom!**", color=0x2f3136)

        embed.add_field(name=f"**Nuked:**", value=f"Channel **{ctx.channel.name}** has been nuked!\n \n", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/777652819700088892/777965574781272125/giphy_4.gif")
        embed.set_footer(text=f'Channel nuked by {ctx.author}')
        channel = channel or ctx.channel
        position = channel.position
        newchannel = await channel.clone(reason=f"Chat Nuked by {ctx.author}")
        await channel.delete()
        await newchannel.edit(position=position)
        await newchannel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, reason=None):
        if not member:
            await ctx.send("`You forgot to mention a user!`")
            return
        await ctx.author.guild.create_role(name="Muted By Drain")
        role = discord.utils.get(ctx.guild.roles, name="protection-mute")
        await member.send(f"You were muted in {ctx.guild} by ``{ctx.author}`` for the reason: `{reason}`")
        await member.add_roles(role)
        await ctx.send(f"`{member.name}#{member.discriminator}` was muted by `{ctx.author}`.")
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to mute people")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None, reason=None):
        if not member:
            await ctx.send("`You forgot to mention a user!`")
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted B Drain")
        await member.send(f"You were unmuted in {ctx.guild} by ``{ctx.author}``")
        await member.remove_roles(role)
        await ctx.send(f"`{member.name}#{member.discriminator}` was unmuted by `{ctx.author}`.")
    @mute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You are not allowed to unmute people`")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def block(self, ctx, user: discord.Member=None):
        if not user:
            await ctx.send("Please specify a member")
            return
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f"`{user.name}#{user.discriminator}` was blocked by `{ctx.author}`.")
    @block.error
    async def block_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to block people!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblock(self, ctx, user: discord.Member=None):
        if not user:
            await ctx.send("Please specify a member")
            return
        await ctx.channel.set_permissions(user, send_messages=None)
        await ctx.send(f"`{user.name}#{user.discriminator}` was unblocked by `{ctx.author}`.")
    @block.error
    async def unblock_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to unblock people!")

      
