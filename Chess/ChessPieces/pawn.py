from .piece import Piece
from ..constans import ROWS, COLS
from ..constans import WHITE_PAWN_SURF, BLACK_PAWN_SURF

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.first_move = True

        if self.color == "white":
            self.direction = -1
        else: 
            self.direction = 1

    def move(self, row, col):
        self.row = row
        self.col = col
        self.first_move = False
        self.calc_pos()


    def set_image(self):
        if self.color == "white":
            return WHITE_PAWN_SURF
        else: 
            return BLACK_PAWN_SURF
            

    def get_valid_moves(self, board):
        valid_moves = []

        possible_moves = [
            (self.row + 1 * self.direction, self.col),
            (self.row + 1 * self.direction, self.col - 1),
            (self.row + 1 * self.direction, self.col + 1),
        ]

        if self.first_move:
            piece = board[self.row + 1 * self.direction][self.col]
            if piece == 0:
                possible_moves.append((self.row + 2 * self.direction, self.col))


        for move in possible_moves:
            row, col = move[0], move[1]

            if row < ROWS and row >= 0:
                if col < COLS and col >= 0:
                    
                    piece = board[row][col]
                    if piece != 0:
                        if piece.get_color() == self.color:
                            continue
                        else:
                            if col == self.col - 1 or col == self.col + 1:
                                valid_moves.append(move)
                            elif row == self.row + 1 * self.direction:
                                continue
                    else:
                        if col == self.col - 1 or col == self.col + 1:
                            continue
                    valid_moves.append(move)

        return valid_moves