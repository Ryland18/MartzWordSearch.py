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
     row = []
     for i in range (len(board)):
          horizon = ''.join(board[i])
          row.append(horizon)
          for t in listOfWords:
               if t in horizon or t[::-1] in horizon:
                    start = horizon.find(t)
                    result.append(t)
                    index.append(i)
                    startingPH.append(start)
     
     return result, row, (f'{result} was found at row {index} starting at column {startingPH}')


searchHorizontally(words,board)

h= searchHorizontally(words,board)


row = h[1]


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
    
     return item, column, (f'{item} was found at column {index} starting at row {startingPV}')

R = searchVerically(words,board)

column = R[1]



searchVerically(words,board)

def searchLeftDiagonal(listOfWords,board,row, column):
     item = []
     word = []
     index = []
     group = []
     startingPDL = []
     p = 0
     print(len(row))
     
     while p != len(board):
          for j in range(len(board)):
               for i in range(len(row)):
                    if p < 1:
                         item.append(board[j][j])
                    else:
                         item.append(board[j+p - (len(column)+1)][j+p - len(row)])
               diagnal = ''.join(item)
               group.append(diagnal)
               item = []
               p+=1
     print(group)
     for i in listOfWords:
          if i in diagnal or i[::-1] in diagnal:
               word.append(i)
     print(f'{word} was found at diagnal ')
     return word
          
searchLeftDiagonal(words,board, row, column)
          
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