from tabulate import tabulate
import pyperclip
import os
import time
import sys

# UNDER DEVELOP 


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
    data = [["Color_Off", "\\033[0m"]]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    reset_color = input('\nCopy to clipboard? (y/n) ')
    
    if reset_color == 'y':
        pyperclip.copy('\\033[0m')
    elif reset_color == 'n':
        os.system('clear')



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
            pyperclip.copy('"\\033[0;37m"')
        elif color_regular == 'red':
            pyperclip.copy('"\\033[0;31m"')
        elif color_regular == ('green'):
            pyperclip.copy('"\\033[0;32m"')
        elif color_regular == ('yellow'):
            pyperclip.copy('"\\033[0;33m"')
        elif color_regular == ('blue'):
            pyperclip.copy('"\\033[0;34m"')
        elif color_regular == ('purple'):
            pyperclip.copy('"\\033[0;35m"')
        elif color_regular == ('cyan'):
            pyperclip.copy('"\\033[0;36m"')
        elif color_regular == ('white'):
            pyperclip.copy('"\\033[0;37m"')
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
        pyperclip.copy('Black = "\\033[0;37m"\nRed = "\\033[0;31m"\nGreen = "\\033[0;32m"\nYellow = "\\033[0;33m"\nBlue = "\\033[0;34m"\nPurple = "\\033[0;35m"\nCyan = "\\033[0;36m"\nWhite = "\\033[0;37m"')
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
        return regular()


def bold():

    print('\n🔰Bold\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[1;30m"],
            [Red + '🔴 ➡ Red', "\\033[1;31m"],
            [Green + "🟢 ➡ Green", "\\033[1;32m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[1;33m"],
            [Blue + "🔵 ➡ Blue", "\\033[1;34m"],
            [Purple + "🟣 ➡ Purple", "\\033[1;35m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[1;36m"],
            [White + "⚪ ➡ White", "\\033[1;37m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))

    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_bold = input('Choose color (lower case): ')
        if color_bold == 'black':     
            pyperclip.copy('"\\033[1;30m"')
        elif color_bold == 'red':
            pyperclip.copy('"\\033[1;31m"')
        elif color_bold == ('green'):
            pyperclip.copy('"\\033[1;32m"')
        elif color_bold == ('yellow'):
            pyperclip.copy('"\\033[1;33m"')
        elif color_bold == ('blue'):
            pyperclip.copy('"\\033[1;34m"')
        elif color_bold == ('purple'):
            pyperclip.copy('"\\033[1;35m"')
        elif color_bold == ('cyan'):
            pyperclip.copy('"\\033[1;36m"')
        elif color_bold == ('white'):
            pyperclip.copy('"\\033[1;37m"')
            print('Color White copied to clipboard', end='') 
            dots_progress(3)
        else:
            os.system('clear')
            print('Has to be a color | ie: black')
            spinning_cursor(3)
            os.system('clear')
            return bold()
            
    elif block_option == '2':
        print('Copying all colors...')
        pyperclip.copy('Black = "\\033[1;37m"\nRed = "\\033[1;31m"\nGreen = "\\033[1;32m"\nYellow = "\\033[1;33m"\nBlue = "\\033[1;34m"\nPurple = "\\033[1;35m"\nCyan = "\\033[1;36m"\nWhite = "\\033[1;37m"')
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
        print('Invalid option, returning to Bold Colors Menu')
        spinning_cursor(3)
        os.system('clear')
        return bold()


def underline():

    print('\n🔰Underline\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[4;30m"],
            [Red + '🔴 ➡ Red', "\\033[4;31m"],
            [Green + "🟢 ➡ Green", "\\033[4;32m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[4;33m"],
            [Blue + "🔵 ➡ Blue", "\\033[4;34m"],
            [Purple + "🟣 ➡ Purple", "\\033[4;35m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[4;36m"],
            [White + "⚪ ➡ White", "\\033[4;37m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))

    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_underline = input('Choose color (lower case): ')
        if color_underline == 'black':     
            pyperclip.copy('"\\033[4;30m"')
        elif color_underline == 'red':
            pyperclip.copy('"\\033[4;31m"')
        elif color_underline == ('green'):
            pyperclip.copy('"\\033[4;32m"')
        elif color_underline == ('yellow'):
            pyperclip.copy('"\\033[4;33m"')
        elif color_underline == ('blue'):
            pyperclip.copy('"\\033[4;34m"')
        elif color_underline == ('purple'):
            pyperclip.copy('"\\033[4;35m"')
        elif color_underline == ('cyan'):
            pyperclip.copy('"\\033[4;36m"')
        elif color_underline == ('white'):
            pyperclip.copy('"\\033[4;37m"')
            print('Color White copied to clipboard', end='') 
            dots_progress(3)
        else:
            os.system('clear')
            print('Has to be a color | ie: black')
            spinning_cursor(3)
            os.system('clear')
            return underline()
            
    elif block_option == '2':
        print('Copying all colors...')
        pyperclip.copy('Black = "\\033[4;30m"\nRed = "\\033[4;31m"\nGreen = "\\033[4;32m"\nYellow = "\\033[4;33m"\nBlue = "\\033[4;34m"\nPurple = "\\033[4;35m"\nCyan = "\\033[4;36m"\nWhite = "\\033[4;37m"')
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
        print('Invalid option, returning to Underline Colors Menu')
        spinning_cursor(3)
        os.system('clear')
        return underline()


def background():

    print('\n🔰Background\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[40m"],
            [Red + '🔴 ➡ Red', "\\033[41m"],
            [Green + "🟢 ➡ Green", "\\033[42m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[43m"],
            [Blue + "🔵 ➡ Blue", "\\033[44m"],
            [Purple + "🟣 ➡ Purple", "\\033[45m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[46m"],
            [White + "⚪ ➡ White", "\\033[47m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    
    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_background = input('Choose color (lower case): ')
        if color_background == 'black':     
            pyperclip.copy('\\033[40m')
        elif color_background == 'red':
            pyperclip.copy('\\033[41m')
        elif color_background == ('green'):
            pyperclip.copy('\\033[42m')
        elif color_background == ('yellow'):
            pyperclip.copy('\\033[43m')
        elif color_background == ('blue'):
            pyperclip.copy('\\033[44m')
        elif color_background == ('purple'):
            pyperclip.copy('\\033[45m')
        elif color_background == ('cyan'):
            pyperclip.copy('\\033[46m')
        elif color_background == ('white'):
            pyperclip.copy('\\033[47m')
            print('Color White copied to clipboard', end='') 
            dots_progress(3)
        else:
            os.system('clear')
            print('Has to be a color | ie: black')
            spinning_cursor(3)
            os.system('clear')
            return background()
            
    elif block_option == '2':
        print('Copying all colors...')
        pyperclip.copy('Black = \\033[40m\nRed = \\033[41m\nGreen = \\033[42m\nYellow = \\033[43m\nBlue = \\033[44m\nPurple = \\033[45m\nCyan = \\033[46m\nWhite = \\033[47m')
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
        print('Invalid option, returning to Background Colors Menu')
        spinning_cursor(3)
        os.system('clear')


def high_intensity():

    print('\n🔰High Intensity\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[0;90m"],
            [Red + '🔴 ➡ Red', "\\033[0;91m"],
            [Green + "🟢 ➡ Green", "\\033[0;92m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[0;93m"],
            [Blue + "🔵 ➡ Blue", "\\033[0;94m"],
            [Purple + "🟣 ➡ Purple", "\\033[0;95m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[0;96m"],
            [White + "⚪ ➡ White", "\\033[0;97m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    
    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_high_intensity = input('Choose color (lower case): ')
        if color_high_intensity == 'black':     
            pyperclip.copy('\\033[0;90m')
        elif color_high_intensity == 'red':
            pyperclip.copy('\\033[0;91m')
        elif color_high_intensity == ('green'):
            pyperclip.copy('\\033[0;92m')
        elif color_high_intensity == ('yellow'):
            pyperclip.copy('\\033[0;93m')
        elif color_high_intensity == ('blue'):
            pyperclip.copy('\\033[0;94m')
        elif color_high_intensity == ('purple'):
            pyperclip.copy('\\033[0;95m')
        elif color_high_intensity == ('cyan'):
            pyperclip.copy('\\033[0;96m')
        elif color_high_intensity == ('white'):
            pyperclip.copy('\\033[0;97m')
            print('Color White copied to clipboard', end='') 
            dots_progress(3)
        else:
            os.system('clear')
            print('Has to be a color | ie: black')
            spinning_cursor(3)
            os.system('clear')
            return high_intensity()
            
    elif block_option == '2':
        print('Copying all colors...')
        pyperclip.copy('Black = \\033[0;90m\nRed = \\033[0;91m\nGreen = \\033[0;92m\nYellow = \\033[0;93m\nBlue = \\033[0;94m\nPurple = \\033[0;95m\nCyan = \\033[0;96m\nWhite = \\033[0;97m')
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
        print('Invalid option, returning to High Intensity Colors Menu')
        spinning_cursor(3)
        os.system('clear')


def bold_high_intensity():

    print('\n🔰Bold High Intensity\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[1;90m"],
            [Red + '🔴 ➡ Red', "\\033[1;91m"],
            [Green + "🟢 ➡ Green", "\\033[1;92m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[1;93m"],
            [Blue + "🔵 ➡ Blue", "\\033[1;94m"],
            [Purple + "🟣 ➡ Purple", "\\033[1;95m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[1;96m"],
            [White + "⚪ ➡ White", "\\033[1;97m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
    
    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_bold_high_intensity = input('Choose color (lower case): ')
        if color_bold_high_intensity == 'black':     
            pyperclip.copy('\\033[1;90m')
        elif color_bold_high_intensity == 'red':
            pyperclip.copy('\\033[1;91m')
        elif color_bold_high_intensity == ('green'):
            pyperclip.copy('\\033[1;92m')
        elif color_bold_high_intensity == ('yellow'):
            pyperclip.copy('\\033[1;93m')
        elif color_bold_high_intensity == ('blue'):
            pyperclip.copy('\\033[1;94m')
        elif color_bold_high_intensity == ('purple'):
            pyperclip.copy('\\033[1;95m')
        elif color_bold_high_intensity == ('cyan'):
            pyperclip.copy('\\033[1;96m')
        elif color_bold_high_intensity == ('white'):
            pyperclip.copy('\\033[1;97m')
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
        pyperclip.copy('Black = \\033[1;90m\nRed = \\033[1;91m\nGreen = \\033[1;92m\nYellow = \\033[1;93m\nBlue = \\033[1;94m\nPurple = \\033[1;95m\nCyan = \\033[1;96m\nWhite = \\033[1;97m')
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
        print('Invalid option, returning to Bold High Intensity Colors Menu')
        spinning_cursor(3)
        os.system('clear')


def high_intensity_backgrounds():

    print('\n🔰High Intensity Backgrounds\n' + Color_Off)
    data = [[Black + "⚫ ➡ Black", "\\033[0;100m"],
            [Red + '🔴 ➡ Red', "\\033[0;101m"],
            [Green + "🟢 ➡ Green", "\\033[0;102m"],
            [Yellow + "🟡 ➡ Yellow", "\\033[0;103m"],
            [Blue + "🔵 ➡ Blue", "\\033[0;104m"],
            [Purple + "🟣 ➡ Purple", "\\033[0;105m"],
            [Cyan + "🔵 ➡ Cyan", "\\033[0;106m"],
            [White + "⚪ ➡ White", "\\033[0;107m" + Color_Off]
    ]
    

    col_names = ["Color", "Code"]

    print(tabulate(data, headers=col_names))
        
    print('Time to color your python code!')
    block()
    block_option = input('\nOption: ')

    if block_option == '1':
        color_high_intensity_backgrounds = input('Choose color (lower case): ')
        if color_high_intensity_backgrounds == 'black':     
            pyperclip.copy('\\033[0;100m')
        elif color_high_intensity_backgrounds == 'red':
            pyperclip.copy('\\033[0;101m')
        elif color_high_intensity_backgrounds == ('green'):
            pyperclip.copy('\\033[0;102m')
        elif color_high_intensity_backgrounds == ('yellow'):
            pyperclip.copy('\\033[0;103m')
        elif color_high_intensity_backgrounds == ('blue'):
            pyperclip.copy('\\033[0;104m')
        elif color_high_intensity_backgrounds == ('purple'):
            pyperclip.copy('\\033[0;105m')
        elif color_high_intensity_backgrounds == ('cyan'):
            pyperclip.copy('\\033[0;106m')
        elif color_high_intensity_backgrounds == ('white'):
            pyperclip.copy('\\033[0;107m')
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
        pyperclip.copy('Black = \\033[0;100m\nRed = \\033[0;101m\nGreen = \\033[0;102m\nYellow = \\033[0;103m\nBlue = \\033[0;104m\nPurple = \\033[0;105m\nCyan = \\033[0;106m\nWhite = \\033[0;107m')
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
        print('Invalid option, returning to High Intensity Backgrounds Colors Menu')
        spinning_cursor(3)
        os.system('clear')

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
        
    elif option == '2':
        os.system('clear')
        while True:
            bold()
            os.system('clear')
            break
        

    elif option == '3':
        os.system('clear')
        while True:
            underline()
            os.system('clear')
            break

    elif option == '4':
        os.system('clear')
        while True:
            background()
            os.system('clear')
            break
    
    elif option == '5':
        os.system('clear')
        while True:
            high_intensity()
            os.system('clear')
            break

    elif option == '6':
        os.system('clear')
        while True:
            bold_high_intensity()
            os.system('clear')
            break
    
    elif option == '7':
        os.system('clear')
        while True:
            high_intensity_backgrounds()
            os.system('clear')
            break

    elif option == '8':
        print('\n❌ Exiting...')
        time.sleep(1)
        os.system('clear')
        exit()