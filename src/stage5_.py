
import time, sys, player_settings
player_name = player_settings.player_name

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def start_stage5():
    print("\033[2J\033[H", end="")
    slow_print("  THE SEALED GATE  \n", 0.06)
    slow_print("You stand before the obsidian door, runes glowing faintly red...")
    time.sleep(1.5)
    slow_print("A whisper echoes from beyond:")
    time.sleep(1)
    slow_print("\n“Only those who answer true may enter the throne of flame.”\n")

### riddle    
    while True:
        slow_print('For those who kneel to Malakar, take your place,')
        slow_print('For those who do not, will be covered in stone,')
        time.sleep(1.7)
        slow_print('For the gate you see before is sealed with souls,')
        slow_print('Of those who did not kneel, but decided to stand so')
        time.sleep(1.5)
        slow_print('For if you wish to see Malakar, state your name')
        slow_print('And we will decide, weather or not your fate shall remain the same')
        player_answer = input('Input your answer to the riddle').lower()
        if player_answer == player_name:
            slow_print('So you are the one Malakar has requested')
            slow_print('The gates open with a loud groan')
            break
        else:
            slow_print('Access denied')
            print(player_answer)
            print(player_name)
    input('\nPress Enter to enter into Malakars throne room...')