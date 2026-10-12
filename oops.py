# # ===============================================================================
# # @File:   main_tui.py (GameOfLife)
# # @Brief:  Implementation of Conways Game of Life
# # @Author: Tejas
# # @Date:   2026-09-15 Tue
# # @Notice: This is a simple implementation of conways game of life
# # @Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# # ===============================================================================

# # IMPORTANT(Tejas): Before you read the code I want you to go through the wiki article 
# # and understand what we are trying to build!!!

# # NOTE(Tejas): we'll use basic random numbers to populate the initial state.
# # You dont have to use this, you can populate it manually
# import random
# import time

# WIDTH = 90
# HEIGHT = 30

# # NOTE(Tejas): this is my convention to put g_ before any global
# # variables I use, you dont have to, but this is what I do...
# g_grid = [] # This is a 2D array which we will populate in init()

# ALIVE = 1
# DEAD = 0

# def print_state():
#     for i in range(HEIGHT):
#         for j in range(WIDTH):
#             if g_grid[i][j] == ALIVE:
#                 print("O", end="")
#             else:
#                 print(" ", end="")
#         print()

# def init():
#     # NOTE(Tejas): I use the random module here to add random state to each cell (ALIVE or DEAD).
#     # if you choose you can populate the grid
#     for i in range(HEIGHT):
#         row = []
#         for j in range(WIDTH):
#             number = random.randint(0, 1)
#             row.append(number)

#         g_grid.append(row)


# def count_neighbors(row, column):

#     # NOTE(Tejas): put your thinking cap on and try to figure out what we are trying to do.
#     # You have the game rules and also the name of the function is a big giveaway...

#     count = 0

#     for i in range(row - 1, row + 2):

#         for j in range(column - 1, column + 2):

#             # NOTE(Tejas): we want to skip the cell itself, we only want to count the neighbors
#             if i == row and j == column:
#                 continue

#             # NOTE(Tejas): we dont want to check outside the grid, so we skip those cells
#             if i < 0 or i >= HEIGHT:
#                 continue
#             if j < 0 or j >= WIDTH:
#                 continue

#             if g_grid[i][j] == ALIVE:
#                 count += 1

#     return count


# def next_generation():

#     # NOTE(Tejas): We have following rules to get the next generation of the grid.
#     # The Rules of Game of Life:
#     #   1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#     #   2. Any live cell with two or three live neighbours lives on to the next generation.
#     #   3. Any live cell with more than three live neighbours dies, as if by overpopulation.
#     #   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#     # Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

#     new_grid = []

#     for i in range(HEIGHT):
#         row = []

#         for j in range(WIDTH):
#             neighbors = count_neighbors(i, j)

#             if g_grid[i][j] == ALIVE:

#                 # NOTE(Tejas): Rule 1 & 3
#                 if neighbors < 2 or neighbors > 3:
#                     row.append(DEAD)

#                 # NOTE(Tejas): Rule 2
#                 else:
#                     row.append(ALIVE)

#             else:

#                 # NOTE(Tejas): Rule 4
#                 if neighbors == 3:
#                     row.append(ALIVE)
#                 else:
#                     row.append(DEAD)

#         new_grid.append(row)

#     return new_grid

# init()

# # NOTE(Tejas): Every application has whats called a main loop or game loop.
# # This will iterate for indefinitely, because we are working in a termainal
# # the program will be terminated by hitting Ctrl+C or closing the terminal window.
# # If this were a GUI application, we have a red cross in the top right corner
# # to close a window.
# while True:

#     # NOTE(Tejas): Think of this as a way to clear the terminal for our redraw.
#     print("\033[H", end="")

#     print_state()

#     # NOTE(Tejas): here we apply the rules to the current state of the grid.
#     g_grid = next_generation()

#     # NOTE(Tejas): Control simulation speed, adjust this value and see what happens...
#     time.sleep(0.1)


# # NOTE(Tejas): Once you think you understand the code
# # Try modifying the program:
# #  - [ ] Change the grid size.
# #  - [ ] Change the simulation speed.
# #  - [ ] Populate the grid manually instead of randomly.
# #  - [ ] Experiment with different initial patterns.
# #  - [ ] Try creating known Game of Life patterns such as a **glider**.
# #  - [ ] Add a generation counter.
# #  - [ ] Add support for pausing the simulation.
# #  - [ ] Try implementing your own improvements.


# ===============================================================================
# @File:   main_tui.py (LagntonsAnt)
# @Brief:  Implementation of LangtonsAnt
# @Author: Tejas
# @Date:   2026-09-18 Thu
# @Notice: 
# @Source: https://en.wikipedia.org/wiki/Langton%27s_ant
# ===============================================================================

# IMPORTANT(Tejas): Before you read the code I want you to go through the wiki article
# and understand what we are trying to build!!!

# NOTE(Tejas): The way we program this is quite similar to GameOfLife, so look
# at that code first and then come back here. I will try to explain the
# differences here.

WIDTH = 90
HEIGHT = 30

# NOTE(Tejas): This is state of each cell, we can either have a cell to be white
# or black (You can rename these to BLACK and WHITE if you want).
STATE_UNSET = 0
STATE_SET   = 1

# NOTE(Tejas): helpers so we know which direction the ant is facing.
# I have arraged them in a clockwise manner because of a reason!
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

# NOTE(Tejas): you could use any datatype to represent the position on the ant
# like a tuple, a list, a dict with x and y keys, but we are representing the row
# and column of the ant.
g_ant_x = 0
g_ant_y = 0
g_ant_facing = 0

g_grid = []

def init():

    global g_ant_x, g_ant_y, g_ant_facing
    global g_grid

    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(STATE_UNSET)
        g_grid.append(row)

    g_ant_x = WIDTH // 2
    g_ant_y = HEIGHT // 2
    g_ant_facing = UP

def turn_and_move_ant_right():

    global g_ant_facing, g_ant_x, g_ant_y

    new_ant_x = g_ant_x
    new_ant_y = g_ant_y

    # NOTE(Tejas): theres a cleaver way to do this using modulo operator which I
    # have commented out below. See if you can figure out how it works.
    # This is one of the very important properties of the modulo operator that I
    # use constantly in my code.

    # g_ant_facing = (g_ant_facing + 1) % 4

    if g_ant_facing == UP:
        g_ant_facing = RIGHT
        new_ant_x += 1
    elif g_ant_facing == RIGHT:
        g_ant_facing = DOWN
        new_ant_y += 1
    elif g_ant_facing == DOWN:
        g_ant_facing = LEFT
        new_ant_x -= 1
    elif g_ant_facing == LEFT: 
        g_ant_facing = UP
        new_ant_y -= 1

    if new_ant_x >= WIDTH:
        new_ant_x = 0
    if new_ant_x < 0:
        new_ant_x = WIDTH - 1
    if new_ant_y >= HEIGHT:
        new_ant_y = 0
    if new_ant_y < 0:
        new_ant_y = HEIGHT - 1

    g_ant_x = new_ant_x
    g_ant_y = new_ant_y

def turn_and_move_ant_left():

    global g_ant_facing, g_ant_x, g_ant_y

    new_ant_x = g_ant_x
    new_ant_y = g_ant_y

    # NOTE(Tejas): theres a cleaver way to do this using modulo operator which I
    # have commented out below. See if you can figure out how it works.
    # This is one of the very important properties of the modulo operator that I
    # use constantly in my code.

    # g_ant_facing = (g_ant_facing - 1) % 4

    if g_ant_facing == UP:
        g_ant_facing = LEFT 
        new_ant_x -= 1
    elif g_ant_facing == RIGHT:
        g_ant_facing = UP
        new_ant_y -= 1
    elif g_ant_facing == DOWN:
        g_ant_facing = RIGHT
        new_ant_x += 1
    elif g_ant_facing == LEFT: 
        g_ant_facing = DOWN
        new_ant_y += 1

    if new_ant_x >= WIDTH:
        new_ant_x = 0
    if new_ant_x < 0:
        new_ant_x = WIDTH - 1
    if new_ant_y >= HEIGHT:
        new_ant_y = 0
    if new_ant_y < 0:
        new_ant_y = HEIGHT - 1

    g_ant_x = new_ant_x
    g_ant_y = new_ant_y

def update_ant():

    # NOTE(Tejas): Rules:
    # 1. If the Ant is on a set square it unsets that square and turns left
    # 2. If the Ant is on an unset square it sets that square and turns right

    current_cell = g_grid[g_ant_y][g_ant_x]

    if current_cell == STATE_UNSET:
        g_grid[g_ant_y][g_ant_x] = STATE_SET
        turn_and_move_ant_right()

    else:
        g_grid[g_ant_y][g_ant_x] = STATE_UNSET
        turn_and_move_ant_left()

def print_state():

    print("\033[H", end="")

    for y in range(HEIGHT):
        for x in range(WIDTH):

            if y == g_ant_y and x == g_ant_x:
                print("A", end="")
            else:
                if g_grid[y][x] == STATE_UNSET:
                    print(" ", end="")
                else:
                    print("O", end="")

        print()

if __name__ == "__main__":
    init()
    while True:
        print_state()
        update_ant()

# TODO(Tejas): Can you do the following:

# 1. I am generally a follower of the DRY principle (Dont Repeat Yourself)
#    and I dont like how I have repeating code in both the turn functions
#    Can you refactor the code to remove the repetition?

# 2. Also I think a fuction in this code should do only one thing as its
#    very easy to debug if something goes wrong.
#    Can you refactor the turn functions into seperate functions that all do
#    one thing that they promise!

# 3. Think if you can add your own rules to how the ant moves and maybe we
#    can call this simulation <yourname>'s Ant!

