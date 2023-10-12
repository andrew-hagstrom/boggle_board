import random
import string

class BoggleBoard:
  
  def __init__(self):
    self.board = [['_', '_', '_', '_',], 
                  ['_', '_', '_', '_',],
                  ['_', '_', '_', '_',],
                  ['_', '_', '_', '_',]]
  
  def empty(self):
    for i in self.board:
      print(i)
    # print(self.board)

  def shake(self):
    dice_list =["AAEEGN", "ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTU","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ","DEILRX"]
    for i in range(4):
      for j in range (4):
        # print([i][j])
        # self.board[i][j] = random.choice(string.ascii_uppercase)
        chosen_dice = random.choice(dice_list)
        print(chosen_dice)
        chosen_letter = random.choice(chosen_dice)
        print(chosen_letter)
        if chosen_letter == "Q":
          chosen_letter = "Qu"
        # else:
        self.board[i][j] = chosen_letter
        print(self.board)        
    for i in self.board:
      print(i)
# BoggleBoard(row, column)
# # board.shake()

# print(BoggleBoard(row, column))
board = BoggleBoard()

board.empty()
board.shake()

