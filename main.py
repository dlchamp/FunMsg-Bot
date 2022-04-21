"""
Version: 1.0.0

Description:
Bot will monitor the configured channel to identify when
the channel has fallen into an active conversation.  Once
the configured amount of messages has been sent, the bot will
randomly join the conversation with a "fun" message.


Available configs:
- Inactivity timer - default 60 seconds
- Min and max amount of message to be sent before bot sends message - default (5, 10)
- Channel ID for the channel to monitor for activity

"""
from disnake.ext import commands
from disnake import Intents
from os import listdir, getenv


intents= Intents()
intents.message_content = True
bot = commands.Bot(intents=intents)


@bot.listen()
async def on_ready():
    """Function called when bot is ready"""
    print(f"{bot.user} is connected to Discord and listening for events.")


def load_cogs(bot):
    for file in listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")


if __name__ == "__main__":
    load_cogs(bot)
    bot.run(getenv('TOKEN'))

