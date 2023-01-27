import modules.create_inline_button 
import telebot

inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(modules.create_inline_button.inline_button1, 
                    modules.create_inline_button.inline_button2)