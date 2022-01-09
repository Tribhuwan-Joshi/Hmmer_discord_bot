import discord
import os
from replit import db
import requests
import random
import json

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable","mar ","dukhi","dard","peda","bad"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person","Himmat rakh","Yep thats it"
]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+" -" + json_data[0]['a']
  return(quote)


wordlist = []


my_secret = os.environ['Token']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  
  if message.author == client.user:
    return


  msg = message.content
  if not msg.startswith("$") and message.channel.name == "word-chain":
       if msg.lower() not in wordlist:
            wordlist.append(msg.lower())
       elif msg.lower() in wordlist:
           await message.channel.send("You already said that word!")
           await message.delete()

  
  if msg.startswith("$hey"):
    await message.channel.send("Hello Human! I will watch your word-chain , don't repeat words ! I am under development you can try [$help]")
    
  

  if message.content.startswith('$8ball'):
        possible_responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes, definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Don\'t count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good'
        ]
        await message.channel.send(random.choice(possible_responses))
        return
  if msg.startswith("$help"):
    await message.channel.send("``` Yo! This is some command you can use 1.$inspire - 'Quotes that may can inspire\n2.$8ball - 'ask a question and I will tell if thats true or not'   ```")
  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  
    
    



client.run(my_secret)
