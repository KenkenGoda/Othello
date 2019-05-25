#ReverseBoard.py
import ReverseCommon

class ReverseBoard:

    def __init__(self):
        self._board = [[ReverseCommon.NONE for i in range(8)] for j in range(8)]
        self._board[3][3] = ReverseCommon.WHITE
        self._board[4][4] = ReverseCommon.WHITE
        self._board[3][4] = ReverseCommon.BLACK
        self._board[4][3] = ReverseCommon.BLACK
        self._turn = ReverseCommon.BLACK
    
    def change_turn(self):
        if self._turn == ReverseCommon.WHITE:
            self._turn = ReverseCommon.BLACK
        else:
            self._turn = ReverseCommon.WHITE
    
    def put_stone(self,color,i,j):
        self._board = ReverseCommon.put_stone(self._board,color,i,j)
        enemy = not(color)
        if len(ReverseCommon.get_puttable_points(self._board,enemy)) > 0:
            self.change_turn()
    
    def is_game_set(self):
        return ReverseCommon.is_game_set(self._board)
    
    def is_my_turn(self,color):
        if self._turn == color:
            return True
        return False
    
    @property
    
    def board(self):
        return self._board

class CustomReverseBoard(ReverseBoard):
    
    def __init__(self,board,turn):
        self._board = board
        self._turn = turn

