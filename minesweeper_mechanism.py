import random as rd

# Global mine percentage
mine_percentage = 0.123  # Approximately 12.3% of grid cells will have mines

def check_around(row: int, col: int, grid: list):
    """
    Check the number of mines in the surrounding 8 cells of a given grid cell.
    Args:
        row (int): Row index of the current cell.
        col (int): Column index of the current cell.
        grid (list): 2D grid representing the Minesweeper board.
    Returns:
        int: Number of adjacent cells containing mines.
    """
    # Define surrounding row and column indices
    l1 = [row - 1, row, row + 1]
    l2 = [col - 1, col, col + 1]
    count = 0
    
    # Iterate over the surrounding cells
    for i in range(3):
        for j in range(3):
            if l1[i] != row or l2[j] != col:  # Exclude the current cell
                try:
                    if grid[l1[i]][l2[j]] == 'M':
                        count += 1  # Increment count if a mine is found
                except IndexError:
                    pass  # Ignore out-of-bound indices
    return count

class MineSweeperMechanism:
    def __init__(self, grid_size: int) -> None:
        """
        Initialize the Minesweeper game mechanism.
        Args:
            grid_size (int): Size of the square grid.
        """
        self.grid_size = grid_size
        self.first_move_played = False  # Track if the first move has been made

        # Calculate the number of mines based on the grid size and mine percentage
        self.mines_count = int(self.grid_size * self.grid_size * mine_percentage)

        # Initialize an empty grid with no mines
        self.minesweeper_grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.mines = []  # Store mine positions

        self.place_mines()  # Randomly place mines on the grid

        print("Initial Minesweeper Grid with Mines:")
        for row in self.minesweeper_grid:
            print(row)
    
    def add_numbers(self):
        """
        Add numbers to each cell indicating the number of adjacent mines.
        """
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.minesweeper_grid[i][j] != 'M':  # Skip mine cells
                    self.minesweeper_grid[i][j] = check_around(i, j, self.minesweeper_grid)

    def place_mines(self):
        """
        Randomly place mines on the grid, ensuring no duplicate positions.
        """
        i = 0
        while i < self.mines_count:
            x = rd.randint(0, self.grid_size - 1)
            y = rd.randint(0, self.grid_size - 1)
            if (x, y) not in self.mines:
                self.minesweeper_grid[x][y] = 'M'  # Place a mine
                self.mines.append((x, y))  # Store mine position
                i += 1
    
    def move_played(self, row_no, col_no):
        """
        Adjust mine placement after the first move to ensure the starting area is mine-free.
        Args:
            row_no (int): Row index of the first move.
            col_no (int): Column index of the first move.
        """
        self.first_move_played = True
        
        # Define the safe zone (a 5x5 area centered on the first move)
        for i in range(row_no - 2, row_no + 3):
            for j in range(col_no - 2, col_no + 3):
                temp_row = i
                temp_col = j
                
                # If a mine is in the safe zone, relocate it
                if (temp_row, temp_col) in self.mines:
                    print("Found a mine in the safe zone")
                    self.minesweeper_grid[temp_row][temp_col] = 0
                    self.mines.remove((temp_row, temp_col))
                    
                    # Relocate the mine to a valid position outside the safe zone
                    while ((temp_row, temp_col) in self.mines) or (row_no-2 <= temp_row <= row_no+2 and col_no-2 <= temp_col <= col_no+2):
                        print("Relocating mine to:", temp_row, temp_col)
                        temp_row = rd.randint(0, self.grid_size - 1)
                        temp_col = rd.randint(0, self.grid_size - 1)
                    
                    self.minesweeper_grid[temp_row][temp_col] = 'M'
                    self.mines.append((temp_row, temp_col))
        
        # Recalculate the numbers after mine relocation
        self.add_numbers()
        
        print("Final Minesweeper Grid with Numbers:")
        for row in self.minesweeper_grid:
            print(row)
