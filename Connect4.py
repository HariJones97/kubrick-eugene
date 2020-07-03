import numpy as np

class Connect4():
    def __init__(self, player1, player2, width = 7, height = 6):
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros(width*height).reshape(height,width )
        self.width = width  - 1
        self.height = height - 1
        self.counter = [0] * width
        self.gamewon = False
        print (self.counter)
        print (self.board)



    def player1turn(self):
        x = input("Player one, choose your position(a-g)")
        dict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6}
        self.board[self.height - self.counter[dict[x]]][dict[x]] = 1
        self.counter[dict[x]] += 1
        print (self.counter)
        print (self.board)



    def player2turn(self):
        x = input("Player two, choose your position(a-g)")
        dict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6}
        self.board[self.height - self.counter[dict[x]]][dict[x]] = 2
        self.counter[dict[x]] += 1
        print (self.board)

    def play(self):
        turncount = 0
        maxturns = (self.width+1)*(self.height+1)
        while self.gamewon == False and turncount < maxturns:
            if turncount % 2 == 0:
                game.player1turn()
            else:
                game.player2turn()
            turncount+=1
            self.wincheck(self.board)

    def wincheck(self,board):
        y,x = np.where(board==1)
        
        #flat
        grid_up = board[:-1,:]
        grid_down = board[1:,:]
        grid_left = board[:,:-1]
        grid_right = board[:,1:]
        #diagonal
        grid_upleft = board[:-1,:-1]
        grid_upright = board[:-1,1:]
        grid_downleft = board[1:,:-1]
        grid_downright = board[1:,1:]

        print(any(1 in t for t in grid_up[grid_down==1])
        #if grid_up[grid_up[grid_down==1]==1].any():
        #    print('bruh')

        #for i,j in zip(y,x):
            #print(i,j)

game = Connect4('teamEugene', 'James')
game.play()