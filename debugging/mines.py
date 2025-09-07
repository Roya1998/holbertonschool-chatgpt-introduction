#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines > width * height:
            raise ValueError("Too many mines for the board size")
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.cells_to_reveal = width * height - mines

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_cell(self, x, y):
        if self.revealed[y][x]:
            return True  # Already revealed
        if (y * self.width + x) in self.mines:
            return False  # Hit a mine
        self.revealed[y][x] = True
        self.cells_to_reveal -= 1
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal_cell(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            if self.cells_to_reveal == 0:
                print("Congratulations! You revealed all safe cells!")
                self.print_board(reveal=True)
                break
            user_input = input("Enter x and y coordinates separated by space (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Game exited.")
                break
            try:
                x_str, y_str = user_input.split()
                x = int(x_str)
                y = int(y_str)
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds! Try again.")
                    input("Press Enter to continue...")
                    continue
                if not self.reveal_cell(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Enter two numbers separated by space or 'q' to quit.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
