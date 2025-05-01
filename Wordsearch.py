import csv

def importWords():
     
     listOfWords = ["BINARY", "COMPUTER", "HEXADECIMAL", "BANDER", "POWERSHELL", "APPS", "WEBSITES", "DUCK", "VSC", "POPTARTS"]
     
     
     return listOfWords


def findEndOfWord(word,start):
     end = start + len(word) -1
     return end

def findRevEndOfWord(word,start,item):
     if start <= -1:
          start = start + len(item)
          end = start - len(word) +1
     else:
          end = start - len(word) +1

     return end

def chechRev(start,item):
     if start <= -1:
          start = start + len(item)
     else:
          pass
     return start


def findRows(columns, item):
     row = columns - item +1
     
     return row

def revfindRows(columns, item):
     row = columns - item
     
     return row

def findTrueLoc(item,part):
     start = item - part
     return start


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
     #made my co-piolet
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
     ending = []
     for i in range (len(board)):
          horizon = ''.join(board[i])
          row.append(horizon)
          for t in listOfWords:
               if t in horizon:
                    start = horizon.find(t)
                    end = findEndOfWord(t,start)
                    ending.append(end)  
                    result.append(t)
                    index.append(i)
                    startingPH.append(start)
               elif t[::-1] in horizon:
                    part = horizon.find(t)
                    end = findRevEndOfWord(t,part,horizon)
                    start = chechRev(part,horizon)
                    ending.append(end)  
                    result.append(t)
                    index.append(i)
                    startingPH.append(start)
               #else:
               #     print("no words on the horizontal axis")
     
     return result, row,(f'{result} was found at row {index} starting at column {startingPH} and ends at column {ending}')


searchHorizontally(words,board)

h= searchHorizontally(words,board)


row = h[1]


def searchVerically(listOfWords,board):
     item = []
     list = []
     index = []
     column = []
     ending =[]
     startingPV=[]
     for i in range(len(board[1])):
          for t in range(len(board)):
               list.append(board[t][i])
          finallvert = ''.join(list)
          column.append(finallvert)
          list = []
     for p in listOfWords:
          for c in range(len(column)):
               if p in column[c]:
                    start = column[c].find(p)
                    end = findEndOfWord(p,start)
                    ending.append(end)  
                    item.append(p)
                    index.append(c)
                    startingPV.append(start)
               elif p[::-1] in column[c]:
                    part = column[c].find(p)
                    end = findRevEndOfWord(p,part,column[c])
                    start = chechRev(part,column[c])
                    ending.append(end)  
                    item.append(p)
                    index.append(c)
                    startingPV.append(start)
               #else:
               #     print("no words in the vertical axis")
     return item, column, (f'{item} was found at column {index} starting at row {startingPV} and ends at row {ending}')

R = searchVerically(words,board)

column = R[1]









searchVerically(words,board)

def searchLeftDiagonal(listOfWords,board,row, column):
     Tgroup = []
     Tword = []
     diagnalLeft = []
     diagnalDown = []
     length = len(row[0])
     rowlength = len(row[0])
     Tending = []
     TStarting = []
     Tcolumns = []
     Bcolumns = []
     Bending = []
     Bstarting = []
     Bword = []
     Bgroup = []
     column = len(column[0])
     for r in range(length):
          line = ""
          columline = ""
          for c in range(length):
               if r>=11 or c>=11:
                    break
               #print(f"{c}{r}",end=" ")
               
               #row = int(word[0])
               #column = int(word[1])
               lright = board[c][r]
               ldown = board[r][c]
               columline +=ldown
               line+=lright
               r+=1
               c+=1
          diagnalLeft.append(line)
          diagnalDown.append(columline)
     for i in listOfWords:
          for d in range(len(diagnalLeft)):
               if i in diagnalLeft[d]:
                    start = diagnalLeft[d].find(i)
                    end = findEndOfWord(i,start)
                    Tending.append(end)  
                    Tword.append(i)
                    if d == 0:
                         Tcolumns.append(end)
                    else:
                         Tcolumns.append(findRows(len(diagnalLeft[d]),len(i)))
                    Tgroup.append(d)
                    TStarting.append(start)
               elif i[::-1] in diagnalLeft[d]:
                    part = diagnalLeft[d].find(i)
                    end = findRevEndOfWord(i,part,diagnalLeft[d])
                    start = chechRev(part,diagnalLeft[d])
                    Tending.append(end)  
                    Tword.append(i)
                    Tgroup.append(d)
                    Tcolumns.append(revfindRows(column, len(diagnalLeft[d])))
                    TStarting.append(start)
          for l in range(len(diagnalDown)):
               if i in diagnalDown[l]:
                    start = diagnalDown[l].find(i)
                    end = findEndOfWord(i,start)
                    Bending.append(end)  
                    Bword.append(i)
                    if l == 0:
                         Bcolumns.append(end)
                    else:
                         Bcolumns.append(findRows(len(diagnalDown[l]),len(i)))
                    Bgroup.append(l)
                    Bstarting.append(start)
               elif i[::-1] in diagnalDown[l]:
                    part = diagnalDown[d].find(i)
                    end = findRevEndOfWord(i,part,diagnalDown[l])
                    start = chechRev(part,diagnalDown[l])
                    Bending.append(end)  
                    Bword.append(i)
                    Bgroup.append(l)
                    Bcolumns.append(revfindRows(column, len(diagnalDown[l])))
                    Bstarting.append(start)
               #else:
               #     print("no words found in set of diagnals")
     
     return #print(f"{Tword} found at diagnals that starts from right to left {Tgroup} starting at row {TStarting} and ends at row {Tending} and column {Tcolumns}"), print(f"{Bword} found at diagnals that starts from top of column 0 to bottom {Bgroup} starting at row {Bstarting} and ends at row {Bending} and column {Bcolumns}")
     
     

     #print(f'{word} was found at diagnal ')
     return
          
searchLeftDiagonal(words,board, row, column)
          
          
def searchRightDiagonal(listOfWords,board,row,column):
     Tgroup = []
     Tword = []
     diagnalRight = []
     diagnalDown = []
     length = len(column[0])
     rowlength = len(row[0])
     Tending = []
     TStarting = []
     Tcolumns = []
     Bcolumns = []
     Bending = []
     Bstarting = []
     Bword = []
     Bgroup = []
     column = len(column[0])
     for r in reversed(range(length)):
          line = ""
          columline = ""
          for c in reversed(range(length)):
               if r>=11 or c>=11:
                    break
               #print(f"{c}{r}",end=" ")
               
               #row = int(word[0])
               #column = int(word[1])
               lright = board[c][r]
               ldown = board[-(c+1)][-(r+1)]
               columline +=ldown
               line+=lright
               r+=1
               c+=1
          diagnalDown.append(line)
          diagnalRight.append(columline)
          print(diagnalRight)
     for i in listOfWords:
          for d in range(len(diagnalRight)):
               if i in diagnalRight[d]:
                    part = diagnalRight[d].find(i)
                    end = findEndOfWord(i,part)
                    Tending.append(end)  
                    Tword.append(i)
                    if d == 0:
                         Tcolumns.append(end)
                    else:
                         Tcolumns.append(findRows(len(diagnalRight[d]),len(i)))
                    Tgroup.append(findTrueLoc(len(diagnalRight[-1]),(len(diagnalRight[d]))))
                    TStarting.append(part)
               elif i[::-1] in diagnalRight[d]:
                    part = diagnalRight[d].find(i)
                    end = findRevEndOfWord(i,part,diagnalRight[d])
                    start = chechRev(part,diagnalRight[d])
                    Tending.append(end)  
                    Tword.append(i)
                    Tgroup.append(findTrueLoc(len(diagnalRight[-1]),(len(diagnalRight[d]))))
                    Tcolumns.append(revfindRows(column, len(diagnalRight[d])))
                    TStarting.append(start)
               #elif not i in diagnalRight[d] or not i[::-1] in diagnalRight[d]:
               #     return print("no words in set of diagnals")
          for l in range(len(diagnalDown)):
               if i in diagnalDown[l]:
                    start = diagnalDown[l].find(i)
                    end = findEndOfWord(i,start)
                    Bending.append(end)  
                    Bword.append(i)
                    if l == 0:
                         Bcolumns.append(end)
                    else:
                         Bcolumns.append(findRows(len(diagnalDown[l]),len(i)))
                    Bgroup.append(l)
                    Bstarting.append(start)
               elif i[::-1] in diagnalDown[l]:
                    part = diagnalDown[d].find(i)
                    end = findRevEndOfWord(i,part,diagnalDown[l])
                    start = chechRev(part,diagnalDown[l])
                    Bending.append(end)  
                    Bword.append(i)
                    Bgroup.append(l)
                    Bcolumns.append(revfindRows(column, len(diagnalDown[l])))
                    Bstarting.append(start)
               #else:
                    #return print("no words found in set of diagnals")

     return print(f"{Tword} found at diagnals that starts from right to left {Tgroup} starting at row {TStarting} and ends at row {Tending} and column {Tcolumns}"), print(f"{Bword} found at diagnals that starts from top of column 0 to bottom {Bgroup} starting at row {Bstarting} and ends at row {Bending} and column {Bcolumns}")

searchRightDiagonal(words,board, row, column)

     
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