#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


account = KeyboardButton('ACCOUNT')
shop = KeyboardButton('SHOP')
policy = KeyboardButton('TERMS & CONDITIONS')
support = KeyboardButton('SUPPORT')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
greet_kb.add(account, shop, policy, support)


pay = InlineKeyboardButton('💰 PAY', callback_data='PAY')
btn_pay = InlineKeyboardMarkup(row_width=1).add(pay)


back_1 = InlineKeyboardButton('⬅️ BACK', callback_data='BACK')
back_docs = InlineKeyboardButton('⬅️ BACK', callback_data='BACK 2')


replenish = InlineKeyboardButton('💰 REPLENISH', callback_data='REPLENISH')
btn_replenish = InlineKeyboardMarkup(row_width=1).add(replenish)


сancel = InlineKeyboardButton('СANCEL', callback_data='СANCEL')
btn_сancel = InlineKeyboardMarkup(row_width=1).add(сancel)


a = InlineKeyboardButton('📰 DOCUMENTS', callback_data='DOCS')
b = InlineKeyboardButton('🔎 LOOK UP INFO', callback_data='LOOK UP INFO')
c = InlineKeyboardButton('🗓 FULL INFO', callback_data='FULL INFO')
d = InlineKeyboardButton('🕹 OWN REGISTERED BANK ACC.', callback_data='OWN REGISTERED BANK ACCOUNTS')
e = InlineKeyboardButton('💳 CC ENROLL', callback_data='CC ENROLL')
f = InlineKeyboardButton('💵 BRUT BANK ACCOUNTS', callback_data='BRUT BANK ACCOUNTS')
g = InlineKeyboardButton('📲 REAL USA NUMBER FOR SMS', callback_data='REAL USA NUMBER FOR SMS')

a_real_num = InlineKeyboardButton('ONE SMS - 5$', callback_data='ONE SMS - 5$')
real_num = InlineKeyboardMarkup(row_width=1).add(a_real_num)


h = InlineKeyboardButton('🇺🇸 US DOCUMENTS', callback_data='US DOCS')
j = InlineKeyboardButton('🇨🇦 CA DOCUMENTS', callback_data='CA DOCS')
l = InlineKeyboardButton('🇪🇺 EU DOCUMENTS', callback_data='EU DOCS')
k = InlineKeyboardButton('🌎 SOUTH AMERICA DOCUMENTS', callback_data='NORTH AMERICA DOCS')


a_ua_docs = InlineKeyboardButton('DL FRONT - 40$', callback_data='DL FRONT - 40$')
b_ua_docs = InlineKeyboardButton('DL FRONT & BACK - 60$', callback_data='DL FRONT & BACK - 60$')
c_ua_docs = InlineKeyboardButton('PASSPORT - 40$', callback_data='PASSPORT - 40$')
d_ua_docs = InlineKeyboardButton('SSN FRONT - 25$', callback_data='SSN FRONT - 25$')
e_ua_docs = InlineKeyboardButton('SSN FRONT & BACK - 40$', callback_data='SSN FRONT & BACK - 40$')
f_ua_docs = InlineKeyboardButton('UTILITY BILL - 30$', callback_data='UTILITY BILL - 30$')
g_ua_docs = InlineKeyboardButton('BANK STATEMENT - 35$', callback_data='BANK STATEMENT - 35$')
h_ua_docs = InlineKeyboardButton('DL 2 SIDE + SELFIE - 135$', callback_data='DL 2 SIDE + SELFIE - 135$')
j_ua_docs = InlineKeyboardButton('CC FRONT + BACK SIDE - 50$', callback_data='CC FRONT + BACK SIDE - 50$')
l_ua_docs = InlineKeyboardButton('TAX FROM 1040 & 1099 - 40$', callback_data='TAX FROM 1040 & 1099 - 40$')
k_ua_docs = InlineKeyboardButton('PAYSTUB - 40$', callback_data='PAYSTUB - 40$')


docs = InlineKeyboardMarkup(row_width=1).add(a, b, c, d, e, f, g)
docs_2 = InlineKeyboardMarkup(row_width=1).add(h, j, l, k, back_1)
us_docs = InlineKeyboardMarkup(row_width=1).add(a_ua_docs, b_ua_docs, c_ua_docs, d_ua_docs, e_ua_docs, f_ua_docs, g_ua_docs, h_ua_docs, j_ua_docs, l_ua_docs, k_ua_docs, back_docs)
ca_docs = InlineKeyboardMarkup(row_width=1).add(a_ua_docs, b_ua_docs, c_ua_docs, f_ua_docs, g_ua_docs, h_ua_docs, j_ua_docs, back_docs)
eu_docs = InlineKeyboardMarkup(row_width=1).add(a_ua_docs, b_ua_docs, c_ua_docs, f_ua_docs, g_ua_docs, h_ua_docs, j_ua_docs, back_docs)
na_docs = InlineKeyboardMarkup(row_width=1).add(a_ua_docs, b_ua_docs, c_ua_docs, f_ua_docs, g_ua_docs, h_ua_docs, j_ua_docs, back_docs)


a_full_info = InlineKeyboardButton('FULL INFO - 5$', callback_data='FULL INFO 2 - 5$')
b_full_info = InlineKeyboardButton('FULL INFO + DL - 17$', callback_data='FULL INFO + DL - 17$')
c_full_info = InlineKeyboardButton('FULL INFO CS 400-599 - 10$', callback_data='FULL INFO CS 400-599 - 10$')
d_full_info = InlineKeyboardButton('FULL INFO CS 600-699 - 15$', callback_data='FULL INFO CS 600-699 - 15$')
e_full_info = InlineKeyboardButton('FULL INFO CS 700-799 - 20$', callback_data='FULL INFO CS 700-799 - 20$')
f_full_info = InlineKeyboardButton('FULL INFO CS 800-899 - 45$', callback_data='FULL INFO CS 800-899 - 45$')
full_info = InlineKeyboardMarkup(row_width=1).add(a_full_info, b_full_info, c_full_info, d_full_info, e_full_info, f_full_info, back_1)


a_cc_enroll = InlineKeyboardButton('0.5-1k - 90$', callback_data='0.5-1k - 90$')
b_cc_enroll = InlineKeyboardButton('1k-3k - 150$', callback_data='1k-3k - 150$')
c_cc_enroll = InlineKeyboardButton('3k-5k - 200$', callback_data='3k-5k - 200$')
d_cc_enroll = InlineKeyboardButton('5k-10k - 400$', callback_data='5k-10k - 400$')
e_cc_enroll = InlineKeyboardButton('>10k - 550$', callback_data='>10k - 550$')
cc_enroll = InlineKeyboardMarkup(row_width=1).add(a_cc_enroll, b_cc_enroll, c_cc_enroll, d_cc_enroll, e_cc_enroll, back_1)

a_brut_bank_accounts = InlineKeyboardButton('0.5-1k - 50$', callback_data='bba 0.5-1k - 50$')
b_brut_bank_accounts = InlineKeyboardButton('1k-3k - 100$', callback_data='bba 1k-3k - 100$')
c_brut_bank_accounts = InlineKeyboardButton('3k-5k - 150$', callback_data='bba 3k-5k - 150$')
d_brut_bank_accounts = InlineKeyboardButton('5k-10k - 250$', callback_data='bba 5k-10k - 250$')
e_brut_bank_accounts = InlineKeyboardButton('>10k - 300$', callback_data='bba >10k - 300$')
brut_bank_accounts = InlineKeyboardMarkup(row_width=1).add(a_brut_bank_accounts, b_brut_bank_accounts, c_brut_bank_accounts, d_brut_bank_accounts, e_brut_bank_accounts, back_1)


a_own_reg_bank_acc = InlineKeyboardButton('CITI BANK - 75$', callback_data='CITI BANK - 75$')
b_own_reg_bank_acc = InlineKeyboardButton('BBT BANK - 75$', callback_data='BBT BANK - 75$')
c_own_reg_bank_acc = InlineKeyboardButton('CHASE BANK - 75$', callback_data='CHASE BANK - 75$')
d_own_reg_bank_acc = InlineKeyboardButton('TD BANK - 75$', callback_data='TD BANK - 75$')
e_own_reg_bank_acc = InlineKeyboardButton('CHIME BANK + VCC - 75$', callback_data='CHIME BANK + VCC - 75$')
own_reg_bank_acc = InlineKeyboardMarkup(row_width=1).add(a_own_reg_bank_acc, b_own_reg_bank_acc, c_own_reg_bank_acc, d_own_reg_bank_acc, e_own_reg_bank_acc, back_1)


a_look_up = InlineKeyboardButton('🇺🇸 US DOB + SNN - 20$', callback_data='US DOB + SNN - 20$')
b_look_up = InlineKeyboardButton('🇺🇸 US DRIVER LICENSE - 40$', callback_data='US DRIVER LICENSE - 40$')
c_look_up = InlineKeyboardButton('🇺🇸 US MMN - 35$', callback_data='US MMN - 35$')
d_look_up = InlineKeyboardButton('🇺🇸 US BACKGROUND REPORT - 25$', callback_data='US BACKGROUND REPORT - 25$')
e_look_up = InlineKeyboardButton('🇺🇸 US CREDIT REPORT - 35$', callback_data='US CREDIT REPORT - 35$')
f_look_up = InlineKeyboardButton('🇺🇸 US VEHICLE LOOK UP - 40$', callback_data='US VEHICLE LOOK UP - 40$')
g_look_up = InlineKeyboardButton('🇬🇧 UK SNN + DOB - 20$', callback_data='UK SNN + DOB  - 20$')
h_look_up = InlineKeyboardButton('SPECIAL ORDER', callback_data='SPECIAL ORDER')
look_up = InlineKeyboardMarkup(row_width=1).add(a_look_up, b_look_up, c_look_up, d_look_up, e_look_up, f_look_up, g_look_up, h_look_up, back_1)

