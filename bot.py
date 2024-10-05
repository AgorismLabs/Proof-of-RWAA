import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: link to connect wallet
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


async def water(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


async def recycle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: reply text generated by LLM here
    await update.message.reply_text(f'Under construction {update.effective_user.first_name}')


app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("connect", hello))
app.add_handler(CommandHandler("water", hello))
app.add_handler(CommandHandler("recycle", hello))
app.add_handler(CommandHandler("bye", hello))

app.run_polling()
