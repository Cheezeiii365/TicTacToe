from tictactoe import GameBoard, game, aiMove, Marker
import unittest

class TestGameBoard(unittest.TestCase):

    def convertToMarker(self, initBoard):
        theBoard = [['', '', ''], ['', '', ''], ['', '', '']]
        for row in range(3):
            for column in range(3):
                if initBoard[row][column] == '-':
                    theBoard[row][column] = Marker.BLANK
                elif initBoard[row][column] == 'X':
                    theBoard[row][column] = Marker.X
                elif initBoard[row][column] == 'O':
                    theBoard[row][column] = Marker.O
        return theBoard

    # def test_waysToWin(self):
    #     initBoard = [['-', '-', '-'],
    #                 ['-', '-', '-'],
    #                 ['-', '-', '-']]
    #     testGame = GameBoard(self.convertToMarker(initBoard))
    #     actual = testGame.waysToWin(testGame.turn)
    #     # expected = (True, [[2, 0]])
    #     expected = (True, [[2, 0]])
    #     self.assertEqual(actual, expected)

    def test_corners(self):
        initBoard = [['O', 'X', '-'],
                    ['X', 'O', '-'],
                    ['X', 'O', 'X']]
        testGame = GameBoard(self.convertToMarker(initBoard))
        if testGame.turn == Marker.O:
            oppTurn = Marker.O
        else:
            oppTurn = Marker.X
        actual = testGame.corners(oppTurn)
        expected = True, [0, 2]
        self.assertEqual(actual, expected)

    def test_aiMove(self):
        initBoard = [['-', 'X', '-'],
                    ['-', '-', '-'],
                    ['-', '-', '-']]
        testGame = GameBoard(self.convertToMarker(initBoard))
        actual = aiMove(testGame)
        expected = ['1', '1']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    # game()
