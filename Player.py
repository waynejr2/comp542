# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:51:09 2024

@author: wayne
"""

# import random

# class Player:
#     def __init__(self, learning_rate=0.1, discount_factor=0.95):
#         # Initialize the Q-table
#         self.q_table = {}
#         self.learning_rate = learning_rate
#         self.discount_factor = discount_factor
#         self.epsilon_lower_limit = 0.01

#     def make_guess(self, cards, player_card):
#         # Implement the logic to make a guess based on the Q-table or randomly
#         return random.choice(cards)  # Placeholder for actual ML-based decision making

#     def feedback(self, result):
#         # Placeholder for Q-value update logic
#         # Actual implementation needed based on specific game design
#         pass

import random

class Player:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=0.2, epsilon_lower_limit=0.01):
        # Initialize the Q-table and set epsilon for exploration
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon  # Controls exploration probability
        self.epsilon_lower_limit = epsilon_lower_limit 
        self.last_set_rule = None  # Store the set-rule for future use
    
    def make_guess(self, cards, player_card):
        # Use choose_method_for_action to decide how to proceed
        key_card = self.choose_method_for_action(player_card, cards)
        return key_card
    
    def get_key_card_from_action(self, set_rule, player_card, cards):
        # Find the card from 'cards' that matches the set-rule value of 'player_card'
        matching_card = next(
            card for card in cards if card[set_rule] == player_card[set_rule]
        )
        # Store the chosen set-rule for later use
        self.last_set_rule = set_rule
        return matching_card
    
    def choose_method_for_action(self, player_card, cards):
        # Randomly decide whether to explore or exploit based on epsilon
        if random.random() < self.epsilon:
            # Exploration: Select a random set-rule and get the key_card
            set_rule = random.choice(['value', 'color', 'shape'])
            self.epsilon = max(self.epsilon * 0.95, self.epsilon_lower_limit)
            return self.get_key_card_from_action(set_rule, player_card, cards)
        else:
            # Exploitation: Placeholder for your specific exploitation logic
            # In this example, you can use a heuristic or Q-learning strategy
            # For now, we'll choose the first card as a placeholder
            return cards[0]  # This should be replaced with actual exploitation logic
    
    def feedback(self, correct):
        # Placeholder for Q-value update logic based on feedback
        # To be implemented as part of reinforcement learning logic
        pass
