from .piece import Piece
from ..constans import ROWS, COLS
from ..constans import WHITE_KNIGHT_SURF, BLACK_KNIGHT_SURF

class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def set_image(self):
        if self.color == "white":
            return WHITE_KNIGHT_SURF
        else: 
            return BLACK_KNIGHT_SURF

    def get_valid_moves(self, board):
        valid_moves = []

        possible_moves = [
            (self.row - 2, self.col - 1),
            (self.row - 2, self.col + 1),
            (self.row + 2, self.col - 1),
            (self.row + 2, self.col + 1),
            (self.row - 1, self.col - 2),
            (self.row + 1, self.col - 2),
            (self.row - 1, self.col + 2),
            (self.row + 1, self.col + 2),
        ]
        
        for move in possible_moves:
            row, col = move[0], move[1]

            if row < ROWS and row >= 0:
                if col < COLS and col >= 0:
                    piece = board[row][col]
                    if piece != 0:
                        if piece.get_color() == self.color:
                            continue
                    valid_moves.append(move)

        return valid_moves
