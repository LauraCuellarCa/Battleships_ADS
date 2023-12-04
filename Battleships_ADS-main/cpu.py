from collections import deque
import random


class CPU_Player:
    def __init__(self, board_size=10):
        self.board_size = board_size
        self.cpu_board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.last_hit = None
        self.target_mode = False
        self.hit_directions = deque()   # Stack to check ship direction
        self.original_hit = None

    def update_board(self, row, col, result):
        self.cpu_board[row][col] = 1 if result == "Hit" else -1
        if result == "Hit":
            if not self.target_mode:
                self.target_mode = True
                self.last_hit = (row, col)
                self.original_hit = (row, col)
                self.determine_hit_directions(row, col)
            else:
                self.last_hit = (row, col)
        elif result == "Miss" and self.target_mode:
            self.switch_hit_direction()

    def determine_hit_directions(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                if self.cpu_board[new_row][new_col] == 0:
                    self.hit_directions.append((dr, dc))

    def switch_hit_direction(self):
        if self.hit_directions:
            self.hit_directions.popleft()
        if not self.hit_directions:
            self.reset_target_mode()
        # Reset last_hit to original hit to check other directions from the first hit
        self.last_hit = self.original_hit

    def choose_shot(self):
        if self.target_mode and self.hit_directions:
            dr, dc = self.hit_directions[0]
            next_row, next_col = self.last_hit[0] + dr, self.last_hit[1] + dc
            if self.board_size > next_row >= 0 == self.cpu_board[next_row][next_col] and 0 <= next_col < self.board_size:
                return next_row, next_col
            else:
                self.switch_hit_direction()
                return self.choose_shot()
        else:
            return self.random_shot()

    def random_shot(self):
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if self.cpu_board[row][col] == 0:
                return row, col

    def reset_target_mode(self):
        self.last_hit = None
        self.target_mode = False
        self.hit_directions.clear()
        self.original_hit = None
