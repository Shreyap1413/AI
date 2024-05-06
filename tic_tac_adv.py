class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i + 3]))
            if i < 6:
                print("-----")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, move):
        self.board[move] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]
        if ' ' not in self.board:
            return 'tie'
        return None

    def minimax(self, depth, maximizing_player):
        winner = self.check_winner()
        if winner == 'X':
            return -10
        elif winner == 'O':
            return 10
        elif winner == 'tie':
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.make_move(move)
                eval = self.minimax(depth + 1, False)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.make_move(move)
                eval = self.minimax(depth + 1, True)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_eval = float('-inf')
        best_move = None
        for move in self.available_moves():
            self.make_move(move)
            eval = self.minimax(0, False)
            self.undo_move(move)
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

# Example usage
if __name__ == "__main__":
    game = TicTacToe()
    while True:
        game.print_board()
        winner = game.check_winner()
        if winner:
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        if game.current_player == 'X':
            move = int(input("Enter your move (0-8): "))
            game.make_move(move)
        else:
            print("Computer's turn...")
            move = game.find_best_move()
            game.make_move(move)