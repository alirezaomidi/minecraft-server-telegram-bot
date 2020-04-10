import argparse
import logging
from telegram.ext import Updater, CommandHandler
from emoji import emojize
import minecraft as mc


HELP_TEXT = '''
Use these commands to interact with me:

/start: See this message.
'''

def start(update, context):
    """
    The /start command of the bot
    Simply greets to the user and shows some help
    """
    text = f'Hi! I can help you to interact with your Minecraft Server. {HELP_TEXT}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def up(update, context):
    """
    The /up command
    Starts the server if it is down.
    """
    msg = context.bot.send_message(chat_id=update.effective_chat.id, text='Checking server status...')
    # check server status
    status = mc.get_status()
    if status == mc.STATUS.UP:
        context.bot.edit_message_text(emojize('The server is already :up:! ', use_aliases=True),
                                      chat_id=update.effective_chat.id, message_id=msg.message_id)
    elif status == mc.STATUS.STARTING:
        context.bot.edit_message_text('The server is already starting...',
                                      chat_id=update.effective_chat.id, message_id=msg.message_id)
    elif status == mc.STATUS.DOWN:
        context.bot.edit_message_text('The server is down. Starting...',
                                      chat_id=update.effective_chat.id, message_id=msg.message_id)
        # TODO: Here we should trigger the start_server job
        # and put responding to the user in a queue
    elif status == mc.STATUS.STOPPING:
        context.bot.edit_message_text('The server is going down. Try again later.',
                                      chat_id=update.effective_chat.id, message_id=msg.message_id)


if __name__ == '__main__':
    # configure CLI parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help='The Token of the bot, provided by @BotFather', type=str, required=True)
    args = parser.parse_args()

    # configure log level
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # create an bot updater 
    updater = Updater(token=args.token, use_context=True)
    dispatcher = updater.dispatcher

    # register command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('up', up))

    # start the bot
    updater.start_polling()