from disnake.ext import commands, tasks
from disnake import Embed

from datetime import datetime, timedelta
from random import choice, sample, randint, shuffle

from config import Config
from utils.buttons import Answers


def ready_to_send(msg_count: int):
    """get the active count and check if message counter has exceeded"""
    _min, _max = Config.active_msg_count
    active_msg_count = randint(_min, _max)

    return msg_count >= active_msg_count
    # return True


def color_options(colors):
    """
    generate a random color as correct, then 3 wrong colors, shuffle, and return
    correct answer and all possible answers
    """
    color = choice(colors)
    wrong = sample([c for c in colors if c != color], 3)
    answers = shuffle_answers(color, wrong)

    return color, answers


def shuffle_answers(color, wrong):
    '''create an list of all answers, shuffle, then return shuffled list'''
    answers = [c for c in wrong]
    answers.append(color)
    shuffle(answers)

    return answers


class FunMsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colors = [
            ("⚫","Black"),
            ("🔵","Blue"),
            ("🟤","Brown"),
            ("🟢","Green"),
            ("🟠","Orange"),
            ("🟣","Purple"),
            ("⚪","White"),
            ("🟡","Yellow"),
            ("🔴","Red")
        ]
        self.last_msg_time = 0
        self.active_msg_count = 0
        self.fun_msg = None
        self.correct = None

    @commands.Cog.listener()
    async def on_ready(self):
        """Function called when bot is ready"""
        await self.bot.wait_until_ready()
        self.monitor_activity.start()
        print(f"Cog loaded: {self.qualified_name}")

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Function called when message event occurs

        Update the last msg timestampe and active msg count
        If msg count == the configured msg count, send the challenge message
        """
        monitor_channel_id = Config.monitor_channel_id
        channel = message.channel

        if not message.author.bot and channel.id == monitor_channel_id:

            # convert message created_at to timestamp + config expiry
            expires = Config.expires  # seconds
            activitiy_expires = datetime.timestamp(
                message.created_at + timedelta(seconds=expires)
            )

            self.last_msg_time = activitiy_expires

            # update message count
            self.active_msg_count += 1

            # get randint from min/max from config
            if ready_to_send(self.active_msg_count):

                        # create the fun msg
                correct, answers = color_options(self.colors)

                view = Answers(correct, answers, channel)

                embed = Embed(
                    title="Quick! Click the button!",
                    description=f'{correct[0]} {correct[1]}'
                )

                # send the embed with attached button view
                msg = await channel.send(embed=embed, view=view)

                # wait for interaction and execute
                await view.wait()

                if view.value is None:
                    # view timeout
                    embed = Embed(title='Gotta be quicker than that')
                else:
                    # correct
                    embed = Embed(
                        title='Holy... that reaction was quick!',
                        description=f'Great job, {view.author.mention}'
                        )

                # update message
                await msg.edit(embed=embed, view=view.clear_items())


                # update variables
                self.active_msg_count = 0
                self.fun_msg = msg
                self.correct = correct[0]






    @tasks.loop(minutes=1)
    async def monitor_activity(self):
        """
        Async tasks functions - Runs every minute

        Every run, check if the last message timestamp is more than
        configured time old (example 60 seconds old) if so, reset the message count)
        """

        # UTC timestamp
        now = datetime.timestamp(datetime.utcnow())

        # check if last message timestamp (+ expiry) < now
        expiry = self.last_msg_time

        if expiry != 0:
            if expiry < now:
                expiry = 0
                self.active_msg_count = 0


def setup(bot):
    bot.add_cog(FunMsg(bot))
