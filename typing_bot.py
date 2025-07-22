import asyncio
from pyrogram import Client
import logging

logging.basicConfig(level=logging.WARNING)

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"

CHATS = [
    "@username",
    -1001234567890,
    "chat_name"
]

app = Client("typing_session", api_id=API_ID, api_hash=API_HASH)

async def typing_forever():
    await app.start()
    print("Запущен! Статус 'печатает' активен в выбранных чатах...")
    
    while True:
        for chat in CHATS:
            try:
                await app.send_chat_action(chat, "typing")
            except Exception as e:
                print(f"Ошибка в чате {chat}: {e}")
        
        await asyncio.sleep(4)

if __name__ == "__main__":
    asyncio.run(typing_forever()) 