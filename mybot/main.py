from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
token = "2898fea46066070eacdf907c2aee08790049809f17fa45bd6db48d9f5b1aa08c35154915c9f951bc4d7c3"
vk_session = vk_api.VkApi(token=token) #залогинились

session_api = vk_session.get_api() #получили доступ к vk_api
longpoll = VkLongPoll(vk_session) #не пингуем все время сервер сообщений, а longpull сам возвращает статус сообщений при наличии

for event in longpoll.listen(): # пока все запущено
    if event.type == VkEventType.MESSAGE_NEW: #если новое сообщение
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "1":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})

