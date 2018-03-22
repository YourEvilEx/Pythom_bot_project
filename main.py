import telebot
import constant

bot = telebot.TeleBot(constant.token)
print(bot.get_me())
flag_0 = 0  # маркер отвечающий за 0 вопрос
flag_1 = 0  # маркер отвечающий за ответ на 0 вопрос
flag_2 = 0  # маркер отвечающий за 1 вопрос
flag_3 = 0  # маркер отвечающий за 2 вопрос
flag_4 = 0  # маркер отвечающий за 3 вопрос
flag_5 = 0  # маркер отвечающий за 4 вопрос
flag_6 = 0  # маркер отвечающий за 5 вопрос
flag_7 = 0  # маркер отвечающий за выдочу флага


def log(message, answer):
    from datetime import datetime
    print('\n=================================')
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nТекст сообщения = {3}'.format(message.from_user.first_name,
                                                                            message.from_user.last_name,
                                                                            str(message.from_user.id),
                                                                            message.text))
    print('Ответ = ', answer)


def log_answer(message, answer, question, true_answer):
    from datetime import datetime
    print('\n=================================')
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nОтвет пользователя = {3}'.format(message.from_user.first_name,
                                                                               message.from_user.last_name,
                                                                               str(message.from_user.id),
                                                                               message.text))
    print('Вопрос = ', question)
    print('Правильный ответ = ', true_answer)
    print('Ответ бота = ', answer)


@bot.message_handler(commands=['help'])
def repeat_help_message(message):
    answer = 'Тут должна быть помощь, но увы не чем не могу помочь'
    bot.send_message(message.chat.id, answer)
    log(message, answer)


@bot.message_handler(commands=['start'])
def repeat_start_message(message):
    global flag_0
    global flag_1
    global flag_2
    global flag_3
    global flag_4
    global flag_5
    global flag_6
    global flag_7

    answer = 'Ну что начнем, но раз уж ты первый кто ко мне зашел я отдам тебе флаг просто так.\n' \
             'Если хочешь напиши "+" если нет то "-".'
    flag_0 = 1
    flag_1 = 0
    flag_2 = 0
    flag_3 = 0
    flag_4 = 0
    flag_5 = 0
    flag_6 = 0
    flag_7 = 0
    bot.send_message(message.chat.id, answer)
    log(message, answer)


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    global flag_0
    global flag_1
    global flag_2
    global flag_3
    global flag_4
    global flag_5
    global flag_6
    global flag_7

    # ========Начало вступлния================
    if message.text == '+' and flag_0 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_1)
        log(message, constant.bot_send_message_begin_1)
        flag_1 = 1

    elif message.text == '-' and flag_0 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_2)
        log(message, constant.bot_send_message_begin_2)
        flag_2 = 2

    elif message.text == constant.bot_true_answer_0 and flag_1 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_3)
        log_answer(message, constant.bot_send_message_begin_3, constant.bot_question_0, constant.bot_true_answer_0)
        flag_2 = 2

    elif message.text != constant.bot_true_answer_0 and flag_1 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_4)
        log_answer(message, constant.bot_send_message_begin_4, constant.bot_question_0, constant.bot_true_answer_0)
    # ========Конец вступлния================

    # ========Первый вопрос==================
    if flag_2 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_1_1)
        log(message, constant.bot_send_message_1_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 1
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0

    elif message.text == constant.bot_true_answer_1 and flag_2 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_1_2)
        log_answer(message, constant.bot_send_message_1_2, constant.bot_question_1, constant.bot_true_answer_1)
        flag_3 = 2

    elif message.text != constant.bot_true_answer_1 and flag_2 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_1_3)
        log_answer(message, constant.bot_send_message_1_3, constant.bot_question_1, constant.bot_true_answer_1)
        flag_2 = 2
    # ========Конец первого вопроса============

    # ========Второй вопрос====================
    if flag_3 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_2_1)
        log(message, constant.bot_send_message_2_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 1
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0

    elif flag_3 == 1 and message.text == constant.bot_true_answer_2:
        bot.send_message(message.chat.id, constant.bot_send_message_2_2)
        log_answer(message, constant.bot_send_message_2_2, constant.bot_question_2, constant.bot_true_answer_2)
        flag_4 = 2

    elif flag_3 == 1 and message.text != constant.bot_true_answer_2:
        bot.send_message(message.chat.id, constant.bot_send_message_2_3)
        log_answer(message, constant.bot_send_message_2_3, constant.bot_question_2, constant.bot_true_answer_2)
        flag_2 = 2
    # ========Конец второго вопроса============

    # ========Третий вопрос====================
    if flag_4 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_3_1)
        log(message, constant.bot_send_message_3_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 1
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0

    elif flag_4 == 1 and message.text == constant.bot_true_answer_3:
        bot.send_message(message.chat.id, constant.bot_send_message_3_2)
        log_answer(message, constant.bot_send_message_3_2, constant.bot_question_3, constant.bot_true_answer_3)
        flag_5 = 2

    elif flag_4 == 1 and message.text != constant.bot_true_answer_3:
        bot.send_message(message.chat.id, constant.bot_send_message_3_3)
        log_answer(message, constant.bot_send_message_3_3, constant.bot_question_3, constant.bot_true_answer_3)
        flag_2 = 2
    # ========Конец третьего вопроса============

    # ========Четвертый вопрос====================
    if flag_5 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_4_1)
        log(message, constant.bot_send_message_4_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 1
        flag_6 = 0
        flag_7 = 0

    elif flag_5 == 1 and message.text == constant.bot_true_answer_4:
        bot.send_message(message.chat.id, constant.bot_send_message_4_2)
        log_answer(message, constant.bot_send_message_4_2, constant.bot_question_4, constant.bot_true_answer_4)
        flag_6 = 2

    elif flag_5 == 1 and message.text != constant.bot_true_answer_4:
        bot.send_message(message.chat.id, constant.bot_send_message_4_3)
        log_answer(message, constant.bot_send_message_4_3, constant.bot_question_4, constant.bot_true_answer_4)
        flag_2 = 2
    # ========Конец четвертого вопроса============

    # ========Пятый вопрос====================
    if flag_6 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_5_1)
        log(message, constant.bot_send_message_5_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 1
        flag_7 = 0

    elif flag_6 == 1 and message.text == constant.bot_true_answer_5:
        bot.send_message(message.chat.id, constant.bot_send_message_5_2)
        log_answer(message, constant.bot_send_message_5_2, constant.bot_question_5, constant.bot_true_answer_5)
        flag_7 = 2

    elif flag_6 == 1 and message.text != constant.bot_true_answer_5:
        bot.send_message(message.chat.id, constant.bot_send_message_5_3)
        log_answer(message, constant.bot_send_message_5_3, constant.bot_question_5, constant.bot_true_answer_5)
        flag_2 = 2
    # ========Конец Пятого вопроса============

    # ========Финальная часть============
    if flag_7 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_6_1)
        log(message, constant.bot_send_message_6_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 1

    elif (flag_7 == 1 and message.text == '+') or (flag_7 == 1 and message.text == '-'):
        bot.send_message(message.chat.id, constant.bot_send_message_6_2)
        log(message, constant.bot_send_message_6_2)
    # ========Финальная часть============


bot.polling(none_stop=True, interval=0)

