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
flag_7 = 0  # маркер отвечающий за 6 вопрос
flag_8 = 0  # маркер отвечающий за 7 вопрос
flag_9 = 0  # маркер отвечающий за 8 вопрос
flag_10 = 0  # маркер отвечающий за 9 вопрос
flag_11 = 0  # маркер отвечающий за 10 вопрос
flag_12 = 0  # маркер отвечающий за выдачу флага


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


@bot.message_handler(commands=['setting'])
def repeat_help_message(message):
    answer = 'Иди своей дорогой путник....'
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
    global flag_8
    global flag_9
    global flag_10
    global flag_11
    global flag_12

    answer = 'Ну что начнем, но раз уж ты первый, кто зашёл ко мне, я отдам тебе флаг просто так.\n' \
             'Если хочешь напиши "+", если нет  "-".'
    flag_0 = 1
    flag_1 = 0
    flag_2 = 0
    flag_3 = 0
    flag_4 = 0
    flag_5 = 0
    flag_6 = 0
    flag_7 = 0
    flag_8 = 0
    flag_9 = 0
    flag_10 = 0
    flag_11 = 0
    flag_12 = 0

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
    global flag_8
    global flag_9
    global flag_10
    global flag_11
    global flag_12

    # ========Начало вступлния================
    if message.text.lower() == '+' and flag_0 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_1)
        log(message, constant.bot_send_message_begin_1)
        flag_1 = 1

    elif message.text.lower() == '-' and flag_0 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_2)
        log(message, constant.bot_send_message_begin_2)
        flag_2 = 2

    elif message.text.lower() == constant.bot_true_answer_0 and flag_1 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_begin_3)
        log_answer(message, constant.bot_send_message_begin_3, constant.bot_question_0, constant.bot_true_answer_0)
        flag_2 = 2

    elif message.text.lower() != constant.bot_true_answer_0 and flag_1 == 1:
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
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif message.text.lower() == constant.bot_true_answer_1 and flag_2 == 1:
        bot.send_message(message.chat.id, constant.bot_send_message_1_2)
        log_answer(message, constant.bot_send_message_1_2, constant.bot_question_1, constant.bot_true_answer_1)
        flag_3 = 2

    elif message.text.lower() != constant.bot_true_answer_1 and flag_2 == 1:
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
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_3 == 1 and message.text.lower() == constant.bot_true_answer_2:
        bot.send_message(message.chat.id, constant.bot_send_message_2_2)
        log_answer(message, constant.bot_send_message_2_2, constant.bot_question_2, constant.bot_true_answer_2)
        flag_4 = 2

    elif flag_3 == 1 and message.text.lower() != constant.bot_true_answer_2:
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
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_4 == 1 and message.text.lower() == constant.bot_true_answer_3:
        bot.send_message(message.chat.id, constant.bot_send_message_3_2)
        log_answer(message, constant.bot_send_message_3_2, constant.bot_question_3, constant.bot_true_answer_3)
        flag_5 = 2

    elif flag_4 == 1 and message.text.lower() != constant.bot_true_answer_3:
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
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_5 == 1 and message.text.lower() == constant.bot_true_answer_4:
        bot.send_message(message.chat.id, constant.bot_send_message_4_2)
        log_answer(message, constant.bot_send_message_4_2, constant.bot_question_4, constant.bot_true_answer_4)
        flag_6 = 2

    elif flag_5 == 1 and message.text.lower() != constant.bot_true_answer_4:
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
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_6 == 1 and message.text.lower() == constant.bot_true_answer_5:
        bot.send_message(message.chat.id, constant.bot_send_message_5_2)
        log_answer(message, constant.bot_send_message_5_2, constant.bot_question_5, constant.bot_true_answer_5)
        flag_7 = 2

    elif flag_6 == 1 and message.text.lower() != constant.bot_true_answer_5:
        bot.send_message(message.chat.id, constant.bot_send_message_5_3)
        log_answer(message, constant.bot_send_message_5_3, constant.bot_question_5, constant.bot_true_answer_5)
        flag_2 = 2
    # ========Конец Пятого вопроса============

    # ========Шестой вопрос====================
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
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_7 == 1 and message.text.lower() == constant.bot_true_answer_6:
        bot.send_message(message.chat.id, constant.bot_send_message_6_2)
        log_answer(message, constant.bot_send_message_6_2, constant.bot_question_6, constant.bot_true_answer_6)
        flag_8 = 2

    elif flag_7 == 1 and message.text.lower() != constant.bot_true_answer_6:
        bot.send_message(message.chat.id, constant.bot_send_message_6_3)
        log_answer(message, constant.bot_send_message_6_3, constant.bot_question_6, constant.bot_true_answer_6)
        flag_2 = 2
    # ========Конец Шестого вопроса============

    # ========Седьмой вопрос====================
    if flag_8 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_7_1)
        log(message, constant.bot_send_message_7_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0
        flag_8 = 1
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_8 == 1 and message.text.lower() == constant.bot_true_answer_7:
        bot.send_message(message.chat.id, constant.bot_send_message_7_2)
        log_answer(message, constant.bot_send_message_7_2, constant.bot_question_7, constant.bot_true_answer_7)
        flag_9 = 2

    elif flag_8 == 1 and message.text.lower() != constant.bot_true_answer_7:
        bot.send_message(message.chat.id, constant.bot_send_message_7_3)
        log_answer(message, constant.bot_send_message_7_3, constant.bot_question_7, constant.bot_true_answer_7)
        flag_2 = 2
    # ========Конец Седьмого вопроса============

    # ========Восьмой вопрос====================
    if flag_9 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_8_1)
        log(message, constant.bot_send_message_8_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0
        flag_8 = 0
        flag_9 = 1
        flag_10 = 0
        flag_11 = 0
        flag_12 = 0

    elif flag_9 == 1 and message.text.lower() == constant.bot_true_answer_8:
        bot.send_message(message.chat.id, constant.bot_send_message_8_2)
        log_answer(message, constant.bot_send_message_8_2, constant.bot_question_8, constant.bot_true_answer_8)
        flag_10 = 2

    elif flag_9 == 1 and message.text.lower() != constant.bot_true_answer_8:
        bot.send_message(message.chat.id, constant.bot_send_message_8_3)
        log_answer(message, constant.bot_send_message_8_3, constant.bot_question_8, constant.bot_true_answer_8)
        flag_2 = 2
    # ========Конец Восьмого вопроса============

    # ========Девятый вопрос====================
    if flag_10 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_9_1)
        log(message, constant.bot_send_message_9_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0
        flag_8 = 0
        flag_9 = 0
        flag_10 = 1
        flag_11 = 0
        flag_12 = 0

    elif flag_10 == 1 and message.text.lower() == constant.bot_true_answer_9:
        bot.send_message(message.chat.id, constant.bot_send_message_9_2)
        log_answer(message, constant.bot_send_message_9_2, constant.bot_question_9, constant.bot_true_answer_9)
        flag_11 = 2

    elif flag_10 == 1 and message.text.lower() != constant.bot_true_answer_9:
        bot.send_message(message.chat.id, constant.bot_send_message_9_3)
        log_answer(message, constant.bot_send_message_9_3, constant.bot_question_9, constant.bot_true_answer_9)
        flag_2 = 2
    # ========Конец Девятого вопроса============

    # ========Десятый вопрос====================
    if flag_11 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_10_1)
        log(message, constant.bot_send_message_10_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 11
        flag_12 = 0

    elif flag_11 == 1 and message.text.lower() == constant.bot_true_answer_10:
        bot.send_message(message.chat.id, constant.bot_send_message_10_2)
        log_answer(message, constant.bot_send_message_10_2, constant.bot_question_10, constant.bot_true_answer_10)
        flag_12 = 2

    elif flag_11 == 1 and message.text.lower() != constant.bot_true_answer_10:
        bot.send_message(message.chat.id, constant.bot_send_message_10_3)
        log_answer(message, constant.bot_send_message_10_3, constant.bot_question_10, constant.bot_true_answer_10)
        flag_2 = 2
    # ========Конец Десятого вопроса============

    # ========Финальная часть============
    if flag_12 == 2:
        bot.send_message(message.chat.id, constant.bot_send_message_11_1)
        log(message, constant.bot_send_message_11_1)
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        flag_3 = 0
        flag_4 = 0
        flag_5 = 0
        flag_6 = 0
        flag_7 = 0
        flag_7 = 0
        flag_8 = 0
        flag_9 = 0
        flag_10 = 0
        flag_11 = 0
        flag_12 = 1

    elif (flag_12 == 1 and message.text.lower() == '+') or (flag_12 == 1 and message.text.lower() == '-'):
        bot.send_message(message.chat.id, constant.bot_send_message_11_2)
        log(message, constant.bot_send_message_11_2)
    # ========Финальная часть============


bot.polling(none_stop=True, interval=0)

