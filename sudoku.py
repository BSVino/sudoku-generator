#!/usr/bin/python

import array
import random

# The grid is a 9 by 9 char array.
# 0 means there is no number.
# 1 to 9 are the numbers.
# Indexing starts on the upper left.
grid = array.array('b',
	[1,2,3,7,8,9,4,5,6,
	 4,5,6,1,2,3,7,8,9,
	 7,8,9,4,5,6,1,2,3,
	 9,1,2,6,7,8,3,4,5,
	 3,4,5,9,1,2,6,7,8,
	 6,7,8,3,4,5,9,1,2,
	 8,9,1,5,6,7,2,3,4,
	 2,3,4,8,9,1,5,6,7,
	 5,6,7,2,3,4,8,9,1])

# Empty grid, start with anything possible.
grid_possibilities = array.array('h',
	[0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0])

# ============================== GRID PROCEDURES =================================

# Return the value of a cell in the grid
def c(grid, x, y):
	return grid[9*y + x]

# Set the value of a cell in the grid
def s(grid, x, y, v):
	grid[9*y + x] = v

# Get the index of a box.
# Indexes start at the top left and go right, just like for cells.
def get_box(x, y):
	return (x/3)%3 + 3*((y/3)%3)

# Get the index of a cell within a box.
# The top left cell in a box is 0, then 1, then 2,
# Then the middle left cell is 3, etc etc.
def get_box_cell(x, y):
	return x%3 + 3*(y%3)

# Given a box and cell index pair, return the index into a grid array for that cell.
def get_box_cell_coord(box, cell):
	return 27*(box/3) + 3*(box%3) + 9*(cell/3) + cell%3

# Get a cell given the index of a box and cell.
# The arguments for this are the return values of get_box and get_box_cell
def b(grid, box, cell):
	return grid[get_box_cell_coord(box, cell)]

def pretty_print(c):
	if c == 0:
		return " "
	else:
		return chr(c + ord('0'))

def grid_print(g):
	print pretty_print(c(g, 0, 0)) + " " + pretty_print(c(g, 1, 0)) + " " + pretty_print(c(g, 2, 0)) + \
		 "|" + pretty_print(c(g, 3, 0)) + " " + pretty_print(c(g, 4, 0)) + " " + pretty_print(c(g, 5, 0)) + \
		 "|" + pretty_print(c(g, 6, 0)) + " " + pretty_print(c(g, 7, 0)) + " " + pretty_print(c(g, 8, 0))
	print pretty_print(c(g, 0, 1)) + " " + pretty_print(c(g, 1, 1)) + " " + pretty_print(c(g, 2, 1)) + \
		 "|" + pretty_print(c(g, 3, 1)) + " " + pretty_print(c(g, 4, 1)) + " " + pretty_print(c(g, 5, 1)) + \
		 "|" + pretty_print(c(g, 6, 1)) + " " + pretty_print(c(g, 7, 1)) + " " + pretty_print(c(g, 8, 1))
	print pretty_print(c(g, 0, 2)) + " " + pretty_print(c(g, 1, 2)) + " " + pretty_print(c(g, 2, 2)) + \
		 "|" + pretty_print(c(g, 3, 2)) + " " + pretty_print(c(g, 4, 2)) + " " + pretty_print(c(g, 5, 2)) + \
		 "|" + pretty_print(c(g, 6, 2)) + " " + pretty_print(c(g, 7, 2)) + " " + pretty_print(c(g, 8, 2))
	print "-----+-----+-----"
	print pretty_print(c(g, 0, 3)) + " " + pretty_print(c(g, 1, 3)) + " " + pretty_print(c(g, 2, 3)) + \
		 "|" + pretty_print(c(g, 3, 3)) + " " + pretty_print(c(g, 4, 3)) + " " + pretty_print(c(g, 5, 3)) + \
		 "|" + pretty_print(c(g, 6, 3)) + " " + pretty_print(c(g, 7, 3)) + " " + pretty_print(c(g, 8, 3))
	print pretty_print(c(g, 0, 4)) + " " + pretty_print(c(g, 1, 4)) + " " + pretty_print(c(g, 2, 4)) + \
		 "|" + pretty_print(c(g, 3, 4)) + " " + pretty_print(c(g, 4, 4)) + " " + pretty_print(c(g, 5, 4)) + \
		 "|" + pretty_print(c(g, 6, 4)) + " " + pretty_print(c(g, 7, 4)) + " " + pretty_print(c(g, 8, 4))
	print pretty_print(c(g, 0, 5)) + " " + pretty_print(c(g, 1, 5)) + " " + pretty_print(c(g, 2, 5)) + \
		 "|" + pretty_print(c(g, 3, 5)) + " " + pretty_print(c(g, 4, 5)) + " " + pretty_print(c(g, 5, 5)) + \
		 "|" + pretty_print(c(g, 6, 5)) + " " + pretty_print(c(g, 7, 5)) + " " + pretty_print(c(g, 8, 5))
	print "-----+-----+-----"
	print pretty_print(c(g, 0, 6)) + " " + pretty_print(c(g, 1, 6)) + " " + pretty_print(c(g, 2, 6)) + \
		 "|" + pretty_print(c(g, 3, 6)) + " " + pretty_print(c(g, 4, 6)) + " " + pretty_print(c(g, 5, 6)) + \
		 "|" + pretty_print(c(g, 6, 6)) + " " + pretty_print(c(g, 7, 6)) + " " + pretty_print(c(g, 8, 6))
	print pretty_print(c(g, 0, 7)) + " " + pretty_print(c(g, 1, 7)) + " " + pretty_print(c(g, 2, 7)) + \
		 "|" + pretty_print(c(g, 3, 7)) + " " + pretty_print(c(g, 4, 7)) + " " + pretty_print(c(g, 5, 7)) + \
		 "|" + pretty_print(c(g, 6, 7)) + " " + pretty_print(c(g, 7, 7)) + " " + pretty_print(c(g, 8, 7))
	print pretty_print(c(g, 0, 8)) + " " + pretty_print(c(g, 1, 8)) + " " + pretty_print(c(g, 2, 8)) + \
		 "|" + pretty_print(c(g, 3, 8)) + " " + pretty_print(c(g, 4, 8)) + " " + pretty_print(c(g, 5, 8)) + \
		 "|" + pretty_print(c(g, 6, 8)) + " " + pretty_print(c(g, 7, 8)) + " " + pretty_print(c(g, 8, 8))

# g should be a grid_possibilities array. x and y are 9x9 cell coordinates.
def gridp_allow(g, x, y, digit):
	g[9*y + x] = g[9*y + x] | (1<<digit)

# g should be a grid_possibilities array. x and y are 9x9 cell coordinates.
def gridp_disallow(g, x, y, digit):
	g[9*y + x] = g[9*y + x] & ~(1<<digit)

# g should be a grid_possibilities array. x and y are 9x9 cell coordinates.
def gridp_is_allowed(g, x, y, digit):
	return g[9*y + x] & (1<<digit)

# g should be a grid_possibilities array. x and y are 9x9 cell coordinates.
# Returns the number of possibilities allowed for this cell.
def gridp_num_allowed(g, x, y):
	allowed = 0
	for k in range(1, 10):
		if gridp_is_allowed(g, x, y, k):
			allowed += 1
	return allowed

# g should be a grid_possibilities array. x and y are 9x9 cell coordinates.
# Returns a list of every number allowed in this cell.
def gridp_get_allowed(g, x, y):
	allowed = []
	for k in range(1, 10):
		if gridp_is_allowed(g, x, y, k):
			allowed.append(k)
	return allowed

# g should be a grid_possibilities array.
# box and cell are indexes from get_box and get_box_cell
def gridp_box_allow(g, box, cell, digit):
	g[get_box_cell_coord(box, cell)] = g[get_box_cell_coord(box, cell)] | (1<<digit)

# g should be a grid_possibilities array.
# box and cell are indexes from get_box and get_box_cell
def gridp_box_disallow(g, box, cell, digit):
	g[get_box_cell_coord(box, cell)] = g[get_box_cell_coord(box, cell)] & ~(1<<digit)

# g should be a grid_possibilities array.
# box and cell are indexes from get_box and get_box_cell
def gridp_box_is_allowed(g, box, cell, digit):
	return g[get_box_cell_coord(box, cell)] & (1<<digit)

def gridp_print_num_allowed_or_space(g, gp, x, y):
	allowed = gridp_num_allowed(gp, x, y)
	if c(g, x, y) == 0:
		return chr(allowed + ord('0'));

	return " "

# g should be a grid_possibilities array.
# Returns a list of every cell that this number is allowed in.
def gridp_get_allowed_cells_in_box_for_digit(g, gp, box, digit):
	allowed = []
	for cell in xrange(0, 9):
		coord = get_box_cell_coord(box, cell);

		if b(g, box, cell) > 0:
			continue

		if gridp_is_allowed(gp, coord%9, coord/9, digit):
			allowed.append(cell)

	return allowed

# There are too many possibilities per square to print them all. Instead use this procedure to print a grid of the number of possibilities.
def grid_print_num_allowed(g, gp):
	print gridp_print_num_allowed_or_space(g, gp, 0, 0) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 0) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 0) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 0) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 0) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 0) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 0) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 0) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 0)
	print gridp_print_num_allowed_or_space(g, gp, 0, 1) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 1) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 1) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 1) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 1) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 1) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 1) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 1) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 1)
	print gridp_print_num_allowed_or_space(g, gp, 0, 2) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 2) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 2) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 2) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 2) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 2) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 2) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 2) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 2)
	print "-----+-----+-----"
	print gridp_print_num_allowed_or_space(g, gp, 0, 3) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 3) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 3) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 3) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 3) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 3) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 3) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 3) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 3)
	print gridp_print_num_allowed_or_space(g, gp, 0, 4) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 4) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 4) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 4) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 4) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 4) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 4) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 4) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 4)
	print gridp_print_num_allowed_or_space(g, gp, 0, 5) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 5) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 5) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 5) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 5) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 5) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 5) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 5) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 5)
	print "-----+-----+-----"
	print gridp_print_num_allowed_or_space(g, gp, 0, 6) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 6) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 6) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 6) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 6) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 6) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 6) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 6) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 6)
	print gridp_print_num_allowed_or_space(g, gp, 0, 7) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 7) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 7) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 7) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 7) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 7) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 7) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 7) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 7)
	print gridp_print_num_allowed_or_space(g, gp, 0, 8) + " " + gridp_print_num_allowed_or_space(g, gp, 1, 8) + " " + gridp_print_num_allowed_or_space(g, gp, 2, 8) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 3, 8) + " " + gridp_print_num_allowed_or_space(g, gp, 4, 8) + " " + gridp_print_num_allowed_or_space(g, gp, 5, 8) + \
		 "|" + gridp_print_num_allowed_or_space(g, gp, 6, 8) + " " + gridp_print_num_allowed_or_space(g, gp, 7, 8) + " " + gridp_print_num_allowed_or_space(g, gp, 8, 8)

# Set a number on a grid, updating the disallow bit on all appropriate cells.
def grid_set(g, gp, x, y, digit):
	s(g, x, y, digit)

	for k in range(0, 9):
		gridp_disallow(gp, x, k, digit)
		gridp_disallow(gp, k, y, digit)

	box = get_box(x, y)
	for i in range(0, 9):
		gridp_box_disallow(gp, box, i, digit)

def get_possibilities(grid):
	grid_possibilities = array.array('h',
		[~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0,
		 ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0, ~0])

	for k in range(0, 9*9):
		grid_set(grid, grid_possibilities, k%9, k/9, grid[k])

	return grid_possibilities

"""
In broad strokes:
1. Generate a valid grid

In a loop:
  2. Remove a point
  3. Run solving algorithms on the grid
  4. Memoize the result (hash it)
  5. Quit the loop when we have enough results

6. Inspect the memoized data and generate puzzles for four difficulty levels
"""

def row_swap(grid, k1, k2):
	for k in range(0, 9):
		grid[k1*9 + k], grid[k2*9 + k] = grid[k2*9 + k], grid[k1*9 + k]

def col_swap(grid, k1, k2):
	for k in range(0, 9):
		grid[k1 + k*9], grid[k2 + k*9] = grid[k2 + k*9], grid[k1 + k*9]

# First make 50 random row and column swaps to randomize the permutations
for k in range(0, 50):
	box = random.randint(0, 2)
	row1 = random.randint(0, 2)
	row2 = (row1+random.randint(1, 2))%3 + box*3
	row1 += box*3
	row_swap(grid, row1, row2)

	box = random.randint(0, 2)
	col1 = random.randint(0, 2)
	col2 = (col1+random.randint(1, 2))%3 + box*3
	col1 += box*3
	col_swap(grid, col1, col2)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
randomized = []

# Now create a random permutation for the digits and apply it
while len(digits):
	index = random.randint(0, len(digits)-1)
	digit = digits.pop(index)
	randomized.append(digit)

for k in range(0, 9*9):
	grid[k] = randomized[grid[k]-1]
	grid_possibilities[k] = 1<<grid[k]

# The next two strategies for generating grids don't work, they eventually hit
# invalid grid positions.
"""
for k in range(1, 10):
	for box in range(0, 9):
		print "Box:  " + str(box)

		# Find the cells in this box that are free for this number
		free_cells = []
		for cell in range(0, 9):
			if gridp_box_is_allowed(grid_possibilities, box, cell, k):
				if b(grid, box, cell) == 0:
					free_cells.append(cell)

		print "Available: "
		print free_cells

		new = random.randint(0, len(free_cells)-1)

		print "Chosen: " + str(free_cells[new])

		index = get_box_cell_coord(box, free_cells[new])
		x = index%9
		y = index/9

		grid_set(grid, grid_possibilities, x, y, k)

		grid_print(grid)
		grid_print_num_allowed(grid_possibilities)
"""

"""
for k in range(0, 9*9+1):
	x = k%9
	y = k/9

	print "Coordinate: " + str(x) + ", " + str(y)
	allowed = gridp_get_allowed(grid_possibilities, x, y)
	print "Allowed: "
	print allowed
	if len(allowed) == 0:
		grid_print(grid)
		grid_print_num_allowed(grid_possibilities)
	new = allowed[random.randint(0, len(allowed)-1)]
	print "New: " + str(new)
	print ""

	grid_set(grid, grid_possibilities, x, y, new)
"""

#grid_print(grid)
#grid_print_num_allowed(grid_possibilities)


""" Sako's notes from Sunday
We will have some function in the creation such that it will contain a loop
while (set_g)

>>>>
int max_val = 0
bool Set_g(grid g, int stopping value)
grid m = Take out random number(g);
int w = coord of number we just took out
int curr_val = 0
if (mv > stopping value)
    return false;
if (solve(m, &curr_val))
    if (curr_val>max_val)
        g=m;
        append.takenout(w) where takenout is an array we have of coords of points we have taken out from grid
        max_val = curr_val
        return true;


bool Solve(grid g)
{
	for coord in takenout array
	run the pips and other techniques we haven't yet decided
}

def pips(grid g, int x, int y)
    Check the box, disallow what can't be
    Check the col, disallow
    Check the row, disallow
    If conclusive(we have a function that check if only one # allowed)
        Set #, +1 difficulty
    else
        use 2nd technique

def allow_all(grid g, int x, int y)
    for k in range(0, 9*9):
    	grid[k] = ~0
    	
"""

grid = array.array('b',
	[0,0,1, 9,5,7, 0,6,3,
	 0,0,0, 8,0,6, 0,7,0,
	 7,6,9, 1,3,0, 8,0,5,

	 0,0,7, 2,6,1, 3,5,0,
	 3,1,2, 4,9,5, 7,8,6,
	 0,5,6, 3,7,8, 0,0,0,

	 1,0,8, 6,0,9, 5,0,7,
	 0,9,0, 7,1,0, 6,0,8,
	 6,7,4, 5,8,3, 0,0,0])

grid_possibilities = get_possibilities(grid)

#grid_print(grid)
#grid_print_num_allowed(grid, grid_possibilities)

# If in a certain box the only candidate cells are all in a line then
# we can eliminate that number in that row in other boxes.
def candidate_lines(grid, grid_p):
	for box in xrange(0, 9):
		for digit in xrange(1, 10):
			allowed = gridp_get_allowed_cells_in_box_for_digit(grid, grid_p, box, digit)
			if not len(allowed):
				continue

			x_mod = allowed[0]%3
			y_mod = allowed[0]/3

			only_x = True
			only_y = True
			for k in xrange(1, len(allowed)):
				if allowed[k]%3 != x_mod:
					only_x = False
				if allowed[k]/3 != y_mod:
					only_y = False

			assert not (only_x and only_y)

			if not only_x and not only_y:
				continue

			if only_x:
				column = get_box_cell_coord(box, allowed[0])%9

				for row in xrange(0, 9):
					if get_box(column, row) == box:
						continue

					gridp_disallow(grid_p, column, row, digit)

			if only_y:
				row = get_box_cell_coord(box, allowed[0])/9

				for column in xrange(0, 9):
					if get_box(column, row) == box:
						continue

					gridp_disallow(grid_p, column, row, digit)

#candidate_lines(grid, grid_possibilities)

#grid_print(grid)
#grid_print_num_allowed(grid, grid_possibilities)



def Pips(g, gp):
	#gp = get_possibilities(g)
	canPips=True
	while(canPips):
		canPips=False
		for cell in range(0,81):
			if c(g, cell%9, cell/9) == 0:
				#print("dude")
				n=gridp_get_allowed(gp,cell%9,cell/9)
				#print cell
				#print n
				if len(n) == 1:
					grid_print(grid)
					#print cell
					#print n
					canPips=True
					grid_set(g,gp,cell%9,cell/9,n[0])
					print '\n'
					continue


grid_print(grid)
grid_print_num_allowed(grid, grid_possibilities)

Pips(grid, grid_possibilities)
grid_print(grid)
grid_print_num_allowed(grid, grid_possibilities)




