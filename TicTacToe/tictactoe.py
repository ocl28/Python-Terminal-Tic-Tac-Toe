"""
Program contains TicTacToe using python
Author: Oliver Clark
Date: 15 November 2022
"""

class Game:
    """TicTacToe"""
    def __init__(self):
        """declares the board and y translate for better player experience"""
        self.board = [["*","*","*"],
                 ["*","*","*"],
                 ["*","*","*"]]
        
        self.y_translate = {
            "0": 2,
            "1": 1,
            "2": 0
        }
        self.introduction()
        
    def introduction(self):
        """introduction to the game"""
        print(20*"-")
        print("Welcome to TicTacToe")
        print(20*"-")
        
        manual_input = input("Type 'Y' to access the manual or type anything " 
        "else to continue: ")
        print(20*"-")        
        if manual_input == "Y":
            self.manual()
            
        play_input = ""
        while play_input != "play" or play_input != "exit":
            play_input = input("Type 'play' to play or type 'exit' to exit out of "
                               "game: ")
            if play_input == "play":
                self.play()            
            elif play_input == "exit":
                print(20*"-")                
                print("Quitting Game")
                print(20*"-")
                [print("|") for i in range(7)]                
                break
        
    def manual(self):
        """access the player manual at the start of the game"""
        [print("|") for i in range(7)]
        print(20*"-")
        print("Player 1 will be 'X' and Player 2 will be 'O'.")
        print(20*"-")
        print("To enter a move, enter the x and y coordinate when it is " 
        "your turn to play. Example: '1 2' translates to x = 1, y = 2.") 
        print(20*"-")
        print("x and y coordinates start from 0.")
        print(20*"-")
        
        cont = ""
        while cont != "Y":
            cont = input("Type 'Y' to exit the manual. ")
        [print("|") for i in range(7)]
        
    def play(self):
        """
        Alternates between players and will call a 'move' function which 
        update the board
        """
        current_player = "1"
        win = False
        tie = False
        [print("|") for i in range(7)]
        print(20*"-")
        
        while not win and not tie:
            print(f"Player {current_player}'s turn!") 
            print(20*"-")
            move_coords = ""
            valid_input = False
            while not valid_input:
                move_coords = input("Enter your x and y coordinates: ")
                valid_input = self.valid_input_check(move_coords)
                
            print(f"Board before move:")        
            [print(i) for i in self.board]
            print(20*"-")        
            self.enter_move(move_coords, current_player)
            win = self.check_win()
            tie  = self.check_tie()
            
            if win is True or tie is True:
                break
            if current_player == "1":
                current_player = "2"
            else:
                current_player = "1"
                
        if win is True:
            self.win(current_player)
        elif tie is True:
            self.tie()

    def valid_input_check(self, move_coords):
        """checks if coords are valid"""
        if len(move_coords) != 3:
            print(20*"-")            
            print("Invalid coordinates! try a format such as '1 2'")
            print(20*"-")            
            return False
        if move_coords[2] in self.y_translate:
            y_location = self.y_translate[move_coords[2]]
        x_location = int(move_coords[0])        
        if int(move_coords[0]) < 0 or int(move_coords[0]) > 2:
            print(20*"-")            
            print("Invalid coordinates! try coordinates between 0 and 2")  
            print(20*"-")            
            return False
        elif int(move_coords[2]) < 0 or int(move_coords[2]) > 2:
            print(20*"-")            
            print("Invalid coordinates! try coordinates between 0 and 2")
            print(20*"-")            
            return False
        elif self.board[y_location][x_location] != "*":
            print(20*"-")            
            print("Invalid coordinates! try using a free space")
            print(20*"-")            
            return False
        return True
    
    
    def enter_move(self, move_coords, current_player):
        """
        Updates the grid with the input and checks if a win condiction was met
        """
        y_location = self.y_translate[move_coords[2]]
        x_location = int(move_coords[0])
        if self.board[y_location][x_location] == "*":
            if current_player == "1":
                self.board[y_location][x_location] = "X"
            else:
                self.board[y_location][x_location] = "O"
        print("Board after move:")
        [print(i) for i in self.board]
        print(20*"-")
        
    def check_win(self):
        """checks if a win conditional is meet"""
        board = self.board
        for row in board: #checking if a row is equal
            if row[0] != "*" and row[1] != "*" and row[2] != "*":
                if row[0] == row[1] and row[0] == row[2] and row[1] == row[2]:
                    return True
        for column_slot in range(3): #checking all columns
            if board[0][column_slot] != "*" and board[1][column_slot] != "*"\
            and board[2][column_slot] != "*":
                if board[0][column_slot] == board[1][column_slot] and\
                board[0][column_slot] == board[2][column_slot] and\
                board[1][column_slot] == board[2][column_slot]:
                    return True
                
        #checking both diagonals    
        if board[0][0] != "*" and board[1][1] != "*" and board[2][2] != "*":
            if board[0][0] == board[1][1] and board[0][0] == board[2][2] and\
            board[1][1] == board[2][2]:
                return True
        
        elif board[0][2] != "*" and board[1][1] != "*" and board[2][0] != "*": 
            if board[0][2] == board[1][1] and board[0][2] == board[2][0] and\
            board[1][1] == board[2][0]:
                return True
        else:
            return False
        
    def check_tie(self):
        """checks if '*' is in the board"""
        counter = 0
        for row in self.board:
            if "*" in row:
                counter += 1
        return counter == 0
        
    def tie(self):
        """tie message and resets board"""
        [print("|") for i in range(7)]
        print(20*"-")
        print("It's a tie!")
        print(20*"-")
        [print(i) for i in self.board]
        print(20*"-")
        cont = input("Type anything to continue. ")
        [print("|") for i in range(7)]
        self.reset_board()        
        self.introduction()        
        
    
    def win(self, current_player):
        """win message and resets the board"""
        [print("|") for i in range(7)]
        print(20*"-")
        print(f"Player {current_player} wins!")
        print(20*"-")
        [print(i) for i in self.board]
        print(20*"-")
        cont = input("Type anything to continue. ")
        [print("|") for i in range(7)]
        self.reset_board()
        self.introduction()
    
    def reset_board(self):
        self.board = [["*","*","*"],
                 ["*","*","*"],
                 ["*","*","*"]]
          
Game()        