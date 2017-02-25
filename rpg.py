#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

rpg_map = {'1': {'name': 'loc1', 'description': 'location 1', 'exit': {'south': '3', 'east': '2'}},
           '2': {'name': 'loc2', 'description': 'location 2', 'exit': {'west': '1', 'south': '4'}},
           '3': {'name': 'loc3', 'description': 'location 3', 'exit': {'east': '4', 'north': '1'}},
           '4': {'name': 'loc4', 'description': 'location 4', 'exit': {'north': '2', 'west': '3'}},
           }

# {'name', loc_id}
char = {'position': '1'}


def check_next_step(direction):
    global char
    try:
        move = rpg_map[char['position']]['exit'][direction]
        char['position'] = move
    except KeyError:git ini 
        return False

print('Current position: ', char['position'])
check_next_step('west')
print('New position: ', char['position'])
