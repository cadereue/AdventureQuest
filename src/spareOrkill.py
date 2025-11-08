import sys, time, player_settings
print("\033[2J\033[H", end="")
def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def start_spareorkill():
    slow_print("\n  With a final strike, your blade shatters Aldric’s cursed armor!")
    slow_print("He falls to one knee, his weapon clattering across the floor.")
    slow_print("The darkness within him flickers — and for a moment, his eyes are human again.")
    slow_print("‘Forgive me... I could not resist the darkness,’ he whispers before collapsing.")
    time.sleep(2)

    slow_print("\nYou step forward to claim your victory...")
    slow_print("...but suddenly, the air grows cold.")
    time.sleep(1)
    slow_print("A black mist seeps from Aldric’s wounds, twisting his body with unnatural force.")
    slow_print("His eyes snap open — glowing brighter than before.")
    slow_print("‘The curse... it does not die with me...’ he rasps.\n")
    time.sleep(2)

    slow_print("You grip your sword tightly. There is still time to act.")
    slow_print("Do you end his suffering — or show mercy and hear his final words?\n")
    time.sleep(1)

    print("  [1] Finish him off — claim his dark power")
    print("  [2] Spare him — accept his guidance and trust\n")

    choice = input("→ Your choice: ").strip()

    if choice == "1":
        # EXECUTION PATH — gain dark power
        slow_print("\nYou raise your sword high as Aldric kneels before you.")
        slow_print("“May the gods forgive me,” you whisper.")
        time.sleep(1.5)
        slow_print("The blade strikes true — and the chamber erupts in violet flame!")
        time.sleep(1)
        slow_print("A surge of dark energy floods through your veins — raw, chaotic, powerful.\n")
        slow_print("You feel your blood burn, your strength grow, and your mind darken.")
        player_settings.player_skill['Sword Slash'] +=75
        player_settings.player_skill.update({'Dark Magic': 150})
        player_settings.keybind.update({'Dark Magic[2]': '-5'})
        player_settings.player_skill['Stamina'] += 5
        player_settings.player_skill['Health'] += 200
        slow_print(" You have gained the ability: Dark Magic! (+75 Sword Damage, +5 Stamina, +200 health, +150 dark magic damage)\n")
        time.sleep(1.5)
        slow_print("The knight’s body turns to ash, leaving behind a faint whisper:")
        slow_print("‘Power always has a price…’")
        time.sleep(2)
        slow_print("\nYou push open the gates and enter the castle, the air heavy with magic and guilt.")
        next_stage = 'dark'
        return next_stage
    elif choice == "2":
        # MERCY PATH — gain Aldric’s sword
        slow_print("\nYou lower your weapon.")
        slow_print("Aldric’s trembling hand reaches for you — not to fight, but to kneel.")
        slow_print("‘You… you would spare me?’ he breathes, disbelief in his tone.")
        time.sleep(1.5)
        slow_print("You nod silently. The light in his eyes softens.")
        slow_print("‘Then I shall repay that mercy. Follow me.’")
        time.sleep(2)
        slow_print("He presses his blade — the Knight’s Honor — into your hands.")
        slow_print("‘It has served me faithfully. Now, it will serve you.’")
        time.sleep(1.5)
        slow_print("\nHe leads you behind the ruins of the hall, revealing a narrow stone passage hidden by shadow.")
        slow_print("‘This way,’ he says. ‘It leads to the castle’s inner sanctum — the dragon’s lair.’\n")
        player_settings.player_skill['Health'] += 150
        player_settings.player_skill['Sword Slash'] += 50
        slow_print("  You have gained: Aldric’s Sword and Armor! (+50 Sword Damage, +50 Health)\n")
        time.sleep(2)
        next_stage = "mercy"
        return next_stage