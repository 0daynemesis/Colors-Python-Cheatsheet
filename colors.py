import emoji
import os
import time

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

#def section


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

def ret_menu():
    ret_menu = input(Color_Off + '🚪 Return Main Menu (y/n): ')

    if ret_menu == 'y':
        print('🔙 Returning...')
        time.sleep(1)
        os.system('clear')
        
    else:
        print('❌ Exiting...')
        time.sleep(1)
        os.system('clear')
        exit()

def reset():
    print('Color_Off')

def regular():
    print('\n🔰Regular Colors\n' + Color_Off)
    print(Black + '⚫ ➡ Black')
    print(Red + '🔴 ➡ Red')
    print(Green + '🟢 ➡ Green')
    print(Yellow +'🟡 ➡ Yellow')
    print(Blue +'🔵 ➡ Blue')
    print(Purple + '🟣 ➡ Purple')
    print(Cyan + '🔵 ➡ Cyan')
    print(White + '⚪ ➡ White\n')

def bold():
    print('\n🔰Bold\n' + Color_Off)
    print(BBlack + '⚫ ➡ BBlack')
    print(BRed + '🔴 ➡ BRed')
    print(BGreen + '🟢 ➡ BGreen')
    print(BYellow + '🟡 ➡ BYellow')
    print(BBlue + '🔵 ➡ BBlue')
    print(BPurple + '🟣 ➡ BPurple')
    print(BCyan + '🔵 ➡ BCyan')
    print(BWhite + '⚪ ➡ BWhite\n')

def underline():
    print('\n🔰Underline\n' + Color_Off)
    print(UBlack + '⚫ ➡ UBlack')
    print(URed + '🔴 ➡ URed')
    print(UGreen + '🟢 ➡ UGreen')
    print(UYellow + '🟡 ➡ UYellow')
    print(UBlue + '🔵 ➡ UBlue')
    print(UPurple + '🟣 ➡ UPurple')
    print(UCyan + '🔵 ➡ UCyan')
    print(UWhite + '⚪ ➡ UWhite\n')

def background():
    print('\Background\n' + Color_Off)
    print(On_Black + '⚫ ➡ On_Black' + Color_Off)
    print(On_Red + '🔴 ➡ On_Red' + Color_Off)
    print(On_Green + '🟢 ➡ On_Green' + Color_Off)
    print(On_Yellow + '🟡 ➡ On_Yellow' + Color_Off)
    print(On_Blue + '🔵 ➡ On_Blue' + Color_Off)
    print(On_Purple + '🟣 ➡ On_Purple' + Color_Off)
    print(On_Cyan + '🔵 ➡ On_Cyan' + Color_Off)
    print(On_White + '⚪ ➡ On_White' + Color_Off + '\n')

def high_intensity():
    print(IBlack + 'IBlack')
    print(IRed + 'IRed')
    print(IGreen + 'IGreen')
    print(IYellow + 'IYellow')
    print(IBlue + 'IBlue')
    print(IPurple + 'IPurple')
    print(ICyan + 'ICyan')
    print(IWhite + 'IWhite\n')

def bold_high_intensity():
    print(BIBlack + 'BIBlack')
    print(BIRed + 'BIRed')
    print(BIGreen + 'BIGreen')
    print(BIYellow + 'BIYellow')
    print(BIBlue + 'BIBlue')
    print(BIPurple + 'BIPurple')
    print(BICyan + 'BICyan')
    print(BIWhite + 'BIWhite\n')

def high_intensity_backgrounds():
    print(On_IBlack + 'On_IBlack' + Color_Off)
    print(On_IRed + 'On_IRed' + Color_Off)
    print(On_IGreen + 'On_IGreen' + Color_Off)
    print(On_IYellow + 'On_IYellow' + Color_Off)
    print(On_IBlack + 'On_IBlue' + Color_Off)
    print(On_IPurple + 'On_IPurple' + Color_Off)
    print(On_ICyan + 'On_ICyan' + Color_Off)
    print(On_IWhite + 'On_IWhite' + Color_Off)

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
        regular()
        ret_menu()

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