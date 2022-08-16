from abc import ABC, abstractmethod
from ..constans import BOARD_LEFT, BOARD_TOP, SQUARE_SIZE


class Piece(ABC):
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

        self.image = self.set_image()

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = BOARD_LEFT + self.col * SQUARE_SIZE + SQUARE_SIZE//2
        self.y = BOARD_TOP + self.row * SQUARE_SIZE + SQUARE_SIZE//2


    def get_color(self) -> str:
        return self.color

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, window):
        left = self.x - self.image.get_width()//2
        top = self.y - self.image.get_height()//2
        window.blit(self.image, (left, top))

    @abstractmethod
    def set_image(self):
        pass

    @abstractmethod
    def get_valid_moves(self, board):
        pass