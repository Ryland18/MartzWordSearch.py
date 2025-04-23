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
     startingPH = []
     for i in range (len(board)):
          horizon = ''.join(board[i])
          print(horizon)
          for t in listOfWords:
               if t in horizon or t[::-1] in horizon:
                    start = horizon.find(t)
                    result.append(t)
                    index.append(i)
                    startingPH.append(start)
     print (f'{result} was found at row {index} starting at column {startingPH}')
     return result


searchHorizontally(words,board)


def searchVerically(listOfWords,board):
     item = []
     list = []
     index = []
     column = []
     startingPV=[]
     for i in range(len(board[1])):
          for t in range(len(board)):
               list.append(board[t][i])
          finallvert = ''.join(list)
          column.append(finallvert)
          list = []
     for p in listOfWords:
          for c in range(len(column)):
               if p in column[c] or p[::-1] in column[c]:
                    start = column[c].find(p)  
                    item.append(p)
                    index.append(c)
                    startingPV.append(start)
     print (f'{item} was found at column {index} starting at row {startingPV}')
     return item


searchVerically(words,board)

def searchLeftDiagonal(listOfWords,board):
     item = []
     word = []
     index = []
     group = []
     startingPDL = []
     for i in range(len(board[1])):     
          item.append(board[i][i])
     diagnal = ''.join(item)
     group.append(diagnal)
     for i in listOfWords:
          if i in diagnal or i[::-1] in diagnal:
               word.append(i) 
     print(f'{word} was found at diagnal ')
     return word
          
searchLeftDiagonal(words,board)
          
def searchRightDiagonal(word,board):


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