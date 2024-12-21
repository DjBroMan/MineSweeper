from tkinter import *

class Block:
    def __init__(self, 
                window: Tk, 
                background: Image, 
                command: callable, 
                block_height: int, 
                block_width: int, 
                row_no: int, 
                col_no: int) -> None:
        """
        Initialize a Minesweeper block with specific properties.
        
        Parameters:
        - window (Tk): The Tkinter window where the block will be displayed.
        - background (Image): The image to use as the block's background.
        - command (callable): The function to call when the block is clicked.
        - block_height (int): The height of the block.
        - block_width (int): The width of the block.
        - row_no (int): The row number of the block on the grid.
        - col_no (int): The column number of the block on the grid.
        """
        self.state = "hidden"  # Initial state of the block (hidden by default)
        self.revealed = False  # Track whether the block has been revealed
        
        # Create a Tkinter button representing the block
        self.button = Button(
            window,  # Parent window
            image=background,  # Background image for the block
            height=block_height,  # Button height
            width=block_width,  # Button width
            command=lambda row=row_no, col=col_no: command(row, col)  # On-click command
        )
        
        # Store the row and column position of the block
        self.row_no = row_no
        self.col_no = col_no

    def show(self, command2: callable) -> None:
        """
        Reveal the block and change its behavior after being shown.
        
        Parameters:
        - command2 (callable): The new function to call when the block is clicked after being revealed.
        """
        self.button.config(state="normal")  # Make the button clickable if disabled
        self.button.config(command=lambda row=self.row_no, col=self.col_no: command2(row, col))  # Update the command for subsequent clicks
