# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from request_jarvis import jarvis



class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    
    async def on_message_activity(self, turn_context: TurnContext):

        if turn_context.activity.type == "message" and turn_context.activity.text:
            # Check to see if the user wants to initiate a conversation/prediction.
            if turn_context.activity.text.lower() == "hi" or turn_context.activity.text.lower() == "hey" or turn_context.activity.text.lower() == "initiate" or turn_context.activity.text.lower() == "restart":
                await turn_context.send_activity("Hi... I'm **Jarvis**. Whatever you say I'll suggest a suitable category for it. I have been trained on historic emails that our support teams have received from clients. I very recently joined and still have lot to learn. Please expect some errors. :)")
                await turn_context.send_activity('Why dont you type your query below for me and i will recommend you probabilites of the queue.')
            # Check to see if the user sent a simple "quit" message.
            elif turn_context.activity.text.lower() == "quit":
                # Send a reply.
                await turn_context.send_activity("It was nice working with you! Feel free to reach out to me! Bye!")
                exit(0)
            else:
                # Echo the message text back to the user. And give them a prediction
                await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
                await turn_context.send_activity(f"My training  tells me that this email can be sent to:")
                result = jarvis(turn_context.activity.text)
                for key, value in result.items():
                    await turn_context.send_activity(f"Queue **{key}** with a probability of ***{round(value, 2)}%***")
                await turn_context.send_activity(f"Please type in another query to predict or type quit to exit")        

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("**Hello and welcome!**")
                await turn_context.send_activity("Hi... I'm **Jarvis**. Whatever you say I'll suggest a suitable category for it. I have been trained on historic emails that our support teams have received from clients. I very recently joined and still have lot to learn. Please expect some errors. :)")
                await turn_context.send_activity('Why dont you type your query below for me and i will recommend you probabilites of the queue.')

