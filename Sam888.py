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
import os
import sys
import time
import random
from datetime import datetime, date
from pytz import timezone
from pystyle import *

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
        with open(phones_path, 'r') as file:
            phone_numbers = file.read().splitlines()
    except FileNotFoundError:
        print(f"File {phones_path} not found")
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

    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    phones_path = os.path.join(os.getcwd(), 'phone_number.txt')
    
    try:
        with open(phones_path, 'r') as file:
            phone_numbers = file.read().splitlines()
            if not phone_numbers:
                print(f"{Colors.FAIL}No phone numbers found in {phones_path}{Colors.WHITE}")
                return
    except FileNotFoundError:
        print(f"{Colors.FAIL}File {phones_path} not found{Colors.WHITE}")
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
    config = configparser.ConfigParser()
    config.read("setting.ini")
    
    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    
    source_group = config['SellLicense'].get('from_group', '').strip()
    if not source_group:
        source_group = input(f"{Colors.WARNING}Enter Group/Channel link to scrape from: {Colors.WHITE}")
        
    phones_path = os.path.join(os.getcwd(), 'phone_number.txt')

    try:
        with open(phones_path, 'r') as file:
            phone_numbers = [p for p in file.read().splitlines() if p.strip()]
            if not phone_numbers:
                print(f"{Colors.FAIL}No phone numbers found in {phones_path}{Colors.WHITE}")
                return
    except FileNotFoundError:
        print(f"{Colors.FAIL}File {phones_path} not found{Colors.WHITE}")
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
    
    config = configparser.ConfigParser()
    config.read('setting.ini')

    api_id = config['SellLicense']['api']
    api_hash = config['SellLicense']['hash']
    delay_min = int(config['SellLicense']['delay_min'])
    delay_max = int(config['SellLicense']['delay_max'])
    
    # Ensure max is not less than min to prevent crash
    if delay_max < delay_min:
        print(f"{Colors.WARNING}Warning: delay_max ({delay_max}) is less than delay_min ({delay_min}). Swapping them.{Colors.WHITE}")
        delay_min, delay_max = delay_max, delay_min
    
    limit_chat = int(config['SellLicense']['limit_chat'])
    
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
            possible_path = f.read().strip()
            if possible_path and os.path.exists(possible_path):
                image_path = possible_path

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

    print(f"{Colors.OKCYAN}Loaded {len(targets)} targets and {len(phones)} accounts.{Colors.WHITE}")
    if image_path:
        print(f"{Colors.OKGREEN}Image found: {image_path}{Colors.WHITE}")
    
    target_index = 0
    for phone in phones:
        if target_index >= len(targets):
            break

        session_file = os.path.join(os.getcwd(), 'Session', phone)
        client = TelegramClient(session_file, api_id, api_hash)
        
        try:
            await client.connect()
            if not await client.is_user_authorized():
                print(f"{Colors.FAIL}[{phone}] Not logged in. Skipping.{Colors.WHITE}")
                continue

            print(f"{Colors.OKGREEN}[{phone}] Successfully logged in. Sending messages...{Colors.WHITE}")
            
            sent_count = 0
            while sent_count < limit_chat and target_index < len(targets):
                username = targets[target_index]
                try:
                    if image_path:
                        await client.send_file(username, image_path, caption=message_text)
                    else:
                        await client.send_message(username, message_text)
                        
                    print(f"{Colors.OKGREEN}[{phone}] Message sent to @{username} ({sent_count + 1}/{limit_chat}){Colors.WHITE}")
                    sent_count += 1
                    target_index += 1
                    
                    if target_index < len(targets) and sent_count < limit_chat:
                        sleep_time = random.randint(delay_min, delay_max)
                        print(f"{Colors.WARNING}Waiting {sleep_time} seconds (randomized)...{Colors.WHITE}")
                        await asyncio.sleep(sleep_time)
                
                except FloodWaitError as e:
                    print(f"{Colors.WARNING}[{phone}] Flood wait for {e.seconds} seconds. Switching account.{Colors.WHITE}")
                    break
                except UserPrivacyRestrictedError:
                    print(f"{Colors.FAIL}[{phone}] Could not send to @{username}: Privacy restricted. Skipping.{Colors.WHITE}")
                    target_index += 1
                except RPCError as e:
                    print(f"{Colors.FAIL}[{phone}] Error sending to @{username}: {str(e)}{Colors.WHITE}")
                    target_index += 1
                except Exception as e:
                    print(f"{Colors.FAIL}[{phone}] Unexpected error: {str(e)}{Colors.WHITE}")
                    target_index += 1

        except Exception as e:
            print(f"{Colors.FAIL}[{phone}] Connection error: {str(e)}{Colors.WHITE}")
        finally:
            await client.disconnect()

    print(f"{Colors.OKGREEN}All tasks completed! Sent messages to {target_index} users.{Colors.WHITE}")

if __name__ == "__main__":
    main()