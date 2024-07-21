import telebot 
from config import token
from random import randint
from logic import Pokemon, SuperPoke

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons.keys():
        s_or_c = randint(0, 100)

        if s_or_c >= 50:
            pokemon = Pokemon(username)
        else:
            pokemon = SuperPoke(username)
        
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img()[0])
        bot.send_photo(message.chat.id, pokemon.show_img()[1])
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        bot.send_message(message.chat.id, pokemon.feed())
    else:
        bot.reply_to(message, "Сначала создай покемона с помощью команды /go")


@bot.message_handler(commands=['fight'])
def fight(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Вы должны ответить на сообщение")
        return

    username = message.from_user.username

    username_enemy = message.reply_to_message.from_user.username

    if not (pokemon_enemy := Pokemon.pokemons.get(username_enemy)):
        bot.reply_to(message, "У другого пользователя нет покемона")
        return

    if not (pokemon := Pokemon.pokemons.get(username)):
        bot.reply_to(message, "Сначала создай покемона с помощью команды /go")
        return

    bot.reply_to(message, pokemon.fight(pokemon_enemy))
        
bot.infinity_polling(none_stop=True)