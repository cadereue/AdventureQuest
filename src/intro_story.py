import time
import sys

def slow_print(text, delay=0.04):
    """Prints text slowly for a cinematic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro_scene():
    # Optional: clear screen (works in most terminals, not always in Jupyter)
    print("\033[2J\033[H", end="")

    slow_print("  THE FALLEN CROWN  ", 0.07)
    time.sleep(3.5)
    print()
    
    slow_print("The kingdom of Aeloria was once a land of light—")
    slow_print("golden fields stretching beyond the horizon, laughter echoing through marble halls,")
    slow_print("and banners of the Crown fluttering proudly in the wind.\n")
    time.sleep(1)

    slow_print("But that was before... the Shadowfall.\n")
    time.sleep(1.2)

    slow_print("One night, the skies split open with black flame, and from it descended Malakar—")
    slow_print("the King’s own High Mage. In his desperate attempt to protect the realm from an otherworldly storm,")
    slow_print("he tore the veil between life and death. What he summoned instead was ruin.\n")
    time.sleep(1.2)

    slow_print("The royal capital burned. The rivers turned to ash.")
    slow_print("Those sworn to protect the throne were corrupted into monsters of smoke and steel—")
    slow_print("the Obsidian Legion.\n")
    time.sleep(1.5)

    slow_print("You were there. A knight of the Crown Guard, loyal until the end.")
    slow_print("You remember the screams, the fire... and the cold touch of death.\n")
    time.sleep(1)

    slow_print("Yet... death never came.\n", 0.07)
    time.sleep(1.3)

    slow_print("You awaken now among the ruins, armor rusted, sword dull, memories fractured.")
    slow_print("The once-vibrant kingdom lies silent—a graveyard wrapped in mist.")
    slow_print("Only the faint echo of the Crown’s sigil still burns within your chest.\n")
    time.sleep(1.3)

    slow_print("A whisper stirs through the wind:\n")
    time.sleep(1)
    slow_print("    “The throne is waiting... Take it back, if you have the strength.”\n", 0.06)
    time.sleep(1.5)

    slow_print("You rise, hand gripping your blade. The journey to reclaim Aeloria begins anew.\n")
    slow_print("Every fall is a lesson. Every death, a rebirth.")
    slow_print("The crown will not rise easily — but neither will you fall quietly.\n")
    time.sleep(1.5)

    input("⚔️  Press Enter to begin your adventure... ")


