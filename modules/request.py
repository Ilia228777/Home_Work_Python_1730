import modules.bot_start

@modules.bot_start.bot.callback_query_handler(func= lambda callback: callback.data)

def processing_request(callback):
    if callback.data == "1":
        modules.bot_start.bot.send_message(
            callback.message.chat.id, 
            "Оформлено"
        )
        #modules.bot_start.bot.send_message(
        #    chat_id=-1001883504324, 
        #    text="Нове замовлення"
        #)