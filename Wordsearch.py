import csv

def importWords():
     listOfWords = ["Binary", "Computer", "Hexadecimal", "Bander", "Powershell", "Apps", "Web Sites", "Duck", "VSC", "Poptarts"]
     return listOfWords

words = importWords()
board = []

def importBoard():
     with open('PracticeWordSearch.csv',mode='r') as file:
          boardset = csv.reader(file)
          for i in boardset:
               board.append(i)     
          
     return board

importBoard()

def printBoard(board):
     col_widths = [max(len(str(item)) for item in col) for col in zip(*board)]
     for row in board:
            print(" | ".join(f"{item:<{col_widths[i]}}" for i, item in enumerate(row)))
     pass

printBoard(board)



def searchHorizontally(listOfWords,board):
     result = []
     for i in range (len(board)):
          horizon = ''.join(board[i])
          for t in range(len(listOfWords)):
               if listOfWords[t] in horizon:
                    result.append(t)
     return result


print(searchHorizontally(words,board))


def searchVerically(words,board):
     
     item = []
     
     for i in range(len(col_widths = [max(len(str(item)) for item in col) for col in zip(*board)])):
          for t in range(len(board)):
               item.append(board[i][t])
     #item = []
     #for i in range(len(board)):
     #     item.append(board[i][1])
     #column = ''.join(item)
     #for i in words:
     #     if i in column:
     #          print(i)
     return

#def searchRightDiagonal(word,board):
#     item = []
#     for i in range(len(board)):
#          item.append(board[i][i])
#     diagnal = ''.join(item)
#     for i in word:
#          if 

     return
def searchLeftDiagonal(word,board):


     return

#wordSearchBoard=importBoard()
##Heads up, for testing, you could comment out this line and set words=your own list
#words=importWords()
#
#print(f'''
#      
#Original Board
#{printBoard(wordSearchBoard)}
#
#''')
#
##TODO:  Between these two print statements, you will run all of your searches.
#
#
#print(f'''
#      
#Answer Board
#{printBoard(wordSearchBoard)}
#
#''')