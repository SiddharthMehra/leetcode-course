#simulation

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:

        if player == 1:
            self.row[row]+=1
            self.col[col]+=1
            #diagonal
            if row == col:
                self.diag+=1
            #anti diagonal
            if row+ col == self.n-1:
                self.anti_diag+=1
            
            #player 1 won
            if self.row[row] == self.n or self.col[col] == self.n or self.diag == self.n or self.anti_diag == self.n:
                return 1
        
        else:
            self.row[row]-=1
            self.col[col]-=1
            if row == col:
                self.diag-=1
            if row+col == self.n-1:
                self.anti_diag-=1
            
            if self.row[row] == -self.n or self.col[col] == -self.n or self.diag == -self.n or self.anti_diag == -self.n:
                return 2

        return 0


            
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
