import tkinter as tk
from functools import partial
from queue import Queue
import random

class Puzzle:
    def __init__(self, board, empty_pos, moves=0, prev=None):
        self.board = board
        self.empty_pos = empty_pos
        self.moves = moves
        self.prev = prev

    def __lt__(self, other):
        return self.moves < other.moves

    def is_goal(self):
        goal = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        return self.board == goal

    def possible_moves(self):
        x, y = self.empty_pos
        moves = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                moves.append(Puzzle(new_board, (nx, ny), self.moves + 1, self))
        return moves

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board]).replace('0', ' ')

def bfs(initial_state):
    visited = set()
    queue = Queue()
    queue.put(initial_state)

    while not queue.empty():
        current = queue.get()
        if current.is_goal():
            return current

        visited.add(str(current.board))
        for neighbor in current.possible_moves():
            if str(neighbor.board) not in visited:
                queue.put(neighbor)
    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.prev
    return path[::-1]

def generate_random_board(goal_board, empty_pos, num_moves=50):
    current_board = [row[:] for row in goal_board]
    x, y = empty_pos

    for _ in range(num_moves):
        possible_moves = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                possible_moves.append((nx, ny))
        
        nx, ny = random.choice(possible_moves)
        current_board[x][y], current_board[nx][ny] = current_board[nx][ny], current_board[x][y]
        x, y = nx, ny

    return current_board, (x, y)

class PuzzleGame:
    def __init__(self, root, initial_state):
        self.root = root
        self.state = initial_state
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.root,
                    text=str(self.state.board[i][j]) if self.state.board[i][j] != 0 else "",
                    font=("Helvetica", 20),
                    width=15,
                    height=5,
                    bg="lightgray", 
                    command=partial(self.move_tile, i, j)
                )
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

        solve_button = tk.Button(self.root, text="Resolver (BFS)", command=self.solve_bfs)
        solve_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
        self.update_ui()

    def update_ui(self):
        for i in range(3):
            for j in range(3):
                value = self.state.board[i][j]
                if value == 0:
                    self.buttons[i][j].config(text="", bg="pink")  
                else:
                    self.buttons[i][j].config(text=str(value), bg="lightgrey")  

    def move_tile(self, i, j):
        x, y = self.state.empty_pos
        if abs(x - i) + abs(y - j) == 1:
            self.state.board[x][y], self.state.board[i][j] = self.state.board[i][j], self.state.board[x][y]
            self.state.empty_pos = (i, j)
            self.state.moves += 1
            self.update_ui()
            if self.state.is_goal():
                self.show_win_message()

    def show_win_message(self):
        win_label = tk.Label(self.root, text="Parabéns! Você venceu!", font=("Helvetica", 18), fg="green")
        win_label.grid(row=4, column=0, columnspan=3)

    def solve_bfs(self):
        solution = bfs(self.state)
        if solution:
            path = reconstruct_path(solution)
            for state in path:
                self.state = state
                self.update_ui()
                self.root.update()
                self.root.after(500)

if __name__ == "__main__":
    goal_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    empty_pos = (2, 2)

    random_board, random_empty_pos = generate_random_board(goal_board, empty_pos)
    initial_state = Puzzle(random_board, random_empty_pos)

    root = tk.Tk()
    root.title("Jogo dos Oito")
    game = PuzzleGame(root, initial_state)
    root.mainloop()
