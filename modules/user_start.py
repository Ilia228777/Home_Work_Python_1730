# import modules.bot_start
# import modules.create_inline_keyboard

# @modules.bot_start.bot.message_handler(commands=["start1"])
# def send_message_user(message):
#     modules.bot_start.bot.send_message(message.chat.id,
#                                         text="Hello world!")

import modules.bot_start
import modules.create_inline_keyboard 
import modules.find_path 

def send_message_user(message):
    if message.text.lower() == "NEW" or "SALE" or "DISCOUNT":
        path_file1 = modules.find_path.find_path_file("img/1.jpg")
        path_file2 = modules.find_path.find_path_file("img/2.jpg")
        path_file3 = modules.find_path.find_path_file("img/3.jpg")
        path_file4 = modules.find_path.find_path_file("img/4.jpg")
        path_file5 = modules.find_path.find_path_file("img/5.jpg")
        modules.bot_start.bot.send_photo(
            message.chat.id, 
            open(path_file1, "rb"),
            "5 фото з нашого магазину",
            reply_markup= modules.create_inline_keyboard.inline_keyboard
        )
        modules.bot_start.bot.send_photo(
            message.chat.id, 
            open(path_file2, "rb"),
            reply_markup= modules.create_inline_keyboard.inline_keyboard
        )
        modules.bot_start.bot.send_photo(
            message.chat.id, 
            open(path_file3, "rb"),
            reply_markup= modules.create_inline_keyboard.inline_keyboard
        )
        modules.bot_start.bot.send_photo(
            message.chat.id, 
            open(path_file4, "rb"),
            reply_markup= modules.create_inline_keyboard.inline_keyboard
        )
        modules.bot_start.bot.send_photo(
            message.chat.id, 
            open(path_file5, "rb"),
            reply_markup= modules.create_inline_keyboard.inline_keyboard
        )