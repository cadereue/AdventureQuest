#Code for player values
from tabulate import tabulate

player_name = input('Please input character name:').lower()


##Dictionary containing all of the players attributes including powers and character values, if you change make sure to change the route in the actual code
player_skill = {'Health': 100,
                'Health potion': 10,
                'Stamina': 5, 
                'Catch Breath': 2,
                'Sword Slash': 15,
                }

keybind = {'Health potion[H]': '-3',
           'Catch Breath[Y]': '+2',
           'Sword Slash[1]': '-2',
           }

def skill_table():
    """Return a live tabulated view of the player's current skills."""
    return tabulate(player_skill.items(), headers=['Player', 'Stats'], tablefmt='grid')

def keybind_table():
    return tabulate(keybind.items(), headers=['Ability', 'Stamina'], tablefmt='grid')