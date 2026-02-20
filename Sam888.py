from telethon.errors import SessionPasswordNeededError, UserDeactivatedBanError, UserDeactivatedError, UserInvalidError, RPCError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl import functions, types
from telethon import TelegramClient, functions, types
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import UserStatusOffline
from datetime import datetime, date
from pytz import timezone
from pystyle import *
import configparser
import inquirer
import asyncio
import getpass
import shutil
import socket
import csv
import os
import sys
import time

class colors:
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
        "{}  _______                _______ _______ _______  {}".format(colors.HEADER, colors.ENDC),
        "{} |   _   .---.-.--------|   _   |   _   |   _   | {}".format(colors.OKBLUE, colors.ENDC),
        "{} |   1___|  _  |        |.  |   |.  |   |.  |   | {}".format(colors.OKGREEN, colors.ENDC),
        "{} |____   |___._|__|__|__|.  _   |.  _   |.  _   | {}".format(colors.WARNING, colors.ENDC),
        "{} |:  1   |              |:  1   |:  1   |:  1   | {}".format(colors.FAIL, colors.ENDC),
        "{} |::.. . |              |::.. . |::.. . |::.. . | {}".format(colors.HEADER, colors.ENDC),
        "{} `-------'              `-------`-------`-------' {}".format(colors.OKBLUE, colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Sam888 Software by @ItKhmerSoftware", colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Version: 1.0.0", colors.ENDC),
    ]

    for line in art_lines:
        centered_line = center_text(line)
        print(centered_line)

def bannerLoginAccounts():
    art_lines = [
        "{}  ___                __         _______                             __   {}".format(colors.HEADER, colors.ENDC),
        "{} |   |  .-----.-----|__.-----.|   _   .----.----.-----.--.--.-----|  |_  {}".format(colors.OKBLUE, colors.ENDC),
        "{} |.  |  |  _  |  _  |  |     ||.  1   |  __|  __|  _  |  |  |     |   _| {}".format(colors.OKGREEN, colors.ENDC),
        "{} |.  |__|_____|___  |__|__|__||.  _   |____|____|_____|_____|__|__|____| {}".format(colors.WARNING, colors.ENDC),
        "{} |:  1   |    |_____|         |:  |   |                                  {}".format(colors.FAIL, colors.ENDC),
        "{} |::.. . |                    |::.|:. |                                  {}".format(colors.HEADER, colors.ENDC),
        "{} `-------'                    `--- ---'                                  {}".format(colors.OKBLUE, colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Sam888 Software by @ItKhmerSoftware", colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Version: 1.0.0", colors.ENDC),
    ]
    for line in art_lines:
        centered_line = center_text(line)
        print(centered_line)
        
def bannerCheckSpamBotMessages():
    art_lines = [
        "{}  _______ __               __    _______                       {}".format(colors.HEADER, colors.ENDC),
        "{} |   _   |  |--.-----.----|  |--|   _   .-----.---.-.--------. {}".format(colors.OKBLUE, colors.ENDC),
        "{} |.  1___|     |  -__|  __|    <|   1___|  _  |  _  |        | {}".format(colors.OKGREEN, colors.ENDC),
        "{} |.  |___|__|__|_____|____|__|__|____   |   __|___._|__|__|__| {}".format(colors.WARNING, colors.ENDC),
        "{} |:  1   |                      |:  1   |__|                   {}".format(colors.FAIL, colors.ENDC),
        "{} |::.. . |                      |::.. . |                      {}".format(colors.HEADER, colors.ENDC),
        "{} `-------'                      `-------'                      {}".format(colors.OKBLUE, colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Sam888 Software by @ItKhmerSoftware", colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Version: 1.0.0", colors.ENDC),
    ]
    for line in art_lines:
        centered_line = center_text(line)
        print(centered_line)
        
def bannerSendMessage():
    art_lines = [
        "{}  _______                __ ___ ___                                      {}".format(colors.HEADER, colors.ENDC),        
        "{} |   _   .-----.-----.--|  |   Y   .-----.-----.-----.---.-.-----.-----. {}".format(colors.OKBLUE, colors.ENDC),        
        "{} |   1___|  -__|     |  _  |.      |  -__|__ --|__ --|  _  |  _  |  -__| {}".format(colors.OKGREEN, colors.ENDC),        
        "{} |____   |_____|__|__|_____|. \_/  |_____|_____|_____|___._|___  |_____| {}".format(colors.WARNING, colors.ENDC),        
        "{} |:  1   |                 |:  |   |                       |_____|       {}".format(colors.FAIL, colors.ENDC),        
        "{} |::.. . |                 |::.|:. |                                     {}".format(colors.HEADER, colors.ENDC),        
        "{} `-------'                 `--- ---'                                     {}".format(colors.OKBLUE, colors.ENDC), 
        "{}{:^78}{}".format(colors.HEADER, "Sam888 Software by @ItKhmerSoftware", colors.ENDC),
        "{}{:^78}{}".format(colors.HEADER, "Version: 1.0.0", colors.ENDC),
    ]
    for line in art_lines:
        centered_line = center_text(line)
        print(centered_line)

def main():
    try:
        banner()
        print(f"{colors.OKBLUE}{Box.DoubleCube(f'Use arrow key to select the options')}{colors.ENDC}")
        questions = [
            inquirer.List('list', message=f"{colors.WARNING}Select Option{colors.ENDC}", choices=['Login Accounts', 'Check Spam Account','Scrape Member', 'Send message to users', 'Exit'])
        ]

        answers = inquirer.prompt(questions)
        if answers['list'] == 'Login Accounts':
            asyncio.run(loginacc())  
        elif answers['list'] == 'Check Spam Account':
            asyncio.run(check_spam_bot_messages())
        elif answers['list'] == 'Send message to users':
            asyncio.run(send_message_to_users())  
        elif answers['list'] == 'Scrape Member':
            asyncio.run(scrape_member())  
        elif answers['list'] == 'Exit':
            print(f"{colors.OKGREEN}Exiting the program...{colors.WHITE}")
            sys.exit()
        else:
            print(f"{colors.FAIL}Invalid option selected{colors.WHITE}")

    except Exception as e:
        print(f"{colors.FAIL}An error occurred: {str(e)}{colors.WHITE}")
    finally:
        print(f"{colors.HEADER}Press enter to exit{colors.ENDC}")
        input()
        sys.exit()

async def loginacc():
    os.system('cls')
    bannerLoginAccounts()

    config = configparser.ConfigParser()
    config.read('setting.ini')
    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    phone_number_file = os.path.join(os.getcwd(), 'Phone Number.txt')

    try:
        with open(phone_number_file, 'r') as file:
            phone_numbers_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"File {phone_number_file} not found")
        return

    session_dir = os.path.join(os.getcwd(), 'Session')
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    for phone_number in phone_numbers_list:
        if not phone_number.strip():
            continue
        session_file = os.path.join(session_dir, f'{phone_number}.session')
        client = TelegramClient(session_file, api_id, api_hash)
        await client.connect()

        try:
            if not await client.is_user_authorized():
                print(f"   Sending code request to {phone_number}")
                await client.send_code_request(phone_number)
                code = input('   Enter the code you received: ')
                try:
                    await client.sign_in(phone_number, code)
                except SessionPasswordNeededError:
                    while True:
                        try:
                            password = getpass.getpass(f'   ! Enter the Two-step verification password: ')
                            await client.sign_in(password=password)
                            break
                        except Exception as e:
                            print(f"   {colors.FAIL}Invalid password. Please try again.{colors.WHITE}")

                except UserDeactivatedBanError:
                    print(f"   {colors.FAIL}This account ({phone_number}) has been banned.{colors.WHITE}")
                    continue
                except UserDeactivatedError:
                    print(f"   {colors.FAIL}This account ({phone_number}) has been deleted.{colors.WHITE}")
                    continue
                except Exception as e:
                    print(f"   {colors.FAIL}The phone code entered was invalid: {str(e)}{colors.WHITE}")
                    await client.disconnect()
                    continue
            
            me = await client.get_me()
            if me:
                print(f"{colors.OKGREEN}   User '{me.first_name if me.first_name else ''} {me.last_name if me.last_name else ''}' is logged in successfully.{colors.WHITE}")

        except UserDeactivatedBanError:
            print(f"   {colors.FAIL}This account ({phone_number}) has been banned.{colors.WHITE}")
        except UserDeactivatedError:
            print(f"   {colors.FAIL}This account ({phone_number}) has been deleted.{colors.WHITE}")
        except Exception as e:
            print(f"   {colors.FAIL}An error occurred for {phone_number}: {str(e)}{colors.WHITE}")
        finally:
            await client.disconnect()

    print(f"{colors.OKGREEN}All accounts processed.{colors.WHITE}")

async def check_spam_bot_messages():
    os.system('cls')
    bannerCheckSpamBotMessages()
    
    print(f'{colors.OKBLUE}Checking messages from @SpamBot{colors.ENDC}')

    config = configparser.ConfigParser()
    config.read('setting.ini')

    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    phone_file = os.path.join(os.getcwd(), 'Phone Number.txt')
    
    try:
        with open(phone_file, 'r') as file:
            phone_numbers_list = file.read().splitlines()
            if not phone_numbers_list:
                print(f"{colors.FAIL}No phone numbers found in {phone_file}{colors.WHITE}")
                return
    except FileNotFoundError:
        print(f"{colors.FAIL}File {phone_file} not found{colors.WHITE}")
        return

    for phone_number in phone_numbers_list:
        if not phone_number.strip():
            continue
        session_file = os.path.join(os.getcwd(), 'Session', f'{phone_number}.session')
        client = TelegramClient(session_file, api_id, api_hash)
        
        try:
            await client.start()

            spam_bot_dialog = None
            async for dialog in client.iter_dialogs():
                if dialog.name == 'SpamBot' or (dialog.entity and hasattr(dialog.entity, 'username') and dialog.entity.username == 'SpamBot'):
                    spam_bot_dialog = dialog
                    break

            if spam_bot_dialog:
                print(f'{colors.OKBLUE}[{phone_number}] Sending /start command to @SpamBot{colors.ENDC}')
                await client.send_message(spam_bot_dialog.id, '/start')

                await asyncio.sleep(5) 

                messages = await client.get_messages(spam_bot_dialog.id, limit=1)

                if messages:
                    message = messages[0]
                    if message.text:
                        print(f'{colors.OKGREEN}[{phone_number}] Message Text: {message.text}{colors.ENDC}')
                else:
                    print(f'{colors.FAIL}[{phone_number}] No messages found from @SpamBot{colors.ENDC}')
            else:
                print(f'{colors.FAIL}[{phone_number}] No dialog found with @SpamBot{colors.ENDC}')

        except Exception as e:
            print(f"{colors.FAIL}Error with {phone_number}: {str(e)}{colors.WHITE}")
        finally:
            await client.disconnect()

async def scrape_member():
    os.system('cls')
    banner()
    config = configparser.ConfigParser()
    config.read("setting.ini")
    
    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    
    link1 = config['SellLicense'].get('from_group', '').strip()
    if not link1:
        link1 = input(f"{colors.WARNING}Enter Group/Channel link to scrape from: {colors.WHITE}")
        
    phone_file = os.path.join(os.getcwd(), 'Phone Number.txt')

    try:
        with open(phone_file, 'r') as file:
            phone_numbers_list = [p for p in file.read().splitlines() if p.strip()]
            if not phone_numbers_list:
                print(f"{colors.FAIL}No phone numbers found in {phone_file}{colors.WHITE}")
                return
    except FileNotFoundError:
        print(f"{colors.FAIL}File {phone_file} not found{colors.WHITE}")
        return

    phone = phone_numbers_list[0]
    print(f"{colors.OKGREEN}Scraping all members with account: {colors.OKBLUE}'{phone}'{colors.ENDC}")

    session_file = os.path.join(os.getcwd(), 'Session', f'{phone}.session')
    client = TelegramClient(session_file, api_id, api_hash)
    await client.connect()
    
    if not await client.is_user_authorized():
        print(f"{colors.FAIL}❖ Error: Account {phone} not logged in. Please login first (Option 1){colors.ENDC}")
        await client.disconnect()
        return

    try:
        group = await client.get_entity(link1)
        channel_full_info = await client(GetFullChannelRequest(group))
        total_members = channel_full_info.full_chat.participants_count

        count = 1

        def write(group_title, member):
            nonlocal count
            username = member.username if member.username else ''
            status = 'offline'
            if isinstance(member.status, UserStatusOffline):
                status = member.status.was_online.strftime('%Y-%m-%d %H:%M:%S')
            elif member.status:
                status = type(member.status).__name__
            
            writer.writerow([count, username, member.id, member.access_hash, member.first_name, group_title, status, 'All'])
            count += 1

        with open("data.csv", "w", encoding='UTF-8', newline='') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(['Index', 'Username', 'User ID', 'Access Hash', 'First Name', 'Group', 'Status', 'Type'])
            
            try:
                index = 0
                async for member in client.iter_participants(group, aggressive=True):
                    print(f"\rProgress: {index + 1}/{total_members}", end="")
                    if index % 100 == 0 and index > 0:
                        await asyncio.sleep(1)
                    if not member.bot:
                        write(group.title if hasattr(group, 'title') else 'Unknown', member)
                    index += 1
            except Exception as e:
                print(f"\n{colors.FAIL}Error occurred during scraping: {str(e)}. Check data.csv for partial results.{colors.ENDC}")

        print(f"\n{colors.OKGREEN}Scraping complete! {count-1} users saved to data.csv.{colors.ENDC}")
    finally:
        await client.disconnect()

async def send_message_to_users():
    os.system('cls')
    bannerSendMessage()
    config = configparser.ConfigParser()
    config.read('setting.ini')

    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    phone_number_file = os.path.join(os.getcwd(), 'Phone Number.txt')
    delay_chat_to_users = int(config['SellLicense']['delay_chat_to_users'])
    limit_chat = int(config['SellLicense']['limit_chat'])
    image_message_file = os.path.join(os.getcwd(), 'image_message.csv')
    

if __name__ == "__main__":
    main()