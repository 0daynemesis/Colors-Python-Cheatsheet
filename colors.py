import emoji
from tabulate import tabulate
import pyperclip
import os
import time
import sys



# Reset
Color_Off="\033[0m"       # Text Reset

# Regular Colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White

# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

# High Intensty
IBlack="\033[0;90m"       # Black
IRed="\033[0;91m"         # Red
IGreen="\033[0;92m"       # Green
IYellow="\033[0;93m"      # Yellow
IBlue="\033[0;94m"        # Blue
IPurple="\033[0;95m"      # Purple
ICyan="\033[0;96m"        # Cyan
IWhite="\033[0;97m"       # White

# Bold High Intensty
BIBlack="\033[1;90m"      # Black
BIRed="\033[1;91m"        # Red
BIGreen="\033[1;92m"      # Green
BIYellow="\033[1;93m"     # Yellow
BIBlue="\033[1;94m"       # Blue
BIPurple="\033[1;95m"     # Purple
BICyan="\033[1;96m"       # Cyan
BIWhite="\033[1;97m"      # White

# High Intensty backgrounds
On_IBlack="\033[0;100m"   # Black
On_IRed="\033[0;101m"     # Red
On_IGreen="\033[0;102m"   # Green
On_IYellow="\033[0;103m"  # Yellow
On_IBlue="\033[0;104m"    # Blue
On_IPurple="\033[10;95m"  # Purple
On_ICyan="\033[0;106m"    # Cyan
On_IWhite="\033[0;107m"   # White


#Timer and Progress Bar section

def loading_bar(iterations):
    for i in range(iterations):
        time.sleep(0.05)  # Simulate some work being done
        progress = (i + 1) / iterations
        bar = "#" * int(progress * 50)  # Create a simple bar of length 50
        print(f"\rProgress: [{bar:<50}] {progress * 100:.2f}%", end="")
    print("\nProgress Completed!")                    

def spinning_cursor(seconds):
    cursor = ['|', '/', '-', '\\']
    for i in range(seconds * 10):  # Multiplied to give finer progress update
        sys.stdout.write(f'\rWaiting... {cursor[i % len(cursor)]}')
        sys.stdout.flush()
        time.sleep(0.1)  # Change this to adjust speed
    print("\nDone!")

# Example usage: 5 seconds wait with spinning cursor

def dots_progress(seconds):
    for _ in range(seconds):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print("\nDone!")

# Example usage: 5 seconds wait with dots progress

#Menu section

def display_menu():
    print(BYellow + '\nColors Python Codes Cheatsheet' + Color_Off)
    print('🔱 C o d e d   b y   0 d a y n e m e s i s 🇵🇹 🔱')
    print('\n🔴🟠🟡🟢🔵🟣🟤⚫⚪')
    print('\nMain Menu:')
    print("0️⃣ - Reset")
    print('1️⃣ - Regular Colors | ie: ' + Yellow + ('Yellow') + Color_Off)
    print("2️⃣ - Bold | ie: " + BYellow + ('Yellow') + Color_Off)
    print("3️⃣ - Underline | ie: " + UYellow + ('Yellow') + Color_Off)
    print("4️⃣ - Background | ie: " + On_Yellow + ('Yellow') + Color_Off)
    print("5️⃣ - High Intensity | ie: " + IYellow + ('Yellow') + Color_Off)
    print("6️⃣ - Bold High Intesity | ie: " + BIYellow + ('Yellow') + Color_Off)
    print("7️⃣ - High Intensty Backgrounds | ie: " + On_IYellow + ('Yellow') + Color_Off)
    print('8️⃣ - Exit')

def block():
    print('\nColor menu:')
    print('1️⃣ - One color')
    print('2️⃣ - All pack')
    print('3️⃣ - Return to Main Menu')
    print('4️⃣ - Exit')
   
def ret_menu():
    ret_menu = input(Color_Off + '🚪 Return Main Menu (y/n): ')

    if ret_menu == 'y':
        print('🔙 Returning...')
        spinning_cursor(3)
        os.system('clear')
        
    else:
        print('❌ Exiting...')
        time.sleep(1)
        os.system('clear')
        exit()

def reset():
    print('\n🔰Reset\n' + Color_Off)
    data = [["Color_Off", "033[0m"]]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')

def regular():

    print('\n🔰Regular Colors\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[0;37m"],
            [Red + '🔴 ➡ Red', "\\033[0;31m"],
            [Green + "🟢 ➡ Green", "\\033[0;32m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[0;33m"],
            [Blue + "🔵 ➡ Blue", "\\033[0;34m"],
            [Purple + "🟣 ➡ Purple", "\\033[0;35m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[0;36m"],
            [White + "⚪ ➡ White", "\\033[0;37m" + Color_Off]
    ]

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))

    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_regular = input('Choose color (lower case): ')
        if color_regular == 'black':     
            pyperclip.copy('\\033[0;37m')
        elif color_regular == 'red':
            pyperclip.copy('\\033[0;31m')
        elif color_regular == ('green'):
            pyperclip.copy('\\033[0;32m')
        elif color_regular == ('yellow'):
            pyperclip.copy('\\033[0;33m')
        elif color_regular == ('blue'):
            pyperclip.copy('\\033[0;34m')
        elif color_regular == ('purple'):
            pyperclip.copy('\\033[0;35m')
        elif color_regular == ('cyan'):
            pyperclip.copy('\\033[0;36m')
        elif color_regular == ('white'):
            pyperclip.copy('White = \\033[0;37m')
            print('Color White copied to clipboard', end='') 
            dots_progress(3)
        else:
            os.system('clear')
            print('Has to be a color | ie: black')
            spinning_cursor(3)
            os.system('clear')
            return regular()
            
    elif block_option == '2':
        print('Copying all colors...')
        pyperclip.copy('Black = \\033[0;37m\nRed = \\033[0;31m\nGreen = \\033[0;32m\nYellow = \\033[0;33m\nBlue = \\033[0;34m\nPurple = \\033[0;35m\nCyan = \\033[0;36m\nWhite = \\033[0;37m')
        loading_bar(100)
        print('Copy finished, paste wherever you want and color the world!!')
        time.sleep(5)
        os.system('clear')

    elif block_option == '3':
        os.system('clear')     
        
        
    elif block_option == '4':
        print('\n❌ Exiting...')
        time.sleep(1)
        os.system('clear')
        exit()
    
    else:
        os.system('clear')
        print('Invalid option, returning to Regular Colors Menu')
        spinning_cursor(3)
        os.system('clear')


def bold():

    print('\n🔰Bold\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "033[1;30m"],
            [Red + '🔴 ➡ Red', "033[1;31m"],
            [Green + "🟢 ➡ Green", "033[1;32m"],
            [Yellow + "🟡 ➡ Yellow", "033[1;33m"],
            [Blue + "🔵 ➡ Blue", "033[1;34m"],
            [Purple + "🟣 ➡ Purple", "033[1;35m"],
            [Cyan + "🔵 ➡ Cyan", "033[1;36m"],
            [White + "⚪ ➡ White", "033[1;37m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')

def underline():

    print('\n🔰Underline\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "033[4;30m"],
            [Red + '🔴 ➡ Red', "033[4;31m"],
            [Green + "🟢 ➡ Green", "033[4;32m"],
            [Yellow + "🟡 ➡ Yellow", "033[4;33m"],
            [Blue + "🔵 ➡ Blue", "033[4;34m"],
            [Purple + "🟣 ➡ Purple", "033[4;35m"],
            [Cyan + "🔵 ➡ Cyan", "033[4;36m"],
            [White + "⚪ ➡ White", "033[4;37m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')


def background():

    print('\n🔰Background\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "033[40m"],
            [Red + '🔴 ➡ Red', "033[41m"],
            [Green + "🟢 ➡ Green", "033[42m"],
            [Yellow + "🟡 ➡ Yellow", "033[43m"],
            [Blue + "🔵 ➡ Blue", "033[44m"],
            [Purple + "🟣 ➡ Purple", "033[45m"],
            [Cyan + "🔵 ➡ Cyan", "033[46m"],
            [White + "⚪ ➡ White", "033[47m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')


def high_intensity():

    print('\n🔰High Intensity\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "033[0;90m"],
            [Red + '🔴 ➡ Red', "033[0;91m"],
            [Green + "🟢 ➡ Green", "033[0;92m"],
            [Yellow + "🟡 ➡ Yellow", "033[0;93m"],
            [Blue + "🔵 ➡ Blue", "033[0;94m"],
            [Purple + "🟣 ➡ Purple", "033[0;95m"],
            [Cyan + "🔵 ➡ Cyan", "033[0;96m"],
            [White + "⚪ ➡ White", "033[0;97m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')


def bold_high_intensity():

    print('\n🔰Bold High Intensity\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "033[1;90m"],
            [Red + '🔴 ➡ Red', "033[1;91m"],
            [Green + "🟢 ➡ Green", "033[1;92m"],
            [Yellow + "🟡 ➡ Yellow", "033[1;93m"],
            [Blue + "🔵 ➡ Blue", "033[1;94m"],
            [Purple + "🟣 ➡ Purple", "033[1;95m"],
            [Cyan + "🔵 ➡ Cyan", "033[1;96m"],
            [White + "⚪ ➡ White", "033[1;97m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')


def high_intensity_backgrounds():

    print('\n🔰High Intensity Backgrounds\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "033[0;10m"],
            [Red + '🔴 ➡ Red', "033[0;101m"],
            [Green + "🟢 ➡ Green", "033[0;102m"],
            [Yellow + "🟡 ➡ Yellow", "033[0;103m"],
            [Blue + "🔵 ➡ Blue", "033[0;104m"],
            [Purple + "🟣 ➡ Purple", "033[10;95m"],
            [Cyan + "🔵 ➡ Cyan", "033[0;106m"],
            [White + "⚪ ➡ White", "033[0;107m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    print('\n Note: Append always a \ before 033\n')


os.system('clear')

#display menu
while True:
    display_menu()
    option = input('Option: ')

#options

    if option == '0':
        os.system('clear')
        reset()
        ret_menu()

    elif option == '1':
        os.system('clear')
        while True:
            regular()
            os.system('clear')
            break
        #regular()
        #ret_menu()
    elif option == '2':
        os.system('clear')
        bold()
        ret_menu()

    elif option == '3':
        os.system('clear')
        underline()
        ret_menu()

    elif option == '4':
        os.system('clear')
        background()
        ret_menu()
    
    elif option == '5':
        os.system('clear')
        high_intensity()
        ret_menu()

    elif option == '6':
        os.system('clear')
        bold_high_intensity()
        ret_menu()
    
    elif option == '7':
        os.system('clear')
        high_intensity_backgrounds()
        ret_menu()

    elif option == '8':
        print('\n❌ Exiting...')
        time.sleep(1)
        os.system('clear')
        exit()