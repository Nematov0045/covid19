import telebot
import  requests
import datetime
# token_API = "https://covid-api.mmediagroup.fr/v1/cases?country={country}"
token = '2084402201:AAEp_fM31RFNMG2K-_JaaMDLk4WtURcnJH4'
# covid= requests.get(token_API.format(country='Kyrgyzstan'))
# covid_json=covid.json()
# print(covid_json['All']['confirmed'])
bot = telebot.TeleBot(token)
# @bot.message_handler(commands=['Kyrgyzstan','k'])
# def send_start(message):
    # bot.reply_to(message,'work')
@bot.message_handler(content_types='text')
def send_start(message):

    country=message.text.title()
    # print("country")
    token_API = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
    covid= requests.get(token_API)
    covid_json=covid.json()
    time=datetime.datetime.now()
    print(covid_json['All']['confirmed'])
    c=f"дата:{time.day}:{time.month}:{time.year},число заболевших:{covid_json['All']['confirmed']}"
    bot.send_message(message.chat.id,c)

print("Bot is working!")
bot.infinity_polling()
