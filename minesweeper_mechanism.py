import random as rd

GRID_SIZE=10
MINES=10

def check_around(row:int,col:int,grid:list):
    l1 = [row-1,row,row+1]
    l2 = [col-1,col,col+1]
    count=0
    for i in range(3):
        for j in range(3):
            if l1[i]!=row or l2[j]!=col:
                try:
                    if grid[l1[i]][l2[j]] == 'M':
                        count+=1
                except IndexError:
                    pass
    return count

    # else:
    #     print("look out. you are on a mine")




#mine = M
class MineSweeperMechanism:
    def __init__(self) -> None:
        self.minesweeper_grid=[[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        # self.minesweeper_grid=[[0, 'M', 0, 0, 0, 'M', 'M', 0, 0, 'M'],
        #                        [0, 0, 'M', 0, 'M', 'M', 0, 0, 0, 0], 
        #                        ['M', 'M', 0, 'M', 0, 0, 'M', 0, 0, 0], 
        #                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'M'], 
        #                        [0, 0, 'M', 'M', 0, 'M', 0, 0, 0, 'M'], 
        #                        [0, 0, 'M', 0, 'M', 0, 0, 'M', 0, 0], 
        #                        [0, 0, 0, 0, 'M', 0, 0, 'M', 'M', 0], 
        #                        [0, 'M', 0, 0, 0, 0, 0, 0, 'M', 0], 
        #                        [0, 0, 0, 0, 0, 'M', 0, 0, 'M', 0], 
        #                        ['M', 'M', 0, 0, 0, 'M', 'M', 0, 0, 'M']]
        self.mines=[]
        i=1
        # j=0
        while i<=MINES:
            # j+=1
            x= rd.randint(0,9)
            y= rd.randint(0,9)
            if (x,y) not in self.mines:
                self.minesweeper_grid[x][y]='M'
                self.mines.append((x,y))
                i+=1
        # print(j)
        print(self.minesweeper_grid)
        self.add_numbers()
        print(self.mines)

    def add_numbers(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.minesweeper_grid[i][j] != 'M':  # Skip cells that already contain mines
                    self.minesweeper_grid[i][j] = check_around(i, j, self.minesweeper_grid)
        print(self.minesweeper_grid)
        # print(check_around(1,2,self.minesweeper_grid))
    
    def floodfill(self,row,col):
        pass
        

mine=MineSweeperMechanism()