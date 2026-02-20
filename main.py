from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8027606714:AAGvA3-G6MUh3msrvOZsVMAftBnM5pahUqQ"

async def poll_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poll = update.message.poll
    
    if poll.type == "quiz":
        question = poll.question
        options = [opt.text for opt in poll.options]
        correct = poll.correct_option_id
        
        await update.message.delete()
        
        await update.effective_chat.send_poll(
            question="NEW NAME - " + question,
            options=options,
            type="quiz",
            correct_option_id=correct
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.POLL, poll_handler))
app.run_polling()
