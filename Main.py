import copy
class Tic_tac_toe():
    x = 1 
    o = 25 #change variable name later
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    gameDone = False
    linear_to_matrix = {0:True}
    
    def init_matrix(self, index) :
        for i in range(0, 3):
            for j in range (0, 3):
                self.linear_to_matrix[str(index)] = (i, j)
                index += 1


    def print_grid(self, player) :
        temp_grid = copy.deepcopy(self.grid)
        for i in range(0, 3):
            for j in range (0, 3):
                if temp_grid[i][j] != 0 :
                    if temp_grid[i][j] == 1 :
                        temp_grid[i][j] = 'X' 
                    else :
                        temp_grid[i][j] = 'O'
                

        for i in range(0, 3) :
            print(temp_grid[i])


    def go_again(self, amount) :
        foo = input()
        i = self.linear_to_matrix[foo][0]
        j = self.linear_to_matrix[foo][1]
        if self.check_there(i,j) :
            self.grid[i][j] = amount 
            print("-------------")
            
                
    def check_there(self, i, j):
        if self.grid[i][j] == 0 :
            return True
        else :
            return False
        
    def get_columns (self) :
        new_grid = self.grid[:]
        for i in range(0,3):
           new_grid[i] = [column[i] for column in new_grid]
        return new_grid

    def check_diagonal (self) :
        first_temp = (self.grid[0][0],self.grid[1][1],self.grid[2][2])
        second_temp = (self.grid[0][2],self.grid[1][1],self.grid[2][0])
        third_temp = (0, 0, 0)
        return (first_temp, second_temp, third_temp)
       
    def check_grid (self) :
        for i in range(0,3):
            if sum(self.grid[i]) == 3 or sum(self.get_columns()[i]) == 3:
                print("The Xs have won!")
                self.gameDone = True
            elif (sum(self.grid[i]) == 75) or (sum(self.get_columns()[i]) == 75):
                print("The Os have won!")
                self.gameDone = True
            elif (sum(self.check_diagonal()[i]) == 3) or (sum(self.check_diagonal()[i]) == 75):
                print ("A player has won via diagonal!!!")
                self.gameDone = True
        
        return self.gameDone
    
if __name__ == "__main__":
    print("Enter linear coordinates to play the game")
    game = Tic_tac_toe()
    game.init_matrix(1)

    while game.check_grid() == False :
        print("Player X: ")
        game.go_again(1)
        game.print_grid('X')
        print("Player O: ")
        game.go_again(25)
        game.print_grid('O')
    
    







    


    



