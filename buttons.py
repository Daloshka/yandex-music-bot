from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

url_get_token = "https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d"
url_with_token = "https://music.yandex.ru/#access_token=y0_AgAAAFFAR-LMAAG8XgAAAADvb6gHK-F12K5bRtOWYZSj2o3Lp8ynOQo&token_type=bearer&expires_in=31534287"
url_article_with_token = "https://yandex-music.readthedocs.io/en/main/token.html"

start_message = f"""
Привет! Для начала работы отправьте токен Яндекс.Музыки
Как его получить написано здесь {url_article_with_token}
У вас должна получиться ссылка вида {url_with_token}
"""

class Buttons:
    def __init__(self):
        self.delete_favorite = "Удалить все треки из избранного"