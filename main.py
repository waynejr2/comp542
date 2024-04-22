# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:26:04 2024

@author: wayne
"""

from rule_based_deck import RuleBasedDeck
import pprint
from Player import Player

def main():
    game_deck = RuleBasedDeck(number_of_turns=100, change_rule_count=1)
    player = Player(learning_rate=0.05)  # Specify a custom learning rate
    pretty_printer = pprint.PrettyPrinter(indent=4)
    
    while True:
        turn_info = game_deck.get_turn()
        pretty_printer.pprint(turn_info)
        
        guess = player.make_guess(turn_info['cards'], turn_info['player_card'])

        correct = (guess == turn_info['key_card'])
        #print(correct)
        player.feedback(correct)
        game_deck.update_game_status(guess_correct=correct)
        
        if turn_info['status'] == 'final':
            break
        #game_deck.update_game_status(guess_correct=True)  # Simulate correct guesses for the example

if __name__ == "__main__":
    main()
