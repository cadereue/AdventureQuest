#Player dictionary values that can be updated by the ints and items that the player has unlocked, also created a shield system
from tabulate import tabulate
import player_settings_t, random
enemy_health = 50
health = 50 - player_settings_t.mydict['sword_damage']
print(health)
player_settings_t.mydict['sword_damage'] += 20
health2 = 50 - player_settings_t.mydict['sword_damage']
print(health2)
print(player_settings_t.mydict)

player_settings_t.mydict.update({'dark matter': 20, 
                                 'shield': 10})
print(player_settings_t.mydict)
##If player has a sheild value > 0, then run this in a try statement and then after it runs through the code for shield damage, you will then move outside the try block and move on to the damage taken.
while enemy_health > 0:
    enemy_damage = random.randint(1,100)
    player_damage = int(input('enter a number'))
    enemy_health -= player_damage
    if enemy_damage == player_settings_t.mydict['shield']:
        print('your shield has been broken')
        player_settings_t.mydict['shield'] = 0 
    elif enemy_damage > player_settings_t.mydict['shield']:
        enemy_damage -= player_settings_t.mydict['shield']
        player_settings_t.mydict['shield'] -= player_settings_t.mydict['shield']
        player_settings_t.mydict['health'] -= enemy_damage
        print(f'you took {enemy_damage} damage')
    else:
        player_settings_t.mydict['shield'] -= enemy_damage
        enemy_damage -= enemy_damage
        print(f'you took {enemy_damage} damage')

    print(tabulate(player_settings_t.mydict.items(), headers=['Stats','Damage' ], tablefmt='grid'))