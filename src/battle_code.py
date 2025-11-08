def dragon():
    import random,enemy_settings,player_settings
    from effects import clear_console, delay, typewriter
    Player = player_settings.player_name
    enemy_type = 'Dragon'
    Alive = True
    #Fight code
    print(enemy_settings.dragon_skill_table())
    print(player_settings.skill_table())
    while Alive == True:
        
        while True:
            enemy_attack_chance = random.randint(1,5)
            player_attack = input('Input player move?').lower()
            #Player move
            if player_attack == 'm':
                print(player_settings.keybind_table())
                continue
            elif player_attack == '1' and player_settings.player_skill['Stamina'] >= 2:
                player_settings.player_skill['Stamina'] -= 2
                enemy_settings.dragon_skill['Health'] -= player_settings.player_skill['Sword Slash']
                typewriter(f'{Player} used sword slash: -{player_settings.player_skill['Sword Slash']} enemy health')
                break
            elif player_attack == '2' and player_settings.player_skill['Stamina'] >= 3:
                if 'Lightning Bolt' in player_settings.player_skill:
                    enemy_settings.dragon_skill['Health'] -= player_settings.player_skill['Lightning Bolt']
                    player_settings.player_skill['Stamina'] -= 3
                    typewriter(f'{Player} used Lightning Bolt: -{player_settings.player_skill['Lightning Bolt']} enemy health')
                    break
                elif 'Dark Magic' in player_settings.player_skill:
                    enemy_settings.dragon_skill['Health'] -= player_settings.player_skill['Dark Magic']
                    player_settings.player_skill['Stamina'] -= 3
                    typewriter(f'{Player} used Dark Magic: -{player_settings.player_skill['Dark Magic']} enemy health')
                    break
                else:
                    print('Please enter a valid key')
            elif player_attack == 'h' and player_settings.player_skill['Stamina'] >= 3:
                player_settings.player_skill['Stamina'] -= 3
                player_settings.player_skill['Health'] += 10
                typewriter(f'{Player} used health potion: +{player_settings.player_skill['Health']} health')
                break
            else:
                player_settings.player_skill['Stamina'] += player_settings.player_skill['Catch Breath']
                typewriter(f'{Player} decided to catch their breath: +{player_settings.player_skill['Catch Breath']} stamina')
                break
        #Enemy move
            if enemy_attack_chance == 1:
                typewriter(f'{enemy_type} used wall of fire: -{enemy_settings.dragon_skill['Wall of Fire']} health')
                player_settings.player_skill['Health'] -= enemy_settings.dragon_skill['Wall of Fire']
                break
            elif enemy_attack_chance == 2:
                typewriter(f'{enemy_type} used fire embers: +{enemy_settings.dragon_skill['Fire Ember']} health')
                enemy_settings.dragon_skill['Health'] += enemy_settings.dragon_skill['Fire Ember']
                break
            elif enemy_attack_chance == 3:
                typewriter(f'{enemy_type} used stomp: -{enemy_settings.dragon_skill['Ember Stomp']} health')
                player_settings.player_skill['Health'] -= enemy_settings.dragon_skill['Ember Stomp']
                break
            elif enemy_attack_chance == 4:
                rand_chance = random.randint(1,20)
                if rand_chance == 15:
                    typewriter(f'{enemy_type} used Blazing Fury: -{enemy_settings.dragon_skill['Blazing Fury']} health')
                    player_settings.player_skill['Health'] -= enemy_settings.dragon_skill['Blazing Fury']
                    break
                else:
                    typewriter(f"{Player} dogged {enemy_type}'s attack")
                    break
        
        delay()
        clear_console()
        print(enemy_settings.dragon_skill_table())
        print(player_settings.skill_table())


        if player_settings.player_skill['Health'] < 1:
            Alive = False
        elif enemy_settings.dragon_skill['Health'] < 1:
            Alive = False
        


    if player_settings.player_skill['Health'] > 0:
        print(f'{Player} slayed the {enemy_type}')
        print('You wipe your sweat from under your brow and examine the damage around the throne room')
        print(f'{player_settings.player_name}: I just dont understand how strong Malakar has gotten...')
        return True
    else:
        print(f'{Player} was slayed by the {enemy_type}')
        return False


def fallen_guard():
    import random, enemy_settings, player_settings
    from effects import clear_console,typewriter,delay
    Player = player_settings.player_name
    enemy_type = 'Fallen Guard'
    Alive = True
    
    print(enemy_settings.fallenGuard_skill_table())
    print(player_settings.skill_table())
    while Alive == True:
        while True:
            enemy_attack_chance = random.randint(1,5)
            player_attack = input('Input player move').lower()
            if player_attack == 'm':
                    print(player_settings.keybind_table())
                    continue
            elif player_attack == '1' and player_settings.player_skill['Stamina'] >= 2:
                player_settings.player_skill['Stamina'] -= 2
                enemy_settings.fallenGuard_skill['Health'] -= player_settings.player_skill['Sword Slash']
                typewriter(f'{Player} used sword slash: -{player_settings.player_skill['Sword Slash']} enemy health')
            elif player_attack == 'h' and player_settings.player_skill['Stamina'] >= 3:
                player_settings.player_skill['Stamina'] -= 3
                player_settings.player_skill['Health'] += 10
                typewriter(f'{Player} used health potion: +{player_settings.player_skill['Health']} health')
            else:
                player_settings.player_skill['Stamina'] += player_settings.player_skill['Catch Breath']
                typewriter(f'{Player} decided to catch their breath: +{player_settings.player_skill['Catch Breath']} stamina')
            #Enemy settings
            #Add shield system here
            
            if enemy_attack_chance == 1:
                typewriter(f'{enemy_type} used Sword Slash: -{enemy_settings.fallenGuard_skill['Sword Slash']} health')
                player_settings.player_skill['Health'] -= enemy_settings.fallenGuard_skill['Sword Slash']
                break
            elif enemy_attack_chance == 2:
                attackchance = random.randint(1,20)
                if attackchance == 10:
                    typewriter(f'{enemy_type} used Eternal Doom: -{enemy_settings.fallenGuard_skill['Eternal Doom']} health')
                    player_settings.player_skill['Health'] -= enemy_settings.fallenGuard_skill['Eternal Doom']
                    break
                else:
                    typewriter(f'{enemy_type} tried to summon Eternal Doom but failed')
                break
            elif enemy_attack_chance == 3:
                typewriter(f'{enemy_type} used Dark Magic: -{enemy_settings.fallenGuard_skill['Dark Magic']} health')
                player_settings.player_skill['Health'] -= enemy_settings.fallenGuard_skill['Dark Magic']
                break
            elif enemy_attack_chance == 4:
                typewriter(f'{enemy_type} used Shield Block: +{enemy_settings.fallenGuard_skill['Shield']} health')
                enemy_settings.fallenGuard_skill['Health'] += enemy_settings.fallenGuard_skill['Shield']
                break
            else:
                typewriter(f"{Player} dogged {enemy_type}'s attack")
                break
        delay()
        clear_console()
        print(enemy_settings.fallenGuard_skill_table())
        print(player_settings.skill_table())
        
        if player_settings.player_skill['Health'] < 1:
            Alive = False
        elif enemy_settings.fallenGuard_skill['Health'] < 1:
            Alive = False

    if player_settings.player_skill['Health'] > 0:
       return True
    else:
        typewriter(f'{Player} was slayed by the {enemy_type}')
        return False


def goblin():
    import random,enemy_settings,player_settings
    from effects import typewriter, clear_console, delay
    Player = player_settings.player_name 
    enemy_type = 'Goblin'
    Alive = True
    #damageType_range = (1,2)
    print(enemy_settings.goblin_skill_table())
    print(player_settings.skill_table())
    while Alive == True:
        while True:
            enemy_attack_chance = random.randint(1,2)
            player_attack = input('Input player move?').lower()
            if player_attack == 'm':
                print(player_settings.keybind_table())
                continue
            elif player_attack == '1' and player_settings.player_skill['Stamina'] >= 2:
                player_settings.player_skill['Stamina'] -= 2
                enemy_settings.goblin_skill['Health'] -= player_settings.player_skill['Sword Slash']
                typewriter(f'{Player} used sword slash: -{player_settings.player_skill['Sword Slash']} enemy health')
                
            elif player_attack == 'h' and player_settings.player_skill['Stamina'] >= 3:
                player_settings.player_skill['Stamina'] -= 3
                player_settings.player_skill['Health'] += 10
                typewriter(f'{Player} used health potion: +{player_settings.player_skill['Health potion']} health')
                
            else:
                player_settings.player_skill['Stamina'] += player_settings.player_skill['Catch Breath']
                typewriter(f'{Player} decided to catch their breath: +{player_settings.player_skill['Catch Breath']} stamina')
                
            
            if enemy_attack_chance == 1:
                typewriter(f'{enemy_type} used sword slash: -{enemy_settings.goblin_skill['Sword Slash']} health')
                player_settings.player_skill['Health'] -= enemy_settings.goblin_skill['Sword Slash']
                break
            elif enemy_attack_chance == 2:
                typewriter(f'{enemy_type} used health potion: +{enemy_settings.goblin_skill['Heal']} health')
                enemy_settings.goblin_skill['Health'] += enemy_settings.goblin_skill['Heal']
                break
        delay()
        clear_console()    
        print(enemy_settings.goblin_skill_table())
        print(player_settings.skill_table())
        
        if enemy_settings.goblin_skill['Health'] < 1:
            Alive = False
        elif player_settings.player_skill['Health'] < 1:
            Alive = False


    if player_settings.player_skill['Health'] > 0:
        typewriter(f'{Player} slayed a {enemy_type}')
        typewriter('You look at the hellish creature that you just slayed and groan with disgust')
        typewriter(f'{player_settings.player_name}: This is going to be quite the journey...')
        return True
    else:
        typewriter(f'{Player} was slayed by a {enemy_type}')
        return False


def malakar():
    import random,enemy_settings,player_settings
    from effects import clear_console, delay, typewriter
    Player = player_settings.player_name
    enemy_type = 'Malakar'
    Alive = True
    #Fight code
    print(enemy_settings.malakar_skill_table())
    print(player_settings.skill_table())
    while Alive == True:
        
        #Player move
        while True: 
            enemy_attack_chance = random.randint(1,5)
            player_attack = input('Input player move?').lower()
            if player_attack == 'm':
                print(player_settings.keybind_table())
                continue
            elif player_attack == '1' and player_settings.player_skill['Stamina'] >= 2:
                player_settings.player_skill['Stamina'] -= 2
                enemy_settings.malakar_skill['Health'] -= player_settings.player_skill['Sword Slash']
                typewriter(f'{Player} used sword slash: -{player_settings.player_skill['Sword Slash']} enemy health')
                break            
            elif player_attack == '2' and player_settings.player_skill['Stamina'] >= 3:
                if 'Lightning Bolt' in player_settings.player_skill:
                    enemy_settings.malakar_skill['Health'] -= player_settings.player_skill['Lightning Bolt']
                    player_settings.player_skill['Stamina'] -= 3
                    typewriter(f'{Player} used Lightning Bolt: -{player_settings.player_skill['Lightning Bolt']} enemy health')
                    break
                elif 'Dark Magic' in player_settings.player_skill:
                    enemy_settings.malakar_skill['Health'] -= player_settings.player_skill['Dark Magic']
                    player_settings.player_skill['Stamina'] -= 3
                    typewriter(f'{Player} used Dark Magic: -{player_settings.player_skill['Dark Magic']} enemy health')
                    break
                else:
                    print('Please enter a valid key')
    
            elif player_attack == 'h' and player_settings.player_skill['Stamina'] >= 3:
                player_settings.player_skill['Stamina'] -= 3
                player_settings.player_skill['Health'] += player_settings.player_skill['Health Potion']
                typewriter(f'{Player} used health potion: +{player_settings.player_skill['Health Potion']} health')
                break
            else:
                player_settings.player_skill['Stamina'] += player_settings.player_skill['Catch Breath']
                typewriter(f'{Player} decided to catch their breath: +{player_settings.player_skill['Catch Breath']} stamina')
                break        
        
        #Enemy move
            if enemy_attack_chance == 1:
                typewriter(f'{enemy_type} used Fireball: -{enemy_settings.malakar_skill['Fireball']} health')
                player_settings.player_skill['Health'] -= enemy_settings.malakar_skill['Fireball']
                break
            elif enemy_attack_chance == 2:
                typewriter(f'{enemy_type} used Dark Arts: +{enemy_settings.malakar_skill['Dark Arts']} health')
                enemy_settings.malakar_skill['Health'] += enemy_settings.malakar_skill['Dark Arts']
                break
            elif enemy_attack_chance == 3:
                typewriter(f'{enemy_type} used Dark Sword: -{enemy_settings.malakar_skill['Dark Sword']} health')
                player_settings.player_skill['Health'] -= enemy_settings.malakar_skill['Dark Sword']
                break
            elif enemy_attack_chance == 4:
                rand_chance = random.randint(1,5)
                if rand_chance == 4:
                    typewriter(f'{enemy_type} used Dark Pursuit: -{enemy_settings.malakar_skill['Dark Pursuit']} health')
                    player_settings.player_skill['Health'] -= enemy_settings.malakar_skill['Dark Pursuit']
                    break
                else:
                    typewriter(f"{Player} dogged {enemy_type}'s attack")
                    break
            elif enemy_attack_chance == 5:
                typewriter(f'{enemy_type} used Stamina Steal: -{enemy_settings.malakar_skill['Stamina Steal']} stamina')
                player_settings.player_skill['Stamina'] -= enemy_settings.malakar_skill['Stamina Steal']
                break
        delay()
        clear_console()
        print(enemy_settings.malakar_skill_table())
        print(player_settings.skill_table())


        if player_settings.player_skill['Health'] < 1:
            Alive = False
        elif enemy_settings.malakar_skill['Health'] < 1:
            Alive = False
        


    if player_settings.player_skill['Health'] > 0:
        print(f'{Player} slayed {enemy_type}')
        return True
    else:
        print(f'{Player} was slayed by {enemy_type}')
        return False
    

def erevos():
    import random,enemy_settings,player_settings
    from effects import clear_console, delay, typewriter
    Player = player_settings.player_name
    enemy_type = 'Erevos'
    ally_type = 'Aldric'
    Alive = True
    #Fight code
    print(enemy_settings.erevos_skill_table())
    print(enemy_settings.aldric_skill_table())
    print(player_settings.skill_table())
    while Alive == True:
        
        #Player move
        while True: 
            alrdic_attack_chance = random.randint(1,3)
            enemy_attack_chance = random.randint(1,3)
            player_attack = input('Input player move?').lower()
            if player_attack == 'm':
                print(player_settings.keybind_table())
                continue
            elif player_attack == '1' and player_settings.player_skill['Stamina'] >= 2:
                player_settings.player_skill['Stamina'] -= 2
                enemy_settings.erevos_skill['Health'] -= player_settings.player_skill['Sword Slash']
                typewriter(f'{Player} used sword slash: -{player_settings.player_skill['Sword Slash']} enemy health')
                break            
            elif player_attack == '2' and player_settings.player_skill['Stamina'] >= 3:
                if 'Lightning Bolt' in player_settings.player_skill:
                    enemy_settings.erevos_skill['Health'] -= player_settings.player_skill['Lightning Bolt']
                    player_settings.player_skill['Stamina'] -= 3
                    typewriter(f'{Player} used Lightning Bolt: -{player_settings.player_skill['Lightning Bolt']} enemy health')
                    break
                elif 'Dark Magic' in player_settings.player_skill:
                    enemy_settings.erevos_skill['Health'] -= player_settings.player_skill['Dark Magic']
                    player_settings.player_skill['Stamina'] -= 3
                    typewriter(f'{Player} used Dark Magic: -{player_settings.player_skill['Dark Magic']} enemy health')
                    break
                else:
                    print('Please enter a valid key')
    
            elif player_attack == 'h' and player_settings.player_skill['Stamina'] >= 3:
                player_settings.player_skill['Stamina'] -= 3
                player_settings.player_skill['Health'] += player_settings.player_skill['Health Potion']
                typewriter(f'{Player} used health potion: +{player_settings.player_skill['Health Potion']} health')
                break
            else:
                player_settings.player_skill['Stamina'] += player_settings.player_skill['Catch Breath']
                typewriter(f'{Player} decided to catch their breath: +{player_settings.player_skill['Catch Breath']} stamina')
                break        
        #Aldric move
            if alrdic_attack_chance == 1:
                typewriter(f'{ally_type} used Sword of Truth: -{enemy_settings.aldric_skill['Sword of Truth']} enemy health')
                enemy_settings.erevos_skill['Health'] -= enemy_settings.aldric_skill['Sword of Truth']
                break
            elif alrdic_attack_chance == 2:
                typewriter(f'{ally_type} used Shield of Nobility: +{enemy_settings.aldric_skill['Shield of Nobility']} health')
                player_settings.player_skill['Health'] += enemy_settings.aldric_skill['Shield of Nobility']
                enemy_settings.aldric_skill['Health'] += enemy_settings.aldric_skill['Shield of Nobility']
                break
            elif alrdic_attack_chance == 3:
                typewriter(f'{ally_type} used Gods of the Divine: -{enemy_settings.aldric_skill['Gods of the Divine']} enemy health')
                enemy_settings.erevos_skill['Health'] -= enemy_settings.aldric_skill['Gods of the Divine']
                break
            
            #Enemy move
            if enemy_attack_chance == 1:
                typewriter(f'{enemy_type} used Dark Synergy: -{enemy_settings.erevos_skill['Dark Synergy']} health')
                player_settings.player_skill['Health'] -= enemy_settings.erevos_skill['Dark Synergy']
                break
            elif enemy_attack_chance == 2:
                typewriter(f'{enemy_type} used Dark Sword: -{enemy_settings.erevos_skill['Dark Sword']} health')
                player_settings.player_skill['Health'] -= enemy_settings.erevos_skill['Dark Sword']
                break
            elif enemy_attack_chance == 3:
                rand_chance = random.randint(1,2)
                if rand_chance == 2:
                    typewriter(f'{enemy_type} used Dark Pursuit: -{enemy_settings.erevos_skill['Dark Pursuit']} Aldric health')
                    enemy_settings.aldric_skill['Health'] -= enemy_settings.erevos_skill['Dark Pursuit']
                    break
                else:
                    typewriter(f'{enemy_type} used Dark Pursuit: -{enemy_settings.erevos_skill['Dark Pursuit']} health')
                    player_settings.player_skill['Health'] -= enemy_settings.erevos_skill['Dark Pursuit']
                    break
        
        delay()
        clear_console()
        print(enemy_settings.erevos_skill_table())
        print(enemy_settings.aldric_skill_table())
        print(player_settings.skill_table())

        if player_settings.player_skill['Health'] < 1:
            Alive = False
        elif enemy_settings.erevos_skill['Health'] < 500:
            Alive = False

        


    if player_settings.player_skill['Health'] > 0:
        typewriter('You fall to the ground and gasp for air\nOut of nowhere Aldric jumps towards Erevos, blade pointed at his skull')
        typewriter('"This is for my family and kingdom, Alaria"')
        typewriter('Aldric slashes into Erevos and for a moment he stands there panting, and the collapses')
        print(f'{Player} slayed {enemy_type}')
        return True
    else:
        print(f'{Player} was slayed by {enemy_type}')
        return False