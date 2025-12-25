###Menu
#import intro_story
# main_game.py

import battle_code, tutorial,player_settings
import intro_story, stage1_,stage2_,stage3_,stage4_,stage5_,stage6_,stage7_
import spareOrkill, spare  # assuming you have a spare.py for mercy path
from effects import typewriter,clear_console
from spareOrkill import start_spareorkill
#Testing
if player_settings.player_name == 'test':
    sword = int(input('input sword damage:'))
    health = int(input('input player health:'))
    stamina = int(input('input player stamina:'))
    player_settings.player_skill['Sword Slash'] = sword
    player_settings.player_skill['Health'] = health
    player_settings.player_skill['Stamina'] = stamina
    battle = input('Who would you like to battle?:').lower()
    if battle == 'goblin':
        battle_code.goblin()
    elif battle == 'fallen_guard':
        battle_code.fallen_guard()
    elif battle == 'dragon':
        battle_code.dragon()
    elif battle == 'malakar':
        battle_code.malakar()
    elif battle == 'erevos':
        battle_code.erevos()
    else:
        print('not found')
        



def main():
    playerAlive = True
    print(f'Welcome {player_settings.player_name}')
    #Intro Scene
    clear_console()
    # intro_story.intro_scene()
    # Ask if the player has played before
    clear_console()
    while True:
        player_start = input('Have you played before? [Yes/No] ').lower()
        if player_start == 'no':
            typewriter('Well, let\'s put you in training then')
            tutorial.training_dummy()
            break
        elif player_start == 'yes':
            break
        else:
            print('Please enter either yes or no')
    clear_console()
    # Stage 1 (optional)
    stage1_.start_stage1()
    clear_console()
    playerAlive = battle_code.goblin()
    if not playerAlive:
        typewriter('You Died')
        return
    clear_console()
    #Stage 2
    stage2_.start_stage2()
    #Stage 3
    clear_console()
    stage3_.start_stage3()
    # Fallen Guard encounter
    clear_console()
    playerAlive = battle_code.fallen_guard()
    if not playerAlive:
        typewriter('You Died')
        return
    clear_console()
    # Decide next stage based on mercy/kill choice
    next_stage = spareOrkill.start_spareorkill()
    if next_stage == 'mercy':
        spare.chapel_of_ashes_scene()
        
    else:
        stage4_.start_stage4()  # Call a function in stage4_.py
        playerAlive = battle_code.dragon()
        if not playerAlive:
            typewriter('You Died')
            return
    clear_console()
    # Stage 5
    stage5_.start_stage5()  # Call a function in stage5_.py
    clear_console()
    stage6_.malakar_intro() #Intro scene to the malakar battle
    playerAlive = battle_code.malakar()
    if not playerAlive:
        typewriter('You Died')
        return
    clear_console()
    stage7_.malakar_final_form_scene()
    clear_console()
    playerAlive = battle_code.erevos()
    if not playerAlive:
        typewriter('You Died')
    # End game if player dies
    if not playerAlive:
        typewriter('You Died')
        return
    if playerAlive:
        typewriter('Thank you for playing "THE FALLEN CROWN"\n Developers: Creedmoor')
# Ensures this only runs if this file is executed directly
if __name__ == "__main__":
    main()


