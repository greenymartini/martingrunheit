from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__, template_folder="templates")
english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("chatb.html")


@app.route("/get")
def get_bot_response():
    userInput = request.args.get('msg')
    return str(english_bot.get_response(userInput))


if __name__ == "__main__":
    app.run(debug=True)
