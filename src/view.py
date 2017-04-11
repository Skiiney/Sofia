import discord
from src.nsfw import boobs, butts, Rule34, Booru
from src.weather import Weather
import asyncio
import time
from datetime import datetime


client = discord.Client()

class OnJoin:
    def MemberJoin(member, member_avatar, avatar):
        server = member.server
        date = "{0.joined_at}".format(member).split('.')
        #embed
        em = discord.Embed(color=0xff0047)
        em.set_author(name="Welcome", url=em.Empty, icon_url=member_avatar)
        em.add_field(name="{0.name}".format(member), value='Joined: '+date[0].replace(' ',' | '))
        em.set_footer(text="Powered by Sofia.", icon_url=avatar)
        return server, em

class UnameView:
    def Uname(command, avatar):
        if command == '-r':
            return UnameView.R(avatar)
        elif command == '-s':
            return UnameView.S(avatar)
        elif command == '-o':
            return UnameView.O(avatar)
        elif command == '-m':
            return UnameView.M(avatar)
        elif command == '-n':
            return UnameView.N(avatar)

    def R(avatar):
        em = discord.Embed(color=0xff0047)
        em.add_field(name='Kernel Release', value='``1.0.0-0-SOFIA``', inline=True)
        em.set_footer(text='Powered by Discord.py', icon_url=avatar)
        return em
    def S(avatar):
        em = discord.Embed(color=0xff0047)
        em.add_field(name='Kernel Name', value='``discord.py``', inline=True)
        em.set_footer(text='Powered by Discord.py', icon_url=avatar)
        return em
    def O(avatar):
        em = discord.Embed(color=0xff0047)
        em.add_field(name='Operating System', value='``Python``', inline=True)
        em.set_footer(text='Powered by Discord.py', icon_url=avatar)
        return em
    def M(avatar):
        em = discord.Embed(color=0xff0047)
        em.add_field(name='Hardware Architecture', value='``x86_64``', inline=True)
        em.set_footer(text='Powered by Discord.py', icon_url=avatar)
        return em

    def N(avatar):
        em = discord.Embed(color=0xff0047)
        em.add_field(name='Nodename', value='``heroku``', inline=True)
        em.set_footer(text='Powered by Discord.py', icon_url=avatar)
        return em

class OnMessageView:
    def GoodMornigView(message):
        em = discord.Embed(color=0xff0047)
        em.add_field(name='Good Morning', value='``{0.author.name} said good morning to @everyone!``'.format(message), inline=True)
        em.set_footer(text='{0.author.name}'.format(message), icon_url=message.author.avatar_url)
        return em


    def BoobsView():
        model, url = boobs.GetSomeBoobs()
        em = discord.Embed(color=0xff0047)
        em.set_author(name='Boobs', url=em.Empty)
        em.add_field(name='Model: ', value=model, inline=True)
        em.set_image(url=url)
        em.set_footer(text='Powered by oboobs API.', icon_url=em.Empty)
        return em

    def ButtsView():
        url = butts.GetSomeButts()
        em = discord.Embed(color=0xff0047)
        em.set_author(name='Butts', url=em.Empty)
        em.set_image(url=url)
        em.set_footer(text='Powered by obutts API.', icon_url=em.Empty)
        return em

    def PingView(msg, avatar):

        em = discord.Embed(color=0xff0047)
        em.add_field(name='Ping', value=msg)
        em.set_footer(text='Powered by Sofia.', icon_url=avatar)
        return em

    def WeatherView(city, avatar,token):
        weather_status, temperature, wind, humidity = Weather.GetTemperature(city, token)
        em = discord.Embed(color=0xff0047)
        em.set_author(name='Weather.', url=em.Empty)
        em.add_field(name='Status:', value=weather_status)
        em.add_field(name='Temperature', value=temperature+' °C')
        em.add_field(name='Wind', value=wind+' km/h')
        em.add_field(name='Humidity', value=humidity+'%')
        em.set_footer(text='Powered by Sofia.', icon_url=avatar)
        return em

    def Rule34View(search, avatar):
        check, url = Rule34.GetSomeRule34(search)
        if check == False:
            em = discord.Embed(color=0xff0047)
            em.set_author(name='Rule 34.', url=em.Empty)
            em.add_field(name='Sorry, I can\'t find a image for:', value=search, inline=True)
            em.set_footer(text='Powered by rule34.xxx API.', icon_url=avatar)
            return em
        else:
            em = discord.Embed(color=0xff0047)
            em.set_author(name='Rule 34.', url=em.Empty)
            em.add_field(name='Character:', value=search, inline=True)
            em.set_image(url=url)
            em.set_footer(text='Powered by rule34.xxx API.', icon_url=avatar)
            return em
    def BooruView(search, avatar):
        check, url = Booru.GetSomeDanbooruImage(search)
        if check == False:
            em = discord.Embed(color=0xff0047)
            em.set_author(name='Danbooru.', url=em.Empty)
            em.add_field(name='Sorry, I can\'t find a image for:', value=search, inline=True)
            em.set_footer(text='Powered by Danbooru API.', icon_url=em.Empty)
            return em
        else:
            em = discord.Embed(color=0xff0047)
            em.set_author(name='Rule 34.', url=em.Empty)
            em.add_field(name='tag:', value=search+' ', inline=True)
            em.set_image(url=url)
            em.set_footer(text='Powered by rule34.xxx API.', icon_url=em.Empty)
            return em
