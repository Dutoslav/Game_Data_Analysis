#game_generator.py generates random game data for data_analysis.py#
import json
import random

def game_name_generator(write_to_json):
    first_name_part = ['Mega', 'Party', 'Ultimate', 'Complete', '', 'Beast', 'Hyper', 'Fearless']
    second_name_part = [' Cycling', ' Outer', ' Racing', ' Fighting', ' Survival', ' Human', ' Viking', ' Sword']
    third_name_part = [' : 2', ' : 3', ' Endless Edition', ' Game', '', ' Legend', ' Complete Edition', ' GOTY']

    write_to_json['Game Name'] = '{first}{second}{third}'.format(first = first_name_part[random.randrange(0, 8)], second = second_name_part[random.randrange(0, 8)], third = third_name_part[random.randrange(0, 8)])
    
def game_release_generator(write_to_json):
    write_to_json['Release Year'] = random.randrange(1990, 2022) 

def sales_number_generator(write_to_json):
    weight = random.randrange(1, 100)
    if weight <= 5:
        write_to_json['Sales'] = random.randrange(8000000, 12000000)
    elif weight <= 15:
        write_to_json['Sales'] = random.randrange(4000000, 7999999)
    elif weight <= 40:
        write_to_json['Sales'] = random.randrange(1000000, 3999999)
    else:
        write_to_json['Sales'] = random.randrange(5000, 999999)

def platform_generator(write_to_json):
    platforms = ['PC', 'Mac', 'PS', 'XBox', 'Linux', 'Mobile']
    platforms_to_add = []
    num_platforms = 5
    i = 0
    platforms_to_generate = random.randrange(1, 6)

    while i < platforms_to_generate:
        if num_platforms != 0:
            add_platform = platforms[random.randrange(0, num_platforms)]
        else:
            add_platform = platforms[0]

        platforms_to_add.append(add_platform)
        platforms.remove(add_platform)
        num_platforms -= 1

        i += 1
    write_to_json['Game Platform(s)'] = platforms_to_add

def is_online_generator(write_to_json):
    if random.randrange(1, 100) < 30:
        write_to_json['Is Online'] = True
    else:
        write_to_json['Is Online'] = False

def developer_generator(write_to_json):
    developers_list = ['Activision', 'EA', 'Blizzard', 'Bethesda', 'Obsidian', 'Valve', '3D', 'Firework', 'Ubisoft', 'Octopie', 'RockSolid', 'CD Project Red', 'Paradox']
    write_to_json['Developer'] = developers_list[random.randrange(0, 12)]

def generate_game_data():
    write_to_json = {}
    
    game_name_generator(write_to_json)
    game_release_generator(write_to_json)
    sales_number_generator(write_to_json)
    platform_generator(write_to_json)
    is_online_generator(write_to_json)
    developer_generator(write_to_json)

    with open('game_info.json', 'w') as json_file:
        json.dump(write_to_json, json_file)
