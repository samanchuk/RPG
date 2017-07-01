#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from random import randint

rpg_map = {
    '1': {'name': 'loc1', 'description': 'location 1', 'exit': {'south': '3', 'east': '2'}, 'inventory': ['book'],
          'npc': {'ork': {'name': 'Bold', 'description': 'Bold Sits on floor he is ork', 'health': 100,
                          'attack': [1, 20]}}},
    '2': {'name': 'loc2', 'description': 'location 2', 'exit': {'west': '1', 'south': '4'}, 'inventory': ['table'],
          'npc': {'gnome': {'name': 'Gimley', 'description': 'Gimley Sits on window he is gnome', 'health': 100,
                            'attack': [1, 20]}}},
    '3': {'name': 'loc3', 'description': 'location 3', 'exit': {'east': '4', 'north': '1'}, 'inventory': ['sofa'],
          'npc': {'elf': {'name': 'Legolas', 'description': 'Legolas Sits on chair he is elf', 'health': 100,
                          'attack': [1, 20]}}},
    '4': {'name': 'loc4', 'description': 'location 4', 'exit': {'north': '2', 'west': '3'}, 'inventory': ['chair'],
          'npc':
              {
                  'gnome': {'name': 'Gimley', 'description': 'Gimley Sits on window he is gnome', 'health': 100,
                            'attack': [1, 20]},
                  'elf': {'name': 'Legolas', 'description': 'Legolas Sits on chair he is elf', 'health': 100,
                          'attack': [1, 20]}
              }
          }
}

# {'name', loc_id}
char = {'position': '1', 'inventory': ['book', 'cup', 'pencil'], 'health': 300, 'attack_type': {'spit': [1, 20]}}

# npc players list
npc = {'ork': {'name': 'Bolk', 'description': 'Bold Sits on floor he is ork', 'health': 100, 'attack': [1, 20]},
       'elf': {'name': 'Legolas', 'description': 'Legolas Sits on chair he is elf', 'health': 100, 'attack': [1, 20]},
       'gnome': {'name': 'Gimley', 'description': 'Gimley Sits on window he is gnome', 'health': 100,
                 'attack': [1, 20]}
       }


def fight(command):
    enemy = command.split()[1]
    room_id = char['position']
    if enemy in rpg_map[room_id]['npc']:
        while char['health'] != 0 and npc[enemy]['health'] != 0:
            input('Press enter to hit')
            char_attack_level = randint(char['attack_type']['spit'][0], char['attack_type']['spit'][1])
            print('You attacking with {0} level damage'.format(char_attack_level))
            npc[enemy]['health'] -= char_attack_level
            print('Enemy left {0} points'.format(npc[enemy]['health']))
            if npc[enemy]['health'] <= 0:
                print('Your hit was deathly!')
                break
            enemy_hits_char = randint(npc[enemy]['attack'][0], npc[enemy]['attack'][1])
            print('Enemy damaged you with {0} points'.format(enemy_hits_char))
            char['health'] -= enemy_hits_char
            print('You have {0} points after round'.format(char['health']))
            if char['health'] <= 0:
                print('You dead with honor')
                break
    else:
        print('Enemy {0} is absent in the room'.format(enemy))
    if char['health'] < npc[enemy]['health']:
        (rpg_map[room_id]['npc']).remove(enemy)
        (rpg_map[room_id]['inventory'].append('Unknown_body'))
        print('You lost this round')
        char['position'] = '1'
    else:
        del rpg_map[room_id]['npc'][enemy]
        rpg_map[room_id]['inventory'].append('Body_of_' + enemy)
        print('You win')


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
    show_room(char['position'])


def possible_move(command=None):
    current_room = char['position']
    exit_list = rpg_map[current_room]['exit'].keys()
    print('See possible exit(s):')
    for exit_direction in exit_list:
        print('{0} - {1}'.format(exit_direction,
                                 rpg_map[rpg_map[current_room]['exit'].get(exit_direction)]['description']))


def all_commands(command=None):
    print(' '.join(handlers.keys()))


def users_inventory(command=None):
    print('\n'.join(char['inventory']))


def take(command=None):
    room_id = char['position']
    if command:
        try:
            command.split()[1]
            try:
                rpg_map[room_id]['inventory'].remove(command.split()[1])
                char['inventory'].append(command.split()[1])
            except ValueError:
                print('No such inventory in the room')
        except IndexError:
            print('What do you want to take?')


def throw(command=None):
    room_id = char['position']
    if command:
        try:
            command.split()[1]
            try:
                char['inventory'].remove(command.split()[1])
                rpg_map[room_id]['inventory'].append(command.split()[1])
            except ValueError:
                print('You have no such inventory')
        except IndexError:
            print('What do you want to throw?')


def show_room(command=None):
    if rpg_map[char['position']]['inventory']:
        print('On floor placed:')
        print('\n'.join(rpg_map[char['position']]['inventory']))
        for room_npc in rpg_map[char['position']]['npc'].keys():
            print(rpg_map[char['position']]['npc'][room_npc]['description'])


handlers = {'scan': location_info, 'exits': possible_move, 'north': step, 'south': step, 'east': step, 'west': step,
            'take': take, 'user_inv': users_inventory, 'throw': throw, 'show_room': show_room, 'fight': fight,
            'commands': all_commands}


def main():
    location_info()
    while True:
        print('Health: [{0}]'.format(char['health']))
        command = input('Enter command: ')
        try:
            if command.split()[0] in handlers:
                handlers[command.split()[0]](command)
            else:
                print('Command "{0}" is not found'.format(command))
        except IndexError:
            print('Command line is empty enter correct one'.format(command))

main()
