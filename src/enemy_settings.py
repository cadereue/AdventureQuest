
from tabulate import tabulate
#Training dummy
trainingDummy_health = 20
trainingDummy_attack1 = 5
trainingDummy_heal = 0

#Goblin
goblin_skill = {'Health': 25,
                'Heal': 5, 
                'Sword Slash': 10 }

def goblin_skill_table():
    RED = "\033[31m"
    RESET =  "\033[0m"
    """Return a live tabulated view of the player's current skills."""
    return tabulate(goblin_skill.items(), headers=[f'{RED}Goblin{RESET}', f'{RED}Stats{RESET}'], tablefmt='grid')

#Fallen Guard
fallenGuard_skill = {'Health': 65,
                     'Shield': 15,
                     'Eternal Doom': 100,
                     'Sword Slash': 20,
                     'Dark Magic': 35,}

def fallenGuard_skill_table():
    RED = "\033[31m"
    RESET =  "\033[0m"
    """Return a live tabulated view of the player's current skills."""
    return tabulate(fallenGuard_skill.items(), headers=[f'{RED}Fallen Guard{RESET}', f'{RED}Stats{RESET}'], tablefmt='grid')

#Dragon
# dragon_health = 145
# dragon_attack1 = 35 #wall of fire
# dragon_attack2 = 45 #Stomp on the player
# dragon_heal = 25 
# dragon_blazing_fury = 100 # 1-20 chance of getting this

dragon_skill = {'Health': 250,
                'Fire Ember': 25,
                'Wall of Fire': 35,
                'Ember Stomp': 45,
                'Blazing Fury': 100}

def dragon_skill_table():
    RED = "\033[31m"
    RESET =  "\033[0m"
    """Return a live tabulated view of the player's current skills."""
    return tabulate(dragon_skill.items(), headers=[f'{RED}Dragon{RESET}', f'{RED}Stats{RESET}'], tablefmt='grid')


#Malakar
# malakar_health = 200
# malakar_attack1 = 50 #Fireball
# malakar_attack2 = 35 #Brings down a dark magic sword
# malakar_attack3 = 5 #takes away stamina so you have to lose a turn
# malakar_attack4 = 60 # death beyond the grave- drags you down to the pits of hell with him for you to fight him
# malakar_heal = 30 

malakar_skill = {'Health': 500,
                 'Dark Arts': 30,
                 'Fireball' : 70,
                 'Dark Sword': 55,
                 'Stamina Steal': 2, #Takes away stamina so you lose a turn
                 'Dark Pursuit': 80, } #Takes you too a new areana and while that happens you lose all your stamina and almost all health

def malakar_skill_table():
    RED = "\033[31m"
    RESET = "\033[0m"
    return tabulate(malakar_skill.items(), headers=[f'{RED}Malakar{RESET}', f'{RED}Stats{RESET}'], tablefmt='grid')

#Dark emperor - player will "defeat" malakar but then the dark emperor will come out, think of it like the gannon fight in legend of zelda, have aldric come back and help the player
#Aldric pics up the player to join him in battle and grants the player more health and stamina only if the player spared him
aldric_skill = {'Health':450,
                'Sword of Truth': 150,
                'Shield of Nobility': 50, #Will heal you and aldric
                'Gods of the Divine': 200} #Drops swords from the sky on erevos

erevos_skill = {'Health':2000,
                'Dark Synergy': 500,
                'Dark Sword': 120,
                'Dark Pursuit': 200}

def erevos_skill_table():
    RED = "\033[31m"
    RESET =  "\033[0m"
    return tabulate(erevos_skill.items(), headers=[f'{RED}Erevos{RESET}', f'{RED}Stats{RESET}'], tablefmt='grid')

def aldric_skill_table():
    BLUE = "\033[34m"
    RESET =  "\033[0m"
    return tabulate(aldric_skill.items(), headers=[f'{BLUE}Aldric{RESET}', f'{BLUE}Stats{RESET}'], tablefmt='grid')
