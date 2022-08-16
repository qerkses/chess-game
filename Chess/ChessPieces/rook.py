from .piece import Piece
from ..constans import ROWS, COLS
from ..constans import WHITE_ROOK_SURF, BLACK_ROOK_SURF

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def set_image(self):
        if self.color == "white":
            return WHITE_ROOK_SURF
        else: 
            return BLACK_ROOK_SURF

    def get_valid_moves(self, board):
        valid_moves = []

        for row in range(self.row + 1, ROWS):
            piece = board[row][self.col]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((row, self.col))
                break
            valid_moves.append((row, self.col))


        for row in range(self.row - 1, -1, -1):
            piece = board[row][self.col]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((row, self.col))
                break
            valid_moves.append((row, self.col))


        for col in range(self.col + 1, COLS):
            piece = board[self.row][col]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((self.row, col))
                break
            valid_moves.append((self.row, col))


        for col in range(self.col - 1, -1, -1):
            piece = board[self.row][col]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((self.row, col))
                break
            valid_moves.append((self.row, col))

        return valid_moves