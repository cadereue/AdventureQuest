import sys, time, player_settings

def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def chapel_of_ashes_scene():
    print("\033[2J\033[H", end="")
    typewriter("  The Chapel of Ashes  \n", 0.06)
    time.sleep(1.2)

    paragraphs = [
        "Aldric leads you through a narrow stone passage, torchlight flickering against the damp walls.\n",
        "The air grows colder with each step until the tunnel opens into a ruined chapel beneath the castle.\n",
        "Once a place of prayer, it now lies buried in silence — pews rotted, windows shattered, light filtering through cracks above.\n",
        "Blue flames dance upon forgotten altars. A massive statue of a weeping angel stands at the far end, clutching a sword broken in half.\n",
        "Aldric stops before it, his voice barely a whisper. ‘This was where I swore my oath... before Malakar fell to shadow.’\n",
        "He turns to you, his eyes dim but steady. ‘The throne room lies beyond this sanctum, sealed by the wisdom of the old kings.’\n",
        "As he speaks, runes ignite on the chapel walls, glowing faint gold — and a voice older than the kingdom echoes through the stone:\n"
    ]

    for p in paragraphs:
        typewriter(p, 0.04)
        time.sleep(1.2)

    typewriter("\n“Only the wise may pass. Speak the answer, and the gate shall open.”\n", 0.04)
    time.sleep(1)
    typewriter("  The runes rearrange, forming words of the riddle:\n", 0.04)
    time.sleep(1)

    typewriter("\n‘I am not alive, but I grow. I have no lungs, but I need air. I have no mouth, yet water kills me. What am I?’\n", 0.05)
    time.sleep(1.5)

    # Riddle answer input
    attempts = 3
    while attempts > 0:
        answer = input("\nYour answer: ").strip().lower()
        if answer in ["fire", "a fire"]:
            typewriter("\n The runes flare bright and dissolve into golden dust, revealing a hidden staircase beneath the angel statue.\n", 0.04)
            typewriter("Aldric smiles faintly. ‘Well done... the old flame still burns in you.’\n", 0.04)
            typewriter(" You feel a warmth surround you. (+50 Health, +10 Stamina, New ability: [2]Lightning Bolt +100 damage)\n", 0.04)
            player_settings.player_skill['Health'] +=50
            player_settings.player_skill['Stamina'] += 10
            player_settings.player_skill.update({'Lightning Bolt': 100})
            player_settings.keybind.update({'Lightning Bolt[2]': '-3'})
            time.sleep(1)
            input("\nPress Enter to descend into Malakar’s Sanctum...")
            return "success"
        else:
            attempts -= 1
            if attempts > 0:
                typewriter(f"\nThe runes flicker angrily. ‘That is not the answer...’ ({attempts} tries left)\n", 0.04)
            else:
                typewriter("\nThe chapel trembles. The light fades — you feel the gate rejecting your soul.\n", 0.04)
                typewriter("Aldric steps forward, chanting words of an old prayer, forcing the runes to calm.\n", 0.04)
                typewriter("‘You may still pass,’ he says wearily, ‘but the blessing is lost.’ (-10 Health, -5 Stamina)\n", 0.04)
                player_settings.player_skill['Health'] -= 10
                player_settings.player_skill['Stamina'] -= 5
                input("\nPress Enter to descend into Malakar’s Sanctum...")
                return "fail"
