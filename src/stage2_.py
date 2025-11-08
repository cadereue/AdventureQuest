import time, sys, random, player_settings

def slow_print(text, delay=0.04):
    """Print text slowly for immersion."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_stage2():
    print("\033[2J\033[H", end="")  # clear screen
    slow_print("  CHAPTER II: CROSSROADS OF DESTINY  ", 0.07)
    time.sleep(1.5)
    print()

    slow_print("You leave the dark cavern behind, climbing a jagged slope toward the surface.")
    slow_print("The faint light you saw before grows brighter until it blinds you momentarily.\n")
    time.sleep(1.2)

    slow_print("When your eyes adjust, you find yourself standing at a fork in the path.")
    slow_print("To the east lies a dense forest — ancient trees whispering secrets through the mist.")
    slow_print("To the west lies a broken trail leading to a ruined village, shrouded in smoke and silence.\n")
    time.sleep(1.5)

    slow_print("The voice within you murmurs:")
    slow_print("    “Two paths, one fate... Choose wisely, knight.”\n", 0.05)
    time.sleep(1)

    choice = ""
    while choice not in ["woods", "village"]:
        choice = input("Do you head into the (woods) or toward the (village)? ").strip().lower()

    if choice == "woods":
        print("\033[2J\033[H", end="")
        slow_print("  THE WHISPERING WOODS  ", 0.07)
        time.sleep(1.3)
        print()

        slow_print("You step beneath the ancient canopy of the forest.")
        slow_print("The air grows thick with fog, and every sound seems to echo endlessly.")
        slow_print("Twisted trees lean close as if listening to your heartbeat.\n")
        time.sleep(1.2)

        slow_print("Whispers drift through the air — soft, melodic, and strangely familiar.")
        slow_print("They call your name, promising rest... power... and forgiveness.\n")
        time.sleep(1.3)

        choice = input("Do you follow the whispers or resist them? (follow/resist): ").strip().lower()
        print()

        if choice == "follow":
            slow_print("You step off the path, drawn toward a pale glow deep within the woods.")
            slow_print("A clearing opens before you, and at its center floats a burning sigil — The Ember Sigil.")
            slow_print("It pulses with power and warmth. You reach out to touch it...")
            time.sleep(1.5)
            slow_print(" The sigil flares, searing your hand — but also filling you with strength!\n")
            player_settings.player_skill['Health'] += 20
            player_settings.player_skill['Sword Slash'] += 25
            slow_print("Your vitality surges. You feel renewed — but something deep within you... changes.(Sword Slash +25, Health +20)")
        else:
            slow_print("You shut your eyes and cover your ears, forcing yourself to ignore the whispers.")
            slow_print("A sudden gust of wind scatters the fog. The voices scream in fury and vanish.\n")
            slow_print("You feel a strange calm settle over you. The forest seems to respect your will.")
            player_settings.player_skill['Sword Slash'] += 25
            player_settings.player_skill['Stamina'] += 5
            slow_print("You gain a quiet strength from your resolve.(Sword Slash +25, Stamina +5)\n")

        time.sleep(1.3)


        slow_print("At the far edge of the woods, you glimpse a towering fortress of black stone — The Iron Citadel.")
        slow_print("You tighten your grip on your sword and march onward.\n")
        input("Press Enter to continue to the next chapter...")









    else:
    # -----------------------------
    # FORGOTTEN VILLAGE STORY PATH
    # -----------------------------
        print("\033[2J\033[H", end="")
        slow_print("  THE FORGOTTEN VILLAGE  ", 0.07)
        time.sleep(1.3)
        print()

        slow_print("The path winds through barren hills until you reach the edge of the village.")
        slow_print("Once a thriving settlement, it now lies in ruins — roofs caved in, windows shattered, streets silent.\n")
        time.sleep(1.3)

        slow_print("As you step through the broken gates, shadows flicker in the corners of your vision.")
        slow_print("Ghostly figures appear — townsfolk going about their lives as if nothing ever happened.")
        slow_print("Their laughter echoes, hollow and distant.\n")
        time.sleep(1.5)

        choice = input("Do you approach the spirits or avoid them? (approach/avoid): ").strip().lower()
        print()

        if choice == "approach":
            slow_print("You step closer, reaching out to one of the ghostly figures.")
            slow_print("It turns to face you — eyes empty, mouth open in silent pain.")
            slow_print("A haunting voice whispers: 'Save us... free us from the curse...'\n")
            slow_print("A wave of sorrow washes over you, but your resolve hardens.")
            player_settings.player_skill['Health'] += 50
            slow_print("You vow to lift the kingdom’s curse. Your heart burns brighter (+50 Health).")
        else:
            slow_print("You walk past the spectral figures, ignoring their cries for help.")
            slow_print("Their whispers fade, replaced by silence... and guilt.")
            slow_print("You find supplies in a nearby house — old bread, a flask of water,.")
            slow_print('As you drink from the flask you feel a rush of energy flow through your veins(+45 Sword Damage)')
            player_settings.player_skill['Sword Slash'] += 45
            slow_print("You feel stronger but colder inside.\n")

        time.sleep(1.3)
        

        slow_print("As you leave the village, a deep rumble shakes the ground.")
        slow_print("In the distance, the Iron Citadel rises like a wound in the earth, calling you forward.\n")
        input("Press Enter to continue to the next chapter...")


