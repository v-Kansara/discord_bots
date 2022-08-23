# main.py imports
import os
import discord
import random
import asyncio
import requests
import json

# From ___ imports
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
com_prefix = 'peppa '
#---------------------------------------------------------
# Leveling system

#---------------------------------------------------------
# Bully Message Databases

#---------------------------------------------------------
# Study Stuff Databases
# Math DB
math_work = [
 
]

#---------------------------------------------------------
# Jokes
jokes = [
"What did the bartender say to the jumper cables? You better not try to start anything.",
"Don't you hate jokes about German sausage? They're the wurst!",
"Two artists had an art contest... It ended in a draw",
"Why did the chicken cross the playground? To get to the other slide.",
"What gun do you use to hunt a moose? A moosecut!",
"If life gives you melons, you might have dyslexia.",
"Broken pencils... ...are pointless.",
"What did one snowman say to the other snowman? 'Do you smell carrots?'",
"How many hipsters does it take to change a lightbulb? It's a really obscure number. You've probably never heard of it.",
"Where do sick boats go? The dock!",
"I like my slaves like I like my coffee: Free.",
"My girlfriend told me she was leaving me because I keep pretending to be a Transformer... I said, No, wait! I can change!",
"Old Chinese proverb: Man who not shower in   days makes one reek.",
"What did the owner of a brownie factory say when his factory caught fire? \"I'm getting the fudge outta here!\"",
"What form of radiation bakes you cookies? A gramma ray",
"Bee jokes, courtesy of my niece (age  ). What did the bee use to dry off after swimming? A *bee*ch towel. What did the bee use to get out the tangles? A honeycomb.",
"What's the loudest economic system? CAPITALISM",
"I went for a job interview today... The interviewer said to me, What would you say your greatest weakness is? I said, I think Id have to say my listening skills are my greatest strength.",
"Who was the knight that invented the round table? Sir Cumference. (via friend who got this from a street performance group in the England area of Epcot)",
"What did the German air force eat for breakfast during WW ? Luftwaffles",
"I the shell off a snail yesterday... you'd think it would move faster, but it was really kinda sluggish.",
"What did the number zero say to the number eight? \"Nice belt.\"",
"What's worse than a centipede with sore feet? A giraffe with a sore throat",
"What's red and bad for your teeth? A brick.",
"Why did the Chicken cross the playground? To get to the other slide",
"Did you hear about the French chef who committed suicide? He lost the huile d'olive",
"Wanna hear a joke about unemployed people? Nevermind, they don't work.",
"Knock Knock Who's there Boo!! Boo who? Don't cry, it's only a joke",
"How much did the skeleton charge for his excellent legal services? An arm and a leg.",
"Why do gorillas have such big nostrils? Cos they got big fingers.",
"What is the difference between a Siberian husky and an Alaskan husky? About miles.",
"What do vegan zombies eat? GRAAAIIINSSS!",
"What's the difference between a Thai man and a Thai woman? Pls help.",
"What do you call a car that eats other cars? A carnivore.",
"Why did the golfer wear two pairs of pants In case he gets a hole in one",
"An Olympic gymnast walked into a bar... She didnt get a medal...",
"What does a mexican magician make for breakfast? Toast-tah-dahs!",
"Why don't Bond villains feel cold in the winter? Because they dress in lairs.",
"What did the figurine say when the boot flew past her protective dome? \"That was a cloche call!\"",
"What was Carl Sagan's favorite drink? Cosmos.",
"What is the medical term for owning too many dogs?  A Roverdose (http://i.imgur.com/BtyF ys.jpg)",
"Knock knock... Who's there? I did up. I did up-who?",
"I like my jokes they way I like my robots. Killer.",
"What type of school did Sherlock Holmes go to? Elementary :)",
"My friend told an out of place joke about police searches. But I don't think it was warranted.",
"The Dalai Lama walks into a pizza store... and says, \"Can you make me one with everything?\"",
"Why did the vampire use mouthwash? Because he had bat breath",
"What did the corn say when it was complemented? Aww, shucks!",
"What did the green grape say to the purple grape? - \"Breathe, stupid!\"",
"Why did the Fall break off from all the other seasons? Because it wanted autumnomy",
"If I ever fire someone who is a Taylor Swift fan I'll say \"I knew you were trouble when you clocked in.\"",
"What do you do if a cow is in the middle of the road you're driving on? steer clear",
"What do you call a blind, legless buck? No eye-deer. EDIT: I totally messed this joke up. Please give me another chance with another joke?",
"What do you get for the women who has everything? A divorce, then she'll only have half of everything.",
"There was a depressed sausage... he thought his life was THE WURST.",
"What's a dog's favorite mode of transportation? A waggin'",
"Why did the sand dune blush? Because the sea weed",
"What happened to the tyrannical peach? He got impeached!",
"Why do elephants paint their toenails red? So they can hide in cherry trees. You ever seen an elephant in a cherry tree? *Then it's working*.",
"what did the mexican firecheif name his kids... Hose A and Hose B",
"What did the German physicist use to drink his beer? Ein stein. - From Big Nate, as told by my kid.",
"What did earth say to the other planets? You guys have no life!",
"One time we ran out of soap- -so we had to use hand sanitizer!!!",
"Wanna hear a dirty joke? Two white stallions fell in the mud.",
"What did one frog say to the other frog? Time's fun when you're having flies.",
"Why did the boy take a pencil and paper to bed? He was told to draw the curtains before going to sleep.",
"Clean joke about sorority girls Why do sorority girls only travel in odd numbered groups? Because they *can't even*!",
"What did the   say to the  ? Hey, fatty",
"KNOCK KNOCK! WHO'S THERE! Sombrero! Sombrero who? SOMBRERO-VER THE RAINBOW",
"I'm reading a book about anti-gravity... ... It's impossible to put down",
"What name is given to the most chickens ? pEGGy",
"Why is Dr. Frankenstein never lonely? He's good at making friends.",
"What do you call a pig that does karate? *A pork chop.*",
"What was the car doing in the dressing room? Changing attire.",
"What do you call a pile of dogs? A ruff terrain.",
"How do you prepare for a party in space? You Planet Thanks u/BostonCentrist",
"What do you get when you cross an octopus with a cow? A stern rebuke from the Ethics Committee, and an immediate cessation of funding.",
"Why did the bicycle fall over? Because it was two-tired",
"Two bookworms were having a dispute... ...across an open book until one bookworm moves closer to the other and says, \"well then, I'm glad we're on the same page.\"",
"Which kitchen appliance tells the best jokes? The beater - he cracks everybody up!",
"Why did the jellyroll? He saw the apple turnover.",
"Why did the chicken? Q: Why did the chicken cross the road naked? A: Because chickens don't wear clothes.",
"What do you call Protestants who want to save a dime? Econoclasts.",
"What do dwarves use to cut their pizza? Little Caesars",
"What did the fish say when it hit the wall? Dam.",
"What's that coffee drink with icecream? I used to know it, but... Affogato.",
"Where did Napoleon keep his armies? In his sleevies!",
"makeup beauty Omg = oh my girl so cute next morning without makeup Omg = ohh My God omg/omg = life without wife",
"Time flies like the wind. Fruit flies like... bananas!",
"What did Vincent van Gogh call himself when he joined the Justice League? The Starry Knight",
"Why did the boy take a ladder to school? He wanted to go to high school.",
"What's the best thing to put into a pie Your teeth.",
"What kind of house does a stoned loaf of bread live in? A high rise",
"What do you get when you cross a firecracker and a duck? A firequacker.",
"What's a baker's biggest fear? Something going a-rye while they're raisin' bread.",
"What's the best way to get a hold of Vin Diesel? IM Groot. : D Source: https://www.youtube.com/watch?v=Lvlj u S  ",
"Why did everyone trust the marsupial? Everything he said was troo",
"This dermatologist waits a month to diagnose a skin disorder... She's reluctant to make a rash decision.",
"Why are manhole covers round? Because manholes are round.",
"What did one casket say to the other? \"Is that you coffin?\"",
"How does a hamburger introduce his girlfriend? Meat patty! Thought of you guys!",
"How does a mathematician get Tan? Sin/Cos",
"What is a martian's favourite chocolate? A mars bar",
"Where did Sally go after the explosion? Everywhere.",
"What did the cow say when it saw the farmer twice in one day? Deja Moo!"
]

#---------------------------------------------------------
# Roasts
roasts = [
"Where’s your off button?",
"You’re so real. A real ass.",
"I’m not shy. I just don’t like you.",
"My hair straightener is hotter than you.",
"I have heels higher than your standards.",
"You have more faces than Mount Rushmore.",
"I’m jealous of people who don’t know you.",
"You’re entitled to your incorrect opinion.",
"I’m visualizing duct tape over your mouth.",
"You’re the reason I prefer animals to people.",
"If I had a face like yours, I’d sue my parents.",
"I’d smack you, but that would be animal abuse.",
"You sound reasonable… Time to up my medication.",
"Hey, I found your nose, it’s in my business again!",
"I might be crazy, but crazy is better than stupid.",
"My middle finger gets a boner every time I see you.",
"Is there an app I can download to make you disappear?",
"90% of your ‘beauty’ could be removed with a Kleenex.",
"The people who know me the least have the most to say.",
"I am allergic to stupidity, so I break out in sarcasm.",
"I didn’t change. I grew up. You should try it sometime.",
"My phone battery lasts longer than your relationships.",
"I’m sorry that my brutal honesty inconvenienced your ego.",
"Some people should use a glue stick instead of chapstick.",
"It’s scary to think people like you are allowed to vote.",
"You are more disappointing than an unsalted pretzel.",
"Light travels faster than sound, which is why you seemed bright until you spoke.",
"We were happily married for one month, but unfortunately, we’ve been married for 10 years.",
"Your kid is so annoying he makes his Happy Meal cry.",
"You have so many gaps in your teeth it looks like your tongue is in jail.",
"Your secrets are always safe with me. I never even listen when you tell me them.",
"I’ll never forget the first time we met. But I’ll keep trying.",
"I forgot the world revolves around you. My apologies! How silly of me.",
"I only take you everywhere I go just so I don’t have to kiss you goodbye.",
"Hold still. I’m trying to imagine you with a personality.",
"Our kid must have gotten his brain from you! I still have mine.",
"Your face makes onions cry.",
"Her teeth were so bad she could eat an apple through a fence.",
"I’m not insulting you; I’m describing you.",
"I’m not a nerd; I’m just smarter than you.",
"Don’t be ashamed of who you are. That’s your parents’ job.",
"Your face is just fine, but we’ll have to put a bag over that personality.",
"You bring everyone so much joy… when you leave the room.",
"I thought of you today. It reminded me to take out the trash.",
"Don’t worry about me. Worry about your eyebrows.",
"You are the human version of period cramps.",
"If you’re going to be two-faced, at least make one of them pretty.",
"You are like a cloud. When you disappear, it’s a beautiful day.",
"I’d rather treat my baby’s diaper rash than have lunch with you.",
"Don’t worry — the first 40 years of childhood are always the hardest.",
"I may love to shop, but I will never buy your bull.",
"I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?",
"OH MY GOD! IT SPEAKS!",
"Someday you’ll go far… and I really hope you stay there.",
"Oh, I’m sorry. Did the middle of my sentence interrupt the beginning of yours?",
"You bring everyone so much joy! You know, when you leave the room. But, still.",
"Oops, my bad. I could’ve sworn I was dealing with an adult.",
"Did I invite you to the barbecue? Then why are you all up in my grill?",
"I’m an acquired taste. If you don’t like me, acquire some taste.",
"Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.",
"Yeah? Well, you smell like hot dog water.",
"*Thumbs down*",
"That sounds like a you problem.",
"Beauty is only skin deep, but ugly goes clean to the bone.",
"Oh, you don’t like being treated the way you treat me? That must suck.",
"I’ve been called worse things by better men.",
"FUN FACT: Pierre Trudeau, a Canadian politician, used this clap back after learning that Richard Nixon had insulted him. The political shade!",
"Well, the jerk store called. They’re running out of you.",
"Sorry, not sorry.",
"I’m busy right now; can I ignore you another time?",
"If you have a problem with me, write the problem on a piece of paper, fold it, and shove it up your ass.",
"You have an entire life to be an idiot. Why not take today off?",
"No matter how much a snake sheds its skin, it’s still a snake.",
"Some people are like slinkies — not really good for much, but they bring a smile to your face when pushed down the stairs.",
"You’re the reason this country has to put directions on shampoo.",
"Of course I’m talking like an idiot… how else could you understand me?",
"Are you almost done with all of this drama? Because I need an intermission.",
"I’d give you a nasty look, but you’ve already got one.",
"If I wanted to hear from an asshole, I’d fart.",
"Your birth certificate is an apology letter from the condom factory.",
"Your family tree must be a cactus because everybody on it is a prick.",
 "Wow, I bet you even fart glitter!",
"I guess if you actually ever spoke your mind, you’d really be speechless.",
"Since you know it all, you should know when to shut up.",
"Life is full of disappointments, and I just added you to the list.",
"I treasure the time I don’t spend with you.",
"I was going to make a joke about your life, but I see life beat me to the punch.",
"The last time I saw something like you… I flushed.",
"The only work-life balance I want is being away from you.",
"When you start talking, I stop listening.",
"Feed your own ego. I’m busy.",
"You look like something that came out of a slow cooker.",
"If laughter is the best medicine, your face must be curing the world.",
"I think I’ve seen you before, but I’m pretty sure I had to pay admission last time."
]

compliments = [
"You’re strong.",
"Your perspective is refreshing.",
"You’re an awesome friend.",
"You light up the room.",
"You deserve a hug right now.",
"You should be proud of yourself.",
"You’re more helpful than you realize.",
"You have a great sense of humor.",
"You’ve got all the right moves!",
"Is that your picture next to 'charming' in the dictionary?",
"Your kindness is a balm to all who encounter it.",
"You’re all that and a super-size bag of chips.",
"On a scale from 1 to 10, you’re an 11.",
"You are brave.",
"You’re even more beautiful on the inside than you are on the outside.",
"You have the courage of your convictions.",
"Aside from food. You’re my favorite.",
"If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.",
"You are making a difference.",
"You’re like sunshine on a rainy day.",
"You bring out the best in other people.",
]

Mix_Roast_Compliment = roasts + compliments

truth = [
"When was the last time you lied?",
"When was the last time you cried?",
"What's your biggest fear?",
"What's your biggest fantasy?",
"Do you have any fetishes?",
"What's something you're glad your mum doesn't know about you?",
"Have you ever cheated on someone?",
"What's the worst thing you've ever done?",
"What's a secret you've never told anyone?",
"Do you have a hidden talent?",
"Who was your first celebrity crush?",
"What are your thoughts on polyamory?",
"What's the worst intimate experience you've ever had?",
"Have you ever cheated in an exam?",
"What's the most drunk you've ever been?",
"Have you ever broken the law?",
"What's the most embarrassing thing you've ever done?",
"What's your biggest insecurity?",
"What's the biggest mistake you've ever made?",
"What's the most disgusting thing you've ever done?",
"Who would you like to kiss in this room?",
"What's the worst thing anyone's ever done to you?",
"Have you ever had a run in with the law?",
"What's your worst habit?",
"What's the worst thing you've ever said to anyone?",
"Have you ever peed in the shower?",
"What's the strangest dream you've had?",
"Have you ever been caught doing something you shouldn't have?",
"What's the worst date you've been on?",
"What's your biggest regret?",
"What's the biggest misconception about you?",
"Where's the weirdest place you've had sex?",
"Why did your last relationship break down?"
]

dare = [
"Show the most embarrassing photo on your phone",
"Show the last five people you texted and what the messages said",
"Let the rest of the group DM someone from your Instagram account",
"Eat a raw piece of garlic",
"Do 100 squats",
"Keep three ice cubes in your mouth until they melt",
"Say something dirty to the person on your left",
"Give a foot massage to the person on your right",
"Put 10 different available liquids into a cup and drink it",
"Yell out the first word that comes to your mind",
"Give a lap dance to someone of your choice",
"Remove four items of clothing",
"Like the first 15 posts on your Facebook newsfeed",
"Eat a spoonful of mustard",
"Keep your eyes closed until it's your go again",
"Send a sext to the last person in your phonebook",
"Show off your orgasm face",
"Seductively eat a banana",
"Empty out your wallet/purse and show everyone what's inside",
"Do your best sexy crawl",
"Pretend to be the person to your right for 10 minutes",
"Eat a snack without using your hands",
"Say two honest things about everyone else in the group",
"Twerk for a minute",
"Try and make the group laugh as quickly as possible",
"Try to put your whole fist in your mouth",
"Tell everyone an embarrassing story about yourself",
"Try to lick your elbow",
"Post the oldest selfie on your phone on Instagram Stories",
"Tell the saddest story you know",
"Howl like a wolf for two minutes",
"Dance without music for two minutes",
"Pole dance with an imaginary pole",
"Let someone else tickle you and try not to laugh",
"Put as many snacks into your mouth at once as you can"
]

people = [
  "<@!888496765068771388>",
  "<@!902602050662174740>",
  "<@!691325622127165491>",
  "<@!807721147906785300>",
  "<@!786409185856061541>",
  "<@!761221516947750912>",
  "<@!713401090472804462>",
  "<@!796129773247528960>",
  "<@!601620218858700813>",
  "<@!758825367766171648>",
  "<@!695335414524936254>",
  "<@!874424604003815437>",
  "<@!755142703674556557>",
  "<@!796043129189826580>",
  "<@!750034219102896149>",
  "@!710587027388760095",
  
]

peoples = "Go bother " + random.choice(people)

peppa_reply = [
  "What do you want, you bozo sussy baka burger?",
  "Wait Wait Wait. Hold on. Moto Moto just dm'd me. I think he likes you",
  "Tf is your problem?",
  "... I was playing peppa. Why did you interupt me?",
  peoples
]

bot_answer = random.randint(1, 3)
print(bot_answer)

#---------------------------------------------------------

#-------------------------------------------------
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name='peppa.lmao'))
 
# Commands by Members
@client.event
async def on_member_join(member):
 await member.create_dm()
 await member.dm_channel.send(f'Hi {member.name}, welcome to Trash!')

@client.event
async def on_message(message):
 if message.author == client.user:
   return

  # Setting `Playing ` status
#game = await bot.change_presence(activity=discord.Game(name="peppa"))

# Setting `Streaming ` status
#stream = await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
#song = await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
#movie = await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

#---------------------------------------------------------
# @PeppaBot
 if message.content == '<@!901849706253127761>':
   await message.channel.send(message.author.mention)
   await message.channel.send(random.choice(peppa_reply))

# Peppa help
 if message.content == 'peppa help':
  embed = discord.Embed(title = "Commands For Peppa Bot", description = "Stuf")
  embed.add_field(name = "Joke", value = "peppa jokes", inline = False)
  embed.add_field(name = "Roast", value = "peppa roast or peppa roast @[user_here]", inline = False)
  embed.add_field(name = "Quote", value = "peppa quote", inline = False)
  embed.add_field(name = "Compliment", value = "peppa compliment me or peppa compliment @[user_here]", inline = False)
  embed.add_field(name = "Truth or Dare", value = "peppa truth/dare", inline = False)
  embed.add_field(name = "Rock Paper Scissors", value = "peppa rps", inline = False)
  await message.channel.send(embed=embed)
 
 if message.content == 'peeep':
   await message.channel.send("pls help")

#---------------------------------------------------------
 
 
#---------------------------------------------------------
# Peppa Joke commands
 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'jokes':
   await message.channel.send(random.choice(jokes))

#---------------------------------------------------------
# Peppa roast Commands
 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast':
   await message.channel.send(message.author.mention)
   await message.channel.send("So you want to get roasted eh?")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @The Peppa

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!888496765068771388>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Hey Hey Hey. <@!888496765068771388> is too cool to be roasted.")

# Peppa roasting @HELLFIRE

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!713401090472804462>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!713401090472804462>")
   await message.channel.send(random.choice(roasts))
 
# Peppa roasting @Undead Peppa

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!750034219102896149>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!750034219102896149>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Dr.Peppa

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!786409185856061541>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!786409185856061541>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Banaboy Moments

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!691325622127165491>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!691325622127165491>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Geetimus

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!761221516947750912>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!761221516947750912>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Master Vijay

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!601620218858700813>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!601620218858700813>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Bleep Bloop

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!807721147906785300>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!807721147906785300>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @hershey

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!796129773247528960>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!796129773247528960>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Julmar54

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!855865283779624991>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!855865283779624991>")
   await message.channel.send(random.choice(roasts))

 if message.author == '<@!601620218858700813>':
   await message.channel.send("Shut Bozo.")
  
# Peppa roasting @JayTheGod

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!842142130692423741>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!842142130692423741>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Octopus 34

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!755142703674556557>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!755142703674556557>")
   await message.channel.send(random.choice(roasts))
  
# Peppa roasting @Thats Crazy

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!796043129189826580>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!796043129189826580>")
   await message.channel.send(random.choice(roasts))
 
# Peppa roasting @Pikachu

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!874424604003815437>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!874424604003815437>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Crumbs

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!711956843563581520>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!711956843563581520>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @WandaMaximoff

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!766787771565211660>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!758825367766171648>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Osiris

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!695335414524936254>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!695335414524936254>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @FlamingHomosapien

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!738087456024428654>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!738087456024428654>")
   await message.channel.send(random.choice(roasts)) 

# Peppa roasting @BigNirdLord

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!898176061534240788>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!898176061534240788>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Justarandomperson

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!828709478923763804>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!828709478923763804>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @aditi

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!784227066459586600>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!784227066459586600>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @NotMrScarz

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!758825367766171648>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!758825367766171648>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Strawberry

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!705068650138435684>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!705068650138435684>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Mars

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!416560331045732373>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!416560331045732373>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Velocity

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!771364188006252554>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!771364188006252554>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Monkey-with-ak47

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!828709478923763804>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!828709478923763804>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Aircash

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!902602050662174740>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!902602050662174740>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Gigachadnicekid

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!625009351832109080>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!625009351832109080>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Bruhily

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!645250399736954910>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!645250399736954910>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Skeptical

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!710587027388760095>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!710587027388760095>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting @Bubby Tube

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast <@!527934523044790272>':
   await message.channel.send(message.author.mention)
   await message.channel.send("Ok fine. I'll roast <@!527934523044790272>")
   await message.channel.send(random.choice(roasts))

# Peppa roasting everyone

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'roast everyone':
   await message.channel.send('Hey everyone')
   await message.channel.send("Imagine getting roasted by PEPPA Bot")
   await message.channel.send(random.choice(roasts))

#---------------------------------------------------------
# Peppa giving compliments

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'compliment':
   await message.channel.send('Do you want to compliment someone else, or do you want to compliment yourself like a nerd?')

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'compliment me':
   await message.channel.send('Ok nerd, here is whats going to happen: you have 15% chance of getting a compliment & a 85% chance of getting roasted. Good luck!')
   await asyncio.sleep(3)
   await message.channel.send(random.choice(Mix_Roast_Compliment))

# Peppa giving compliments to people

#---------------------------------------------------------
# Peppa Saying Quotes
 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'quote':
   await message.channel.send(message.author.mention + 'This is your inspirational quote')
   quote = get_quote()
   await message.channel.send(quote)

#---------------------------------------------------------
# Peppa Truth or Dare
 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'truth or dare':
   await message.channel.send('Do you want a truth :laughing:, or a dare :smiling_imp:')

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'truth':
   await message.channel.send(message.author.mention + ' ' + random.choice(truth))

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'dare':
   await message.channel.send(message.author.mention + ' ' + random.choice(dare))

#---------------------------------------------------------
# Peppa Rock Paper Scissors

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'rps':
  embed=discord.Embed(title="Peppa RPS", description="Peppa Rock, Paper, Scissors - Input Your Choice", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="Choices", value="Here Are The Choices", inline=False)
  embed.add_field(name="Rock :rock:", value="peppa rock", inline=True)
  embed.add_field(name="Paper :page_facing_up:", value="peppa paper", inline=True)
  embed.add_field(name="Scissors :scissors:", value="peppa scissors", inline=True)
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'rock' and bot_answer == 1:
  embed=discord.Embed(title="Tie! :rock: :page_facing_up: :scissors:", description="Well, that was weird. We tied.", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Rock :rock:", inline=True)
  embed.add_field(name="Bot Choice", value="Rock :rock:", inline=True)
  embed.set_footer(text="Imagine Being Bad")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'rock' and bot_answer == 2:
  embed=discord.Embed(title="Peppa Bot is Insane! :page_facing_up: beats :rock:", description="Nice try, but I won that time!!", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Rock :rock:", inline=True)
  embed.add_field(name="Bot Choice", value="Paper :page_facing_up:", inline=True)
  embed.set_footer(text="Loser :regional_indicator_l:")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'rock' and bot_answer == 3:
  embed=discord.Embed(title="I Call Cheating! :rock: beats :scissors:", description=f"Aw, you beat me. It won't happen again!", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Rock :rock:", inline=True)
  embed.add_field(name="Bot Choice", value="Scissors :scissors:", inline=True)
  embed.set_footer(text="Cheater")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'paper' and bot_answer == 1:
  embed=discord.Embed(title="Stop The Cap! :page_facing_up: beats :rock:", description=f"The pen beats the sword? More like the paper beats the rock!!", color=discord.Color.orange())
  embed.set_footer(text="Lmao")
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Paper :page_facing_up:", inline=True)
  embed.add_field(name="Bot Choice", value="Rock :rock:", inline=True)
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'paper' and bot_answer == 2:
  embed=discord.Embed(title="Ok? :rock: :page_facing_up: :scissors:", description=f"Oh, wacky. We just tied. I call a rematch!!", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Paper :page_facing_up:", inline=True)
  embed.add_field(name="Bot Choice", value="Paper :page_facing_up:", inline=True)
  embed.set_footer(text="Why r u gae?")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'paper' and bot_answer == 3:
  embed=discord.Embed(title="Ur Actually Dog Water :scissors: beats :page_facing_up:", description=f"Imagine being so doo-doo water.", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Paper :page_facing_up:", inline=True)
  embed.add_field(name="Bot Choice", value="Scissors :scissors:", inline=True)
  embed.set_footer(text="Absolute Clown :clown:")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'scissors' and bot_answer == 1:
  embed=discord.Embed(title="I Never Knew You Were This Bad! Lol! :rock: beats :scissors:", description=f"HAHA!! I JUST CRUSHED YOU!! I rock!!", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Scissors :scissors:", inline=True)
  embed.add_field(name="Bot Choice", value="Rock :rock:", inline=True)
  embed.set_footer(text=":dogwater: just :dogwater:")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'scissors' and bot_answer == 2:
  embed=discord.Embed(title="... Unbelievable. :scissors: beats :page_facing_up:", description=f"Bruh. >: |", color=discord.Color.orange())
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Scissors :scissors:", inline=True)
  embed.add_field(name="Bot Choice", value="Paper :page_facing_up:", inline=True)
  embed.set_footer(text="Underestimation? Never.")
  await message.channel.send(embed=embed)

 if message.content.startswith(com_prefix) and message.content == (com_prefix) + 'scissors' and bot_answer == 3:
  embed.set_author(name="Peppa Bot", icon_url="https://i.pinimg.com/736x/17/1b/17/171b170c053d1e9f7a6a8947b595cf9e.jpg")
  embed.add_field(name="User Choice", value="Scissors :scissors:", inline=True)
  embed.add_field(name="Bot Choice", value="Scissors :scissors:", inline=True)
  embed.set_footer(text="Lmao :disguised_face:")
  await message.channel.send(embed=embed)

#---------------------------------------------------------
 #if message.content.startswith(com_prefix) and message.content == (command_prefix) + 'work' and message.author.id == 888496765068771388:
  #await message.channel.send("Working as Peppa")
  #await asyncio.sleep(3)
  #await message.channel.send("hello")
 
 #if message.content.startswith(command_prefix) and message.content == (command_prefix) + 'study':
  # await message.channel.send(message.author.mention, "What do you want to study")
 
# Keeping the bot running and inserting the token for the bot to function

keep_alive()
client.run(os.getenv('Token'))