# Triki xde
 
import random
 
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
 
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Quieres ser X o O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def QVaPrimero():
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'oponente'
 
def JugarOtraVez():
    print('Quieres intentarlo otra vez? (si/no)')
    return input().lower().startswith('s')
 
def makeMove(board, letter, move):
    board[move] = letter
 
def Ganador(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 
 
def getBoardCopy(board):
    dupeBoard = []
 
    for i in board:
        dupeBoard.append(i)
 
    return dupeBoard
 
def EspacioLibre(board, move):
    return board[move] == ' '
 
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not EspacioLibre(board, int(move)):
        print('Cual es tu movimiento? (1-9)')
        move = input()
    return int(move)
 
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if EspacioLibre(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if EspacioLibre(copy, i):
            makeMove(copy, computerLetter, i)
            if Ganador(copy, computerLetter):
                return i
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if EspacioLibre(copy, i):
            makeMove(copy, playerLetter, i)
            if Ganador(copy, playerLetter):
                return i
 
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
  
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
def isBoardFull(board):

    for i in range(1, 10):
        if EspacioLibre(board, i):
            return False
    return True
 
 
print('Bienvenido a tres en raya!')
 
while True:

    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = QVaPrimero()
    print('EL ' + turn + ' empieza el juego.')
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
 
            if Ganador(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Muy bien, ganaste :3!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empate!')
                    break
                else:
                    turn = 'computer'
 
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
 
            if Ganador(theBoard, computerLetter):
                drawBoard(theBoard)
                print("Te gano la computadora, perdiste :c")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empate!!!!!!')
                    break
                else:
                    turn = 'player'
 
    if not JugarOtraVez():
        break
print("a.Snake")
print("b.Ping Pong")
print("c.Ahorcado")
print("d.Triki")
print("e.salir")
