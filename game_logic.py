# Added comment for branch merge requirement

class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            return True
        return False

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a,b,c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return self.board[a]

        if "" not in self.board:
            return "Draw"

        return None