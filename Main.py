#Main.py
import ReverseBoard
import Player
import ReverseCommon
import Game

if __name__ == '__main__':
    black_win = 0
    white_win = 0
    times = 1
    output = True
    for i in range(times):
        reverse_board = ReverseBoard.ReverseBoard()
        black_player = Player.Human(ReverseCommon.BLACK)
        #black_player = Player.RandomAiKnowGoodMove(ReverseCommon.BLACK)
        white_player = Player.Human(ReverseCommon.WHITE)
        #white_player = Player.RandomAiKnowGoodMove(ReverseCommon.WHITE)
        game = Game.Game(black_player,white_player,reverse_board)
        game.play(output)
        if game.get_winner(times) == black_player:
            black_win += 1
            if times==1:
                print('[ Winner ]\nBlack')
        else:
            white_win += 1
            if times==1:
                print('[ Winner ]\nWhite')
    print('[ Total Wins ]')
    print(f'Black: {black_win}, White: {white_win}')
