import sys, time, os

def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def delay():
    time.sleep(1.5)
# Text colors

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets all formatting
