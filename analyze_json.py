# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:35:42 2024

@author: wayne
"""
# import json

# def analyze_json(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)  # Load the JSON data
    
#     number_of_games = len(data)  # Total number of games
#     total_turns = sum(len(game['turns']) for game in data)  # Total turns across all games
#     average_turns_per_game = total_turns / number_of_games if number_of_games > 0 else 0
    
#     # Display key statistics
#     print("Total number of games:", number_of_games)
#     print("Total number of turns:", total_turns)
#     print("Average number of turns per game:", average_turns_per_game)

#     # Loop through each game to provide detailed information in a single line
#     for i, game in enumerate(data, start=1):  # Start enumeration from 1
#         game_id = game.get('game_id', i)  # Use game ID or loop index
#         turns_in_game = len(game['turns'])  # Total turns in this game
        
#         # Get the last turn in the game
#         last_turn = game['turns'][-1]  # Retrieve the last turn
        
#         # Number of set-rule changes from the last turn
#         set_rule_changes = last_turn.get('deck_turn_info', {}).get('number_of_rule_switches', 0)
        
#         # Learning rate for the game
#         learning_rate = game.get('initial_parameters', {}).get('learning_rate', 0.1)
        
#         # Calculate the average turns per set-rule change
#         avg_turns_per_change = (turns_in_game / set_rule_changes) if set_rule_changes > 0 else "N/A"
        
#         # Display all information in a single line for easier readability
#         print(f"Game {game_id}: Number of set-rule changes: {set_rule_changes}, Total turns: {turns_in_game}, "
#               f"Learning rate: {learning_rate}, Average turns per set-rule change: {avg_turns_per_change}")

# # Example usage
# if __name__ == "__main__":
#     analyze_json('all_games_data.json')  # Adjust the file path if needed

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
            avg_turns_per_change = None  # If no set-rule changes, avoid division by zero
        
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
