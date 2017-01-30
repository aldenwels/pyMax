import random
col = 8
row = 8

def init():
  for i in range(col):
    for j in range(row):
      board[i][j] = random.getrandbits(1)
  return board

def printState(board):
  print ("\n")
  print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in board]))


def generate(board):
  hold = board
  next = [[0 for x in range(col)] for y in range(row)]
  for x in range(col):
    for y in range(row):
      neighbors = 0
      for i in range(-1,1):
        for j in range(-1,1):
          neighbors += hold[x+i][y+j]
      

      if((board[x][y] == 1) & (neighbors <  2)):
        next[x][y] = 0;         
      elif((board[x][y] == 1) & (neighbors >  3)):
        next[x][y] = 0;        
      elif ((board[x][y] == 0) & (neighbors == 3)):
        next[x][y] = 1;          
      else:                                         
        next[x][y] = hold[x][y];
  return next 


def main():
  board = [[0 for x in range(col)] for y in range(row)]
  for i in range(col):
    for j in range(row):
      board[i][j] = random.getrandbits(1)
  printState(board)
  for i in range(5):
    board = generate(board)
    printState(board)


  

  


if __name__ == '__main__':
  main()

