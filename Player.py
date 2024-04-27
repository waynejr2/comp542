# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:51:09 2024

@author: wayne
"""

import random

class Player:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=0.2):
        # Initialize Q-table and other parameters
        self.q_table = {
            'value': 0.5,
            'color': 0.5,
            'shape': 0.5,
        }
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon  # exploration probability
        self.last_set_rule = None  #last used set-rule

    def get_key_card_from_action(self, set_rule, player_card, cards):
        matching_card = next(
            card for card in cards if card[set_rule] == player_card[set_rule]
        )
        self.last_set_rule = set_rule  #set-rule required for feedback
        return matching_card

    def choose_method_for_action(self, player_card, cards):
        # explore or exploit
        if random.random() < self.epsilon:
            set_rule = random.choice(['value', 'color', 'shape'])
            self.epsilon = max(self.epsilon * 0.95, 0.01)  ##lower limit for epsilon
            return self.get_key_card_from_action(set_rule, player_card, cards)
        else:
            # Exploitation: Choose the set-rule with the highest Q-value, with tie-breaker
            max_q_value = max(self.q_table.values())
            set_rules_with_max_q = [key for key, value in self.q_table.items() if value == max_q_value]
            set_rule = random.choice(set_rules_with_max_q)  # Resolve ties with random choice
            return self.get_key_card_from_action(set_rule, player_card, cards)

    def make_guess(self, cards, player_card):
        return self.choose_method_for_action(player_card, cards)

    def feedback(self, correct):
        # Define the reward and penalty rates
        reward = self.learning_rate
        penalty = self.learning_rate
        
        if correct:
            # Correct case: Increase Q-value for the set-rule used
            self.q_table[self.last_set_rule] += reward
            # Decrease Q-values for other set-rules
            for rule in self.q_table:
                if rule != self.last_set_rule:
                    self.q_table[rule] -= penalty
        else:
            # Incorrect case: Decrease Q-value for the used set-rule
            self.q_table[self.last_set_rule] -= penalty
            # Increase Q-values for the other set-rules
            for rule in self.q_table:
                if rule != self.last_set_rule:
                    self.q_table[rule] += reward
        
        # Apply upper limit to Q-values
        upper_limit = 1.0  # Define an upper limit for Q-values
        for rule in self.q_table:
            # Ensure Q-values are between 0 and the upper limit
            self.q_table[rule] = min(max(self.q_table[rule], 0), upper_limit)

    def getTurnInfo(self):
        # Return the current state information from the Player class
        return {
            'learning_rate': self.learning_rate,
            'discount_factor': self.discount_factor,
            'epsilon': self.epsilon,
            'last_set_rule': self.last_set_rule,
            'q_table': self.q_table,  # Return the Q-table state
        }
