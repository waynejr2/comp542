# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:35:42 2024

@author: wayne
"""

import json

# Function to create the learning rate vs. average turns per rule change JSON file
def create_lr_vs_arprc_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)  # Load the large JSON data

    # Prepare a list to hold the desired information
    new_data = []
    
    # Loop through each game to extract the required data
    for i, game in enumerate(data, start=1):
        game_id = game.get('game_id', i)  # Game ID or loop index
        turns_in_game = len(game['turns'])  # Total turns in this game
        
        # Get the last turn to find the set-rule changes
        last_turn = game['turns'][-1]  # Retrieve the last turn
        set_rule_changes = last_turn.get('deck_turn_info', {}).get('number_of_rule_switches', 0)
        
        # Retrieve the learning rate for this game
        learning_rate = game.get('initial_parameters', {}).get('learning_rate', 0.1)
        
        # Calculate the average turns per set-rule change
        if set_rule_changes > 0:
            avg_turns_per_change = turns_in_game / set_rule_changes
        else:
            avg_turns_per_change = None  #n0 set-rule changes
        
        # Store the desired data in the new list
        new_data.append({
            'game_id': game_id,
            'learning_rate': learning_rate,
            'avg_turns_per_change': avg_turns_per_change,
        })
    
    # Write the new data to the specified output JSON file
    with open(output_file, 'w') as outfile:
        json.dump(new_data, outfile, indent=4)

# Example usage to create 'lr_vs_arprc.json'
if __name__ == "__main__":
    create_lr_vs_arprc_json('all_games_data.json', 'lr_vs_arprc.json')  # Create the output JSON
