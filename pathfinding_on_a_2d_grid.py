# PHASE 1

# Implement a 10x10 grid that contains a starting point
# on (0,0), the delivery point on (9,9) and the following
# obstacles on locations (9,7) (8,7) (6,7) (6,8).

# Your algorithm should calculate a valid path avoiding 
# the obstacles and reaching the delivery point.

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

def formatting(steps=None):
    visual_grid = grid[:]
    if not steps is None:
        for step in steps[:-1]:
            visual_grid[step[0]][step[1]] = ">"
    print('\n'.join([str(lst) for lst in visual_grid]))

def is_valid(coordinates, grid):
    """Check if a location is valid.
    Is it in the boundaries? Is it an obstacle?"""  
    x, y = coordinates 
    if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
        if grid[x][y] == 1:
            return False
        else:
            return True
    else:
        return False

def find(element, matrix):
    """Returns a tuple of coordinates.
    Not really useful in this case as the matrix
    contains multiple zeros so it can only track 
    the first occurrance."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)

def get_adjacent(coordinates, grid):
    """Checks adjacent values to the selected cell.
    Returns a list of adjacent coordinates."""
    x, y = coordinates
    l = []

    for check_one in [-1, 0, 1]:
        for check_two in [-1, 0, 1]:
            position = (x+check_one, y+check_two)
            if not (check_one == check_two == 0) and is_valid(position, grid):
                l.append(position) 
    return l

def euclidian_distance(point_one, point_two):
    """Calculate the distance between two coordinates."""
    differences = [point_one[x] - point_two[x] for x in range(len(point_one))]
    differences_squared = [difference ** 2 for difference in differences]
    sum_of_squares = sum(differences_squared)
    return sum_of_squares ** 0.5

def find_path(starting_point, ending_point):
    """Return a list of coordinates for the best path."""
    path = []
    
    current_position = starting_point    
    current_distance = euclidian_distance(starting_point, ending_point)

    while current_position != ending_point:
        list_of_possible_steps = get_adjacent(current_position, grid)

        for step in list_of_possible_steps:
            distance = euclidian_distance(step, ending_point)

            if current_distance > distance:
                current_distance = distance
                current_position = step
                # Testing better cell
                #print("Found better cell:", current_distance, current_position)
        
        # For testing
        #print("Stepping to:", current_position)
        path.append(current_position)
        
                
        if path[-1] == ending_point:
            #print("We reached the final destination: ", current_position)
            break
        
    return path       
        
#print("This is the current path: ",find_path(starting_point, ending_point))

grid = make_grid()

# starting point
grid[0][0]="s"

# ending point
grid[9][9]="e"

# obstacles locations
grid[9][7]=1
grid[8][7]=1
grid[6][7]=1
grid[6][8]=1

print("This is the original grid: \n s = starting point \n e = ending point \n 0 = accessible cell \n 1 = obstable")
formatting()

starting_point = find("s", grid)
ending_point = find("e", grid)

path = find_path(starting_point, ending_point)

print("\n")
print("> for visual path: \n")
formatting(path)
print("\n")
print("PATH: ", path)