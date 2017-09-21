import telegram
import os

from source.db import Db

about_text = '''
Пожалуйста, оцените этого бота https://telegram.me/storebot?start=IcePlaybookBot

Для связи с разработчиком используйте Telegram @KonstantinShpilko, сайт http://way23.ru
'''

help_text = '''Международная статистическая классификация болезней и проблем, связанных со здоровьем.
Вводите код и бот вернёт расшифровку.'''

class Domain():

    def __init__(self, setting):
        self.db = Db(setting)

    def on_start(self, bot, update):
        self.on_help(bot, update)

    def on_about(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=about_text,
                        parse_mode=telegram.ParseMode.HTML)
        return 'about'

    def on_help(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=help_text,
                        parse_mode=telegram.ParseMode.HTML)
        return 'about'

    def on_text(self, bot, update):
        text = self.db.getDia(update.message.text)
        update.message.reply_text(text)

