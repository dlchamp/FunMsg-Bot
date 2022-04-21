from disnake.ui import View, Button
from disnake import ButtonStyle


class Answers(View):
    '''
    Answers class that contains emoji and name
    for FunMSg
    '''

    def __init__(self, correct, answers, channel):
        super().__init__(timeout=5.5)
        self.correct = correct[0]
        self.channel = channel
        [self.add_item(Button(label=a[1], emoji=a[0], style=ButtonStyle.primary)) for a in answers]
        self.value = None
        self.author = None


    async def interaction_check(self, interaction):
        '''Function called when any interactiont place place against this view class'''

        author = interaction.author
        button_emoji = interaction.component.emoji.name

        if button_emoji == self.correct: # emoji
            await interaction.response.send_message("Hey, you did it", ephemeral=True)
            self.value=True
            self.author = interaction.author
            self.stop()

        else:
            await interaction.response.send_message(f"That ain't it, chief", ephemeral=True)