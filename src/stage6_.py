def malakar_intro():
    from effects import typewriter, time, clear_console
    print("\033[2J\033[H", end="")
    typewriter("  The Throne of Ash and Chains  \n", 0.06)
    time.sleep(1.2)

    paragraphs = [
        "You step into the grand throne room — or what remains of it.\n",
        "Once draped in gold and glory, now it lies drowned in shadow.\n",
        "The stained glass is shattered, the red sun bleeding through its broken shards.\n",
        "A black flame burns atop the dais, where the royal throne has become a twisted monument of bone and iron.\n",
        "Chains hang from the ceiling, clinking softly in the cold wind that seeps through the cracks of the ruined keep.\n",
        "And upon the throne, you see him — Malakar, the Fallen King.\n",
        "His armor, once shining silver, now crawls with veins of darkness. His eyes glow like dying embers.\n",
        "He rises slowly, his voice echoing through the chamber like the toll of a funeral bell:\n"
    ]

    for p in paragraphs:
        typewriter(p, 0.04)
        time.sleep(1.2)
    clear_console()
    dialogue = [
        "\"So... the world still sends its champions.\"\n",
        "\"Do you even know what you fight for? The people? The kingdom?\"\n",
        "He laughs — a sound hollow and cruel. ‘They begged for salvation... but when I sought to give it, they called me monster.’\n",
        "\"I saw the rot beneath their smiles. The greed of nobles. The prayers of cowards. The gods turned their backs, so I burned their thrones.\"\n",
        "\"This land was never pure — I merely tore away its mask.\"\n",
        "He steps down from the dais, dragging a massive blade that leaks black fire across the floor.\n",
        "\"Now you stand where I once stood — believing yourself righteous. Tell me, hero...\"\n",
        "\"Will you save them? Or will you see, as I did, that they are not worth saving?\"\n"
    ]

    for line in dialogue:
        typewriter(line, 0.045)
        time.sleep(1.3)

    typewriter("\n  The air trembles. The black flame roars to life. Malakar draws his blade, and the throne room itself begins to twist around him.\n", 0.04)
    time.sleep(1.2)
    typewriter("  Boss Fight: Malakar, The Fallen King\n", 0.05)
    input("\nPress Enter to begin the final battle...")
