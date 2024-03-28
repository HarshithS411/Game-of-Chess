import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# Game varaibles and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_location = [(0,0),(1, 0), (2, 0), (3, 0), (4, 0), (5,0), (6, 0), (7, 0),
                  (0,1),(1, 1), (2, 1), (3, 1), (4, 1), (5,1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_location = [(0,7),(1, 7), (2, 7), (3, 7), (4, 7), (5,7), (6, 7), (7, 7),
                  (0,6),(1, 6), (2, 6), (3, 6), (4, 6), (5,6), (6,6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0 
selection = 100
valid_moves = []
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen,(65,65))
black_queen_small = pygame.transform.scale(black_queen,(45,45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_queen,(65,65))
black_king_small = pygame.transform.scale(black_queen,(45,45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook,(65,65))
black_rook_small = pygame.transform.scale(black_rook,(45,45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop,(65,65))
black_bishop_small = pygame.transform.scale(black_bishop,(45,45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight,(65,65))
black_knight_small = pygame.transform.scale(black_knight,(45,45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn,(65,65))
black_pawn_small = pygame.transform.scale(black_pawn,(45,45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen,(65,65))
white_queen_small = pygame.transform.scale(white_queen,(45,45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king,(65,65))
white_king_small = pygame.transform.scale(white_king,(45,45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook,(65,65))
white_rook_small = pygame.transform.scale(white_rook,(45,45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop,(65,65))
white_bishop_small = pygame.transform.scale(white_bishop,(45,45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight,(65,65))
white_knight_small = pygame.transform.scale(white_knight,(45,45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn,(65,65))
white_pawn_small = pygame.transform.scale(white_pawn,(45,45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'rook', 'bishop', 'knight']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False

# draw main game board
def draw_board():
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 0:
                pygame.draw.rect(screen, 'light gray', [column * 100, row * 80, 100, 100])
            else:
                pygame.draw.rect(screen, 'black', [column * 100, row * 80, 100, 100])
    pygame.draw.rect(screen, 'gray', [0, HEIGHT - 100, WIDTH, 100])
    pygame.draw.rect(screen, 'gold', [0, HEIGHT - 100, WIDTH, 100], 5)
    pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    text_surface = big_font.render(status_text[turn_step], True, 'black')
    text_rect = text_surface.get_rect(topleft=(20, 675))
    screen.blit(text_surface, text_rect)
    
# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_location[i][0] * 100 + 22, white_location[i][1] * 80 + 5))
        elif white_pieces[i] == 'rook':
            screen.blit(white_rook, (white_location[i][0] * 100, white_location[i][1] * 80))
        elif white_pieces[i] == 'knight':
            screen.blit(white_knight, (white_location[i][0]*100 , white_location [i ][1]*80)) 
        elif white_pieces[i] == 'bishop':
             screen.blit(white_bishop, (white_location[i][0]*100 , white_location[i][1]*80)) 
        elif   white_pieces[i]== 'queen':
            screen.blit(white_queen, (white_location[i][0] * 100, white_location[i][1] * 80))
        elif   white_pieces[i] == 'king':
             screen.blit(white_king, (white_location[i][0]*100 , white_location[i][1]*80))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [black_location[i][0] * 100 + 1, black_location[i][1] * 100 + 1, 50, 50], 2)



    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_location[i][0] * 100 + 22, black_location[i][1] * 80 + 5))
        elif black_pieces[i] == 'rook':
            screen.blit(black_rook, (black_location[i][0]*100 , black_location[i][1]*80 + 5)) 
        elif black_pieces[i] == 'knight':
             screen.blit(black_knight, (black_location[i][0]*100 , black_location[i][1]*80 + 5 )) 
        elif   black_pieces[i] == 'bishop':
             screen.blit(black_bishop, (black_location[i][0]*100 , black_location[i][1]*80 + 5 )) 
        elif   black_pieces[i] == 'queen':
             screen.blit(black_queen ,(black_location[i][0]*100 , black_location[i][1]*80 + 5 )) 
        elif   black_pieces[i] == 'king':
             screen.blit(black_king, (black_location[i][0]*100 , black_location[i][1]*80 + 5 ))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_location[i][0] * 100 + 1, white_location[i][1] * 100 + 1, 100, 100], 2)

# function to check all pieces valid options on board
def check_options():
    pass


# Main game loop
black_options = check_options(black_pieces, black_location, 'black')
white_options = check_options(white_pieces, white_location, 'white')
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coord in white_location:
                    selection = white_location.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    white_location[selection] = click_coord
                    if click_coord in black_location:
                        black_pieces = black_location.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_pieces])
                        black_pieces.pop(black_pieces)
                        black_location.pop(black_pieces)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coord in black_location:
                    selection = black_location.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in valid_moves and selection != 100:
                    black_location[selection] = click_coord
                    if click_coord in white_location:
                        white_pieces = white_location.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_pieces])
                        white_pieces.pop(white_pieces)
                        white_location.pop(white_pieces)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            
    pygame.display.flip()
pygame.quit()