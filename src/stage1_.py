import time
import sys
import random
import player_settings
def slow_print(text, delay=0.04):
    """Prints text slowly for immersion."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_stage1():
    slow_print("  STAGE 1: THE RUINED OUTSKIRTS ", 0.07)
    time.sleep(1.5)
    print()

    slow_print("The cold wind cuts through your battered armor as you rise from the ashen ground.")
    slow_print("You steady yourself and look around—the ruins of Aeloria stretch endlessly before you.")
    slow_print("Crumbling walls, collapsed towers, and scorched earth. The smell of smoke never left this place.\n")
    time.sleep(1.2)

    slow_print("Your sword feels heavy... but familiar. You grip it tighter.")
    time.sleep(1)

    slow_print("As you make your way down the cracked stone path, you notice something in the distance.")
    slow_print("An old church stands alone among the ruins, its bell long fallen and its doors shattered.\n")
    time.sleep(1.5)

    choice = input("Do you wish to enter the church or pass by it? (enter/pass): ").strip().lower()
    print()

    if choice == "enter":
        slow_print("You step carefully inside the darkened church. The air is thick with dust and silence.")
        slow_print("Faded murals of the old gods line the walls. You feel... watched.")
        time.sleep(1.5)
        slow_print("Suddenly, something rustles behind the altar.")
        slow_print("A sharp pain grips your ankle—")
        slow_print("Before you can react, a clawed hand yanks you into the darkness below!\n")
    else:
        slow_print("You decide not to linger. The church feels... wrong.")
        slow_print("As you pass its broken gates, you hear a low growl beneath your feet.")
        slow_print("The ground cracks open and something drags you down into the abyss!\n")

    time.sleep(1.5)
    slow_print("You tumble through the darkness, the echo of your own heartbeat pounding in your ears...")
    slow_print("When you finally land, you find yourself in a dim cavern beneath the ruins.\n")
    time.sleep(1.5)

    slow_print("A hunched creature crawls from the shadows—a goblin, twisted and wild-eyed, drooling with hunger.")
    slow_print("Its jagged blade drips with the blood of other unlucky souls.\n")
    time.sleep(1)

    slow_print("⚔️  The goblin snarls and lunges at you!\n", 0.07)
    time.sleep(1)