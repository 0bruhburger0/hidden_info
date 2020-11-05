#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiogram, config, btn, bitcoin
from db import new_user, get_acc, update, clear_table
from aiogram import executor, Bot, Dispatcher, types, filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import ParseMode
from block_io import BlockIo


dp = Bot(config.TOKEN)
bot = Dispatcher(dp)


# Обработчик /start
@bot.message_handler(commands=['start'])
async def start(message: types.Message):
    tg_id = message.from_user.id
    new_user(tg_id) # Добавляет юзера
    await dp.send_message(tg_id, config.hi, reply_markup=btn.greet_kb, parse_mode=ParseMode.HTML)


# Кнопки-клавиатура
@bot.message_handler()
async def send(message: types.Message):
    tg_id = message.from_user.id
    if message.text == "ACCOUNT":
        data = get_acc(tg_id)
        await dp.send_message(tg_id, f'<b>Id:</b> {data[0][0]}\n<b>Balance:</b> {data[0][2]}', reply_markup=btn.btn_replenish, parse_mode=ParseMode.HTML)
    elif message.text == "SHOP":
        await dp.send_message(tg_id, 'SHOP', reply_markup=btn.docs, parse_mode=ParseMode.HTML)
    elif message.text == "TERMS & CONDITIONS":
        await dp.send_message(tg_id, config.policy, reply_markup=btn.greet_kb, parse_mode=ParseMode.HTML)
    elif message.text == "SUPPORT":
        await dp.send_message(tg_id, config.support, reply_markup=btn.greet_kb, parse_mode=ParseMode.HTML)
    else:
        await dp.send_message(tg_id, config.error, reply_markup=btn.greet_kb, parse_mode=ParseMode.HTML)


# Разделы и товары
@bot.callback_query_handler(lambda call: True)
async def process_callback_admin(call):
    tg_id = call.from_user.id
    msg = call.message.message_id
    data = get_acc(tg_id)
    btc = bitcoin.get_price()
    

    # Отправляет сообщения после оплаты оплаты
    if call.data == 'BACK':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='SHOP', reply_markup=btn.docs, parse_mode=ParseMode.HTML)
    # if call.data == 'BACK 2':
    #     await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='SHOP', reply_markup=btn.docs, parse_mode=ParseMode.HTML)
    elif call.data == 'REPLENISH':
        dt = bitcoin.create_address()
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=f'<b>To top up your account transfer bitcoins to this address - <code>{dt}</code></b>', parse_mode=ParseMode.HTML)
        await bitcoin.get_lead(10, dt, tg_id)
        update('address', dt, tg_id)
    elif call.data == 'СANCEL':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=f'<b>Id:</b> {data[0][0]}\n<b>Balance:</b> {data[0][2]}', reply_markup=btn.btn_replenish, parse_mode=ParseMode.HTML)
    elif call.data == 'PAY':
        prise = data[0][4]
        order_1 = data[0][5]
        balance = float(data[0][2])
        if balance >= prise:
            if order_1 == 'DL FRONT':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.dl_front, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'DL FRONT & BACK':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.dl_front_back, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'UTILITY BILL':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.utility_bill, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'BANK STATEMENT':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.bank_statement, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'DL FRONT & BACK + SELFIE':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.dl_front_back_selfie, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'CC Front & Back side':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.cc_front_back_side, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'TAX FORM 1090 or 1040':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.tax_form_1090_or_1040, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'PAYSTUB':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.paystub, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'SSN FRONT & BACK':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.ssn_front_back, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'SSN FRONT':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.ssn_front, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            

            elif order_1 in ('FULL INFO 2', 'FULL INFO + DL', 'FULL INFO CS 800-899', 'FULL INFO CS 700-799', 'FULL INFO CS 600-699', 'FULL INFO CS 400-599'):
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.full_info, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            

            elif order_1 in ('0.5-1k', '>10k', '5k-10k', '3k-5k', '1k-3k'):
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.enroll, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)

            
            elif order_1 == 'US DOB + SNN':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.us_dob_ssn, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'US DRIVER LICENSE':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.us_driver_license, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'US MMN':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.us_mmn, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'US BACKGROUND REPORT':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.us_background_report, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'US CREDIT REPORT':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.us_credit_report, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'US VEHICLE LOOK UP':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.us_vehicle_look_up, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'UK SNN + DOB':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.uk_ssn_dob, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            elif order_1 == 'SPECIAL ORDER':
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.special_order, parse_mode=ParseMode.HTML)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)
            

            elif order_1 in ('CHIME BANK + VCC', 'TD BANK', 'CHASE BANK', 'BBT BANK', 'CITI BANK'):
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.bank, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)

            
            elif order_1 in ('>10k', '5k-10k', '3k-5k', '1k-3k', '0.5-1k'):
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.brut, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)

            
            elif order_1 == "ONE SMS":
                await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=config.sms, parse_mode=ParseMode.HTML)
                new_balance = balance - prise
                update('balance', new_balance, tg_id)
                clear_table(tg_id)
                await support(order_1, call.from_user.username)

        # Если не хватает средств на балансе 
        else:
            await dp.edit_message_text(chat_id=tg_id, message_id=msg, text=f'❌ Insufficient funds\n\n<b>Id:</b> {data[0][0]}\n<b>Balance:</b> {data[0][2]}', reply_markup=btn.btn_replenish, parse_mode=ParseMode.HTML)


    # Основные разделы
    elif call.data == 'REAL USA NUMBER FOR SMS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='REAL USA NUMBER FOR SMS', reply_markup=btn.real_num, parse_mode=ParseMode.HTML)
    elif call.data == 'BRUT BANK ACCOUNTS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='BRUT BANK ACCOUNTS', reply_markup=btn.brut_bank_accounts, parse_mode=ParseMode.HTML)
    elif call.data == 'CC ENROLL':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='CC ENROLL', reply_markup=btn.cc_enroll, parse_mode=ParseMode.HTML)
    elif call.data == 'OWN REGISTERED BANK ACCOUNTS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='OWN REGISTERED BANK ACCOUNTS', reply_markup=btn.own_reg_bank_acc, parse_mode=ParseMode.HTML)
    elif call.data == 'FULL INFO':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='FULL INFO', reply_markup=btn.full_info, parse_mode=ParseMode.HTML)
    elif call.data == 'LOOK UP INFO':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='LOOK UP INFO', reply_markup=btn.look_up, parse_mode=ParseMode.HTML)
    elif call.data in ('DOCS', 'BACK 2'):
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='DOCS', reply_markup=btn.docs_2, parse_mode=ParseMode.HTML)


    # Раздел DOCS
    elif call.data == 'US DOCS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='US DOCS', reply_markup=btn.us_docs, parse_mode=ParseMode.HTML)
    elif call.data == 'CA DOCS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='CA DOCS', reply_markup=btn.ca_docs, parse_mode=ParseMode.HTML)
    elif call.data == 'EU DOCS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='EU DOCS', reply_markup=btn.eu_docs, parse_mode=ParseMode.HTML)
    elif call.data == 'NORTH AMERICA DOCS':
        await dp.edit_message_text(chat_id=tg_id, message_id=msg, text='NORTH AMERICA DOCS', reply_markup=btn.na_docs, parse_mode=ParseMode.HTML)


    # Обработчик кнопок разделов US DOCS, CA DOCS, EU DOCS, NA DOCS
    elif call.data == 'DL FRONT - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nDL FRONT (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "DL FRONT", tg_id)
    elif call.data == 'DL FRONT & BACK - 60$':
        prise = str(60 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nDL FRONT & BACK (60$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "DL FRONT & BACK", tg_id)
    elif call.data == 'PASSPORT - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nPASSPORT (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "PASSPORT", tg_id)
    elif call.data == 'SSN FRONT - 25$':
        prise = str(25 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nSSN FRONT (25$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "SSN FRONT", tg_id)
    elif call.data == 'SSN FRONT & BACK - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nSSN FRONT & BACK (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "SSN FRONT & BACK", tg_id)
    elif call.data == 'UTILITY BILL - 30$':
        prise = str(30 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUTILITY BILL (30$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "UTILITY BILL", tg_id)
    elif call.data == 'BANK STATEMENT - 35$':
        prise = str(35 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nBANK STATEMENT (35$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "BANK STATEMENT", tg_id)
    elif call.data == 'DL 2 SIDE + SELFIE - 135$':
        prise = str(135 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nDL 2 SIDE + SELFIE (135$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', "DL 2 SIDE + SELFIE", tg_id)
    elif call.data == 'CC FRONT + BACK SIDE - 50$':
        prise = str(50 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nCC FRONT + BACK SIDE (50$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "CC FRONT + BACK SIDE", tg_id)
    elif call.data == 'TAX FROM 1040 & 1099 - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nTAX FROM 1040 & 1099 (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "TAX FROM 1040 & 1099", tg_id)
    elif call.data == 'PAYSTUB - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nPAYSTUB (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "PAYSTUB", tg_id)
    

    # Обработчик кнопок раздела FULL INFO
    elif call.data == 'FULL INFO 2 - 5$':
        prise = str(5 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nFULL INFO (5$) - {prise[:7]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:7], tg_id)
        update('order_1', "FULL INFO 2", tg_id)
    elif call.data == 'FULL INFO + DL - 17$':
        prise = str(17 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nFULL INFO + DL (17$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "FULL INFO + DL", tg_id)
    elif call.data == 'FULL INFO CS 400-599 - 10$':
        prise = str(10 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nFULL INFO CS 400-599 (10$) - {prise[:7]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:7], tg_id)
        update('order_1', "FULL INFO CS 400-599", tg_id)
    elif call.data == 'FULL INFO CS 600-699 - 15$':
        prise = str(15 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nFULL INFO CS 600-699 (15$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "FULL INFO CS 600-699", tg_id)
    elif call.data == 'FULL INFO CS 700-799 - 20$':
        prise = str(20 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nFULL INFO CS 700-799 (20$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "FULL INFO CS 700-799", tg_id)
    elif call.data == 'FULL INFO CS 800-899 - 45$':
        prise = str(45 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nFULL INFO CS 800-899 (45$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "FULL INFO CS 800-899", tg_id)
    

    # Обработчик кнопок раздела LOOK UP INFO
    elif call.data == 'US DOB + SNN - 20$':
        prise = str(20 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUS DOB + SNN (20$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "US DOB + SNN", tg_id)
    elif call.data == 'US DRIVER LICENSE - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUS DRIVER LICENSE (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "US DRIVER LICENSE", tg_id)
    elif call.data == 'US MMN - 35$':
        prise = str(35 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUS MMN (35$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "US MMN", tg_id)
    elif call.data == 'US BACKGROUND REPORT - 25$':
        prise = str(25 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUS BACKGROUND REPORT (25$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "US BACKGROUND REPORT", tg_id)
    elif call.data == 'US CREDIT REPORT - 35$':
        prise = str(35 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUS CREDIT REPORT (35$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "US CREDIT REPORT", tg_id)
    elif call.data == 'US VEHICLE LOOK UP - 40$':
        prise = str(40 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUS VEHICLE LOOK UP (40$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "US VEHICLE LOOK UP", tg_id)
    elif call.data == 'UK SNN + DOB  - 20$':
        prise = str(20 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nUK SNN + DOB  (20$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "UK SNN + DOB", tg_id)
    elif call.data == 'SPECIAL ORDER':
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nSPECIAL ORDER', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('order_1', "SPECIAL ORDER", tg_id)


    # Обработчик кнопок раздела OWN REGISTERED BANK ACC.
    elif call.data == 'CITI BANK - 75$':
        prise = str(75 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nCITI BANK (75$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "CITI BANK", tg_id)
    elif call.data == 'BBT BANK - 75$':
        prise = str(75 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nBBT BANK (75$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "BBT BANK", tg_id)
    elif call.data == 'CHASE BANK - 75$':
        prise = str(75 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nCHASE BANK (75$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "CHASE BANK", tg_id)
    elif call.data == 'TD BANK - 75$':
        prise = str(75 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nTD BANK (75$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "TD BANK", tg_id)
    elif call.data == 'CHIME BANK + VCC - 75$':
        prise = str(75 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nCHIME BANK + VCC (75$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "CHIME BANK + VCC", tg_id)
    

    # Обработчик кнопок раздела CC ENROLL
    elif call.data == '0.5-1k - 90$':
        prise = str(90 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n0.5-1k (90$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "0.5-1k", tg_id)
    elif call.data == '1k-3k - 150$':
        prise = str(150 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n1k-3k (150$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', "1k-3k", tg_id)
    elif call.data == '3k-5k - 200$':
        prise = str(200 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n3k-5k (200$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', "3k-5k", tg_id)
    elif call.data == '5k-10k - 400$':
        prise = str(400 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n5k-10k (400$) - {prise[:4]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:4], tg_id)
        update('order_1', "5k-10k", tg_id)
    elif call.data == '>10k - 550$':
        prise = str(550 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n>10k - (550$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', ">10k", tg_id)


    # Обработчик кнопок раздела BRUT BANK ACCOUNTS
    elif call.data == 'bba 0.5-1k - 50$':
        prise = str(50 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n0.5-1k (50$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "bba 0.5-1k", tg_id)
    elif call.data == 'bba 1k-3k - 100$':
        prise = str(100 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n1k-3k (100$) - {prise[:6]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:6], tg_id)
        update('order_1', "bba 1k-3k", tg_id)
    elif call.data == 'bba 3k-5k - 150$':
        prise = str(150 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n3k-5k (150$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', "bba 3k-5k", tg_id)
    elif call.data == 'bba 5k-10k - 250$':
        prise = str(250 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n5k-10k (250$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', "bba 5k-10k", tg_id)
    elif call.data == 'bba >10k - 300$':
        prise = str(300 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\n>10k (300$) - {prise[:5]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:5], tg_id)
        update('order_1', "bba >10k", tg_id)

    
    # Обработчик кнопоки раздела REAL USA NUMBER FOR SMS
    elif call.data == 'ONE SMS - 5$':
        prise = str(5 / float(btc))
        await dp.send_message(chat_id=tg_id, text=f'<b>You chose:</b>\n\nONE SMS (5$) - {prise[:7]}₿', reply_markup=btn.btn_pay, parse_mode=ParseMode.HTML)
        update('prise', prise[:7], tg_id)
        update('order_1', "ONE SMS", tg_id)


async def support(order, username):
    await dp.send_message(chat_id=1316389508, text=f'New order\n\nUsername: @{username}\nOrder: {order}', reply_markup=btn.greet_kb, parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)

