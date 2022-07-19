import random

# PHASE 1

# Implement a 10x10 grid that contains a starting point
# on (0,0), the delivery point on (9,9) and the following
# obstacles on locations (9,7) (8,7) (6,7) (6,8).

# Your algorithm should calculate a valid path avoiding 
# the obstacles and reaching the delivery point.

# Your solution should print the path in the format of 
# [(x1, y1), (x2, y2)... . .] and also the number of steps.

def create_empty_grid():
    """Make a grid 10x10."""
    grid = []
    rows, cols = (10,10)
    for x in range(rows):
        col = []
        for y in range(cols):
            col.append(0)
        grid.append(col)
    
    return grid

def print_grid(grid, steps=None):
    """Print the grid formatted with a list on each line."""
    visual_grid = grid[:]
    if not steps is None:
        for step in steps[:-1]:
            visual_grid[step[0]][step[1]] = ">"

    print('\n'.join([str(lst) for lst in visual_grid]))

def can_step_to_coordinate(coordinates, grid):
    """Check if a location is valid.
    Is it in the boundaries? Is it an obstacle?"""  
    x, y = coordinates 
    if 0 <= x and x < len(grid) and 0 <= y and y < len(grid[x]):
        if grid[x][y] == 1:
            return False
        else:
            return True
    else:
        return False

def find_value_in_grid(element, grid):
    """Return a tuple of coordinates.
    Not really useful in this case as the matrix
    contains multiple zeros so it can only track 
    the first occurrance."""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == element:
                return (i, j)

def get_valid_adjacent_coordinates(coordinates, grid):
    """Check adjacent values to the selected cell.
    Returns a list of adjacent coordinates."""
    x, y = coordinates
    steps = []

    for x_change in [-1, 0, 1]:
        for y_change in [-1, 0, 1]:
            if x_change == 0 and y_change == 0:
                continue

            position = (x+x_change, y+y_change)

            if can_step_to_coordinate(position, grid):
                steps.append(position)

    return steps

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
        list_of_adjacent_coordinates = get_valid_adjacent_coordinates(current_position, grid)
        if len(list_of_adjacent_coordinates) == 0:
            print("There are no valid steps from location", current_position, "!\n")
            break

        we_are_moving_away = True
        for coordinate in list_of_adjacent_coordinates:
            distance = euclidian_distance(coordinate, ending_point)

            if distance < current_distance:
                
                current_distance = distance
                current_position = coordinate
                we_are_moving_away = False
                
        if we_are_moving_away:
            print("There are no valid steps from location", current_position, "!\n")
            break

        path.append(current_position)
                
        if path[-1] == ending_point:
            break
        
    return path
        
# grid
grid = create_empty_grid()

# starting, ending points
grid[0][0]="s"
grid[9][9]="e"

# obstacles locations
obstacles_location = [(9,7), (8,7), (6,7), (6,8)]
for obstacle_loc in obstacles_location:
    x = obstacle_loc[0]
    y = obstacle_loc[1]
    grid[x][y] = 1

starting_point = find_value_in_grid("s", grid)
ending_point = find_value_in_grid("e", grid)
path = find_path(starting_point, ending_point)

# initial grid

print("PHASE 1\n")
print("This is the original grid: \n s = starting point \n e = ending point \n 0 = accessible cell \n 1 = obstable \n > = visual path \n")
print_grid(grid)
#print("\n> for visual path: \n")
#print_grid(grid, path)
print("\nPATH Phase 1: ", path)
print("Number of steps: ", len(path), "\n")

# PHASE 2

# Add an additional 20 randomly placed obstacles and print their location using the format [(x1, y2), (x2, y2)... . .]
# The obstacles should not overlap existing ones and should not be placed at the start and delivery points.
# Your algorithm should calculate a valid path avoiding the obstacles and reaching the delivery point.
# Your solution should print the path in the format of [(x1, y2), (x2, y2)... . .]

def random_obstacles(grid):
    """Place 20 random obstacles and 
    return a list of their coordinates."""
    random_obstacles_loc = []
    current_obstacle = 0
    while current_obstacle < 30:
        x = random.randrange(10)
        y = random.randrange(10)
            
        if (x,y) not in obstacles_location and (x,y) != starting_point and (x,y) != ending_point:
            if (x,y) not in random_obstacles_loc:
                random_obstacles_loc.append((x,y))
                grid[x][y] = 1
            else: 
                continue
        else:
            continue
        current_obstacle += 1
    print("20 new random obstacles locations: \n", random_obstacles_loc)
    

random_obstacles(grid)
print("\n")
print("Grid with new obstacles:\n")
print_grid(grid)

print("\nGrid with new visual path:\n")
path = find_path(starting_point, ending_point)
print_grid(grid, path)
print("\nPATH Phase 2: ", path)
