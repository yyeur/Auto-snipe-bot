from telethon import TelegramClient, events
from colorama import Fore, Style, init

# تهيئة colorama
init(autoreset=True)

# كلمة المرور
password = "Yassour0X"

# طلب API ID و API Hash من المستخدم
api_id = input(Fore.BLUE + "أدخل API ID الخاص بك: ")
api_hash = input(Fore.BLUE + "أدخل API Hash الخاص بك: ")

# طلب يوزر بوت السنايبر
sniper_bot = input(Fore.BLUE + "أدخل يوزر بوت السنايبر (مثال: @YourSniperBot): ")

# إنشاء جلسة تيليجرام
client = TelegramClient("session_name", int(api_id), api_hash)

# نصوص مميزة
print(Fore.CYAN + Style.BRIGHT + "Made by Yasser AbuJamea")
print(Fore.YELLOW + "------------------------------")
print(Fore.GREEN + "DM me on Telegram: " + Fore.RED + "@Yasourr")
print(Fore.YELLOW + "------------------------------")
print(Fore.MAGENTA + "✅ البوت يعمل الآن...")

# طلب يوزرات القنوات من المستخدم
channel_usernames = input(Fore.BLUE + "أدخل يوزرات القنوات (فصل بينهم بمسافة): ").split()

# التحقق من كلمة السر
input_password = input(Fore.RED + "أدخل كلمة السر لتشغيل السكربت: ")
if input_password != password:
    print(Fore.RED + "كلمة السر غير صحيحة!")
    exit()

@client.on(events.NewMessage(chats=channel_usernames))
async def forward_to_bot(event):
    message = event.message.text
    if message:  # تأكد أن الرسالة ليست فارغة
        await client.send_message(sniper_bot, message)
        print(Fore.GREEN + f"تم إرسال الرسالة إلى {sniper_bot}: {message}")

client.start()
client.run_until_disconnected()