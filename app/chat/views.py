from flask import render_template, session, redirect, url_for, request
from . import chat
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# chatbot = ChatBot("My ChatterBot")
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")

# @chat.route("/get")
# def get_bot_response():
#     user_text = request.args.get("msg")
#     return str(chatbot.get_response(user_text))

@chat.route("/get")
def get_bot_response():
    return str("Nice question")


@chat.route('/admin_chat')
def admin_chat():
    return render_template('chat/admin_chat.html')


@chat.route('/customer_chat')
def customer_chat():
    return render_template('chat/customer_chat.html')
#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
