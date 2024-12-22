from tkinter import *
from PIL import Image, ImageTk  # For image resizing
from minesweeper_mechanism import MineSweeperMechanism
from minesweeper_block import Block

# Set grid size (can be changed dynamically)
GRID = 18  # Maximum recommended size is 18

# Block size (width and height in pixels)
BLOCK_WIDTH = 30
BLOCK_HEIGHT = 30

class MineSweeperInterface:
    def __init__(self) -> None:
        """
        Initialize the Minesweeper game interface.
        Creates the main window, sets up the game grid, loads images, and initializes blocks.
        """
        print("Initializing MineSweeperInterface...")  # Print statement
        self.window = Tk()
        self.window.title("MineSweeper")

        # Get screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate window size based on grid size and block size
        window_width = GRID * BLOCK_WIDTH + 100  # Adding padding to the window
        window_height = GRID * BLOCK_HEIGHT + 150  # Adding padding for top and bottom

        # Calculate position to center the window
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set window size and position
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Initialize Minesweeper Mechanism
        self.mechanism = MineSweeperMechanism(GRID)
        self.button_number_relation = {}

        # Create a canvas to hold the grid blocks
        self.block_canvas = Canvas(self.window, width=GRID * BLOCK_WIDTH, height=GRID * BLOCK_HEIGHT, bg="lightgray")
        self.block_canvas.place(x=(window_width - GRID * BLOCK_WIDTH) / 2, y=50)  # Center the canvas

        # NUMBER IMAGES: Preload and resize images
        self.numbers = {}
        for i in range(9):  # Load images for numbers 0 to 8
            image_path = f"images/numbers/{i}.png"
            self.numbers[i] = self.load_and_resize_image(image_path)
        self.numbers['M'] = self.load_and_resize_image("images/numbers/mine.png")
        self.numbers["flag"] = self.load_and_resize_image("images/background.png")
        
        # Background images for block states
        self.background = self.load_and_resize_image("images/background.png")
        self.default = self.load_and_resize_image("images/White background.png")

        # Initialize grid blocks
        self.blocks = []
        for i in range(GRID):
            self.blocks.append([])
            for j in range(GRID):
                # Create each block with button and configuration
                block = Block(
                    window=self.window,
                    background=self.background,
                    command=self.flood,
                    block_height=BLOCK_HEIGHT,
                    block_width=BLOCK_WIDTH,
                    row_no=i,
                    col_no=j
                )

                # Place the block on the canvas
                self.block_canvas.create_window(
                    j * (BLOCK_WIDTH + 2),  # Adjust the spacing between blocks
                    i * (BLOCK_HEIGHT + 2),
                    window=block.button,
                    anchor="nw"
                )
                self.blocks[i].append(block)

        # Start the Tkinter main loop
        self.window.mainloop()

    def load_and_resize_image(self, path):
        """
        Load and resize an image to fit the button dimensions.
        """
        print(f"Loading and resizing image: {path}")  # Print statement
        original_image = Image.open(path)
        resized_image = original_image.resize((BLOCK_WIDTH, BLOCK_HEIGHT), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    
    def flood(self, r, c):
        print(f"Flood fill initiated at ({r}, {c})")  # Print statement
        self.show_number(r,c)
        self.mechanism.flood_fill(r, c, self.blocks)
        self.reveal_the_revealed()
    
    def reveal_the_revealed(self):
        print("Revealing all the revealed blocks...")  # Print statement
        for i in range(GRID):
            for j in range(GRID):
                if self.blocks[i][j].revealed:
                    self.show_number(i, j)

    def show_number(self, r, c):
        """
        Display the number or mine image on a block after being clicked.
        """
        print(f"Showing number at block ({r}, {c})")  # Print statement
        if not self.mechanism.first_move_played:
            self.played_first_move(r, c)
        
        number = self.mechanism.minesweeper_grid[r][c]
        number_image = self.numbers.get(number, self.default)  # Default to white if number not found

        # Update the button to display the number image and disable further clicks
        self.blocks[r][c].button.config(
            image=number_image,
            text=''
        )

        # Store a reference to prevent garbage collection
        self.blocks[r][c].button.image = number_image

        # Prevent further clicks on revealed blocks
        self.blocks[r][c].show(self.display_all_blocks)

    def played_first_move(self, row_no, col_no):
        """
        Handle logic for the first move, ensuring no mines are in the initial clicked area.
        """
        print(f"First move played at ({row_no}, {col_no})")  # Print statement
        self.mechanism.move_played(row_no, col_no)

    def dummy_function(self, r: int, c: int) -> None:
        """
        Dummy function to prevent further clicks on an already revealed block.
        """
        print(f"Dummy function called at ({r}, {c})")  # Print statement
        pass

    def display_all_blocks(self, r, c):
        """
        Display all blocks by showing their numbers or state when triggered.
        """
        print("Displaying all blocks...")  # Print statement
        for i in range(GRID):
            for j in range(GRID):
                if not self.blocks[i][j].revealed:  # Only show the number if not revealed
                    self.show_number(i, j)

# Run the interface
interface = MineSweeperInterface()
