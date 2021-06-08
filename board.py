# Python imports
import pygame
import math

# Import from the utils class
from Utils.constants import WHITE, BLACK, GREY, PLAYER1, PLAYER2

# Variables for the game itself -- DON'T TOUCH!
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH)) # Width only --> 2D
pygame.display.set_caption("Board") # Text above the board

# Main class for the variables, and init!
class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Get position of col and row
    def get_pos(self):
        return self.row, self.col

    # Reset board, sets everything to white
    def reset(self):
        self.color = WHITE

    # Create a start point, which is black
    def make_start(self):
        self.color = BLACK

    # Create the player1, which is the player1 colour
    def create_player1(self):
        self.color = PLAYER1

    # Create the player2, which is the player2 colour
    def create_player2(self):
        self.color = PLAYER2

    # Draw the board itself by calling this function
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    
# Combines each cord of the board to get the exact position!
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Create the grid by using a 2d array
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    return grid

# "Draw" the created grid, by extrating the data from the 2d array
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows): # Horizontal
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows): # Vertical
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

# Draw the board, including the grid
def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width) # Draw the grid on the board!
    pygame.display.update() # Update the frame/board -- IMPORTANT

# Check for win
def check_win():
    pass

# Get the mouse click position
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    # Calculating the difference between the y & x, with the gap size!
    row = y // gap 
    col = x // gap
    return row, col

# Main function
def main(win, width):
    ROWS = 15 # Amount of squares (15x15)
    grid = make_grid(ROWS, width)

    # Temp variables
    player1 = None
    player2 = None

    # Constant variables
    start = None
    end = None
    run = True

    # Keep track of whose turn it is
    turn = 0

    # Make the game run with the while loop; if it breaks, the game will stop instantly!
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # LEFT MOUSE BUTTON CLICK EVENT
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos() # Calling the function to get the exact position
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                # Player 1 turn check
                if turn == 0:
                    player1 = spot # Setting up a temp variable to keep track of where it's being placed!
                    turn = 1 # --1
                    player1.create_player1() # Calling the function to create a player with a specific colour

                # Player 2 turn check
                elif turn == 1:
                    player2 = spot # Setting up a temp variable to keep track of where it's being placed!
                    turn = 0 # ++1
                    player2.create_player2() # Calling the function to create a player with a specific colour

            # Clear event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit() # Stop the game here <--

main(WIN, WIDTH) # Calling the main function -- IMPORTANT for the game to run!