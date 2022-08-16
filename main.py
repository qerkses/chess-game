import pygame
from Chess.board import Board
from Chess.constans import SIZE, BOARD_LEFT, BOARD_TOP
from Chess.constans import ROWS, COLS, GAME_TITLE, DARK_GREY, SQUARE_SIZE
from sys import exit

# initialization
pygame.init()
WINDOW = pygame.display.set_mode(SIZE)
pygame.display.set_caption(GAME_TITLE)
FPS = 60


def get_row_col(mouse_pos) -> tuple:
    x, y = mouse_pos
    row = (y - BOARD_TOP)//SQUARE_SIZE
    col = (x - BOARD_LEFT)//SQUARE_SIZE
    return row, col


def main():
    clock = pygame.time.Clock()
    game_board = Board(BOARD_LEFT, BOARD_TOP)

    turn = "white"
    valid_moves = []


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()

                if mouse_presses[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col(pos)

                    if row in range(ROWS) and col in range(COLS):
                        if not game_board.is_selected():
                            piece = game_board.get_piece(row, col)

                            if piece != 0 and piece.get_color() == turn:
                                valid_moves = piece.get_valid_moves(game_board.board)
                                game_board.set_valid_moves(valid_moves)
                                game_board.select_piece(piece)
                        else:
                            if (row, col) in valid_moves:
                                piece = game_board.selected_piece
                                game_board.move_piece(piece, row, col)
                                piece.move(row, col)
                                game_board.unselect_piece()
                                if turn == "white": 
                                    turn = "black"
                                else:
                                    turn = "white"

                elif mouse_presses[2]:
                    game_board.unselect_piece()


        WINDOW.fill(DARK_GREY)
        game_board.draw(WINDOW)
        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()

if __name__ == '__main__':
    main()
    