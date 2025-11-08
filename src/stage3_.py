import time, sys, random

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()



def start_stage3():
    print("\033[2J\033[H", end="")
    slow_print("⚔️  CHAPTER III: THE FALLEN KNIGHT  ⚔️", 0.07)
    time.sleep(1.5)
    print()

    slow_print("You approach the gates of the Iron Citadel, where shadows crawl across the stones.")
    slow_print("The air feels heavier here — charged with magic and malice.\n")
    time.sleep(1.3)

    slow_print("Suddenly, the ground trembles. A dark figure blocks your path.")
    slow_print("It wears cracked armor marked with the royal crest — your old order’s emblem.")
    slow_print("But the eyes beneath its helm glow with a sickly violet light.\n")
    time.sleep(1.5)

    slow_print("‘You should not have returned,’ a voice growls — distorted, echoing from beyond the grave.")
    slow_print("You recognize it. Ser Aldric, your former captain — the strongest of the Crown Guard.")
    slow_print("Now twisted by Malakar’s curse into something monstrous.\n")
    time.sleep(1.5)

    slow_print("Aldric raises his sword, black smoke trailing from the blade’s edge.")
    slow_print("“The King is gone... The throne is ash... and so shall you be.”\n")
    input("Press Enter to prepare for battle...")