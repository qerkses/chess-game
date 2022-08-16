from .piece import Piece
from ..constans import ROWS, COLS
from ..constans import WHITE_BISHOP_SURF, BLACK_BISHOP_SURF

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def set_image(self):
        if self.color == "white":
            return WHITE_BISHOP_SURF
        else: 
            return BLACK_BISHOP_SURF

    def get_valid_moves(self, board):
        valid_moves = []

        i = 1
        while self.row + i < ROWS and self.col + i < COLS:
            piece = board[self.row + i][self.col + i]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((self.row + i, self.col + i))
                break
            valid_moves.append((self.row + i, self.col + i))
            i += 1


        i = 1
        while self.row + i < ROWS and self.col - i > -1:
            piece = board[self.row + i][self.col - i]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((self.row + i, self.col - i))
                break
            valid_moves.append((self.row + i, self.col - i))
            i += 1


        i = 1
        while self.row - i > - 1 and self.col + i < COLS:
            piece = board[self.row - i][self.col + i]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((self.row - i, self.col + i))
                break
            valid_moves.append((self.row - i, self.col + i))
            i += 1


        i = 1
        while self.row - i > - 1 and self.col - i > -1:
            piece = board[self.row - i][self.col - i]
            if piece != 0:
                if piece.get_color() == self.color:
                    break
                valid_moves.append((self.row - i, self.col - i))
                break
            valid_moves.append((self.row - i, self.col - i))
            i += 1



        return valid_moves
