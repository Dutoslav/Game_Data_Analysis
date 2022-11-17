#data_analysis.py analyzes the randomly generated data from game_generator.py#
import time
import json
import game_generator   #Importing the game_generator module in order to access its generate_game_data() function#

def average_sales(analyzed_data, sales_per_developer):   #This function calculates the average number of sales per game for each Developer and stores the results in the analyzed_data dictionary#
  for key, value in sales_per_developer.items():
    analyzed_data['Average Sales per Developer'][key] = sales_per_developer[key] / analyzed_data['Games per Developer'][key]

def data_analysis(game_data, analyzed_data, sales_per_developer):   #This function analyzes data in the game_data dictionary and stores the results in the analyzed_data dictionary#
  for key, value in game_data.items():
    if key == 'Release Year':
      if str(value) in analyzed_data['Release']:
        analyzed_data['Release'][str(value)] += 1
      else:
        analyzed_data['Release'][str(value)] = 1
    
    elif key == 'Game Platform(s)':
      for platform in value:
        if platform in analyzed_data['Platforms']:
          analyzed_data['Platforms'][platform] += 1
        else:
          analyzed_data['Platforms'][platform] = 1
    
    elif key == 'Is Online':
      if value in analyzed_data['Online']:
        analyzed_data['Online'][value] += 1
      else:
        analyzed_data['Online'][value] = 1

    elif key == 'Developer':
      if value in analyzed_data['Games per Developer']:
        analyzed_data['Games per Developer'][value] += 1
      else:
        analyzed_data['Games per Developer'][value] = 1
      
      if value in sales_per_developer:
        sales_per_developer[value] += game_data['Sales']
      else:
        sales_per_developer[value] = game_data['Sales']

def print_results(analyzed_data):
  for key, value in analyzed_data.items():  #This part of code prints out the results of the anlysis from the analyzed_data dictionary#
    print(str(key) + ':\n')
    if key == 'Release':
      years = analyzed_data['Release']
      sorted_years = sorted(years.items())
      sorted_years_dict = {k:v for k, v in sorted_years}
      for inner_key, inner_value in sorted_years_dict.items():
        print(' ' + str(inner_key) + ': ' + str(inner_value) + '\n')
    else:
      for inner_key, inner_value in value.items():
        print(' ' + str(inner_key) + ': ' + str(inner_value) + '\n')

def user_input():
  user_input = input('Please enter number of games to analyze: ')
  while True:
    try:
      user_input = int(user_input)
      break
    except ValueError:
      user_input = input('Input was not an integer, please try again: ')
  
  return user_input

def start_analysis(number_of_games):
  startTime = time.time()
  analyzed_data = {'Release' : {}, 'Platforms' : {}, 'Online' : {}, 'Games per Developer' : {}, 'Average Sales per Developer' : {}} #Dictionary where final results are stored#
  sales_per_developer = {}  #Dictionary for sales per developer that are needed in the average_sales() function#
  i = 0  #Iterator for the main data analysis block of code#

  while i < number_of_games:   #Main block of code, opens the game_info.json file, stores the dictionary in game_data, generates the random game data through game_generator.generate_game_data() and runs the data_analysis() function#
    game_generator.generate_game_data()
    with open('game_info.json') as game_json:
      game_data = json.load(game_json)

    print(game_data)
    data_analysis(game_data, analyzed_data, sales_per_developer)
    i += 1
  
  average_sales(analyzed_data, sales_per_developer)
  print_results(analyzed_data)
  print('Final script time in seconds: ' + str(time.time() - startTime))  #This is just so I know how inefficient my code is#

start_analysis(user_input())