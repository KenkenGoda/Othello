#Game.py
import ReverseCommon

class Game:

    def __init__(self,player1,player2,reverse_board):
        self._player1 = player1
        self._player2 = player2
        self._reverse_board = reverse_board
    
    def play(self,output_board):
        if output_board:
            ReverseCommon.print_board(self._reverse_board.board)
        while True:
            if self._reverse_board.is_game_set():
                break
            if self._reverse_board.is_my_turn(self._player1.color):
                next_move = self._player1.next_move(self._reverse_board.board)
                self._reverse_board.put_stone(self._player1.color,next_move[0],next_move[1])
                if output_board:
                    ReverseCommon.print_board(self._reverse_board.board)
            if self._reverse_board.is_game_set():
                break
            if self._reverse_board.is_my_turn(self._player2.color):
                next_move = self._player2.next_move(self._reverse_board.board)
                self._reverse_board.put_stone(self._player2.color,next_move[0],next_move[1])
                if output_board:
                    ReverseCommon.print_board(self._reverse_board.board)
    
    def get_winner(self, times):
        player1_score = ReverseCommon.get_score(self._reverse_board.board,self._player1.color)
        player2_score = ReverseCommon.get_score(self._reverse_board.board,self._player2.color)
        if times==1:
            print('[ Number of Stones ]')
            print(f'Black: {player1_score}, White: {player2_score}')
        if player1_score > player2_score:
            return self._player1
        else:
            return self._player2

