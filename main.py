import telebot

TOKEN = "5986693247:AAEHjCalzFy6GZpgW41s5WYg34RG39m32Zs"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def greetings(message):
    reply = "Hello. I am simple data collection bot!"
    bot.reply_to(message, reply)
    
    
is_taking_data = False
@bot.message_handler(content_types=['text'])
def message_handler(message):
    chat_id = message.chat.id
    global is_taking_name
    global is_taking_surname
    
    
    if is_taking_data:
        user_name = message.text
        print(user_name)
        
        
        is_taking_name = False
        
    
    
    if is_taking_name:
        user_name = message.text
        print(user_name)
        is_taking_name = False
        is_taking_surname = True
        bot.send_message(chat_id, "Input your surname:")
    
    
    
    
    
    
    if message.text == 'Save user':t
        is_taking_name = True
        
        
        
        
        bot.send_message(chat_id, "Input your Name:")
        
bot.infinity_polling()
