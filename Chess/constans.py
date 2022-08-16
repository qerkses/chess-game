import pygame
from pathlib import Path

SIZE = WIDTH, HEIGHT = 850, 850
GAME_TITLE = "Chess Game"

ROWS, COLS = 8, 8
SQUARE_SIZE = 100
BOARD_LEFT = 25
BOARD_TOP = 25

PIECE_SIZE = (96, 96)

# rgb, colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 230)
BLUE = (128, 212, 255)
GREY = (191, 191, 191)
DARK_GREY = (43, 44, 46)
LIGHT_GREEN = (179, 255, 179)
LIGHT_RED = (255, 153, 153)


# images
WHITE_PAWN_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_pl.png'), PIECE_SIZE)
WHITE_QUEEN_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_ql.png'), PIECE_SIZE)
WHITE_ROOK_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_rl.png'), PIECE_SIZE)
WHITE_KNIGHT_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_nl.png'), PIECE_SIZE)
WHITE_BISHOP_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_bl.png'), PIECE_SIZE)
WHITE_KING_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_kl.png'), PIECE_SIZE)

BLACK_PAWN_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_pd.png'), PIECE_SIZE)
BLACK_QUEEN_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_qd.png'), PIECE_SIZE)
BLACK_ROOK_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_rd.png'), PIECE_SIZE)
BLACK_KNIGHT_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_nd.png'), PIECE_SIZE)
BLACK_BISHOP_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_bd.png'), PIECE_SIZE)
BLACK_KING_SURF = pygame.transform.scale(pygame.image.load(Path('Assets') / 'Chess_tile_kd.png'), PIECE_SIZE)
