
def training_dummy():
    import enemy_settings,player_settings,effects
    from tabulate import tabulate
    from effects import delay
    Player = player_settings.player_name
    enemy_health = enemy_settings.trainingDummy_health
    enemy_type = 'Training Dummy'
    typewritter = effects.typewriter
    typewritter(f'Enemy type: {enemy_type}')
    typewritter('Welcome to training fellow knight \nIm going to be guiding you through the basic mechanics so that you can reclaim the kingdom back from the sinistar Malakar') 
    print(f'\nEnemy health: {enemy_health}')
    print(f'Player health: {player_settings.player_skill['Health']}')
    while True:
        player_attack1 = input('Press [1] to use your sword attack: -10 Enemy Health').lower()
        if player_attack1 == '1':
            typewritter('Perfect!')
            typewritter('Each time you use one of your abilities it effects the battle in a certain way')
            enemy_health -= 10
            break
        else:
            print('Please press [1]')
    
    
    typewritter('\nAs you progress through the game you will gain opertunities to unlock different abilities')
    typewritter('The new abilites you unlock will bind to the different number keys, ex). [2],[3]...')
    typewritter('At anytime during the game, you can press the key [M] to display your different keybinds')
    
    print(f'\nEnemy health: {enemy_health}')
    print(f'Player health: {player_settings.player_skill['Health']}')
    
    while True:
        player_attack2 = input('Press [2] to use the punch ability: -5 Enemy Health').lower()
        if player_attack2 == '2':
            typewritter('Bravo!')
            typewritter('You will not have this ability in the game but this is an example of how to use your learned powers as you progress\nNext up we are going to try healing your player')
            enemy_health -=5
            break
        else:
            print('Please press [2]')

    print(f'\nEnemy health: {enemy_health}')
    print(f'Player health: {player_settings.player_skill['Health']}')

    while True:
        player_attack2 = input('Now press [h] to heal your player: +5 Player Health').lower()
        if player_attack2 == 'h':
            typewritter('\nNice job!')
            typewritter('Using your healing ability can be crucial to stay in the fight \nMake sure to watch your health as some of the enemies can deal massive damage')
            player_settings.player_skill['Health'] += 5
            break
        else:
            print('Please press [h]')
    
    typewritter('\nThe crucial role in staying in any fight is to keep your stamina up')
    typewritter('Different abilities will exert a certain amount of stamina on your player')
    
    print(f'\nEnemy health: {enemy_health}')
    print(f'Player health: {player_settings.player_skill['Health']}')
    print(f'Player Stamina: {player_settings.player_skill['Stamina']}')
    while True:
        player_attack3 = input('Press [y] to skip your turn against the enemy and allow you to gain stamina: +2').lower()
        if player_attack3 == 'y':
            typewritter('\nPerfect, while the enemy did gain a turn on you you were able to gain stamina')
            typewritter('Abilities that you unlock later in the game cost more stamina so it is import to conserve it wisely')
            player_settings.player_skill['Stamina'] += 2
            break
        else:
            print('Please enter [y]')
    typewritter('\nBelow is you skill table, the skill table shows all of your players stats and values')
    typewritter('When you unlock new abilities they will apear here for you to see')
    
    print(player_settings.skill_table())

    typewritter('\nWell done, you have completed the tutorial, here is a little gift to help you on your journey')
    while True:
        player_upgrade = input('Would you like to improve Stamina(+2), [2] Health(+10), or [3] Sword Damage(+5)?').lower()
        if player_upgrade == "1":
            player_settings.player_skill['Stamina'] += 2
            typewritter('You received a magic potion that increases your stamina: Stamina +2')
            break
        elif player_upgrade == "2":
            player_settings.player_skill['Health'] += 10
            typewritter('You received a peice of iron armor that blocks enemy attacks: Health +10')
            break
        elif player_upgrade == "3":
            player_settings.player_skill['Sword Slash'] += 5
            typewritter('You received a new sword that glistens in the light: Sword Damage +5')
            break
        else:
            typewritter('Please select an option: [1] Stamina, [2] Health, [3] Sword Damage')
        

    typewritter(f'\nSo I guess you are up for the real challenge then {Player}')
    delay()