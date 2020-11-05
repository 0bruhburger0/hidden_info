#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
from block_io import BlockIo
from db import update
from config import BTC_PIN, BTC_TOKEN, BTC_VERSION


version = BTC_VERSION
block_io_2 = BlockIo(BTC_TOKEN, BTC_PIN, version)


# Создание нового адреса
def create_address():
    new_address = block_io_2.get_new_address()
    data = new_address['data']['address']
    return data


# Достает цену битка
def get_price():
    price_btc = block_io_2.get_current_price(price_base='USD')
    return price_btc['data']['prices'][0]['price']


# Достает все транзакции
async def get_lead(sleep_for, address, tg_id):
    while True:
        transactions = block_io_2.get_transactions(type='received')
        for t in transactions['data']['txs']:
            for i in t['amounts_received']:
                recipient = i['recipient']
                amount = i['amount']
                if recipient == address:
                    update('balance', amount, tg_id)
                    return True

        await asyncio.sleep(sleep_for)

