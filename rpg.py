#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

rpg_map = {'1': {'name': 'loc1', 'description': 'location 1', 'exit': {'south': '3', 'east': '2'}},
           '2': {'name': 'loc2', 'description': 'location 2', 'exit': {'west': '1', 'south': '4'}},
           '3': {'name': 'loc3', 'description': 'location 3', 'exit': {'east': '4', 'north': '1'}},
           '4': {'name': 'loc4', 'description': 'location 4', 'exit': {'north': '2', 'west': '3'}},
           }

# {'name', loc_id}
char = {'position': '1'}


def step(direction):
    try:
        move = rpg_map[char['position']]['exit'][direction]
        char['position'] = move
        print('\nYou moved to: ', direction)
        location_info()
    except KeyError:
        print('Direction \"{0}\" is forbidden'.format(direction))


def location_info(command=None):
    room_id = char['position']
    print('Location name:\n\t{0}\t\nlocation description:\n\t{1}'.format(rpg_map[room_id]['name'],
                                                                         rpg_map[room_id]['description']))


def possible_move(command=None):
    current_room = char['position']
    exit_list = rpg_map[current_room]['exit'].keys()
    print('See possible exit(s):')
    for exit_direction in exit_list:
        print('{0} - {1}'.format(exit_direction,
                                 rpg_map[rpg_map[current_room]['exit'].get(exit_direction)]['description']))


def all_commands(command=None):
   print(' '.join(handlers.keys()))


handlers = {'scan': location_info, 'exits': possible_move, 'north': step, 'south': step, 'east': step, 'west': step,
            'commands': all_commands}


def main():
    location_info()
    while True:
        command = input('Enter command: ')
        if command.split()[0] in handlers:
            handlers[command.split()[0]](command)
        else:
            print('Command "{0}" is not found'.format(command))


main()
