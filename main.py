# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:26:04 2024

@author: wayne
"""

# from rule_based_deck import RuleBasedDeck
# import pprint
# from Player import Player

# def main():
#     game_deck = RuleBasedDeck(number_of_turns=100, change_rule_count=1)
#     player = Player(learning_rate=0.05)  # Specify a custom learning rate
#     pretty_printer = pprint.PrettyPrinter(indent=4)
    
#     while True:
#         turn_info = game_deck.get_turn()
#         pretty_printer.pprint(turn_info)
        
#         guess = player.make_guess(turn_info['cards'], turn_info['player_card'])

#         correct = (guess == turn_info['key_card'])
#         #print(correct)
#         player.feedback(correct)
#         game_deck.update_game_status(guess_correct=correct)
        
#         if turn_info['status'] == 'final':
#             break
#         #game_deck.update_game_status(guess_correct=True)  # Simulate correct guesses for the example

# if __name__ == "__main__":
#     main()
    
# from rule_based_deck import RuleBasedDeck
# import pprint
# from Player import Player
# import json
# import os

# def run_game(number_of_turns, change_rule_count, learning_rate, discount_factor, log_file):
#     game_deck = RuleBasedDeck(number_of_turns=number_of_turns, change_rule_count=change_rule_count)
#     player = Player(learning_rate=learning_rate, discount_factor=discount_factor)
#     pretty_printer = pprint.PrettyPrinter(indent=4)

#     correct_guesses = 0
#     total_turns = 0

#     with open(log_file, 'w') as log:
#         while True:
#             turn_info = game_deck.get_turn()
#             pretty_printer.pprint(turn_info)

#             # Player makes a guess based on current cards and player_card
#             guess = player.make_guess(turn_info['cards'], turn_info['player_card'])

#             # Check if the guess is correct by comparing it to the key_card
#             correct = (guess == turn_info['key_card'])  # Comparing guess with key_card

#             # Update statistics
#             correct_guesses += correct
#             total_turns += 1
            
#             # Provide feedback to the player
#             player.feedback(correct)
            
#             # Update game status based on whether the guess was correct
#             game_deck.update_game_status(guess_correct=correct)

#             if turn_info['status'] == 'final':
#                 break
        
#         # Write data to log file at the end of the game
#         log_data = {
#             'learning_rate': learning_rate,
#             'correct_guesses': correct_guesses,
#             'total_turns': total_turns,
#             'accuracy': correct_guesses / total_turns if total_turns > 0 else 0
#         }
#         json.dump(log_data, log, indent=2)  # Store data in JSON format

# def main():
#     # Constants and initial parameters
#     number_of_turns = 250
#     change_rule_count = 5
#     learning_rate = 0.1
#     discount_factor = 0.95
#     learning_rate_increment = 0.01
#     number_of_games = 10  # Number of games to be played

#     for i in range(number_of_games):
#         # Adjust learning rate for each game
#         current_learning_rate = learning_rate + (i * learning_rate_increment)

#         # Define the log file name for this game
#         log_file = f'game_{i + 1}.json'  # Unique file for each game

#         # Run the game with the current settings
#         run_game(number_of_turns, change_rule_count, current_learning_rate, discount_factor, log_file)

# if __name__ == "__main__":
#     main()

import json
import pprint
from rule_based_deck import RuleBasedDeck
from Player import Player

def run_game(game_id, number_of_turns, change_rule_count, learning_rate, discount_factor, log_data):
    game_deck = RuleBasedDeck(number_of_turns=number_of_turns, change_rule_count=change_rule_count)
    player = Player(learning_rate=learning_rate, discount_factor=discount_factor)
    pretty_printer = pprint.PrettyPrinter(indent=4)

    # Store information for each game in the overall log data
    game_data = {
        'game_id': game_id,
        'initial_parameters': {
            'number_of_turns': number_of_turns,
            'change_rule_count': change_rule_count,
            'learning_rate': learning_rate,
            'discount_factor': discount_factor,
        },
        'turns': []  # Empty list to store information for each turn
    }

    while True:
        turn_info = game_deck.get_turn()
        pretty_printer.pprint(turn_info)

        # Player makes a guess and checks its correctness
        guess = player.make_guess(turn_info['cards'], turn_info['player_card'])
        correct = (guess == turn_info['key_card'])  # Check if guess is correct

        # Provide feedback to the player and update game status
        player.feedback(correct)
        game_deck.update_game_status(guess_correct=correct)

        # Add the current turn's information to the game's data
        game_data['turns'].append({
            'deck_turn_info': turn_info,
            'player_turn_info': player.getTurnInfo(),
            'guess': guess,
            'correct': correct,
        })

        if turn_info['status'] == 'final':
            break

    # Append the game data to the overall log_data
    log_data.append(game_data)

def main():
    # Constants and initial parameters
    number_of_turns = 250
    change_rule_count = 5
    learning_rate = 0.1
    discount_factor = 0.95
    learning_rate_increment = 0.01
    number_of_games = 10  # Total number of games to be played

    # List to hold all game data
    all_games_data = []

    for i in range(number_of_games):
        # Adjust learning rate for each game
        current_learning_rate = learning_rate + (i * learning_rate_increment)

        # Run the game with the current settings
        run_game(i, number_of_turns, change_rule_count, current_learning_rate, discount_factor, all_games_data)

    # Write all games' data to a single JSON file at the end
    with open('all_games_data.json', 'w') as log_file:
        json.dump(all_games_data, log_file, indent=4)  # Write the entire log data to a single file

if __name__ == "__main__":
    main()
