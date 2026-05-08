import telebot
import json
import requests
from dotenv import load_dotenv
from telebot import apihelper
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

load_dotenv()
# api token obtained by bale botfather
API_TOKEN = os.environ.get("API_TOKEN")
#  api key obtained from www.nerkh.io to authorize our requests
API_KEY = os.environ.get("API_KEY")
# base api url where data comes from
BASE_URL = 'https://api.nerkh.io/'

# config telebot package for bale development
apihelper.API_URL = 'https://tapi.bale.ai/bot{0}/{1}'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"سلام یه بازو قیمت لحظه ای ارض های دیجیتال و طلا و ارض کشور های دیگه خوش آمدی")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('نرخ ارض دیجیتال', 'نرخ ارض کشور ها')
    markup.add('نرخ طلا و سکه')
    bot.send_message(message.chat.id, "از خدمات زیر میتوانید استفاده کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'نرخ طلا و سکه')
def gold_price(message):
    response = requests.get(BASE_URL + f'v1/prices/json/gold?x-api-key={API_KEY}')
    dicti = json.loads(response.text)
    bot.send_message(message.chat.id,f"تاریخ: {dicti['data']['date']}\n"
                     f"قیمت طلا 18 عیار: {dicti['data']['prices']['GOLD18K']['current']} تومان \n"
                     f"قیمت طلا 24 عیار: {dicti['data']['prices']['GOLD24K']['current']} تومان \n"
                     f"قیمت مظنه طلا: {dicti['data']['prices']['MAZANEH']['current']} تومان \n"
                     f"قیمت انس طلا: {dicti['data']['prices']['GOLD18K']['current']} تومان \n"
                     f"قیمت سکه طلا1 گرمی: {dicti['data']['prices']['SEKE_1G']['current']} تومان \n"
                     f"قیمت سکه تمام بهار: {dicti['data']['prices']['SEKE_BAHAR']['current']} تومان \n"
                     f"قیمت نیم سکه: {dicti['data']['prices']['SEKE_NIM']['current']} تومان \n"
                     f"قیمت ربع سکه: {dicti['data']['prices']['SEKE_ROB']['current']} تومان \n"
                     f"قیمت سکه پارسیان 100 صوتی: {dicti['data']['prices']['SEKE_PRS100']['current']} تومان \n"
                     f"قیمت سکه پارسیان 200 صوتی: {dicti['data']['prices']['SEKE_PRS200']['current']} تومان \n"
                     f"قیمت سکه پارسیان نیم گرمی: {dicti['data']['prices']['SEKE_PRS500']['current']} تومان \n"
                     )



bot.infinity_polling()