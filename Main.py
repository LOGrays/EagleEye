import os
import sys
import time
import subprocess
import yt_dlp
from colorama import Fore, init, Style
from datetime import datetime
import itertools
init(autoreset=True)

REMOTE_SCRIPT_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/main.py"
VERSION = "1.0.0"


# Initialize colorama
init(autoreset=True)

#here to update

def check_for_update():
    print(Fore.CYAN + "[INFO] Checking for script updates...")
    try:
        remote_code = requests.get(REMOTE_SCRIPT_URL).text
        with open(__file__, "r", encoding="utf-8") as local_file:
            local_code = local_file.read()

        if remote_code.strip() != local_code.strip():
            print(Fore.YELLOW + "[UPDATE] New version found. Updating...")
            with open(__file__, "w", encoding="utf-8") as local_file:
                local_file.write(remote_code)

            print(Fore.GREEN + "[SUCCESS] Script updated.")
            print(Fore.BLUE + "[INFO] Restarting...")
            time.sleep(1)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            print(Fore.GREEN + "[OK] Script is up to date.")
    except Exception as e:
        print(Fore.RED + f"[ERROR] Update failed: {e}")

def auto_update_yt_dlp():
    try:
        print(Fore.CYAN + "[INFO] Updating yt-dlp...")
        subprocess.run(["yt-dlp", "-U"], check=True)
        print(Fore.GREEN + "[SUCCESS] yt-dlp updated.")
    except Exception as e:
        print(Fore.RED + f"[ERROR] yt-dlp update failed: {e}")

# Default save location
download_folder = "Downloaded_Videos"

# Tool info
slogan = " 🗂️  ＯＲＧＡＮＩＺＥ．   🔎  ＥＸＰＬＯＲＥ．   📦  ＤＥＬＩＶＥＲ."
tool_version = "v1.0.0"
creator_name = "AZsubay"
creator_contact = "BlackEagle@protonmail.com"
creator_website = "https://www.AZsubay.com"

# Turbo mode flag
turbo_mode = False

# Display banner with ASCII and creator info
def display_banner():
    width = 80
    banner = r"""
                                           
                                         ██╗     ██╗   ██╗██╗  ██╗    ███╗   ███╗███████╗██████╗ ██╗ █████╗ 
                                         ██║     ██║   ██║ ╚███╔╝     ██╔████╔██║█████╗  ██║  ██║██║███████║
                                         ██║     ██║   ██║ ██╔██╗     ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║
                                         ███████╗╚██████╔╝██╔╝ ██╗    ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║
                                         ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝
                                            ＯＲＧＡＮＩＺＥ．     ＥＸＰＬＯＲＥ．     ＤＥＬＩＶＥＲ．
                         
"""
    info_box = f"""
{'=' * width}
{'YOUTUBE VIDEO FINDER ' + tool_version.center(width - len('YOUTUBE VIDEO FINDER ') - 1)}
{'Created by: ' + creator_name.center(width - len('Created by: ') - 1)}
{'Contact: ' + creator_contact.center(width - len('Contact: ') - 1)}
{'Website: ' + creator_website.center(width - len('Website: ') - 1)}
{'=' * width}
"""
    print(Fore.YELLOW + banner)
    print(Fore.CYAN + info_box)

def display_menu():
    print(Fore.GREEN + "\n[1] Download Video by URL")
    print(Fore.LIGHTMAGENTA_EX + "[2] Search YouTube and Download")
    print(Fore.GREEN + "[3] Help")
    print(Fore.MAGENTA + "[4] Set Save Location")
    print(Fore.RED + "[5] Exit")
    print(Fore.YELLOW + "[6] Toggle Turbo Mode")

def set_save_location():
    os.system('cls' if os.name == 'nt' else 'clear')
    folder()
    global download_folder
    new_location = input(f"{Fore.YELLOW}\n[+] Enter new save location (full path): ").strip()
    if os.path.exists(new_location):
        download_folder = new_location
        print(f'{Fore.LIGHTRED_EX}\n[-]Saving..')
        time.sleep(0.9)
        print(f'{Fore.LIGHTRED_EX}...........')
        time.sleep(0.8)
        print(f'{Fore.LIGHTRED_EX}...........')
        time.sleep(0.7)
        print(Fore.YELLOW + f"[SUCCESS] Save location set to: {download_folder}")
    else:
        print('\n[]Searching.')
        time.sleep(0.6)
        print('............')
        time.sleep(0.6)
        print('............')
        time.sleep(0.7)
        print('\n[-] OOpps !!..\n')
        print(Fore.RED + "[ERROR!] Invalid directory. Please enter a valid path :).")
    input(Fore.GREEN + "\n[+]Press Enter to return to the main menu...")

def choose_quality():
    print(Fore.CYAN + "\nChoose Video Quality:")
    print("[1] 8K (4320p)")
    print("[2] 4K (2160p)")
    print("[3] 1440p")
    print("[4] 1080p")
    print("[5] 720p")
    print("[6] 480p")
    print("[7] 360p")
    print("[8] 240p")
    print("[9] Best Available")

    choice = input(Fore.YELLOW + "[+] Select an option (1-9): ").strip()
    quality_map = {
        '1': 'bestvideo[height<=4320]+bestaudio/best',
        '2': 'bestvideo[height<=2160]+bestaudio/best',
        '3': 'bestvideo[height<=1440]+bestaudio/best',
        '4': 'bestvideo[height<=1080]+bestaudio/best',
        '5': 'bestvideo[height<=720]+bestaudio/best',
        '6': 'bestvideo[height<=480]+bestaudio/best',
        '7': 'bestvideo[height<=360]+bestaudio/best',
        '8': 'bestvideo[height<=240]+bestaudio/best',
        '9': 'bestvideo+bestaudio/best',
    }
    return quality_map.get(choice, 'bestvideo+bestaudio/best')

def choose_download_type():
    print(Fore.CYAN + "\nChoose Download Type:")
    print("[1] Download Video + Audio (default)")
    print("[2] Download Audio Only")
    print("[3] Download Video with Subtitles")

    choice = input(Fore.YELLOW + "[+] Select an option (1-3): ").strip()
    if choice == '1':
        return 'bestvideo+bestaudio/best'
    elif choice == '2':
        return 'bestaudio/best'
    elif choice == '3':
        return 'bestvideo+bestaudio/subtitles'
    else:
        return 'bestvideo+bestaudio/best'

def show_file_details(filepath):
    if os.path.exists(filepath):
        file_size = os.path.getsize(filepath) / (1024 * 1024)
        print(Fore.RED + f"[ERROR] File '{filepath}' already exists!")
        print(Fore.GREEN + f"    File Size: {file_size:.2f} MB")
        print(Fore.GREEN + f"    File Path: {os.path.abspath(filepath)}")
        print(Fore.GREEN + f"    Last Modified: {datetime.fromtimestamp(os.path.getmtime(filepath))}")
    else:
        print(Fore.RED + "[ERROR] File not found!")

def download_video(url):
    os.makedirs(download_folder, exist_ok=True)

    download_type = choose_download_type()
    quality = choose_quality()
    video_file = f"{download_folder}/{url.split('=')[-1]}.mp4"

    if os.path.exists(video_file):
        show_file_details(video_file)
        print(Fore.YELLOW + "| > Skipping download, file already exists.")
        time.sleep(1.0)
        input(Fore.CYAN + "\n[_] Press Enter to return to the main menu...")
        return

    ydl_opts = {
        'format': quality,
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'progress_hooks': [download_progress],
        'quiet': False,
        'writesubtitles': True,
        'writeautomaticsub': True,
    }

    print(Fore.YELLOW + "\n [#] Download Loading..")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(Fore.GREEN + "\n[SUCCESS] Video downloaded successfully!Dude :)")
    except Exception as e:
        print(Fore.RED + f"[ERROR] {e}")

    input(Fore.CYAN + "\n [+] Press Enter to return to the main menu...")

# PROGRESS FUNCTION - for download only AZsubay hahhahah
def download_progress(d):
    color_cycle = itertools.cycle([Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.RED])

    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        downloaded = d.get('_downloaded_bytes', 0)
        total = d.get('_total_bytes') or d.get('total_bytes_estimate') or 1

        try:
            progress = downloaded / total if total > 0 else 0
        except:
            progress = 0

        bar_length = 40
        filled_length = int(progress * bar_length)

        current_color = next(color_cycle)
        bar = f"{current_color}{'█' * filled_length}{Fore.RED}{'░' * (bar_length - filled_length)}"
        sys.stdout.write(f"\r{Fore.CYAN}[Downloading] {percent} | {bar} ")
        sys.stdout.flush()

    elif d['status'] == 'finished':
        sys.stdout.write(f"\r{Fore.GREEN}[SUCCESS] Download complete! Processing file...\n")
        sys.stdout.flush()

def youtube_search():
    os.system('cls' if os.name == 'nt' else 'clear')
    head3()
    query = input(Fore.GREEN + "\n[+] Enter search keywords (or 'back' to return): ").strip()
    if not query or query.lower() == 'back':
        return

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': 'in_playlist',
    }

    print(Fore.CYAN + "\n[INFO] Searching YouTube...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            search_result = ydl.extract_info(f"ytsearch50:{query}", download=False)
            results = search_result.get('entries', [])
        except Exception as e:
            print(Fore.RED + f"[ERROR] Failed to search: {e}")
            return

    if not results:
        print(Fore.RED + "[ERROR] No results found :_).")
        return

    index = 0
    per_page = 10
    all_results = []  # store all results here for cumulative display

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        head3()
        print(Fore.GREEN + f"\n Searched :> Results for: {query}")
        print(Fore.CYAN + "([+] Press Enter to load more, enter number to download, or 'back' to return :)")

        new_results = results[index:index + per_page]
        all_results.extend(new_results)  # add newly fetched ones to the overall list

        for i, entry in enumerate(all_results): 
            print(Fore.YELLOW + f"{i + 1}. {entry.get('title')}")

        user_input = input(Fore.CYAN + "\n[+] Your choice: ").strip().lower()

        if user_input == '':
            index += per_page
            if index >= len(results):
                print(Fore.RED + "\n[INFO] No more results.")
                input(Fore.CYAN + "[=] Press Enter to return to main menu...")
                return

        elif user_input == 'back':
            return

        elif user_input.isdigit():
            selected_index = int(user_input) - 1
            if 0 <= selected_index < len(all_results):
                selected_url = all_results[selected_index].get('url') or all_results[selected_index].get('webpage_url')
                if selected_url:
                    download_video(selected_url)
                else:
                    print(Fore.RED + "[ERROR] Could not get video URL.")
                input(Fore.CYAN + "\nPress Enter to return to the search menu...")
            else:
                print(Fore.RED + "[ERROR] Invalid selection.")
                input(Fore.CYAN + "Press Enter to continue...")
         
    
  
                                        
def show_help():
    os.system('cls' if os.name == 'nt' else 'clear')
    help_banner()
    print(Fore.YELLOW + "\n[HELP] How to Use:")
    print(Fore.CYAN + "\n1.> Choose option 1 to download by direct YouTube URL.")
    print(Fore.CYAN + "\n2.> Choose option 2 to search YouTube and pick a video.")
    print(Fore.CYAN + "\n3.> Choose option 4 to set where videos are saved.")
    print(Fore.CYAN + "\n4.> Use option 5 to exit the program.")
    input(Fore.RED + "\n[_] Press Enter to return to the main menu...")
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        display_menu()

        # Input validation: keep asking until valid option (1–6) is chosen. so ukikosea bado nakutaka ujazeh valid one guys :)
        valid_choices = {'1', '2', '3', '4', '5', '6'}
        choice = input(Fore.YELLOW + "\n[+] Choose an option (1-6): ").strip()
        while choice not in valid_choices:
            print(Fore.RED + "[ERROR] Invalid option. Please enter a number from 1 to 6.")
            choice = input(Fore.YELLOW + "[+] Choose again (1-6): ").strip()

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            head1()
            head2()
            url = input(Fore.YELLOW + " [+] Enter YouTube URL: ").strip()
            download_video(url)

        elif choice == '2':
            youtube_search()

        elif choice == '3':
            show_help()

        elif choice == '4':
            set_save_location()

        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            goodby()
            time.sleep(0.5)
            print(f'{Fore.LIGHTMAGENTA_EX}\n[ ] Program is ShuttingDown :(')
            time.sleep(0.6)
            print(f"{Fore.GREEN}\n.........")
            time.sleep(0.7)
            print(f"{Fore.CYAN}\n.........")
            time.sleep(0.8)
            print(f"{Fore.YELLOW}\n.........")  
            time.sleep(2.0) 
            print(f'{Fore.BLUE}\n Thanks You for Choosing our Services, Your Welcome :)')
            time.sleep(1.3)
            sys.exit(0)      

        elif choice == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{Fore.GREEN} TURBO MODE is LOADING..')
            print(f'\n{Fore.CYAN} Please Wait ...')
            time.sleep(1)
            print(f'\n{Fore.YELLOW} ............')
            time.sleep(.8)
            print(f'\n{Fore.CYAN} Please Wait ...')
            time.sleep(.7)
            print(f'\n{Fore.RED} ............')
            time.sleep(.6)
            print(f'\n{Fore.LIGHTMAGENTA_EX} Please Wait ...')
            time.sleep(.5)
            print(f'\n{Fore.YELLOW} ............')
            time.sleep(.4)

            global turbo_mode
            turbo_mode = not turbo_mode
            print(Fore.GREEN + f"\n[__] Turbo Mode {'enabled' if turbo_mode else 'disabled'}.")
            turbo()
            input(Fore.RED + "\n[+]Press Enter to return to the main menu...")

def goodby():
    RED(f'''{Fore.LIGHTMAGENTA_EX} 
   ___      ____      ____      ___      ___    _  _                    
 ,"___".   F __ ]    F __ ]    F __".   F _ ", FJ  LJ                   
 FJ---L]  J |--| L  J |--| L  J |--\ L J `-'(| J \/ F                   
J |  [""L | |  | |  | |  | |  | |  J | | ,--.\ J\  /L                   
| \___] | F L__J J  F L__J J  F L__J | F L__J \ F  J     __  __  __  __ 
J\_____/FJ\______/FJ\______/FJ______/FJ_______J|____|   J__LJ__LJ__LJ__L
 J_____F  J______F  J______F |______F |_______F|____|   |__||__||__||__|
 ''')   
    
    
def head1():
    RED(r'''  
           
      ____  ____ _       ___   ____    ____  ___    ____ 
     / __ \/ __ \ |     / / | / / /   / __ \/   |  / __ \
    / / / / / / / | /| / /  |/ / /   / / / / /| | / / / /
   / /_/ / /_/ /| |/ |/ / /|  / /___/ /_/ / ___ |/ /_/ / 
  /_____/\____/ |__/|__/_/ |_/_____/\____/_/  |_/_____/  
                         
               [+] unlimited Download :)                                                                                          
                                         _    _   
                                        | |  | |  
                                        | |__| |_ 
                                        |____   _|
                                            _| |_  
                                           |_____|                    
                                                         _   ______ _       __
                                                        / | / / __ \ |     / /
                                                       /  |/ / / / / | /| / / 
                                                      / /|  / /_/ /| |/ |/ /  
                                                     /_/ |_/\____/ |__/|__/   
                                                     ---------------------
                                                     ---------------------
                                                     ''')   
    
def head2():
    GREEN(r'''
                                                     
,---..  ,,---.|    ,---.,---.,---.    ,   .,---.. . .
|---  >< |---'|    |   ||---'|---     |\  ||   || | |
|    |  ||    |    |   ||  \ |        | \ ||   || | |
`---''  ``    `---'`---'`   ``---'    `  `'`---'`-'-'
=====================================================
''')   
    
def head3():
    RED(r'''
     ____  _   ____    _____   ________   _____ _________    ____  ________  __
    / __ \/ | / / /   /  _/ | / / ____/  / ___// ____/   |  / __ \/ ____/ / / /
   / / / /  |/ / /    / //  |/ / __/     \__ \/ __/ / /| | / /_/ / /   / /_/ / 
  / /_/ / /|  / /____/ // /|  / /___    ___/ / /___/ ___ |/ _, _/ /___/ __  /  
  \____/_/ |_/_____/___/_/ |_/_____/   /____/_____/_/  |_/_/ |_|\____/_/ /_/   .........
                                     [+] With &
                                __  __      ___           _ __           __   _____                     __
                               / / / /___  / (_)___ ___  (_) /____  ____/ /  / ___/____  ___  ___  ____/ /
                              / / / / __ \/ / / __ `__ \/ / __/ _ \/ __  /   \__ \/ __ \/ _ \/ _ \/ __  / 
                             / /_/ / / / / / / / / / / / / /_/  __/ /_/ /   ___/ / /_/ /  __/  __/ /_/ /  
                             \____/_/ /_/_/_/_/ /_/ /_/_/\__/\___/\__,_/   /____/ .___/\___/\___/\__,_/   
                                                                               /_/
  -----------------------------
   EXPLORE NEW TECH@AZsubay.com
  -----------------------------''')       

def folder():
    GREEN(r'''
        ________  __    ____  __________     ____  ___  ________  __
      / ____/ __ \/ /   / __ \/ ____/ __ \   / __ \/   |/_  __/ / / /
     / /_  / / / / /   / / / / __/ / /_/ /  / /_/ / /| | / / / /_/ / 
    / __/ / /_/ / /___/ /_/ / /___/ _, _/  / ____/ ___ |/ / / __  /  
   /_/    \____/_____/_____/_____/_/ |_|  /_/   /_/  |_/_/ /_/ /_/                                                 
                                                 
                     [] Enter Valid Folder Path. eg { C:\Users\user\Music }
           ''')

def help_banner():
    YELLOW(r'''
_______ ___ ___ _______ _______ _______ ___ _______ ___      
|       |   Y   |       |   _   |   _   |   |   _   |   |     
|.|   | |.  |   |.|   | |.  |   |.  l   |.  |.  1   |.  |     
`-|.  |-|.  |   `-|.  |-|.  |   |.  _   |.  |.  _   |.  |___  
  |:  | |:  1   | |:  | |:  1   |:  |   |:  |:  |   |:  1   | 
  |::.| |::.. . | |::.| |::.. . |::.|:. |::.|::.|:. |::.. . | 
  `---' `-------' `---' `-------`--- ---`---`--- ---`-------' 
                                                             

                                                ______                 __   ___                                       
                                               |   _  \.-----.-----.--|  |.'  _.-----.----..--------.-----.----.-----.
                                               |.  |   |  -__|  -__|  _  ||   _|  _  |   _||        |  _  |   _|  -__|
                                               |.  |   |_____|_____|_____||__| |_____|__|  |__|__|__|_____|__| |_____|
                                               |:  |   |                                                              
                                               |::.|   |                                                              
                                               `--- ---'                         __  __     __         ___ 
                                                                                / / / /__  / /___     /__ \
                                                                               / /_/ / _ \/ / __ \     / _/
                                                                              / __  /  __/ / /_/ /    /_/  
                                                                             /_/ /_/\___/_/ .___/    (_)   
                                                                                         /_/               
    [ Email Us ] at black_shadow@gmail.come :)                         
                               ''')
def turbo():
   RED(r''' 
                                                            ___    __    __  _______  ___________   ____  ____  _   ________           
                                                           /   |  / /   /  |/  / __ \/ ___/_  __/  / __ \/ __ \/ | / / ____/           
                                                          / /| | / /   / /|_/ / / / /\__ \ / /    / / / / / / /  |/ / __/              
                                                         / ___ |/ /___/ /  / / /_/ /___/ // /    / /_/ / /_/ / /|  / /___    _ _ _ _ _ 
                                                        /_/  |_/_____/_/  /_/\____//____//_/    /_____/\____/_/ |_/_____/   (_|_|_|_|_)
                                                                               
                                                                                                    : ).
''')
    

# COLOUR FUNCTION
def outer_job(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


# COLORS PRINT
RED = outer_job('\033[91m')
YELLOW = outer_job('\033[93m')
GREEN = outer_job('\033[92m')


if __name__ == "__main__":
    check_for_update()
    auto_update_yt_dlp()
    main_menu()
