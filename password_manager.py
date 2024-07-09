#!/usr/bin/env python
import sqlite3
from enum import Enum
import random
from passlib.hash import pbkdf2_sha256


class PasswordManager:
    def generate_password():
        password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_-='
        return ''.join(random.choice(password_characters) for _ in range(10))
        
    
    def save_account_credentials():
        pass

    def view_accounts():
        pass

    def remove_account():
        pass


class Database:
    def connect():
        sql_connection = sqlite3.connect('user.db')
        sql_cursor = sql_connection.cursor()
        return [sql_connection, sql_cursor]

    def create_table():
        sql_cursor = Database.connect()
        table = """CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(150) NOT NULL, 
        password VARCHAR(200) NOT NULL);""" 
        sql_cursor[1].execute(table)
   
    def get_data():
        pass

    def insert_data(username, password):
        sql_cursor = Database.connect()
        Database.create_table()
        sql_cursor[1].execute("""INSERT INTO user(username, password) VALUES(?, ?)""", (username, password))
        sql_cursor[0].commit()
        sql_cursor[0].close()

class User:
    def create_account(username, password):
        Database.insert_data(username, pbkdf2_sha256.hash(password))
        

    def signin():
        pass

    def signout():
        pass
    
class Menu(Enum):
    FIRSTITEM = "1: Login"
    SECONDITEM = "2: Create an account"
    THIRDITEM = "3: Generate a password"


def main():
    print('''
     ***********************************
     *                                 *
     *  . . . Password Manager . . .   *
     *                                 *
     ***********************************
    ''')

    for menu in (Menu):
       print(menu.value)

    print("\n")
    userInput = int(input('Enter your choice: '))  
    if userInput == 1:
       pass
    elif userInput == 2:
        print("\n")
        username = input('Enter your username: ')
        print("\n")
        password = input('Enter your password: ')
        User.create_account(username, password)
        print("\n")
        print("Account created")
        print("\n")
    elif userInput == 3:
       print("\n")
       print(f'Here is your password: {PasswordManager.generate_password()}')
       print("\n")
       




if __name__ == '__main__':
    main()