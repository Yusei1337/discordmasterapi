import discord
from discord.ext import commands
import datetime
from discord.utils import get
import youtube_dl
import os
import json
import shutil
import asyncio

TOKEN = 'BOT_TOKEN'

PREFIX = '>>'

bot = commands.Bot(command_prefix=PREFIX) #инициализируем бота с префиксом '>>'
bot.remove_command('help')


#Words
#hello_words = ['qq','hi','хай','ky','zdarova','privet','здарова','привет']
#answer_words = ['инфа','info','commands']
#godbye_words = ['bb','poka','я спать','пока','gl']

@bot.event

async def on_ready():
	print ('ONLINE')

	await bot.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game('  >>help ') )

@bot.listen()

async def on_message(message):
	print('Message from {0.author}: {0.content}'.format(message))

	


@bot.event
async def on_command_error (ctx, error):
	pass

#joining message
@bot.event
@commands.has_permissions (administrator = True)

async def on_member_join( member ):
	channel = bot.get_channel( 706569039245213726 )

	role = discord.utils.get (member.guild.roles, id = 706685775944876092)

	await member.add_roles( role )
	await channel.send(embed = discord.Embed (description = f'ZDAROVA DRUG ``{member.name}``, NE RADI TEBYA VIDETb', color = 0x0c0c0c ) )



#clear message
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)

async def purge( ctx, amount : int ):
	await ctx.channel.purge(limit= amount)
	await ctx.send(embed = discord.Embed(description = f':white_check_mark: Deleted {amount} messages', color = 0x0c0c0c))

#clear command
@bot.command(pass_context=True)

async def hello(ctx, amount = 1):
	await ctx.channel.purge (limit=amount)

	author = ctx.message.author
	await ctx.send(f'O4koWnik { author.mention }')

#kick
@bot.command(pass_context = True)
@commands.has_permissions (administrator = True)

async def kick (ctx, member: discord.Member,*, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.kick(reason = reason)
	await ctx.send(f'kick user { member.name}')

#ban
@bot.command(pass_context=True)
@commands.has_permissions (administrator = True)

async def ban(ctx, member: discord.Member, *, reason=None):
	emb = discord.Embed (title = 'BANN4eLLo Ebana', color = discord.Color.red() )
	await ctx.channel.purge (limit=1)

	await member.ban (reason = reason)

	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field(name = 'Token Bana ',value = 'Dosvidaniya (BAN) : {}'.format ( member.mention ) )
	emb.set_footer (text = 'Poly4iL v Ebas0siny ot {}'. format( ctx.author.name), icon_url = ctx.author.avatar_url)

	await ctx.send (embed = emb)

	#await ctx.send(f'Ban user {member.mention}')

#unban
@bot.command (pass_context=True)
@commands.has_permissions (administrator = True)

async def unban(ctx,*,member):
	await ctx.channel.purge(limit = 1)

	emb = discord.Embed (title = 'Razban Ebana', color = discord.Color.green() )
	#emb.set_author( name = member.name, icon_url = member.avatar_url )
	#emb.add_field(name = 'Token Bana ',value = 'Razban: {}'.format ( member.mention ) )
	emb.set_footer (text = 'Razban ot admina {}'. format( ctx.author.name), icon_url = ctx.author.avatar_url)

	banned_users = await ctx.guild.bans()


	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)

		#await ctx.send(f'Unbanned user {user.mention}')

		await ctx.send (embed = emb)

		return


#Command help us
@bot.command(pass_context=True)
@commands.has_permissions (administrator = True)

async def help(ctx):
	emb = discord.Embed(title = 'Navigacia po komandam')

	emb.add_field(name='{}purge'.format(PREFIX), value ='Clear Shit 👅')   #Добавить смайлик - DONE
	emb.add_field(name ='{}ban'.format(PREFIX), value = 'Ban bitches 👺')  #Добавить смайлик - DONE
	emb.add_field(name= '{}kick'.format(PREFIX), value = 'Kick rats 👁')   #Добавить смайлик - DONE
	emb.add_field(name='{}unban'.format(PREFIX), value= 'Unban Losers 🖕') #Добавить смайлик  - DONE
	emb.add_field(name='{}hello'.format(PREFIX), value = 'FUCK U 🤬')     #Добавить смайлик  - DONE
	emb.add_field(name='{}time'.format(PREFIX), value = 'VREMYA NAHOY 👨‍🦽') #Добавить смайлик - DONE
	emb.add_field(name='{}spam'.format(PREFIX), value = 'spam for friends 👨‍')
	emb.add_field(name='{}play'.format(PREFIX), value = '[URL] ONLY YOUTUBE add music to bot 🎵')
	emb.add_field(name='{}join (until >>play,'.format(PREFIX), value = 'bot connect to voice channel [TO YOU] 🔔')
	emb.add_field(name='{}leave'.format(PREFIX), value = 'bot say: FUCK U and leave from channel 🔕')
	emb.add_field(name='{}skip'.format(PREFIX), value = '[IN DEBUG] skip ON Playing music and start NEW ⏱') # TO FIX
	emb.add_field(name='{}pause'.format(PREFIX), value = 'pause playing music 🔈')
	emb.add_field(name='{}resume'.format(PREFIX), value = 'resumed played music 🔊')
	emb.add_field(name='{}stop'.format(PREFIX), value = 'stop playing music ⚠️')
	emb.add_field(name='{}mute'.format(PREFIX), value = 'mute text chat 💬')


	await ctx.send( embed = emb )

#time 
@bot.command (pass_context=True)
@commands.has_permissions (administrator = True)

async def time (ctx):
	emb = discord.Embed( title = 'Allah govorit...', description  = 'ESLI VPADLY SMOTREtb NA 4aci ebanat', colour = discord.Color.red(), url ='https://time100.ru/Saint-Petersburg')

	emb.set_author( name = bot.user.name, icon_url = bot.user.avatar_url)
	emb.set_footer( text = 'AYE TEAM TY FOR USE <3', icon_url = ctx.author.avatar_url)
	emb.set_image( url = 'https://i.pinimg.com/originals/66/18/e1/6618e193bb9f88f8c69b05267ffdacf7.jpg')
	emb.set_thumbnail( url ='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRJgJ_A80MnOk0yrQxqHS-OdajDhCfPW4hofVtnqHQnCL6Sa0wu&usqp=CAU')

	now_date = datetime.datetime.now()
	abcd=format( now_date )
	abcd='DATA|TIME: '+abcd



	emb.add_field( name = 'VREMYA NAHOY', value = abcd[0:30] )

	await ctx.send( embed = emb)


#mute
@bot.command (pass_context=True)
@commands.has_permissions (administrator = True)

async def mute (ctx, member: discord.Member):
	await ctx.channel.purge (limit = 1)

	mute_role = discord.utils.get ( ctx.message.guild.roles, name = 'MUTED')

	await member.add_roles( mute_role )
	await ctx.send (f' {member.mention}, ograni4enie za narushenie pravil!')


#join|leave voice
@bot.command()
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send (embed = discord.Embed(description = f' {ctx.author.mention}, bot is connected to channel "{channel}" ', color = 0x0c0c0c) )

@bot.command()
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		
		await ctx.send (embed = discord.Embed(description = f' {ctx.author.mention}, bot leave from channel "{channel}" ', color = 0x0c0c0c) ) # FIX - STATUS FIXED

#music ON

@bot.command()
async def play(ctx, url: str):

	def check_queue():
		Queue_infile = os.path.isdir('./Queue')
		if Queue_infile is True:
			DIR = os.path.abspath(os.path.realpath('Queue'))
			length = len(os.listdir(DIR))
			still_q = length - 1
			try:
				first_file = os.listdir(DIR)[0]
			except:
				print('No more queued sond(s)')
				queues.clear()
				return
			main_location = os.path.dirname(os.path.realpath(__file__))
			song_path = os.path.abspath(os.path.realpath('Queue') + '\\' + first_file)
			if length != 0:
				print('Song done,playing next queued')
				print(f'Songs still in queue: {still_q}')
				song_there = os.path.isfile('song.mp3')
				if song_there:
					os.remove('song.mp3')
				shutil.move(song_path, main_location)
				for file in os.listdir('./'):
					if file.endswith('.mp3'):
						os.rename(file,'song.mp3')

				voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e:check_queue())
				voice.source = discord.PCMVolumeTransformer(voice.source)
				voice.source.volume = 0.09

			else:
				queues.clear()
				return
		else:
			queues.clear()
			print('No song were queued before the ending of the last song')


	song_there = os.path.isfile('song.mp3')
	try:
		if song_there:
			os.remove('song.mp3')
			queues.clear()
			print('[log] Старый файл удалён')
	except PermissionError:
		print('[log] Не удалось удалить файл')
		await ctx.send('Wait pls')
		return

	Queue_infile = os.path.isdir('./Queue')
	try:
		Queue_folder = './Queue'
		if Queue_infile is True:
			print('Removed old Queue Folder')
			shutil.rmtree(Queue_folder)
	except:
		print('No old Queue folder')


	voice = get(bot.voice_clients, guild = ctx.guild)

	ydl_opts = {
		'format' : 'bestaudio/best',
		'postprocessors': [{
  			'key': 'FFmpegExtractAudio',
  			'preferredcodec'  : 'mp3',
  			'preferredquality' : '192'		
		}],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print('[log] Загружаю музыку...')
		ydl.download([url])

	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			name = file
			print(f'[log] Переименовываю файл: {file}')
			os.rename(file, 'song.mp3')

	voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: check_queue())
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 0.09

	nname = name.rsplit('-', 2)
	await ctx.send(f'Playing: {nname[0]}')
	print('playing')

@bot.command(pass_context=True, aliases = ['pa', 'pau'])
async def pause(ctx):

	voice = get(bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_playing():
		print('Music pause')
		voice.pause()
		await ctx.send('Music paused')
	else:
		print('Music not playing failed pause')

@bot.command(pass_context = True, aliases = ['r', 'res'])
async def resume(ctx):
	voice = get(bot.voice_clients, guild=ctx.guild)

	if voice and voice.is_paused():
		print('Resumed music')
		voice.resume()
		await ctx.send('Resumed music')
	else:
		print('Music is not paused')
		await ctx.send('Music is not paused')


@bot.command()
async def stop(ctx):
	voice = get(bot.voice_clients, guild=ctx.guild)

	queues.clear()

	if voice and voice.is_playing():
		print('Music stopped')
		voice.stop()
		await ctx.send('Music stopped')
	else:
		print('No music playing failed to stop')
		await ctx.send('No music playing failed to stop')

@bot.command(pass_context=True, aliases=['s','ski'])
async def skip(ctx):
	voice = get(bot.voice_clients, guild = ctx.guild)

	queues.clear()

	if voice and voice.is_playing():
		print("Music skipped")
		voice.stop()
		await ctx.send("Music skipped")

	else:
		print("No music playing failed to skip")
		await ctx.send("No music playing failed to skip")


queues = {}

@bot.command(pass_context = True, aliases = ['q','que'])
async def queue(ctx, url: str):
	Queue_infile = os.path.isdir("./Queue")
	if Queue_infile is False:
		os.mkdir("Queue")
	DIR = os.path.abspath(os.path.realpath("Queue"))
	q_num = len(os.listdir(DIR))
	q_num += 1
	add_queue = True
	while add_queue:
		if q_num is queues:
			q_num += 1
		else:
			add_queue = False
			queues[q_num] = q_num

	queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

	ydl_opts = {
		'format' : 'bestaudio/best',
		'quiet' : True,
		'outtmpl' : queue_path,
		'postprocessors' :[{
			'key': 'FFmpegPCMAudio',
			'preferredcodec' : 'mp3',
			'preferredquality': '192',
		}],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print ("Download audio now\n")
		ydl.download([url])
	await ctx.send("Adding song " + str(q_num) + "to the queue")

	print("Song added to queue\n")

#spam
@bot.command()
async def spam (ctx,member: discord.Member):

	await member.send (f'{member.name}, zdarova puki4 go igratb ')

@purge.error
async def clear_error( ctx, error):
	if isinstance ( error, commands.MissingRequiredArgument ):
		await ctx.send (embed = discord.Embed(description = f'{ctx.author.mention}, skoko clear?', color = 0x9c6c8c ) )

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(embed = discord.Embed(description = f'{ctx.author.mention}, nedostato4no prav dryjok', color = 0x9c6c8c  ) )

	#if isinstance (error, commands.CommandNotFound):
		#await ctx.sed (embed = discord.Embed(description = f'{ctx.author.mention}, takoy komandi ne cywectvyet', color = 0x9c6c8c ) ) # FIX IN WORK





#@bot.event

#async def on_message( message ):
#	msg = message.content.lower()

#	if msg in hello_words:
#		await message.channel.send('Ny zdarova, ebat')

#	if msg in answer_words:
#		await message.channel.send('Write in chat ">>help" clown')

#	if msg in godbye_words:
#		await message.channel.send('Ti opyatb vihodish na svyazb mudila?')

#test message 
@bot.command(pass_context=True) #разрешаем передавать агрументы

async def test(ctx, arg): #создаем асинхронную фунцию бота

	await ctx.send(arg) #отправляем обратно аргумент

#@bot.command() #разрешаем передавать агрументы

#async def hello(ctx):
	#author = ctx.message.author
	#await ctx.send(f' { author.mention } Hello O4koWnik')

#@bot.event

#hello_words = ['qq','hi','хай','ky','zdarova','privet','здарова','привет']
#answer_words = ['инфа','info','commands']
#godbye_words = ['bb','poka','я спать','пока','gl']

#async def on_message( message ):
	#msg = message.content.lower()

	#if msg in hello_words:
		#await message.channel.send('Ny zdarova, ebat')

	#if msg in answer_words:
		#await message.channel.send('Write in chat ">>help" clown')

	#if msg in godbye_words:
		#await message.channel.send('Ti opyatb vihodish na svyazb mudila?')


bot.run(TOKEN)