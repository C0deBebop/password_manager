#!/usr/bin/env python
import sqlite3
from enum import Enum
import random


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
        pass

class User:
    def create_account():
        pass

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
       pass 
    elif userInput == 3:
       print("\n")
       print(f'Here is your password: {PasswordManager.generate_password()}')
       print("\n")
       




if __name__ == '__main__':
    main()