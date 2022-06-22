# PHASE 1

# Implement a 10x10 grid that contains a starting point
# on (0,0), the delivery point on (9,9) and the following
# obstacles on locations (9,7) (8,7) (6,7) (6,8).


def make_grid():
    """Make a grid 10x10."""
    grid = []
    rows, cols = (10,10)
    for x in range(rows):
        col = []
        for y in range(cols):
            col.append(0)
        grid.append(col)
    
    return grid

grid = make_grid()

def formatting():
    print('\n'.join([str(lst) for lst in grid]))

# Your algorithm should calculate a valid path avoiding 
# the obstacles and reaching the delivery point.

# starting point
grid[0][0]="s"

# ending point
grid[9][9]="e"

# obstacles locations
grid[9][7]=1
grid[8][7]=1
grid[6][7]=1
grid[6][8]=1

def is_valid(x, y, grid):
    """Check if a location is valid.
    Is it in the boundaries? Is it an obstacle?"""   
    if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
        if grid[x][y] == 1:
            print("Obstacle")
            return False
        else:
            return True
    else:
        return False
       

formatting()

#print(is_valid(8,7,grid))

def get_adjacent(x, y, grid):
    """Check adjacent values to the selected cell."""
    l = []

    for check_one in [-1, 0, 1]:
        for check_two in [-1, 0, 1]:
            if not (check_one == check_two == 0) and is_valid(x+check_one, y+check_two, grid):
                l.append(grid[x+check_one][y+check_two])
            
    return l

print(get_adjacent(0,0, grid))

def find_path(starting_point, ending_point):

    path = []

    current_position = starting_point

    while current_position:
        if current_position != ending_point:
            get_adjacent()
        else:
            break
    

