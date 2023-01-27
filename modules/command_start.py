import modules.bot_start
import modules.keyboard_creation
import modules.user_start
@modules.bot_start.bot.message_handler(commands=["start"])
def bot_start(message):
    modules.bot_start.bot.send_message(
        message.chat.id, "Hi user!", 
        reply_markup=modules.keyboard_creation.bar 
    )
    modules.bot_start.bot.register_next_step_handler(
    message, 
    modules.user_start.send_message_user
    )