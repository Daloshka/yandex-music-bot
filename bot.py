import urllib.parse as parser

import telebot

from database import Database
from config import BOT_TOKEN
from buttons import *



def get_token_from_url(url_with_token: str) -> str:
    schema_url_with_token = parser.urlparse(url_with_token)
    token = parser.parse_qs(schema_url_with_token.fragment)['access_token'][0]
    return token

def main():
    print(f"Бот запущен")
    
    @bot.message_handler(commands=['start'])
    def start_message_reply(message):
        tgid = message.chat.id
        if not db.user_exists(tgid):
            db.create_user(tgid)
        bot.send_message(tgid, start_message)

    @bot.message_handler(content_types="text")
    def message_reply(message):
        tgid = message.chat.id
        if "access_token" in message.text:
            token = get_token_from_url(message.text)
            db.set_token(tgid, token)
            bot.send_message(tgid, "Токен успешно сохранён", reply_markup=main_menu)
        


    bot.infinity_polling()
        


if __name__ == "__main__":
    bot = telebot.TeleBot(BOT_TOKEN)
    db = Database()

    main()
    