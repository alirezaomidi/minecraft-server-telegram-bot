import argparse
import logging
from telegram.ext import Updater, CommandHandler


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


if __name__ == '__main__':
    # configure CLI parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help='The Token of the bot, provided by @BotFather', type=str, required=True)
    args = parser.parse_args()
    print(args)

    # configure log level
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # create an bot updater 
    updater = Updater(token=args.token, use_context=True)
    dispatcher = updater.dispatcher

    # creater command handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', start)

    # register command handlers
    dispatcher.add_handler(start_handler)

    # start the bot
    updater.start_polling()