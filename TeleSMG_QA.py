from telethon.errors import SessionPasswordNeededError, UserDeactivatedBanError, UserDeactivatedError, UserInvalidError, RPCError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl import functions, types
from telethon import TelegramClient, functions, types
from telethon.sync import TelegramClient
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
    ]
    for line in art_lines:
        centered_line = center_text(line)
        print(centered_line)
        
def header():
    print(f'{colors.OKGREEN}This Script is officially activated to: {colors.FAIL}t.me/it_computer_khmer')
    print(f'{colors.OKGREEN}        ')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(f'{colors.OKGREEN}Your IP: {colors.FAIL}{str(s.getsockname()[0])}             {colors.OKGREEN}Version: {colors.FAIL}v1.3')
    print(f'{colors.OKGREEN}Current Directory: {colors.FAIL}{os.getcwd()}')

    format = "%d-%m-%Y %I:%M:%S %p"
    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Bangkok'))
    print(f'{colors.OKGREEN}Current time in {colors.OKBLUE}Asia/Bangkok {colors.OKGREEN}time zone: {colors.FAIL}{now_asia.strftime(format)}')
    print(' ')

def main():
    try:
        banner()
        header()
        print(f"{colors.OKBLUE}{Box.DoubleCube(f'Use arrow key to select the options')}{colors.ENDC}")
        questions = [
            inquirer.List('list', message=f"{colors.WARNING}Select Option{colors.ENDC}", choices=['Login Accounts', 'Check Spam Account', 'Send message to users', 'Exit'])
        ]

        answers = inquirer.prompt(questions)
        if answers['list'] == 'Login Accounts':
            asyncio.run(loginacc())  
        elif answers['list'] == 'Check Spam Account':
            asyncio.run(check_spam_bot_messages())
        elif answers['list'] == 'Send message to users':
            asyncio.run(send_message_to_users())  
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
        
async def send_reaction(client, channel, message_id):
    try:
        reaction_emoji = types.ReactionEmoji(emoticon='❤️')
        await client(functions.messages.SendReactionRequest(
            peer=channel,
            msg_id=message_id,
            big=True,
            add_to_recent=True,
            reaction=[reaction_emoji]
        ))
    except Exception:
        pass

async def loading_animation(stop_event):
    while not stop_event.is_set():
        for dots in range(1, 4):
            if stop_event.is_set():
                break
            print(f'\r{colors.WARNING}Verifying{"." * dots}{colors.WHITE}   ', end="", flush=True)
            await asyncio.sleep(1)
    print(f'\r{colors.HEADER}Verifying complete!{colors.WHITE}\n', end="", flush=True)

async def loginacc():
    os.system('cls')
    bannerLoginAccounts()

    config = configparser.ConfigParser()
    config.read('setting.ini')
    api_id = config['Selllicense']['api_id']
    api_hash = config['Selllicense']['api_hash']
    phone_number_file = os.path.join(os.getcwd(), 'Phone Number.txt')

    try:
        with open(phone_number_file, 'r') as file:
            phone_numbers_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"File {phone_number_file} not found")
        return

    for phone_number in phone_numbers_list:
        session_dir = os.path.join(os.getcwd(), 'Session')
        if not os.path.exists(session_dir):
            os.makedirs(session_dir)

        session_file = os.path.join(session_dir, f'{phone_number}.session')

        client = TelegramClient(session_file, api_id, api_hash)
        await client.connect()

        try:
            if not await client.is_user_authorized():
                print(f"Sending code request to {phone_number}")
                await client.send_code_request(phone_number)
                code = input('   Enter the code you received: ')
                try:
                    await client.sign_in(phone_number, code)
                except SessionPasswordNeededError:
                    while True:
                        try:
                            password = getpass.getpass(f'{colors.WHITE} ! Enter the Two-step verification password: ')
                            await client.sign_in(password=password)
                            break
                        except Exception as e:
                            print(f"{colors.FAIL}Invalid password. Please try again.{colors.WHITE}")

                except UserDeactivatedBanError:
                    print(f"{colors.FAIL}This account ({phone_number}) has been banned.{colors.WHITE}")
                    continue  # Skip to the next account
                except UserDeactivatedError:
                    print(f"{colors.FAIL}This account ({phone_number}) has been deleted.{colors.WHITE}")
                    continue  # Skip to the next account
                except Exception as e:
                    print(f"{colors.FAIL}The phone code entered was invalid{colors.WHITE}")
                    await client.disconnect()
                    return
                    sys.exit() 
            else:
                me = await client.get_me()
                print(f"{colors.OKGREEN}⚛ User '{me.first_name} {me.last_name}' is logged in successfully.{colors.WHITE}")
                await client(JoinChannelRequest('@it_computer_khmer'))
                await client(functions.account.UpdateProfileRequest(
                    about='Software by @it_computer_khmer'
                ))

            channel_username = '@it_computer_khmer'
            channel = await client.get_entity(channel_username)
            channel_entity = types.InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)

            messages = []
            async for message in client.iter_messages(channel_entity, limit=5):
                messages.append(message)

            stop_event = asyncio.Event()
            loading_task = asyncio.create_task(loading_animation(stop_event))

            for message in reversed(messages):
                await send_reaction(client, channel_entity, message.id)

            stop_event.set()
            await loading_task
            await client.disconnect()

        except UserDeactivatedBanError:
            print(f"{colors.FAIL}This account ({phone_number}) has been banned.{colors.WHITE}")
        except UserDeactivatedError:
            print(f"{colors.FAIL}This account ({phone_number}) has been deleted.{colors.WHITE}")
        except Exception as e:
            print(f"{colors.FAIL}An error occurred: {str(e)}{colors.WHITE}")
        finally:
            await client.disconnect()

    sys.exit() 

async def check_spam_bot_messages():
    os.system('cls')
    bannerCheckSpamBotMessages()
    
    print(f'{colors.OKBLUE}Checking messages from @SpamBot{colors.ENDC}')

    config = configparser.ConfigParser()
    config.read('setting.ini')

    api_id = config['Selllicense']['api_id']
    api_hash = config['Selllicense']['api_hash']
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
        session_file = os.path.join(os.getcwd(), 'Session', f'{phone_number}.session')
        client = TelegramClient(session_file, api_id, api_hash)
        await client.start()

        spam_bot_dialog = None
        async for dialog in client.iter_dialogs():
            if dialog.name == 'SpamBot' or dialog.entity.username == 'SpamBot':
                spam_bot_dialog = dialog
                break

        if spam_bot_dialog:
            print(f'{colors.OKBLUE}Sending /start command to @SpamBot{colors.ENDC}')
            await client.send_message(spam_bot_dialog.id, '/start')

            # Wait a short period to allow the bot to respond
            await asyncio.sleep(5)  # Adjust sleep time if needed

            print(f'{colors.OKBLUE}Retrieving the latest response from @SpamBot{colors.ENDC}')
            messages = await client.get_messages(spam_bot_dialog.id, limit=1)  # Retrieve the latest message

            if messages:
                message = messages[0]  # Get the latest message
                if message.text:
                    print(f'{colors.OKGREEN}Message Text: {message.text}{colors.ENDC}')
            else:
                print(f'{colors.FAIL}No messages found from @SpamBot{colors.ENDC}')
        else:
            print(f'{colors.FAIL}No dialog found with @SpamBot{colors.ENDC}')

        await client.disconnect()

async def send_message_to_users():
    os.system('cls')
    bannerSendMessage()
    config = configparser.ConfigParser()
    config.read('setting.ini')

    api_id = config['Selllicense']['api_id']
    api_hash = config['Selllicense']['api_hash']
    phone_number_file = os.path.join(os.getcwd(), 'Phone Number.txt')
    delay_chat_to_users = int(config['Selllicense']['delay_chat_to_users'])
    limit_chat = int(config['Selllicense']['limit_chat'])
    not_sending_file = os.path.join(os.getcwd(), 'not_sending.csv')
    already_send_file = os.path.join(os.getcwd(), 'already_send.csv')
    date_file = os.path.join(os.getcwd(), 'last_run_date.txt')
    image_message_file = os.path.join(os.getcwd(), 'image_message.csv')
    continue_sending = config['Selllicense'].get('continue', 'No').strip().lower() == 'yes'
    
    limit_phone_numbers = 1
    
    if not os.path.exists(phone_number_file):
        with open(phone_number_file, 'w') as file:
            file.write('')
    
    with open(phone_number_file, 'r') as file:
        phone_numbers_list = file.read().splitlines()
    
    if not phone_numbers_list:
        print(f"{colors.FAIL}No phone numbers found in {phone_number_file}{colors.WHITE}")
        return
    
    if len(phone_numbers_list) > limit_phone_numbers:
        print(f"{colors.FAIL}---> No more than {limit_phone_numbers} phone number(s) allowed.{colors.WHITE}")
        print(f"{colors.FAIL}---> Contact the developer for more information.{colors.WHITE}")
        return
    
    not_sending_users = set()
    if os.path.exists(not_sending_file):
        with open(not_sending_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            not_sending_users = {row[0] for row in reader if row and len(row) > 0} 
    
    already_sent_users = set()
    if os.path.exists(already_send_file):
        with open(already_send_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                user_id = row[0].lstrip('\ufeff') 
                already_sent_users.add(int(user_id))
    
    last_run_date = None
    if os.path.exists(date_file):
        with open(date_file, 'r') as file:
            last_run_date = file.read().strip()

    today_date = date.today().isoformat()
    
    if not continue_sending and last_run_date != today_date:
        already_sent_users.clear()
        with open(already_send_file, 'w', encoding='utf-8-sig') as file:
            pass

    if os.path.exists(already_send_file):
        with open(already_send_file, 'r+', encoding='utf-8-sig', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            if headers != ['User Id', "User Name", 'Message', 'Date Sent', 'Images Sent']:
                file.seek(0)
                writer = csv.writer(file)
                writer.writerow(['User Id', "User Name", 'Message', 'Date Sent', 'Images Sent'])
                file.writelines(file.readlines())

    image_messages = []
    if os.path.exists(image_message_file):
        with open(image_message_file, 'r', encoding='utf-8') as file:
            image_messages = [row[0] for row in csv.reader(file) if row]
            
    if len(image_messages) > 1:
        print(f"{colors.FAIL}More than one image message, please use only 1 image only.{colors.WHITE}")
        print(f"{colors.FAIL}---> Contact the developer for more information.{colors.WHITE}")
        return
    
    flood_wait_count = 0  # Counter for FloodWaitError occurrences
    max_flood_wait_errors = 5  # Maximum allowed FloodWaitError before termination

    for phone_index, phone_number in enumerate(phone_numbers_list[:limit_phone_numbers], start=1):
        session_file = os.path.join(os.getcwd(), 'Session', f'{phone_number}.session')
        client = TelegramClient(session_file, api_id, api_hash)
        
        try:
            await client.start()
            
            if not os.path.exists("message.txt"):
                print(f"{colors.FAIL}message.txt not found!{colors.WHITE}")
                return
            
            with open("message.txt", "r", encoding="utf-8") as file:
                message_text = file.read().strip()
            
            if not message_text:
                print(f"{colors.FAIL}Message file is empty!{colors.WHITE}")
                return
            
            users = []
            async for dialog in client.iter_dialogs():
                if dialog.is_user and not dialog.entity.bot:
                    users.append((dialog.id, dialog.name))
            
            if users:
                print(f"\n     {colors.HEADER}Index: {phone_index} - {colors.OKBLUE}Detected {len(users)} users you have chatted with:{colors.WHITE}")
                
                for i, (user_id, name) in enumerate(users, start=1):
                    print(f"{colors.WARNING}{i}. {colors.OKGREEN}{name}{colors.ENDC}  --  {colors.FAIL}(ID: {user_id}){colors.ENDC}")
                
                users_to_chat = [user for user in users if user[1] not in not_sending_users and user[0] not in already_sent_users]
                users_to_chat = users_to_chat[:limit_chat]
                print(f"\n{colors.WARNING}Limiting to chat with {len(users_to_chat)} users.{colors.WHITE}")
                
                for i, (user_id, name) in enumerate(users_to_chat, start=1):
                    should_delay = True  # Flag to determine if delay should be applied
                    try:
                        if image_messages:
                            await client.send_file(user_id, image_messages, caption=message_text)
                            images_sent = ', '.join(image_messages) if image_messages else 'NONE'
                        else:
                            await client.send_message(user_id, message_text)
                            images_sent = 'NONE'
                        print(f"{colors.WARNING}{i}. {colors.OKGREEN}Message sent to {colors.FAIL}{name}{colors.ENDC}")
                        already_sent_users.add(user_id) 
                        with open(already_send_file, 'a', encoding='utf-8-sig', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([user_id, name, message_text, datetime.now().strftime('%d-%b-%y %I:%M %p'), images_sent])
                        flood_wait_count = 0  # Reset counter on successful send
                    except (UserDeactivatedError, UserInvalidError) as e:
                        print(f"{colors.FAIL}{i}. Skipped {colors.WARNING}{name}: Account deleted or invalid ({str(e)}){colors.WHITE}")
                        not_sending_users.add(str(user_id))
                        with open(not_sending_file, 'a', encoding='utf-8', newline='') as file: 
                            writer = csv.writer(file)
                            writer.writerow([user_id])
                        should_delay = False  # Skip delay for deleted accounts
                        flood_wait_count = 0  # Reset counter on deleted account
                    except FloodWaitError as e:
                        flood_wait_count += 1
                        print(f"{colors.FAIL}{i}. Failed to send message to {colors.WARNING}{name}: Too many requests (FloodWaitError, attempt {flood_wait_count}/{max_flood_wait_errors}){colors.WHITE}")
                        if flood_wait_count >= max_flood_wait_errors:
                            print(f"{colors.FAIL} Please Check your account or go to check spam bot messages.{colors.WHITE}")
                            await client.disconnect()
                            return  # Exit the function, terminating the script
                        await asyncio.sleep(e.seconds)  # Respect the flood wait time
                        should_delay = False  # Skip additional delay after flood wait
                    except RPCError as e:
                        if "user was deleted" in str(e).lower():
                            print(f"{colors.FAIL}{i}. Skipped {colors.WARNING}{name}: Account deleted ({str(e)}){colors.WHITE}")
                            not_sending_users.add(str(user_id))
                            with open(not_sending_file, 'a', encoding='utf-8', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([user_id])
                            should_delay = False  # Skip delay for deleted accounts
                            flood_wait_count = 0  # Reset counter on deleted account
                        else:
                            print(f"{colors.FAIL}{i}. Failed to send message to {colors.WARNING}{name}: {str(e)}{colors.WHITE}")
                    except Exception as e:
                        print(f"{colors.FAIL}{i}. Failed to send message to {colors.WARNING}{name}: {str(e)}{colors.WHITE}")
                    if should_delay:
                        await asyncio.sleep(delay_chat_to_users)  # Apply delay only if should_delay is True
            else:
                print(f"{colors.FAIL}No previous chat users detected.{colors.WHITE}")
        except Exception as e:
            print(f"{colors.FAIL}An error occurred: {str(e)}{colors.WHITE}")
        finally:
            await client.disconnect()

    with open(date_file, 'w') as file:
        file.write(today_date)

if __name__ == "__main__":
    main()