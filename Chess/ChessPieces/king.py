from .piece import Piece
from ..constans import ROWS, COLS
from ..constans import WHITE_KING_SURF, BLACK_KING_SURF

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def set_image(self):
        if self.color == "white":
            return WHITE_KING_SURF
        else: 
            return BLACK_KING_SURF

    def get_valid_moves(self, board):
        valid_moves = []

        possible_moves = [
            (self.row - 1, self.col),
            (self.row - 1, self.col - 1),
            (self.row - 1, self.col + 1),
            (self.row + 1, self.col),
            (self.row + 1, self.col - 1),
            (self.row + 1, self.col + 1),
            (self.row, self.col - 1),
            (self.row, self.col + 1),
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

        possible_moves = valid_moves.copy()
        valid_moves.clear()
        
        # get position of second king
        row_king, col_king = 0, 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece != 0: 
                    if type(piece) == King:
                        if piece.get_color() != self.color:
                            row_king, col_king = row, col

        for move in possible_moves:
            row, col = move[0], move[1]
            if abs(row - row_king) > 1 or abs(col - col_king) > 1:
                valid_moves.append(move)

        return valid_moves

