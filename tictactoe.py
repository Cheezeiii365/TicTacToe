import unittest
import enum

class TestGameBoard(unittest.TestCase):

    def test_waysToWin(self):
        initBoard = [['X', '-', '-'], ['X', 'O', '-'], ['-', '-', '-']]
        testGame = GameBoard(initBoard)
        actual = testGame.waysToWin(testGame.turn)
        # expected = (True, [[2, 0]])
        expected = (None, None)
        self.assertEqual(actual, expected)

    def test_corners(self):
        initBoard = [['-', 'X', '-'], ['-', 'O', '-'], ['X', '-', '-']]
        testGame = GameBoard(initBoard)
        if testGame.turn == 'X':
            oppTurn = 'O'
        else:
            oppTurn = 'X'
        actual = testGame.corners(oppTurn)
        expected = True, [0, 2]
        self.assertEqual(actual, expected)

    def test_aiMove(self):
        initBoard = [['-', 'X', '-'], ['-', '-', '-'], ['-', '-', '-']]
        testGame = GameBoard(initBoard)
        actual = aiMove(testGame)
        expected = ['1', '1']
        self.assertEqual(actual, expected)

class Marker(enum.Enum):
    BLANK = 1
    X = 2
    O = 3

class GameBoard:
    def initNewGameBoard(self, initBoard):
        theBoard = [['', '', ''], ['', '', ''], ['', '', '']]
        for row in range(3):
            for column in range(3):
                theBoard[row][column] = Marker.BLANK

        self.board = theBoard
        self.turn = Marker.X
        self.turnCount = 0

    def initInProgressGame(self, initBoard):
        self.board = initBoard
        initCountX = 0
        initCountO = 0
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == Maker.X:
                    initCountX += 1
                elif self.board[row][column] == Marker.O:
                    initCountO += 1
        if initCountX == initCountO:
            self.turn = Marker.X
        else:
            self.turn = Marker.O

        self.turnCount = initCountX + initCountO

    def __init__(self, initBoard):
        if initBoard == None:
            self.initNewGameBoard(initBoard)
        else:
            self.initInProgressGame(initBoard)

    def intToMove(self, strInputMove):
        inputMove = int(strInputMove)
        if inputMove == 1:
            return ['2', '0']
        elif inputMove == 2:
            return ['2', '1']
        elif inputMove == 3:
            return ['2', '2']
        elif inputMove == 4:
            return ['1', '0']
        elif inputMove == 5:
            return ['1', '1']
        elif inputMove == 6:
            return ['1', '2']
        elif inputMove == 7:
            return ['0', '0']
        elif inputMove == 8:
            return ['0', '1']
        elif inputMove == 9:
            return ['0', '2']

    def printOutConverter(self, mark):
        if mark == Marker.BLANK:
            return '-'
        elif mark == Marker.X:
            return 'X'
        elif mark == Marker.O:
            return 'O'

    def printBoard(self):
        for i in range(3):
            print(self.printOutConverter(self.board[i][0]), self.printOutConverter(self.board[i][1]), self.printOutConverter(self.board[i][2]))

    def waysToWin(self, player):
        # print('in ways to win')
        winningMoves = []
        diagU = [self.board[0][2], self.board[1][1], self.board[2][0]]
        diagD = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if diagD.count(player) == 2 and diagD.count(Marker.BLANK) == 1:
            for cell in range(3):
                if diagD[cell] == Marker.BLANK:
                    winningMoves.append([cell, cell])
        if diagU.count(player) == 2 and diagU.count(Marker.BLANK) == 1:
            for cell in range(3):
                if diagU[cell] == Marker.BLANK:
                    winningMoves.append([cell, (2 - cell)])
        for i in range(3):
            row = self.board[i]
            column = [self.board[0][i], self.board[1][i], self.board[2][i]]
            # print('P:', row.count(player), ' -: ', row.count('-'))
            # print(i, ' ', row, ' ',column)
            # print(self.board)
            if row.count(player) == 2 and row.count(Marker.BLANK) == 1:
                for cell in range(3):
                    if row[cell] == Marker.BLANK:
                        winningMoves.append([i, cell])
            if column.count(player) == 2 and column.count(Marker.BLANK) == 1:
                for cell in range(3):
                    if column[cell] == Marker.BLANK:
                        winningMoves.append([cell, i])
        # print(winningMoves)
        # print(player)
        if len(winningMoves) > 0:
            return True, winningMoves

        else:
            return None, None

    def findForks(self, player):
        # print('finding forks')
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == Marker.BLANK:
                    self.board[row][column] = player
                    canWin, winningMoves = self.waysToWin(player)
                    forkMove = [row, column]
                else:
                    # self.board[row][column] = '-'
                    continue
                if canWin and len(winningMoves) == 2:
                    # print(winningMoves)
                    # print(forkMove)
                    self.board[row][column] = Marker.BLANK
                    return True, forkMove
                else:
                    self.board[row][column] = Marker.BLANK
        return None, None

    def corners(self, player):
        opposingCornersU = [self.board[2][0], self.board[0][2]]
        opposingCornersD = [self.board[0][0], self.board[2][2]]
        if opposingCornersU[0] == player and opposingCornersU[1] == Marker.BLANK:
            return True, [0, 2]
        elif opposingCornersU[1] == player and opposingCornersU[0] == Marker.BLANK:
            return True, [2, 0]
        elif opposingCornersD[0] == player and opposingCornersD[1] == Marker.BLANK:
            return True, [2, 2]
        elif opposingCornersD[1] == player and opposingCornersD[0] == Marker.BLANK:
            return True, [0, 0]
        else:
            return None, None

    def testForWin(self):
        # print('testing for win')
        gameOver = False
        for players in range(2):
            if players == 0:
                player = Marker.X
            else:
                player = Marker.O
            # print(gameOver, players, player)
            diagU = [self.board[0][2], self.board[1][1], self.board[2][0]]
            diagD = [self.board[0][0], self.board[1][1], self.board[2][2]]
            if diagD.count(player) == 3:
                gameOver = True
            if diagU.count(player) == 3:
                gameOver = True
            for i in range(3):
                row = self.board[i]
                column = [self.board[0][i], self.board[1][i], self.board[2][i]]
                if row.count(player) == 3:
                    gameOver = True
                if column.count(player) == 3:
                    gameOver = True
            if gameOver:
                return True, player
        return None, None

    def validateMove(self, move):
        if self.board[int(move[0])][int(move[1])] == Marker.BLANK:
            return True

    def updateBoard(self, move):
        if self.validateMove(move):
            self.board[int(move[0])][int(move[1])] = self.turn
            self.turnCount += 1
            return True
        else:
            return False


def aiMove(board):
    if board.turn == Marker.X:
        oppTurn = Marker.O
    else:
        oppTurn = Marker.X

    # moveBoard = GameBoard()
    # oppMoveBoard = GameBoard()
    forkBoard = GameBoard(None)
    forkBoard = board

    canWin, winningMoves = board.waysToWin(board.turn)
    canBlock, blockMoves = board.waysToWin(oppTurn)
    canFork, forkMove = forkBoard.findForks(board.turn)
    canBlockFork, blockForkMove = forkBoard.findForks(oppTurn)
    corner, cornerMove = board.corners(oppTurn)
    # print(corner, cornerMove)

    if canWin:
        # print('Winning')
        return winningMoves[0]
    elif canBlock:
        # print('Blocking')
        return blockMoves[0]
    elif canFork:
        # print('Forking')
        return forkMove
    elif canBlockFork:
        # print('Blocking fork')
        return blockForkMove
    elif board.board[1][1] == Marker.BLANK:
        return ['1', '1']
    elif corner:
        # print('Opposite corner')
        return cornerMove
    elif board.board[0][1] == Marker.BLANK:
        return ['0', '1']
    elif board.board[0][2] == Marker.BLANK:
        return ['0', '2']
    elif board.board[2][0] == Marker.BLANK:
        return ['2', '0']
    elif board.board[2][2] == Marker.BLANK:
        return ['2', '2']
    elif board.board[0][1] == Marker.BLANK:
        return ['0', '1']
    elif board.board[1][0] == Marker.BLANK:
        return ['1', '0']
    elif board.board[1][2] == Marker.BLANK:
        return ['1', '2']
    elif board.board[2][1] == Marker.BLANK:
        return ['2', '1']

def game():
    gameBoard = GameBoard(None)

    # intro
    print('\n===============================')
    print('TicTacToe play against computer')
    print('===============================\n')
    print('Board indexes:')
    print('7 8 9')
    print('4 5 6')
    print('1 2 3')
    print('\n')

    # game
    while gameBoard.turnCount < 9:
        # print(turnCount)
        gameBoard.printBoard()
        print('Its your turn, ', gameBoard.printOutConverter(gameBoard.turn), '. Move to which place?' )

        if gameBoard.turn == Marker.X:
            playerMove = input()
            move = gameBoard.intToMove(playerMove)
        else:
            move = aiMove(gameBoard)

        if not gameBoard.updateBoard(move):
            print("That place is already filled.\nMove to which place?")
            continue

        if gameBoard.turnCount > 0:
            gameOver, winner = gameBoard.testForWin()
            # print(gameOver)
            if gameOver:
                print('\n==========')
                print('Game Over.')
                print('==========\n')
                gameBoard.printBoard()
                print("\n **** " + winner.name+ " won. ****")
                break

        if gameBoard.turnCount == 9:
            print('\n==========')
            print('Game Over.')
            print('==========\n')
            gameBoard.printBoard()
            print("\nIt's a Tie!")

        # change player
        if gameBoard.turn == Marker.X:
            gameBoard.turn = Marker.O
            # notTurn = 'X'
        else:
            gameBoard.turn = Marker.X
            # notTurn = 'O'



# Start
if __name__ == '__main__':
    # unittest.main()
    game()
