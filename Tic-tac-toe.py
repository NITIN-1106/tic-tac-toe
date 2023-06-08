#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nitin
#
# Created:     08/06/2023
# Copyright:   (c) nitin 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math


class Board:
    def __init__(self, board):
        self.board = board
        self.win = False
        self.play = True


    def display_board(self, board):

        #Displaying board with player
        count = 0
        print("\n")
        for i in range((int(math.sqrt(len(self.board))))):
            print(self.board[count : int(math.sqrt(len(self.board))) + count])
            count += int(math.sqrt(len(self.board)))
        print("\n")


    def check_board(self, board, gameover, player):
        dim = (round(math.sqrt(len(self.board))))
        count4 = 0

        #Checking rows
        for i in range(dim):
            if all(self.board[count4 + i] == player.symbol for i in range(dim)):
                count3 = 0
                print ("Player "+player.symbol+" wins.")
                print (" -------------")
                for i in range(dim):
                    print(self.board[0 + count3 : dim + count3])
                    count3 += dim
                print (" -------------")
                self.win = True
                return (self.win, self.play)
            count4 += dim
        count4 = 0

        #Checking columns
        for i in range(dim):
            if all(self.board[count4 + i] == player.symbol for i in range(0, (dim * dim), dim)):
                count3 = 0
                print ("Player "+player.symbol+" wins.")
                print (" -------------")
                for i in range(dim):
                    print(self.board[0 + count3 : dim + count3])
                    count3 += dim
                print (" -------------")
                self.win = True
                return (self.win, self.play)
            count4 += 1
        diagonal1 = [(dim + 1) * i for i in range(dim)]
        diagonal2 = [(i + 1) * (dim - 1) for i in range(dim)]

        #Checking right diagonal
        if all(self.board[d] == player.symbol for d in diagonal1):
            print ("Player "+player.symbol+" wins.")
            count3 = 0
            print (" -------------")
            for i in range(dim):
                print(self.board[0 + count3 : dim + count3])
                count3 += dim
            print (" -------------")
            self.win = True
            return (self.win, self.play)

        #Checking left diagonal
        if all(self.board[d] == player.symbol for d in diagonal2):
            count3 = 0
            print ("Player "+player.symbol+" wins.")
            print (" -------------")
            for i in range(dim):
                print(self.board[0 + count3 : dim + count3])
                count3 += dim
            print (" -------------")
            self.win = True
            return (self.win, self.play)

        #Checking if players run out of turns
        if gameover == len(self.board):
            self.play= False
            self.display_board(board)
            return(self.win, self.play)

        self.display_board(board)
        return (self.win, self.play)

#------------------------------------------------------------------------------

class Player:
    def __init__(self, symbol):
       self.symbol= symbol


    def _interaction(self):
        player_postion=int(input ("Enter position for player "+self.symbol+": "))
        return player_postion


    def update_board(self, board, player, player_postion):
        board.board[player_postion-1]= player.symbol
        return board


    def __str__(self):
        return self.symbol

#------------------------------------------------------------------------------

class GameState:
    def __init__(self, p1, p2, board):
        self.p1 = p1
        self.p2 = p2
        self.board = board
        self.play = True
        self.win = False
        self.add_x = True
        self.add_o = True
        self.count = 0


    def turn(self, board):
        try:
            while self.play:
                self.add_x = True
                self.add_o = True

                # Player X
                while self.add_x:
                    try:
                        pl_1 = Player(self.p1.symbol)
                        player_postion_1 = pl_1._interaction()
                        if 0 < player_postion_1 <= len(self.board.board):
                            a_p1 = self.place(self.p1, board, player_postion_1)
                            self.add_x = a_p1[0]
                            self.win = a_p1[3]
                            self.play = a_p1[4]

                        else:
                            raise ValueError()
                    except:
                        print("Oops! PLease enter the position between: 1 to "+str(len(self.board.board))+".")


                if self.win==True:
                    print ("Game Over")
                    return(self.win, self.play)
                    break

                elif self.play==False:
                    print ("Game Over but no winner")
                    return(self.win, self.play)
                    break

                # Player O
                while self.add_o:
                    try:
                        pl_2 = Player(self.p2.symbol)
                        player_postion_2 = pl_2._interaction()
                        if 0 < player_postion_2 <= len(self.board.board):
                            a_p2= self.place(self.p2, board, player_postion_2)
                            self.add_o = a_p2[1]
                            self.win = a_p2[3]
                            self.play = a_p2[4]

                        else:
                            raise ValueError()
                    except:
                        print("Oops! PLease enter the position between: 1 to "+str(len(self.board.board))+".")


                if self.win==True:
                    print ("Game Over")
                    return(self.win, self.play)
                    break

                elif self.play==False:
                    print ("Game Over but no winner")
                    return(self.win, self.play)
                    break


        except:
            print("Oops! PLease enter the position between: 1 to "+str(len(self.board.board))+".")


    def place(self, player, old_board, player_postion):
        if old_board.board[player_postion-1]!="X" and old_board.board[player_postion-1]!="O":
            pl = Player(player.symbol)
            new_board = pl.update_board(old_board, player, player_postion)
            b2 = Board(new_board.board)
            self.count += 1
            if player.symbol == 'X':

                b_1 = b2.check_board(new_board, self.count, player)
                self.add_x =False
                return (self.add_x, self.add_o, self.count, b_1[0], b_1[1])
            else:

                b_2 = b2.check_board(new_board, self.count, player)
                self.add_o =False
                return (self.add_x, self.add_o, self.count, b_2[0], b_2[1])

        else:
            print ("Sorry! " +str(player_postion) + " " + "Position has been taken by Player " + old_board.board[player_postion-1]+". Please enter again.")
            return (self.add_x, self.add_o, self.count, self.win, self.play)




    def game_loop(self, grid):
            self.turn(grid)



#------------------------------------------------------------------------------

def main():
     print("\nWelcome to Naughts and Crosses game (aka Tic-Tac-Toe)!!!")
     while True:
        try:
            #Enter or quit game.
            userinput = input("Begin the game. Enter begin(Y) or quit(Q): ")
            if userinput.upper() == "Q":
                print("Game quit!")
                break
            elif userinput.upper() == "Y":
                print("The game has begun!")
                #Game Instructions
                print("\n", "INSTRUCTIONS:", "\n", "\n", "1. '*' represent empty place.",
                              "\n", "2. 'X' represent Crosses player's place.", "\n", "3. 'O' represent Naughts player's place.",
                              "\n", "4. The positions on board are row-wise; for example a 3 by 3 board has 1 to 9 postions.",
                              "\n", " - First row has 1, 2, 3 positions", "\n", " - Second row has 4, 5, 6 positions", "\n",
                              " - Third row has 7, 8, 9 positions", "\n", "5. You can select the size of playing board; example for 3 by 3, enter 3.",
                              "\n", "6. Minmum acceptable size of board is 3 by 3.")
                play = True
                while play:
                    try:


                        # Define grid : board
                        userinput_size = int(input("Enter size of playing board: "))
                        grid = []
                        if userinput_size < 3:
                            raise ValueError()
                        #Creating empty board
                        for i in range(userinput_size**2):
                            grid.append('*')


                        # Displaying empty board
                        b1 = Board(grid)
                        b1.display_board(grid)

                        # Initilizing game loop
                        p1 = Player('X')
                        p2 = Player('O')
                        play = GameState(p1, p2, b1)
                        play.game_loop(b1)
                        break

                    except:
                        print("Sorry! Please enter board size 3 or greater.")

            else:
                raise ValueError()

        except:
            print("Sorry! Please try again with either begin(Y/y) or quit(Q/q).")

main()