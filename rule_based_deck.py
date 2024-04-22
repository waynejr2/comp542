import random

class RuleBasedDeck:
    def __init__(self, number_of_turns, change_rule_count):
        self.number_of_turns = number_of_turns
        self.change_rule_count = change_rule_count
        self.correct_guesses = 0
        self.number_of_rule_switches = 0
        self.set_rule = random.choice(['value', 'color', 'shape'])
        self.status = 'ongoing'
        self.rules = ['value', 'color', 'shape']
        self.values = [1, 2, 3, 4]
        self.colors = ['red', 'green', 'blue', 'yellow']
        self.shapes = ['square', 'circle', 'triangle', 'cross']

    def create_cards(self):
        cards = []
        values = self.values[:]
        colors = self.colors[:]
        shapes = self.shapes[:]
        random.shuffle(values)
        random.shuffle(colors)
        random.shuffle(shapes)
        for i in range(4):
            card = {
                'value': values[i],
                'color': colors[i],
                'shape': shapes[i]
            }
            cards.append(card)
        return cards

    def create_player_card(self, match_value=None, match_color=None, match_shape=None):
        # Determine the values for each attribute, either by matching the key card or randomly.
        value = match_value if match_value is not None else random.choice(self.values)
        color = match_color if match_color is not None else random.choice(self.colors)
        shape = match_shape if match_shape is not None else random.choice(self.shapes)

        # Create the player card ensuring it's not the same as the key card
        player_card = {'value': value, 'color': color, 'shape': shape}
        while player_card == self.key_card:
            player_card = {
                'value': random.choice(self.values),
                'color': random.choice(self.colors),
                'shape': random.choice(self.shapes)
            }
        return player_card
    
    import random

    def change_set_rule(self):
        self.number_of_rule_switches += 1
        # Make a list of possible rules excluding the current set_rule
        possible_rules = [rule for rule in self.rules if rule != self.set_rule]
        # Randomly select a new rule from the reduced list of possible rules
        self.set_rule = random.choice(possible_rules)


    def get_turn(self):
        self.cards = self.create_cards()  # Recreate cards every turn
        self.key_card = random.choice(self.cards)  # Pick a new key card every turn

        if self.correct_guesses >= self.change_rule_count:
            #self.set_rule = random.choice(self.rules)
            self.change_set_rule()
            self.correct_guesses = 0  # Reset the count after rule change

        # Define the player card based on the current set_rule
        if self.set_rule == 'value':
            self.player_card = self.create_player_card(match_value=self.key_card['value'])
        elif self.set_rule == 'color':
            self.player_card = self.create_player_card(match_color=self.key_card['color'])
        else:
            self.player_card = self.create_player_card(match_shape=self.key_card['shape'])

        return {
            'cards': self.cards,
            'key_card': self.key_card,
            'player_card': self.player_card,
            'set_rule': self.set_rule,
            'correct_guesses': self.correct_guesses,
            'number_of_turns': self.number_of_turns,
            'number_of_rule_switches': self.number_of_rule_switches,
            'status': self.status if self.number_of_turns > 0 else 'final'
        }

    def update_game_status(self, guess_correct):
        if guess_correct:
            self.correct_guesses += 1
        self.number_of_turns -= 1
        if self.number_of_turns <= 1:
            self.status = 'final'
