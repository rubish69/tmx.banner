# termux_banner.py
import time
import random

def print_colored_text(text, color):
    color_code = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    colored_text = f"{color_code[color]}{text}{color_code['reset']}"
    print(colored_text)

def change_text_color(text):
    colors = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
    colored_text = ''.join([f"{random.choice(colors)}{char}" for char in text])
    return colored_text

def main():
    banner_text = "Termux Banner"
    for _ in range(5):  # Change text color 5 times
        colored_banner = change_text_color(banner_text)
        print_colored_text(colored_banner, 'cyan')
        time.sleep(1)

if __name__ == "__main__":
    main()
