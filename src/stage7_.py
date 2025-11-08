def malakar_final_form_scene():
    from effects import typewriter,time
    print("\033[2J\033[H", end="")
    typewriter("  The Abyss Below  \n", 0.06)
    time.sleep(1.5)

    paragraphs = [
        "Malakar staggers backward, his blade clattering across the marble floor.\n",
        "Dark smoke seeps from the cracks in his armor — his form flickering between shadow and flesh.\n",
        "He drops to one knee, clutching his chest as the black fire in his eyes begins to fade.\n",
        "For a moment, the throne room is silent — only the echo of his ragged breathing remains.\n",
        "You step forward, weapon in hand... ready to finish it.\n",
        "Then — he laughs.\n",
        "It starts as a rasping chuckle, then grows into a deep, bone-rattling howl.\n",
        "The floor trembles. The air burns cold.\n",
        "Crimson cracks split through the stone beneath his feet, spreading like veins of molten glass.\n",
        "‘You think... this ends with, me?’ he croaks, voice warping — layered with something ancient, something wrong.\n",
        "The ground collapses beneath you both, plunging you into the dark.\n",
        "Your body slams into cold stone, the world spinning — dust and shadows swirling around you.\n",
        "You raise your head just in time to see him descend... reborn.\n"
    ]

    for p in paragraphs:
        typewriter(p, 0.04)
        time.sleep(1.2)

    typewriter("  His armor reforms — no longer silver or black, but a shifting void of flame and bone.\n", 0.04)
    time.sleep(1)
    typewriter("Where his face once was now burns a crown of horns and lightless eyes.\n", 0.04)
    time.sleep(1)
    typewriter("The dark spirit that haunted the kingdom finally reveals its name — Erevos, the Devourer of Light.\n", 0.05)
    time.sleep(1.5)
    typewriter("Malakar’s voice now echoes as many, twisted and distorted: ‘I am the end... and the beginning reborn.’\n", 0.05)
    time.sleep(1.2)

    typewriter("\nYou struggle to rise, the weight of his power pressing down like a storm.\n", 0.04)
    time.sleep(1)
    typewriter("A faint groan comes from nearby — and then, a voice you recognize.\n", 0.04)
    time.sleep(1.2)
    typewriter("‘Still breathing, are you?’\n", 0.04)
    time.sleep(1)
    typewriter("Aldric pulls himself from the rubble, clutching his sword, his armor cracked but his eyes burning bright.\n", 0.04)
    time.sleep(1.2)
    typewriter("He spits blood and steadies his stance beside you.\n", 0.04)
    time.sleep(1.2)
    typewriter("‘I swore an oath to end the shadow... and I’m not going down without a fight.’\n", 0.05)
    time.sleep(1.2)
    typewriter("Together, you face Erevos — the corrupted soul of Malakar reborn.\n", 0.05)
    time.sleep(1.2)
    input("\nPress Enter to begin the final battle: Erevos, Devourer of Light...")
