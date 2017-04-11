import discord
from src.nsfw import boobs, butts, Rule34, Booru
from src.weather import Weather
from src.view import OnMessageView, UnameView, OnJoin
from src.authentication import Authentication
import asyncio
import time
from datetime import datetime



client = discord.Client()
auth = Authentication()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself

    avatar = client.user.avatar_url
    if message.author == client.user:
        return

    if message.content.startswith('!s bd'):
        em = OnMessageView.GoodMornigView(message)
        await client.send_message(message.channel, '',embed=em)

    if message.content.startswith('uname'):
        command = message.content.replace('uname ','')
        em = UnameView.Uname(command,avatar)
        await client.send_message(message.channel, '',embed=em)

    if message.content.startswith('!s ping'):
        start = time.time()
        msg = '``Pong ``:ping_pong:'.format(message)
        em = OnMessageView.PingView(msg,avatar)
        m = await client.send_message(message.channel, ' ',embed=em)
        end = time.time()
        response_time = end - start
        msg = msg+'``%.2f ms``'% response_time
        em = OnMessageView.PingView(msg,avatar)
        await client.edit_message(m, ' ',embed=em)


    if message.content.startswith('!s -w'):
        if message.content.replace('!s -w','') == '':
            msg = 'Please insert your city name!'
            await client.send_message(message.channel, msg)
        else:
            city = message.content.replace('!s -w','')
            em = OnMessageView.WeatherView(city, avatar, auth.WeatherToken())
            await client.send_message(message.channel, '**This is the current weather forecast of '+city+'.**', embed=em)

    if message.content.startswith('!s -boobs'):
        em = OnMessageView.BoobsView()
        await client.send_message(message.channel, ' ',embed=em)

    if message.content.startswith('!s -butts'):
        em = OnMessageView.ButtsView()
        m = await client.send_message(message.channel, ' ',embed=em)

    if message.content.startswith('!s -d'):
        user_msg = message.content.replace('!s -d ','')
        if user_msg.isdigit():
            number = int(user_msg)
            if number > 100:
                await client.send_message(message.channel, 'The limit is 100 messages in a row.')
            else:
                await client.purge_from(message.channel, limit=number)
        else:
            await client.send_message(message.channel, 'Please, insert a valid number.')

    if message.content.startswith('!s -34'):
        search = message.content.replace('!s -34 ' ,'')
        em = OnMessageView.Rule34View(search, avatar)
        await client.send_message(message.channel, '', embed=em)

    if message.content.startswith('!s -booru'):
        search = message.content.replace('!s -booru ' ,'')
        em = OnMessageView.Rule34View(search, avatar)
        await client.send_message(message.channel, '', embed=em)

    if message.content.startswith('!s -r'):
        private = await client.start_private_message(message.author)
        msg = '**Hello! Nice to meet you, {0.author.mention}!** :smiley:\nPlease, tell me your name or how you like most to be called. ``(ex.: !s Sofia)``'.format(message)
        await client.send_message(private, msg)

        #Name
        def check(msg):
            return msg.content.startswith('!s')
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('!s'):].strip()
        print(name)

        #SO
        msg = 'What OS do you use? ``(ex.: !s Windows 7)``'.format(message)
        await client.send_message(message.channel, msg)
        message = await client.wait_for_message(author=message.author, check=check)
        operacional_system = message.content[len('!s'):].strip()
        print(operacional_system)

        #Game
        msg = 'What\'s your favorite game?``(ex.: !s Portal 2)``'.format(message)
        await client.send_message(message.channel, msg)
        message = await client.wait_for_message(author=message.author, check=check)
        game = message.content[len('!s'):].strip()
        print(game)

        #About
        msg = 'You seem to be interesting! :blush:\nTell me more about you. You hobbies, your personal likes and so on! ``(ex.: !s I play basketball at school. I like to programming and so on...)``'.format(message)
        await client.send_message(message.channel, msg)
        message = await client.wait_for_message(author=message.author, check=check)
        about = message.content[len('!s'):].strip()
        print(about)

        await client.send_message(message.channel, '{} is cool indeed!'.format(game))

        await client.send_message(message.channel, '**Let me put my goggles on and see if I read everything right...**'.format(game))

        user = '{0.author.mention}'.format(message)
        em = discord.Embed(color=0xff0047)
        em.set_author(name='About you', url=em.Empty)
        em.add_field(name="Your name:", value=name, inline=False)
        em.add_field(name="Your OS:", value=operacional_system, inline=False)
        em.add_field(name="Your favorite game:", value=game, inline=False)
        em.add_field(name="More about you:", value=about, inline=False)
        em.set_footer(text="Powered by Sofia.", icon_url=client.user.avatar_url)

        await client.send_message(message.channel, '', embed=em)

    if message.content.startswith('!s -h'):
        em = discord.Embed(color=0xff0047)
        em.set_author(name="Commands list.", url=em.Empty)
        em.add_field(name="Helpful commands", value="teste\naaa", inline=True)
        em.set_footer(text="Powered by Sofia.", icon_url=em.Empty)
        await client.send_message(m, '', embed=em)
    if message.content.startswith('!s -kitty'):
        em = OnMessageView.KittyView(avatar)
        m = await client.send_message(message.channel, ' ',embed=em)
@client.event
async def on_member_join(member):
    avatar = client.user.avatar_url
    member_avatar = member.avatar_url
    server, em = OnJoin.MemberJoin(member, member_avatar, avatar)
    await client.send_message(server, ' ',embed=em)

@client.event
async def on_member_remove(member):
    avatar = client.user.avatar_url
    member_avatar = member.avatar_url
    server = member.server
    date = "{0.joined_at}".format(member).split('.')
    date_now = str(datetime.now()).split('.')
    em = discord.Embed(color=0xff0047)
    em.set_author(name="{0.name}".format(member), url=em.Empty, icon_url=member.avatar_url)
    em.add_field(name="{0.name}".format(member), value='Joined: '+date[0].replace(' ',' , ')+"\nLeft: "+date_now[0].replace(' ',' , '))
    em.set_footer(text="Powered by Sofia.", icon_url=client.user.avatar_url)
    await client.send_message(server, ' ',embed=em)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(auth.DiscordToken())
