import pygame
from .ChessPieces import pawn, king, queen, bishop, knight, rook
from .constans import BOARD_LEFT, BOARD_TOP, ROWS, COLS, SQUARE_SIZE
from .constans import YELLOW, BLUE, LIGHT_GREEN, LIGHT_RED

class Board:
    def __init__(self, left=0, top=0):
        self.left = left
        self.top = top

        self.selected_piece = None
        self.board = []

        self._valid_moves = []

        self.create_board()
        
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 1:
                    self.board[row].append(pawn.Pawn('black', row, col))
                elif row == 6:
                    self.board[row].append(pawn.Pawn('white', row, col))
                else:
                    self.board[row].append(0)

        self.board[7][0] = rook.Rook("white", 7, 0)
        self.board[7][1] = knight.Knight("white", 7, 1)
        self.board[7][2] = bishop.Bishop("white", 7, 2)
        self.board[7][3] = queen.Queen("white", 7, 3)
        self.board[7][4] = king.King("white", 7, 4)
        self.board[7][5] = bishop.Bishop("white", 7, 5)
        self.board[7][6] = knight.Knight("white", 7, 6)
        self.board[7][7] = rook.Rook("white", 7, 7)

        self.board[0][0] = rook.Rook("black", 0, 0)
        self.board[0][1] = knight.Knight("black", 0, 1)
        self.board[0][2] = bishop.Bishop("black", 0, 2)
        self.board[0][3] = queen.Queen("black", 0, 3)
        self.board[0][4] = king.King("black", 0, 4)
        self.board[0][5] = bishop.Bishop("black", 0, 5)
        self.board[0][6] = knight.Knight("black", 0, 6)
        self.board[0][7] = rook.Rook("black", 0, 7)


    def get_piece(self, row, col):
        return self.board[row][col]

    def select_piece(self, piece):
        self.selected_piece = piece

    def unselect_piece(self):
        self.selected_piece = None

    def is_selected(self) -> bool:
        if self.selected_piece != None:
            return True
        return False

    def set_valid_moves(self, valid_moves):
        self._valid_moves = valid_moves

    def move_piece(self, piece, row, col):
        self.board[row][col] = piece
        self.board[piece.row][piece.col] = 0
        piece.move(row, col)

    def draw_selected_square(self, window):
        row = self.selected_piece.row
        col = self.selected_piece.col

        left = col * SQUARE_SIZE + BOARD_LEFT
        top = row * SQUARE_SIZE + BOARD_TOP

        pygame.draw.rect(window, LIGHT_GREEN, (left, top, SQUARE_SIZE, SQUARE_SIZE))

    def draw_valid_moves(self, window):
        if len(self._valid_moves) != 0:
            for coordinates in self._valid_moves:
                row, col = coordinates

                left = col * SQUARE_SIZE + BOARD_LEFT
                top = row * SQUARE_SIZE + BOARD_TOP

                valid_square_surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
                valid_square_surf.fill(LIGHT_RED)
                valid_square_surf.set_alpha(128)
                window.blit(valid_square_surf, (left, top))

    def draw_squares(self, window):
        pygame.draw.rect(window, YELLOW, (self.left, self.top, SQUARE_SIZE*ROWS, SQUARE_SIZE*COLS))

        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == (row + 1) % 2:
                    square_left = self.left + row * SQUARE_SIZE
                    square_top = self.top + col * SQUARE_SIZE
                    pygame.draw.rect(window, BLUE, (square_left, square_top, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, window):
        self.draw_squares(window)
        
        if self.is_selected():
            self.draw_selected_square(window)
            self.draw_valid_moves(window)

        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]

                if piece != 0:
                    piece.draw(window)