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
    bot.send_message(message.chat.id,"سلام یه بازو قیمت لحظه ای ارز های دیجیتال و طلا و ارز کشور های دیگه خوش آمدی")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('نرخ ارز دیجیتال', 'نرخ ارز کشور ها')
    markup.add('نرخ طلا و سکه')
    bot.send_message(message.chat.id, "از خدمات زیر میتوانید استفاده کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'نرخ طلا و سکه')
def gold_price(message):
    response = requests.get(BASE_URL + f'v1/prices/json/gold?x-api-key={API_KEY}')
    raw_dict = json.loads(response.text)
    price_dict = raw_dict['data']['prices']
    bot.send_message(message.chat.id,f"تاریخ: {raw_dict['data']['date']}\n"
                     f"قیمت طلا 18 عیار: {price_dict['GOLD18K']['current']} تومان \n"
                     f"قیمت طلا 24 عیار: {price_dict['GOLD24K']['current']} تومان \n"
                     f"قیمت مظنه طلا: {price_dict['MAZANEH']['current']} تومان \n"
                     f"قیمت انس طلا: {price_dict['GOLD18K']['current']} تومان \n"
                     f"قیمت سکه طلا1 گرمی: {price_dict['SEKE_1G']['current']} تومان \n"
                     f"قیمت سکه تمام بهار: {price_dict['SEKE_BAHAR']['current']} تومان \n"
                     f"قیمت نیم سکه: {price_dict['SEKE_NIM']['current']} تومان \n"
                     f"قیمت ربع سکه: {price_dict['SEKE_ROB']['current']} تومان \n"
                     f"قیمت سکه پارسیان 100 صوتی: {price_dict['SEKE_PRS100']['current']} تومان \n"
                     f"قیمت سکه پارسیان 200 صوتی: {price_dict['SEKE_PRS200']['current']} تومان \n"
                     f"قیمت سکه پارسیان نیم گرمی: {price_dict['SEKE_PRS500']['current']} تومان \n"
                     )

@bot.message_handler(func=lambda message: message.text == 'نرخ ارز دیجیتال')
def crypto_price(message):
    response = requests.get(BASE_URL + f'v1/prices/json/crypto?x-api-key={API_KEY}')
    raw_dict = json.loads(response.text)
    price_dict = raw_dict['data']['prices']
    bot.send_message(message.chat.id, f"تاریخ: {raw_dict['data']['date']}\n"
                f"قیمت بیتکوین : {price_dict['BTC']['current']} تومان \n"
                f"قیمت اتریوم : {price_dict['ETH']['current']} تومان \n"
                f"قیمت تتر : {price_dict['USDT']['current']} تومان \n"
                f"قیمت ریپل : {price_dict['XRP']['current']} تومان \n"
                     )
@bot.message_handler(func=lambda message: message.text == 'نرخ ارز کشور ها')
def currency_price(message):
    response = requests.get(BASE_URL + f'v1/prices/json/currency?x-api-key={API_KEY}')
    raw_dict = json.loads(response.text)
    price_dict = raw_dict['data']['prices']
    bot.send_message(message.chat.id, f"تاریخ: {raw_dict['data']['date']}\n"
                f"قیمت دلار آمریکا : {price_dict['USD']['current']} تومان \n"
                f"قیمت یورو : {price_dict['EUR']['current']} تومان \n"
                f"قیمت پوند : {price_dict['GBP']['current']} تومان \n"
                f"قیمت درهم امارات : {price_dict['AED']['current']} تومان \n"
                f"قیمت لیر ترکیه : {price_dict['TRY']['current']} تومان \n"
                     )

bot.infinity_polling()