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
    print(f"Hello! Welcome to the main menu.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())