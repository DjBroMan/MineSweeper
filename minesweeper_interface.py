from tkinter import *
from minesweeper_mechanism import MineSweeperMechanism
# Block size in pixels (width and height)
GRID=10
BLOCK_CANVAS_SIZE=(350,350)
# 500-350/2
CANVAS_LOCATION=((500-BLOCK_CANVAS_SIZE[0])/2,100)
BLOCK_HEIGHT = int(BLOCK_CANVAS_SIZE[0]/GRID)
BLOCK_WIDTH = int(BLOCK_CANVAS_SIZE[1]/GRID)



class MineSweeperInterface:
    def __init__(self) -> None:
        self.window=Tk()
        self.window.title("MineSweeper")
        self.window.geometry("500x500")
        self.mechanism = MineSweeperMechanism()
        self.button_number_relation={}

        # Create a canvas and set a size
        self.block_canvas = Canvas(self.window, width=BLOCK_CANVAS_SIZE[0], height=BLOCK_CANVAS_SIZE[1], bg="lightgray")
        self.block_canvas.place(x=CANVAS_LOCATION[0],y=CANVAS_LOCATION[1])

        #IMAGES
        #Images
        self.white_background=PhotoImage(file="images/White background.png")
        self.green_background=PhotoImage(file="images/green_background.png")
        self.red_background=PhotoImage(file="images/red_background.png")

        #BLOCKS in canvas
        self.blocks=[]
        for i in range(GRID):
            self.blocks.append([])
            for j in range(GRID):
                # block = Button(padx = 10, pady=10)
                # # block.place(x=i*20,y=j*20)
                # self.block_canvas.create_window(i*50,j*50,window=block)
                # self.blocks[i].append(block)

                # Create square buttons with fixed width and height
                block = Button(self.window, image=self.white_background,height=BLOCK_HEIGHT,width=BLOCK_WIDTH,command=lambda row=i, col=j: self.show_number(row,col))  # Adjust to get square buttons
                # Add button to canvas at the correct position (i * BLOCK_SIZE, j * BLOCK_SIZE)
                self.block_canvas.create_window(i * (BLOCK_HEIGHT+5), j * (BLOCK_WIDTH+5), window=block, anchor="nw")
                self.blocks[i].append(block)
                

        







        self.window.mainloop()
    

    def show_number(self,r,c):
        # self.blocks[r][c].config(text=self.mechanism.minesweeper_grid[r][c], image='', compound="center")
        self.blocks[r][c].destroy()
        



interface=MineSweeperInterface()