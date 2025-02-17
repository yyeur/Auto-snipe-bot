from telethon import TelegramClient, events
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Password protection
password = "Yassour0X"

# Ask for API credentials
api_id = input(Fore.BLUE + "Enter your API ID: ")
api_hash = input(Fore.BLUE + "Enter your API Hash: ")

# Ask for the sniper bot username
sniper_bot = input(Fore.BLUE + "Enter your Sniper Bot username (e.g., @YourSniperBot): ")

# Initialize Telegram session
client = TelegramClient("session_name", int(api_id), api_hash)

# Display script details
print(Fore.CYAN + Style.BRIGHT + "Made by Yasser AbuJamea")
print(Fore.YELLOW + "------------------------------")
print(Fore.GREEN + "DM me on Telegram: " + Fore.RED + "@Yasourr")
print(Fore.YELLOW + "------------------------------")
print(Fore.MAGENTA + "✅ The bot is now running...")

# Ask for channel usernames
channel_usernames = input(Fore.BLUE + "Enter the channel usernames (separate them with spaces): ").split()

# Password verification
input_password = input(Fore.RED + "Enter the password to start the script: ")
if input_password != password:
    print(Fore.RED + "Incorrect password!")
    exit()

@client.on(events.NewMessage(chats=channel_usernames))
async def forward_to_bot(event):
    message = event.message.text
    if message:  # Ensure the message is not empty
        await client.send_message(sniper_bot, message)
        print(Fore.GREEN + f"Message forwarded to {sniper_bot}: {message}")

client.start()
client.run_until_disconnected()