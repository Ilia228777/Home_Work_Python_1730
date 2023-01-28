import telebot
import modules.names

inline_button1 = telebot.types.InlineKeyboardButton(modules.names.list[3], callback_data="1")
inline_button2 = telebot.types.InlineKeyboardButton(modules.names.list[4], url="https://yabloki.ua/ukr/")