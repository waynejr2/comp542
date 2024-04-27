# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:26:04 2024

@author: wayne
"""

import json
#import pprint
from rule_based_deck import RuleBasedDeck
from Player import Player

def run_game(game_id, number_of_turns, change_rule_count, learning_rate, discount_factor, log_data):
    game_deck = RuleBasedDeck(number_of_turns=number_of_turns, change_rule_count=change_rule_count)
    player = Player(learning_rate=learning_rate, discount_factor=discount_factor)
    #pretty_printer = pprint.PrettyPrinter(indent=2)

    # game info
    game_data = {
        'game_id': game_id,
        'initial_parameters': {
            'number_of_turns': number_of_turns,
            'change_rule_count': change_rule_count,
            'learning_rate': learning_rate,
            'discount_factor': discount_factor,
        },
        'turns': []  # information for each turn
    }

    while True:
        turn_info = game_deck.get_turn()
        #pretty_printer.pprint(turn_info)

        guess = player.make_guess(turn_info['cards'], turn_info['player_card'])
        correct = (guess == turn_info['key_card'])  # Check if guess is correct

        player.feedback(correct)
        game_deck.update_game_status(guess_correct=correct)

        # add turn info
        game_data['turns'].append({
            'deck_turn_info': turn_info,
            'player_turn_info': player.getTurnInfo(),
            'guess': guess,
            'correct': correct,
        })

        if turn_info['status'] == 'final':
            break

    log_data.append(game_data)

def main():
    # initial parameters
    number_of_turns = 10000
    change_rule_count = 10
    learning_rate = 0.1
    discount_factor = 0.95
    learning_rate_increment = 0.01
    number_of_games = 100  # Total number of games to be played

    # List to hold all game data
    all_games_data = []

    for i in range(1, number_of_games + 1):
        # pdate learning rate
        current_learning_rate = learning_rate + (i * learning_rate_increment)

        # Run a game
        run_game(i, number_of_turns, change_rule_count, current_learning_rate, discount_factor, all_games_data)

    # output all games
    with open('all_games_data.json', 'w') as log_file:
        json.dump(all_games_data, log_file, indent=2)  # Write the entire log data to a single file

if __name__ == "__main__":
    main()
