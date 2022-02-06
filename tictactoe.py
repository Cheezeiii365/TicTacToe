# gameBoard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

class GameBoard:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.turn = 'X'
        self.turnCount = 0

    def printBoard(self):
        for i in range(3):
            print(self.board[i][0], self.board[i][1], self.board[i][2])

    def waysToWin(self, player):
        # print('in ways to win')
        winningMoves = []
        diagU = [self.board[0][2], self.board[1][1], self.board[2][0]]
        diagD = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if diagD.count(player) == 2 and diagD.count('-') == 1:
            for cell in range(3):
                if diagD[cell] == '-':
                    winningMoves.append([cell, cell])
        if diagU.count(player) == 2 and diagU.count('-') == 1:
            for cell in range(3):
                if diagU[cell] == '-':
                    winningMoves.append([cell, (2 - cell)])
        for i in range(3):
            row = self.board[i]
            column = [self.board[0][i], self.board[1][i], self.board[2][i]]
            # print('P:', row.count(player), ' -: ', row.count('-'))
            # print(i, ' ', row, ' ',column)
            # print(self.board)
            if row.count(player) == 2 and row.count('-') == 1:
                for cell in range(3):
                    if row[cell] == '-':
                        winningMoves.append([i, cell])
            if column.count(player) == 2 and column.count('-') == 1:
                for cell in range(3):
                    if column[cell] == '-':
                        winningMoves.append([cell, i])
        # print(winningMoves)
        # print(player)
        if len(winningMoves) > 0:
            return True, winningMoves

        else:
            return None, winningMoves

    def findForks(self, player):
        # print('finding forks')
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == '-':
                    self.board[row][column] = player
                    canWin, winningMoves = self.waysToWin(player)
                    forkMove = [row, column]
                else:
                    # self.board[row][column] = '-'
                    continue
                if canWin and len(winningMoves) == 2:
                    # print(winningMoves)
                    # print(forkMove)
                    self.board[row][column] = '-'
                    return True, forkMove
                else:
                    self.board[row][column] = '-'
        return None, None

    def testForWin(self):
        # print('testing for win')
        gameOver = False
        for players in range(2):
            if players == 0:
                player = 'X'
            else:
                player = 'O'
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
        if self.board[int(move[0])][int(move[1])] == '-':
            return True

    def updateBoard(self, move):
        if self.validateMove(move):
            self.board[int(move[0])][int(move[1])] = self.turn
            self.turnCount += 1
            return True
        else:
            return False


def aiMove(board):
    if board.turn == 'X':
        oppTurn = 'O'
    else:
        oppTurn = 'X'

    # moveBoard = GameBoard()
    # oppMoveBoard = GameBoard()
    forkBoard = GameBoard()
    forkBoard = board

    canWin, winningMoves = board.waysToWin(board.turn)
    canBlock, blockMoves = board.waysToWin(oppTurn)
    canFork, forkMove = forkBoard.findForks(board.turn)
    canBlockFork, blockForkMove = forkBoard.findForks(oppTurn)

    if canWin:
        return winningMoves[0]
    elif canBlock:
        return blockMoves[0]
    elif canFork:
        return forkMove
    elif canBlockFork:
        return blockForkMove
    elif board.board[1][1] == '-':
        return ['1', '1']
    elif board.board[0][1] == '-':
        return ['0', '1']
    elif board.board[0][2] == '-':
        return ['0', '2']
    elif board.board[2][0] == '-':
        return ['2', '0']
    elif board.board[2][2] == '-':
        return ['2', '2']
    elif board.board[0][1] == '-':
        return ['0', '1']
    elif board.board[1][0] == '-':
        return ['1', '0']
    elif board.board[1][2] == '-':
        return ['1', '2']
    elif board.board[2][1] == '-':
        return ['2', '1']

def game():
    gameBoard = GameBoard()

    while gameBoard.turnCount < 9:
        # print(turnCount)
        gameBoard.printBoard()
        print('Its your turn, ', gameBoard.turn, '. Move to which place?' )

        if gameBoard.turn == 'X':
            move = [char for char in input()]
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
                print("\n **** " + winner + " won. ****")
                break

        if gameBoard.turnCount == 9:
            print('\n==========')
            print('Game Over.')
            print('==========\n')
            gameBoard.printBoard()
            print("\nIt's a Tie!!")

        # change player
        if gameBoard.turn == 'X':
            gameBoard.turn = 'O'
            # notTurn = 'X'
        else:
            gameBoard.turn = 'X'
            # notTurn = 'O'
if __name__ == '__main__':
    game()