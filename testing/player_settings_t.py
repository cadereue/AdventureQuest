#sword_damage = 10
from tabulate import tabulate
player_name = input('Input player name').lower()

mydict = {'sword_damage': 10, 
          'bow_damage': 20,
          'health': 100 }

# table = tabulate(mydict.items(), headers=['Stats','Damage' ], tablefmt='grid')
print(tabulate(mydict.items(), headers=['Stats','Damage' ], tablefmt='grid'))

