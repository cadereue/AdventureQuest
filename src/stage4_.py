import time, sys, random

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def start_stage4():
    print("\033[2J\033[H", end="")
    slow_print("  CHAPTER IV: THE DRAGON OF THE THRONE  ", 0.07)
    time.sleep(1.5)
    print()

    slow_print("The great iron gates of the castle groan as you push them open.")
    slow_print("Ash and embers drift through the air — the scent of smoke thick and bitter.")
    slow_print("The grand hall is silent, but scorch marks stain the marble floors.")
    time.sleep(1.3)

    slow_print("At the far end of the hall, beneath the shattered throne, lies something vast.")
    slow_print("Scales like molten gold... a heartbeat like thunder.")
    slow_print("A single burning eye opens, bathing the room in crimson light.\n")
    time.sleep(1.5)

    slow_print("‘Another mortal seeks the throne?’ a voice rumbles, shaking the walls.")
    slow_print("‘I am **Vaelgrath**, last sentinel of the Crown. I burned the invaders... and I shall burn you.’")
    slow_print("The dragon rises, its wings unfurling in a storm of dust and fire.\n")
    input("Press Enter to prepare for battle...")