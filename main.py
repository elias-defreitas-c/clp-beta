from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Loading Token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# BOT SETUP
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


# Message Functionality
async def send_message(message, user_message):
    if not user_message:
        print("message was empty because intents were not enabled")
        return

    if user_message[0] == '?':
        try:
            response = get_response(user_message)
            await message.channel.send(response)
        except Exception as e:
            print(e)


# Handling the startup
@client.event
async def on_ready():
    print(f'{client.user} is now running.')


# Handling Incoming Messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Main Entry Point
def main():
    client.run(TOKEN)


if __name__ == '__main__':
    main()

