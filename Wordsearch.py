import csv

def importWords():
     listOfWords = ["BINARY", "COMPUTER", "HEXADECIMAL", "BANDER", "POWERSHELL", "APPS", "WEBSITES", "DUCK", "VSC", "POPTARTS"]
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
     index = []
     for i in range (len(board)):
          horizon = ''.join(board[i])
          print(horizon)
          for t in listOfWords:
               if t in horizon:
                    result.append(t)
                    index.append(i)
     print (f'{result} was found at row {index}')
     return result


searchHorizontally(words,board)


def searchVerically(listOfWords,board):
     item = []
     list = []
     index = []
     column = []
     for i in range(len(board[1])):
          for t in range(len(board)):
               list.append(board[t][i])
          finallvert = ''.join(list)
          column.append(finallvert)
          list = []
     for p in listOfWords:
          for c in range(len(column)):
               if p in column[c]:
                    item.append(p)
                    index.append(c)
     print (f'{item} was found at row {index}')
     return item


searchVerically(words,board)

#def searchRightDiagonal(word,board):
#     item = []
#        for i in range(len(board[1])):
          #list.append(board[i][0+i])
#     diagnal = ''.join(item)
#     for i in word:
#          if 

     #return
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