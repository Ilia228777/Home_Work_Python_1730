import telebot

inline_button1 = telebot.types.InlineKeyboardButton("Замовити", callback_data="1")
inline_button2 = telebot.types.InlineKeyboardButton("Перейти до сайту", url="https://yabloki.ua/ukr/")