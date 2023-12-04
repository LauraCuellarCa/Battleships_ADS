import json


class RankingSystem:
    def __init__(self):
        self.players = {}

    def add_player(self, player_name):
        self.players[player_name] = {'plays': 0, 'wins': 0}

    def record_play(self, player_name, won=False):
        # Check if the player exists in the dictionary
        if player_name in self.players:
            self.players[player_name]['plays'] += 1
            if won:
                self.players[player_name]['wins'] += 1
        else:
            # If the player doesn't exist, add them with initial values
            self.add_player(player_name)
            # Now, update their plays and wins
            self.players[player_name]['plays'] += 1
            if won:
                self.players[player_name]['wins'] += 1
            else:
                print(f"Player {player_name} not found. Please add the player first.")

    def merge_sort(self, player_list):      # MERGE SORT
        if len(player_list) > 1:
            mid = len(player_list) // 2
            left_half = player_list[:mid]
            right_half = player_list[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][1]['wins'] > right_half[j][1]['wins']:
                    player_list[k] = left_half[i]
                    i += 1
                else:
                    player_list[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                player_list[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                player_list[k] = right_half[j]
                j += 1
                k += 1

    def get_ranking(self):
        player_list = list(self.players.items())
        self.merge_sort(player_list)
        return player_list
    
    def save_data(self):
        data = {"players": self.players}
        with open("player_data.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open("player_data.json", "r") as file:
                data = json.load(file)
            self.players = data.get("players", {})
        except FileNotFoundError:
            # Return empty data if the file is not found
            self.players = {}

    def load_existing_players(self):
        # Call this method at the beginning of the game
        self.load_data()
