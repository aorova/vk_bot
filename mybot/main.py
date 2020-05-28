from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time

token = "8907473a9dc5cd1491a312f71571f252c452099cfeea74950c091e92ce6a757dac12a3d1e9a178ff7e5c6"
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'привет':

        keyboard.add_button('Викторина 1', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Викторина 2', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Ссылка на группу', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Факты о добровольчестве', color=VkKeyboardColor.PRIMARY)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:

            if response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите интересующее вас действие',keyboard=keyboard)
            #elif response == "начать":
            #    send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)
            elif response=='команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')

            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)
