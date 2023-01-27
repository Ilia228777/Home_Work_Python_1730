import modules.button_creation
import telebot

bar = telebot.types.ReplyKeyboardMarkup(row_width = 1)

bar.add(modules.button_creation.button1, modules.button_creation.button2, modules.button_creation.button3)