#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from typing import List, Tuple


conn = sqlite3.connect("shop1.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                tg_id INT PRIMARY KEY,
                phone TEXT,
                balance FLOAT DEFAULT 0.00, 
                address TEXT,
                prise INT, 
                order_1 TEXT
                )""")


# Добавляет юзера
def new_user(tg_id: int):
    try:
        cursor.execute(
            f"INSERT INTO users (tg_id) VALUES ({tg_id})")
        conn.commit()
    except:
        print('Такой юзер уже есть')
    

def get_acc(tg_id: int):
    cursor.execute(f"SELECT * FROM users WHERE tg_id={tg_id}")
    rows = cursor.fetchall()
    return rows


def update(column: str, value, tg_id: int):
    cursor.execute(
        f"UPDATE users SET {column}=? WHERE tg_id={tg_id}", 
        (value,))
    conn.commit()


def clear_table(tg_id):
    cursor.execute(f"UPDATE users SET prise='', order_1='' WHERE tg_id={tg_id}")
    conn.commit()

