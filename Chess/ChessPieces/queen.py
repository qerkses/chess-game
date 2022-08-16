from .piece import Piece
from .rook import Rook
from .bishop import Bishop
from ..constans import WHITE_QUEEN_SURF, BLACK_QUEEN_SURF

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def set_image(self):
        if self.color == "white":
            return WHITE_QUEEN_SURF
        else: 
            return BLACK_QUEEN_SURF

    def get_valid_moves(self, board):
        valid_moves = []

        rook_piece = Rook(self.color, self.row, self.col)
        bishop_piece = Bishop(self.color, self.row, self.col)

        valid_moves.extend(rook_piece.get_valid_moves(board))
        valid_moves.extend(bishop_piece.get_valid_moves(board))

        return valid_moves
