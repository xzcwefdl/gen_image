from confing import *
import telebot

from kodland.gen_image import confing
from logic import Text2ImageAPI
bot = telebot.TeleBot(confing.token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "подожди куда спешишь очередь")
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', YOUR_API_KEY, SECRET)
    model_id = api.get_model()
    uuid = api.generate(message.text, model_id)
    images = api.check_generation(uuid)[0]
    api.save_image(images, "image.jpg")

    with ("image.jpg", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
     bot.infinity_polling()