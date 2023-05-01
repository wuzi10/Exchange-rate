from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types

bot = telebot.TeleBot("5857391463:AAG3SH7AVNjHWYmPT4hfUIRQ0rFwus2skQg")

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Cryptocurrency💰")
    btn2 = types.KeyboardButton("Currency💲")
    btn3 = types.KeyboardButton("Help❓")
    kb.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Hello, this is the latest bot that shows the current exchange rate of various currencies. Choose the desired operation", reply_markup=kb)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Cryptocurrency💰":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("BITCOIN (ВТС)")
        btn2 = types.KeyboardButton("TETHER (USDT)")
        btn3 = types.KeyboardButton("ETHEREUM (ETH)")
        btn4 = types.KeyboardButton("Go Back🔙")
        kb.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Choose the desired cryptocurrency", reply_markup=kb)
    if message.text == "Go Back🔙":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Cryptocurrency💰")
        btn2 = types.KeyboardButton("Currency💲")
        btn3 = types.KeyboardButton("Help❓")
        kb.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Hello, this is the latest bot that shows the current exchange rate of various currencies. Choose the desired operation",
                         reply_markup=kb)

    if message.text == "BITCOIN (ВТС)":
        url = "https://www.google.com/finance/quote/BTC-USD?sa=X&ved=2ahUKEwiCgPyFqdL-AhUr_SoKHc6EBQEQ-fUHegQIBhAf"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        time = soup.find("div", class_="ygUjEc")
        result = soup.find("div", class_="YMlKec fxKbKc")
        bot.reply_to(message, f"1 BTC = {result.text}$, updated: {time.text.replace('Disclaimer', '')}")


    if message.text == "TETHER (USDT)":
        url = "https://www.google.com/finance/quote/USDT-USD?sa=X&ved=2ahUKEwjd4trZq9L-AhUw_SoKHe3xC1EQ-fUHegQIBhAf"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        time = soup.find("div", class_="ygUjEc")
        result = soup.find("div", class_="YMlKec fxKbKc")
        bot.reply_to(message, f"1 USDT = {result.text}$, updated: {time.text.replace('Disclaimer', '')}")

    if message.text == "ETHEREUM (ETH)":
        url = "https://www.google.com/finance/quote/ETH-USD?sa=X&ved=2ahUKEwihxe2lrNL-AhXhDRAIHevUBZ8Q-fUHegQIBhAf"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        time = soup.find("div", class_="ygUjEc")
        result = soup.find("div", class_="YMlKec fxKbKc")
        bot.reply_to(message, f"1 ETH = {result.text}$, updated: {time.text.replace('Disclaimer', '')}")

    if message.text == "Currency💲":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Dollar - USD - $")
        btn2 = types.KeyboardButton("Euro - EUR - €")
        btn3 = types.KeyboardButton("Go Back🔙")
        kb.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Choose the desired currency", reply_markup=kb)
    if message.text == "Dollar - USD - $":
        url = "https://www.google.com/finance/quote/USD-UAH?sa=X&ved=2ahUKEwjyt-DYtdT-AhUVz4sKHdylAK4QmY0JegQIBhAd"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        course = soup.find("div", class_="YMlKec fxKbKc")
        time = soup.find("div", class_="ygUjEc")
        bot.reply_to(message, f"1 USD = {course.text} UAH\nupdated: {time.text.replace('Disclaimer', '')}")
    if message.text == "Euro - EUR - €":
        url = "https://www.google.com/finance/quote/EUR-UAH?sa=X&ved=2ahUKEwi217PouNT-AhUDtYsKHRwmAIoQmY0JegQIARAd"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        course = soup.find("div", class_="YMlKec fxKbKc")
        time = soup.find("div", class_="ygUjEc")
        bot.reply_to(message, f"1 USD = {course.text} UAH\nupdated: {time.text.replace('Disclaimer', '')}")

    if message.text == "Help❓":
        bot.reply_to(message, "Any questions? Write your question or suggestion here and soon the administrator will contact you")
    if message.text not in ["Cryptocurrency💰", "Currency💲", "Help❓", "Go Back🔙", "Euro - EUR - €", "Dollar - USD - $", "ETHEREUM (ETH)", "TETHER (USDT)", "BITCOIN (ВТС)"]:
        bot.send_message(586532309, f"User: {message.from_user.username}\nText: {message.text}")



bot.polling(non_stop=True)