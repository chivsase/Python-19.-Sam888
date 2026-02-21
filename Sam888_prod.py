from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from colorama import Fore
import webbrowser
import requests
import pickle
import wmi
import os
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.errors import (
    SessionPasswordNeededError, 
    UserDeactivatedBanError, 
    UserDeactivatedError, 
    UserInvalidError, 
    RPCError, 
    FloodWaitError,
    UserPrivacyRestrictedError
)
from telethon.tl.functions.channels import JoinChannelRequest, GetFullChannelRequest
from telethon.tl.types import UserStatusOffline
import configparser
import inquirer
import asyncio
import getpass
import shutil
import socket
import csv
import sys
import time
import random
from datetime import datetime, date
from pytz import timezone
from pystyle import *

URL = os.getenv("EMPLOYEE_API_URL", "https://admintool.laarekjewelry.com/api/data/logins")

CREDENTIALS_FILE = "License key.pkl"

TOOL_NAME = "Sam888 V1.0.0"

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer 735cd755208526addbc3050fca7915c704f8187504484eb7fb7182301413",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
}

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[1;36m'
    OKGREEN = '\033[38;5;48m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'
    OPTION = '\033[38;5;208m'

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(300, 250))
        Dialog.setMaximumSize(QtCore.QSize(1000, 700))

        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.label_login = QtWidgets.QLabel(Dialog)
        self.label_login.setFont(font)
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setMinimumSize(QtCore.QSize(300, 51))
        self.label_login.setMaximumSize(QtCore.QSize(1000, 51))
        self.label_login.setGeometry(QtCore.QRect(50, 10, 300, 51))
        self.label_login.setObjectName("label_login")

        self.entry_username = QtWidgets.QLineEdit(Dialog)
        self.entry_username.setGeometry(QtCore.QRect(55, 75, 291, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entry_username.setFont(font)
        self.entry_username.setStyleSheet(
            "QLineEdit {background-color: rgba(0, 0, 0, 0); border: none; "
            "border-bottom: 2px solid rgba(46, 82, 101, 200); color: rgba(0, 0, 0, 240); padding-bottom: 7px;}")
        self.entry_username.setObjectName("username")

        self.entry_password = QtWidgets.QLineEdit(Dialog)
        self.entry_password.setGeometry(QtCore.QRect(55, 135, 291, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entry_password.setFont(font)
        self.entry_password.setStyleSheet(
            "background-color:rgba(0,0,0,0);border:none;"
            "border-bottom:2px solid rgba(46,82,101,200);color:rgba(0,0,0,240);"
            "padding-bottom:7px;"
        )
        self.entry_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_password.setObjectName("password")

        self.button_login = QtWidgets.QPushButton(Dialog)
        self.button_login.setGeometry(QtCore.QRect(65, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet(
            "QPushButton#button_login {background-color: qlineargradient(spread:pad, "
            "x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), "
            "stop: 1 rgba(85, 98, 112, 226)); color: rgba(255, 255, 255, 210); "
            "border-radius: 5px;} QPushButton#button_login:hover {background-color: "
            "qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 "
            "rgba(150, 123, 111, 219), stop: 1 rgba(85, 81, 84, 226));} "
            "QPushButton#button_login:pressed {padding-left: 5px; padding-top: 5px; "
            "background-color: rgba(150, 123, 111, 255);} "
        )
        self.button_login.setObjectName("button_login")

        self.button_telegram = QtWidgets.QPushButton(Dialog)
        self.button_telegram.setGeometry(QtCore.QRect(65, 240, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_telegram.setFont(font)
        self.button_telegram.setStyleSheet(
            "QPushButton#button_telegram {background-color: qlineargradient(spread:pad, "
            "x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(53, 92, 125, 219), stop: "
            "1 rgba(86, 156, 183, 226)); color: rgba(255, 255, 255, 210); border-radius: 5px;} "
            "QPushButton#button_telegram:hover {background-color: qlineargradient(spread:pad, "
            "x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(86, 156, 183, 219), stop: "
            "1 rgba(53, 92, 125, 226));} QPushButton#button_telegram:pressed {padding-left: "
            "5px; padding-top: 5px; background-color: rgba(86, 156, 183, 255);} "
        )
        self.button_telegram.setObjectName("button_telegram")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_login.setText(_translate("Dialog", "L o g I n"))
        self.entry_password.setPlaceholderText(_translate("Dialog", "  Password"))
        self.button_login.setText(_translate("Dialog", "L o g  I n"))
        self.entry_username.setPlaceholderText(_translate("Dialog", "  User Name"))
        self.button_telegram.setText(_translate("Dialog", "Buy tool "))
        self.button_telegram.clicked.connect(open_telegram_channel)
            
class LoginWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        print(f"{colors.WARNING}Checking for User Login...{colors.WHITE}", end='\r')
        if self.auto_login():
            main_menu() 
        else:
            self.setupUi(self)
            self.button_login.clicked.connect(self.authenticate_user)
            self.load_saved_credentials()
            self.show()

    def auto_login(self):
        username, password = load_credentials()
        if username and password:
            data = fetch_employee_data(URL, HEADERS)
            if data:
                login_status, expiration_date = validate_login(data, username, password, TOOL_NAME)
                if login_status == "success":
                    current_system_id = get_system_id()
                    api_system_id = self.get_user_system_id(data, username)
                    if current_system_id == api_system_id:
                        ip_address = self.get_ip_address()
                        self.update_login_info_in_api(username, ip_address)
                        self.username = username
                        self.expiration_date = expiration_date
                        return True
                    else:
                        self.show_message("Wrong computer system ID.")
                        return False
                elif login_status == "wrong_tool":
                    self.show_message("Login failed: User account login has Incorrect tool.")
                    return False
        return False

    def load_saved_credentials(self):
        username, password = load_credentials()
        if username and password:
            self.entry_username.setText(username)
            self.entry_password.setText(password)

    def authenticate_user(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if not username or not password:
            self.show_message("Please enter both username and password.")
            return
        
        current_system_id = get_system_id()
        data = fetch_employee_data(URL, HEADERS)
        if data is None:
            return
        login_status, self.expiration_date = validate_login(data, username, password, TOOL_NAME)

        if login_status == "success":
            api_system_id = self.get_user_system_id(data, username)
            if not api_system_id:
                self.update_system_id_in_api(username, current_system_id)
            elif current_system_id != api_system_id:
                self.show_message("Wrong computer system ID.")
                return
            
            ip_address = self.get_ip_address()
            self.update_login_info_in_api(username, ip_address)
            
            save_credentials(username, password)
            self.username = username
            self.show_message("Login successful! Redirecting to main menu.")
            self.hide()
            main_menu()
        elif login_status == "expired":
            self.show_message("User account has expired.")
            if os.path.exists(CREDENTIALS_FILE):
                os.remove(CREDENTIALS_FILE)
        elif login_status == "wrong_tool":
            self.show_message("Login failed: User account login has Incorrect tool.")
            if os.path.exists(CREDENTIALS_FILE):
                os.remove(CREDENTIALS_FILE)
        else:
            self.show_message("Login failed: Invalid username or password")
            if os.path.exists(CREDENTIALS_FILE):
                os.remove(CREDENTIALS_FILE)

    def update_system_id_in_api(self, username, system_id):
        data = {
            'action': 'update_system_id',
            'username': username,
            'system_id': system_id
        }
        try:
            response = requests.post(URL, json=data, headers=HEADERS)  
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.show_message(f"Failed to update System ID: {e}")
            print(f"Failed to update System ID: {e}")
                
    def update_login_info_in_api(self, username, ip_address):
        data = {
            'action': 'update_login_info',
            'username': username,
            'ip': ip_address
        }
        try:
            response = requests.post(URL, json=data, headers=HEADERS) 
            response.raise_for_status()
            result = response.json()

            if result.get('status') == 'success':
                last_login = result.get('last_login')
                if last_login:
                    pass
                else:
                    self.show_message("Datetime not found in API response. Response content: " + str(result))
                    print("Datetime not found in API response. Response content:", result)
            else:
                self.show_message(f"Failed to update login info: {result.get('message') or 'Unknown error'}")

        except requests.exceptions.RequestException as e:
            self.show_message(f"Failed to update login info: {e}")
        except ValueError:
            self.show_message("Error parsing JSON response. Please check the API response format.")

    def get_ip_address(self):
        try:
            ip_address = requests.get('https://api.ipify.org').text
            return ip_address
        except requests.exceptions.RequestException as e:
            self.show_message(f"Failed to get IP address: {e}")
            return "Unknown"
        
    def get_user_system_id(self, data, username):
        for user in data.get('api_users', []):
            if user.get('username') == username:
                return user.get('system_id')
        return None

    def get_user_info(self, data, username, password):
        for user in data.get('api_users', []):
            if user.get('username') == username and user.get('password') == password:
                expiration_date = user.get('expiration_date')
                return username, expiration_date
        return None, None
    
    def show_message(self, message):
        QtWidgets.QMessageBox.information(self, "Login", message)

def get_system_id():
    c = wmi.WMI()
    system_product = c.Win32_ComputerSystemProduct()[0]
    return system_product.UUID

def fetch_employee_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        QtWidgets.QMessageBox.critical(None, "Error", f"Error fetching data: {e}")
        return None
    
def validate_login(data, username, password, TOOL_NAME):
    if not data or data.get('status') != 'success':
        return None, None
    users = data.get('api_users', [])
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            if username != "admin" and user.get('tool') != TOOL_NAME:
                return "wrong_tool", None
            expiration_date_str = user.get('expiration_date')
            if expiration_date_str:
                if expiration_date_str == "0000-00-00 00:00:00":
                    return "expired", None
                try:
                    expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d %H:%M:%S")
                    if expiration_date < datetime.now():
                        return "expired", None
                    return "success", expiration_date
                except ValueError:
                    print("Date format is incorrect.")
                    return "failed", None
            return "success", None
    return "failed", None

def save_credentials(username, password):
    with open(CREDENTIALS_FILE, "wb") as f:
        pickle.dump((username, password), f)

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        try:
            with open(CREDENTIALS_FILE, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            os.remove(CREDENTIALS_FILE)
            return None, None
    return None, None

def open_telegram_channel():
    webbrowser.open("https://t.me/it_computer_khmer")

def main_menu():
    class Colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        WHITE = '\033[97m'

    def center_text(text):
        terminal_width = shutil.get_terminal_size().columns
        padding = (terminal_width - len(text)) // 2
        return ' ' * padding + text

    def banner():
        art_lines = [
            "{}  _______                _______ _______ _______  {}".format(Colors.HEADER, Colors.ENDC),
            "{} |   _   .---.-.--------|   _   |   _   |   _   | {}".format(Colors.OKBLUE, Colors.ENDC),
            "{} |   1___|  _  |        |.  |   |.  |   |.  |   | {}".format(Colors.OKGREEN, Colors.ENDC),
            "{} |____   |___._|__|__|__|.  _   |.  _   |.  _   | {}".format(Colors.WARNING, Colors.ENDC),
            "{} |:  1   |              |:  1   |:  1   |:  1   | {}".format(Colors.FAIL, Colors.ENDC),
            "{} |::.. . |              |::.. . |::.. . |::.. . | {}".format(Colors.HEADER, Colors.ENDC),
            "{} `-------'              `-------`-------`-------' {}".format(Colors.OKBLUE, Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Sam888 Software by @ItKhmerSoftware", Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Version: 1.0.0", Colors.ENDC),
        ]

        for line in art_lines:
            centered_line = center_text(line)
            print(centered_line)

    def banner_login_accounts():
        art_lines = [
            "{}  ___                __         _______                             __   {}".format(Colors.HEADER, Colors.ENDC),
            "{} |   |  .-----.-----|__.-----.|   _   .----.----.-----.--.--.-----|  |_  {}".format(Colors.OKBLUE, Colors.ENDC),
            "{} |.  |  |  _  |  _  |  |     ||.  1   |  __|  __|  _  |  |  |     |   _| {}".format(Colors.OKGREEN, Colors.ENDC),
            "{} |.  |__|_____|___  |__|__|__||.  _   |____|____|_____|_____|__|__|____| {}".format(Colors.WARNING, Colors.ENDC),
            "{} |:  1   |    |_____|         |:  |   |                                  {}".format(Colors.FAIL, Colors.ENDC),
            "{} |::.. . |                    |::.|:. |                                  {}".format(Colors.HEADER, Colors.ENDC),
            "{} `-------'                    `--- ---'                                  {}".format(Colors.OKBLUE, Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Sam888 Software by @ItKhmerSoftware", Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Version: 1.0.0", Colors.ENDC),
        ]
        for line in art_lines:
            centered_line = center_text(line)
            print(centered_line)
            
    def banner_check_spam_bot():
        art_lines = [
            "{}  _______ __               __    _______                       {}".format(Colors.HEADER, Colors.ENDC),
            "{} |   _   |  |--.-----.----|  |--|   _   .-----.---.-.--------. {}".format(Colors.OKBLUE, Colors.ENDC),
            "{} |.  1___|     |  -__|  __|    <|   1___|  _  |  _  |        | {}".format(Colors.OKGREEN, Colors.ENDC),
            "{} |.  |___|__|__|_____|____|__|__|____   |   __|___._|__|__|__| {}".format(Colors.WARNING, Colors.ENDC),
            "{} |:  1   |                      |:  1   |__|                   {}".format(Colors.FAIL, Colors.ENDC),
            "{} |::.. . |                      |::.. . |                      {}".format(Colors.HEADER, Colors.ENDC),
            "{} `-------'                      `-------'                      {}".format(Colors.OKBLUE, Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Sam888 Software by @ItKhmerSoftware", Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Version: 1.0.0", Colors.ENDC),
        ]
        for line in art_lines:
            centered_line = center_text(line)
            print(centered_line)
            
    def banner_send_message():
        art_lines = [
            "{}  _______                __ ___ ___                                      {}".format(Colors.HEADER, Colors.ENDC),        
            "{} |   _   .-----.-----.--|  |   Y   .-----.-----.-----.---.-.-----.-----. {}".format(Colors.OKBLUE, Colors.ENDC),        
            "{} |   1___|  -__|     |  _  |.      |  -__|__ --|__ --|  _  |  _  |  -__| {}".format(Colors.OKGREEN, Colors.ENDC),        
            "{} |____   |_____|__|__|_____|. \_/  |_____|_____|_____|___._|___  |_____| {}".format(Colors.WARNING, Colors.ENDC),        
            "{} |:  1   |                 |:  |   |                       |_____|       {}".format(Colors.FAIL, Colors.ENDC),        
            "{} |::.. . |                 |::.|:. |                                     {}".format(Colors.HEADER, Colors.ENDC),        
            "{} `-------'                 `--- ---'                                     {}".format(Colors.OKBLUE, Colors.ENDC), 
            "{}{:^78}{}".format(Colors.HEADER, "Sam888 Software by @ItKhmerSoftware", Colors.ENDC),
            "{}{:^78}{}".format(Colors.HEADER, "Version: 1.0.0", Colors.ENDC),
        ]
        for line in art_lines:
            centered_line = center_text(line)
            print(centered_line)

    def main():
        try:
            banner()
            print(f"{Colors.OKBLUE}{Box.DoubleCube(f'Use arrow key to select the options')}{Colors.ENDC}")
            questions = [
                inquirer.List('list', message=f"{Colors.WARNING}Select Option{Colors.ENDC}", choices=['Login Accounts', 'Check Spam Account','Scrape Member', 'Send message to users', 'Exit'])
            ]

            answers = inquirer.prompt(questions)
            if answers['list'] == 'Login Accounts':
                asyncio.run(login_accounts())  
            elif answers['list'] == 'Check Spam Account':
                asyncio.run(check_spam_bot_messages())
            elif answers['list'] == 'Send message to users':
                asyncio.run(send_message_to_username())  
            elif answers['list'] == 'Scrape Member':
                asyncio.run(scrape_members())  
            elif answers['list'] == 'Exit':
                print(f"{Colors.OKGREEN}Exiting the program...{Colors.WHITE}")
                sys.exit()
            else:
                print(f"{Colors.FAIL}Invalid option selected{Colors.WHITE}")

        except Exception as e:
            print(f"{Colors.FAIL}An error occurred: {str(e)}{Colors.WHITE}")
        finally:
            print(f"{Colors.HEADER}Press enter to exit{Colors.ENDC}")
            input()
            sys.exit()

    async def login_accounts():
        os.system('cls')
        banner_login_accounts()

        config = configparser.ConfigParser()
        config.read('setting.ini')
        api_id = config['SellLicense']['api']
        api_hash = config['SellLicense']['hash']
        phones_path = os.path.join(os.getcwd(), 'phone_number.txt')

        try:
            if not api_id or not api_hash:
                print(f"{Colors.FAIL}Error: API ID or API Hash is missing in setting.ini!{Colors.WHITE}")
                return
            api_id = int(api_id)
        except (ValueError, KeyError):
            print(f"{Colors.FAIL}Error: API ID in setting.ini must be a number!{Colors.WHITE}")
            return

        try:
            with open(phones_path, 'r') as file:
                phone_numbers = [line.strip() for line in file if line.strip()]
            if not phone_numbers:
                print(f"{Colors.FAIL}Error: phone_number.txt is empty!{Colors.WHITE}")
                return
        except FileNotFoundError:
            print(f"{Colors.FAIL}Error: {phones_path} not found!{Colors.WHITE}")
            return

        session_dir = os.path.join(os.getcwd(), 'Session')
        if not os.path.exists(session_dir):
            os.makedirs(session_dir)

        for phone in phone_numbers:
            if not phone.strip():
                continue
            session_file = os.path.join(session_dir, phone)
            client = TelegramClient(session_file, api_id, api_hash)
            await client.connect()

            try:
                if not await client.is_user_authorized():
                    print(f"   Sending code request to {phone}")
                    await client.send_code_request(phone)
                    code = input('   Enter the code you received: ')
                    try:
                        await client.sign_in(phone, code)
                    except SessionPasswordNeededError:
                        while True:
                            try:
                                password = getpass.getpass(f'   ! Enter the Two-step verification password: ')
                                await client.sign_in(password=password)
                                break
                            except Exception:
                                print(f"   {Colors.FAIL}Invalid password. Please try again.{Colors.WHITE}")

                    except UserDeactivatedBanError:
                        print(f"   {Colors.FAIL}This account ({phone}) has been banned.{Colors.WHITE}")
                        continue
                    except UserDeactivatedError:
                        print(f"   {Colors.FAIL}This account ({phone}) has been deleted.{Colors.WHITE}")
                        continue
                    except Exception as e:
                        print(f"   {Colors.FAIL}The phone code entered was invalid: {str(e)}{Colors.WHITE}")
                        await client.disconnect()
                        continue
                
                me = await client.get_me()
                if me:
                    print(f"{Colors.OKGREEN}   User '{me.first_name if me.first_name else ''} {me.last_name if me.last_name else ''}' is logged in successfully.{Colors.WHITE}")

            except UserDeactivatedBanError:
                print(f"   {Colors.FAIL}This account ({phone}) has been banned.{Colors.WHITE}")
            except UserDeactivatedError:
                print(f"   {Colors.FAIL}This account ({phone}) has been deleted.{Colors.WHITE}")
            except Exception as e:
                print(f"   {Colors.FAIL}An error occurred for {phone}: {str(e)}{Colors.WHITE}")
            finally:
                await client.disconnect()

        print(f"{Colors.OKGREEN}All accounts processed.{Colors.WHITE}")

    async def check_spam_bot_messages():
        os.system('cls')
        banner_check_spam_bot()
        
        print(f'{Colors.OKBLUE}Checking messages from @SpamBot{Colors.ENDC}')

        config = configparser.ConfigParser()
        config.read('setting.ini')

        try:
            api_id = config['SellLicense']['api']
            api_hash = config['SellLicense']['hash']
            if not api_id or not api_hash:
                print(f"{Colors.FAIL}Error: API ID or API Hash is missing in setting.ini!{Colors.WHITE}")
                return
            api_id = int(api_id)
        except (ValueError, KeyError):
            print(f"{Colors.FAIL}Error: API ID in setting.ini must be a number!{Colors.WHITE}")
            return

        phones_path = os.path.join(os.getcwd(), 'phone_number.txt')
        
        try:
            with open(phones_path, 'r') as file:
                phone_numbers = [line.strip() for line in file if line.strip()]
                if not phone_numbers:
                    print(f"{Colors.FAIL}Error: No phone numbers found in phone_number.txt!{Colors.WHITE}")
                    return
        except FileNotFoundError:
            print(f"{Colors.FAIL}Error: {phones_path} not found!{Colors.WHITE}")
            return

        for phone in phone_numbers:
            if not phone.strip():
                continue
            session_file = os.path.join(os.getcwd(), 'Session', phone)
            client = TelegramClient(session_file, api_id, api_hash)
            
            try:
                await client.connect()
                if not await client.is_user_authorized():
                    print(f"{Colors.FAIL}[{phone}] Not logged in. Please use Option 1 first.{Colors.WHITE}")
                    continue

                spam_bot_dialog = None
                async for dialog in client.iter_dialogs():
                    if dialog.name == 'SpamBot' or (dialog.entity and hasattr(dialog.entity, 'username') and dialog.entity.username == 'SpamBot'):
                        spam_bot_dialog = dialog
                        break

                if spam_bot_dialog:
                    print(f'{Colors.OKBLUE}[{phone}] Sending /start command to @SpamBot{Colors.ENDC}')
                    await client.send_message(spam_bot_dialog.id, '/start')

                    await asyncio.sleep(5) 

                    messages = await client.get_messages(spam_bot_dialog.id, limit=1)

                    if messages:
                        message = messages[0]
                        if message.text:
                            print(f'{Colors.OKGREEN}[{phone}] Message Text: {message.text}{Colors.ENDC}')
                    else:
                        print(f'{Colors.FAIL}[{phone}] No messages found from @SpamBot{Colors.ENDC}')
                else:
                    print(f'{Colors.FAIL}[{phone}] No dialog found with @SpamBot{Colors.ENDC}')

            except Exception as e:
                print(f"{Colors.FAIL}Error with {phone}: {str(e)}{Colors.WHITE}")
            finally:
                await client.disconnect()

    async def scrape_members():
        os.system('cls')
        banner()
        if not os.path.exists("setting.ini"):
            print(f"{Colors.FAIL}Error: setting.ini not found!{Colors.WHITE}")
            return

        config = configparser.ConfigParser()
        config.read("setting.ini")
        
        try:
            api_id = config['SellLicense']['api']
            api_hash = config['SellLicense']['hash']
            if not api_id or not api_hash:
                print(f"{Colors.FAIL}Error: API ID or API Hash is missing in setting.ini!{Colors.WHITE}")
                return
            api_id = int(api_id)
        except (ValueError, KeyError):
            print(f"{Colors.FAIL}Error: API ID in setting.ini must be a number!{Colors.WHITE}")
            return
        
        source_group = config['SellLicense'].get('from_group', '').strip()
        if not source_group:
            print(f"{Colors.WARNING}No 'from_group' found in setting.ini.{Colors.WHITE}")
            source_group = input(f"{Colors.WARNING}Enter Group/Channel link to scrape from: {Colors.WHITE}")
        
        phones_path = os.path.join(os.getcwd(), 'phone_number.txt')

        try:
            with open(phones_path, 'r') as file:
                phone_numbers = [p.strip() for p in file if p.strip()]
                if not phone_numbers:
                    print(f"{Colors.FAIL}Error: No phone numbers found in phone_number.txt!{Colors.WHITE}")
                    return
        except FileNotFoundError:
            print(f"{Colors.FAIL}Error: {phones_path} not found!{Colors.WHITE}")
            return

        phone = phone_numbers[0]
        print(f"{Colors.OKGREEN}Scraping all members with account: {Colors.OKBLUE}'{phone}'{Colors.ENDC}")

        session_file = os.path.join(os.getcwd(), 'Session', phone)
        client = TelegramClient(session_file, api_id, api_hash)
        await client.connect()
        
        if not await client.is_user_authorized():
            print(f"{Colors.FAIL}❖ Error: Account {phone} not logged in. Please login first (Option 1){Colors.ENDC}")
            await client.disconnect()
            return

        me = await client.get_me()
        my_id = me.id

        try:
            group = await client.get_entity(source_group)
            
            # Fetch all admin and owner IDs to exclude them
            admin_and_owner_ids = set()
            async for admin in client.iter_participants(group, filter=types.ChannelParticipantsAdmins()):
                admin_and_owner_ids.add(admin.id)

            channel_full_info = await client(GetFullChannelRequest(group))
            total_members = channel_full_info.full_chat.participants_count

            count = 1

            def write_member(group_title, member):
                nonlocal count
                username = member.username if member.username else ''
                status = 'offline'
                if isinstance(member.status, UserStatusOffline):
                    status = member.status.was_online.strftime('%Y-%m-%d %H:%M:%S')
                elif member.status:
                    status = type(member.status).__name__
                
                csv_writer.writerow([count, username, member.first_name, group_title, status, 'All'])
                count += 1

            with open("data.csv", "w", encoding='UTF-8', newline='') as f:
                csv_writer = csv.writer(f, delimiter=",")
                csv_writer.writerow(['Index', 'Username', 'First Name', 'Group', 'Status', 'Type'])
                
                try:
                    processed = 0
                    async for member in client.iter_participants(group, aggressive=True):
                        print(f"\rProgress: {processed + 1}/{total_members}", end="")
                        if processed % 100 == 0 and processed > 0:
                            await asyncio.sleep(1)
                        
                        # Filter: no bots, must have username, skip own account, skip admins/owners
                        if not member.bot and member.username and member.id != my_id and member.id not in admin_and_owner_ids:
                            write_member(group.title if hasattr(group, 'title') else 'Unknown', member)
                        processed += 1
                except Exception as e:
                    print(f"\n{Colors.FAIL}Error occurred during scraping: {str(e)}. Check data.csv for partial results.{Colors.ENDC}")

            print(f"\n{Colors.OKGREEN}Scraping complete! {count-1} users saved to data.csv.{Colors.ENDC}")
        finally:
            await client.disconnect()

    async def send_message_to_username():
        os.system('cls' if os.name == 'nt' else 'clear')
        banner_send_message()
        
        if not os.path.exists("setting.ini"):
            print(f"{Colors.FAIL}Error: setting.ini not found!{Colors.WHITE}")
            return

        config = configparser.ConfigParser()
        config.read('setting.ini')

        try:
            api_id = config['SellLicense']['api']
            api_hash = config['SellLicense']['hash']
            if not api_id or not api_hash:
                print(f"{Colors.FAIL}Error: API ID or API Hash is missing in setting.ini!{Colors.WHITE}")
                return
            api_id = int(api_id)
            
            delay_min = int(config['SellLicense']['delay_min'])
            delay_max = int(config['SellLicense']['delay_max'])
            limit_chat = int(config['SellLicense']['limit_chat'])
        except (ValueError, KeyError) as e:
            print(f"{Colors.FAIL}Error: Missing or invalid setting in setting.ini ({str(e)}){Colors.WHITE}")
            return
        
        # Ensure max is not less than min to prevent crash
        if delay_max < delay_min:
            print(f"{Colors.WARNING}Warning: delay_max ({delay_max}) is less than delay_min ({delay_min}). Swapping them.{Colors.WHITE}")
            delay_min, delay_max = delay_max, delay_min
        
        phone_number_file = os.path.join(os.getcwd(), 'phone_number.txt')
        data_file = os.path.join(os.getcwd(), 'data.csv')
        message_text_file = os.path.join(os.getcwd(), 'message_text.txt')
        message_image_file = os.path.join(os.getcwd(), 'message_image.txt')

        message_text = ""
        if os.path.exists(message_text_file):
            with open(message_text_file, 'r', encoding='utf-8') as f:
                message_text = f.read().strip()

        image_path = None
        if os.path.exists(message_image_file):
            with open(message_image_file, 'r', encoding='utf-8') as f:
                possible_path = f.read().strip().strip('"').strip("'")
                if possible_path:
                    if os.path.exists(possible_path):
                        image_path = possible_path
                    else:
                        print(f"{Colors.FAIL}Error: Image file not found at: {possible_path}{Colors.WHITE}\n(Please check path in message_image.txt)")
                        return

        if not message_text and not image_path:
            print(f"{Colors.FAIL}Error: Both message_text.txt and message_image.txt (with valid path) are missing or empty!{Colors.WHITE}")
            return

        phones = []
        if os.path.exists(phone_number_file):
            with open(phone_number_file, 'r') as f:
                phones = [line.strip() for line in f if line.strip()]

        if not phones:
            print(f"{Colors.FAIL}Error: No phone numbers found in phone_number.txt!{Colors.WHITE}")
            return

        targets = []
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                for row in reader:
                    if len(row) > 1 and row[1]:  # Ensure username exists
                        targets.append(row[1])

        if not targets:
            print(f"{Colors.FAIL}Error: No targets found in data.csv!{Colors.WHITE}")
            return

        print(f"\n{Colors.HEADER}{'='*50}{Colors.WHITE}")
        print(f"{Colors.OKCYAN}   MESSAGE DELIVERY SUMMARY{Colors.WHITE}")
        print(f"{Colors.HEADER}{'='*50}{Colors.WHITE}")
        print(f" > Total Accounts: {Colors.OKGREEN}{len(phones)}{Colors.WHITE}")
        print(f" > Total Targets : {Colors.OKGREEN}{len(targets)}{Colors.WHITE}")
        print(f" > Message Type  : {Colors.OKGREEN}{'Image + Text' if image_path and message_text else ('Image Only' if image_path else 'Text Only')}{Colors.WHITE}")
        print(f" > Delay Range   : {Colors.OKGREEN}{delay_min}s - {delay_max}s{Colors.WHITE}")
        print(f" > Limit/Account : {Colors.OKGREEN}{limit_chat}{Colors.WHITE}")
        print(f"{Colors.HEADER}{'='*50}{Colors.WHITE}\n")
        
        total_sent = 0
        total_failed = 0
        target_index = 0
        
        for i, phone in enumerate(phones):
            if target_index >= len(targets):
                break

            print(f"{Colors.OKBLUE}[Account {i+1}/{len(phones)}] Connecting to {phone}...{Colors.WHITE}")
            session_file = os.path.join(os.getcwd(), 'Session', phone)
            client = TelegramClient(session_file, api_id, api_hash)
            
            try:
                await client.connect()
                if not await client.is_user_authorized():
                    print(f"{Colors.FAIL}   [!] {phone} is not logged in. Skipping this account.{Colors.WHITE}")
                    continue

                print(f"{Colors.OKGREEN}   [✓] {phone} Authorized. Starting delivery loop...{Colors.WHITE}")
                
                sent_count = 0
                while sent_count < limit_chat and target_index < len(targets):
                    username = targets[target_index]
                    try:
                        print(f"{Colors.WHITE}[{target_index+1}/{len(targets)}] Sending to @{username}...", end=" ", flush=True)
                        if image_path:
                            await client.send_file(username, image_path, caption=message_text)
                        else:
                            await client.send_message(username, message_text)
                            
                        print(f"{Colors.OKGREEN}SENT ✓{Colors.WHITE}")
                        sent_count += 1
                        total_sent += 1
                        target_index += 1
                        
                        if target_index < len(targets) and sent_count < limit_chat:
                            sleep_time = random.randint(delay_min, delay_max)
                            print(f"    {Colors.WARNING}Waiting {sleep_time}s...{Colors.WHITE}")
                            await asyncio.sleep(sleep_time)
                    
                    except FloodWaitError as e:
                        print(f"{Colors.WARNING}FLOOD WAIT!{Colors.WHITE}")
                        print(f"    [!] Account {phone} hit flood limit for {e.seconds}s. Switching...{Colors.WHITE}")
                        break
                    except UserPrivacyRestrictedError:
                        print(f"{Colors.FAIL}PRIVACY RESTRICTED!{Colors.WHITE}")
                        total_failed += 1
                        target_index += 1
                    except RPCError as e:
                        print(f"{Colors.FAIL}RPC ERROR: {str(e)}{Colors.WHITE}")
                        total_failed += 1
                        target_index += 1
                    except Exception as e:
                        print(f"{Colors.FAIL}ERROR: {str(e)}{Colors.WHITE}")
                        total_failed += 1
                        target_index += 1

            except Exception as e:
                print(f"{Colors.FAIL}   [!] Connection error on {phone}: {str(e)}{Colors.WHITE}")
            finally:
                await client.disconnect()

        print(f"\n{Colors.HEADER}{'='*50}{Colors.WHITE}")
        print(f"{Colors.OKCYAN}   DELIVERY PROCESS COMPLETE{Colors.WHITE}")
        print(f"{Colors.HEADER}{'='*50}{Colors.WHITE}")
        print(f" > Total Targets Processed : {target_index}")
        print(f" > Total Messages Sent     : {Colors.OKGREEN}{total_sent}{Colors.WHITE}")
        print(f" > Total Skips/Failed      : {Colors.FAIL}{total_failed}{Colors.WHITE}")
        print(f"{Colors.HEADER}{'='*50}{Colors.WHITE}")

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())