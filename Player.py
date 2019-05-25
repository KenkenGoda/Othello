#Player.py
import copy
import random
import ReverseCommon
import ReverseBoard
import Game


class Player:

    def __init__(self,color):
        self._color = color
    
    def next_move(self,board):
        pass
    
    @property
    
    def color(self):
        return self._color


class RandomAi(Player):
    
    def next_move(self,board):
        all_candidates = ReverseCommon.get_puttable_points(board,self._color)
        index = random.randint(0,len(all_candidates)-1)
        return all_candidates[index]


class NextStoneMaxAi(Player):

    def next_move(self,board):
        all_candidatess = ReverseCommon.get_puttable_points(board,self._color)
        filtered_candidates = []
        max_score = -1
        for candidates in all_candidatess:
            next_board = ReverseCommon.put_stone(board,self._color,candidates[0],candidates[1])
            score = ReverseCommon.get_score(next_board,self._color)
            if score >= max_score:
                filtered_candidates.append(candidates)
                max_score = score
        return filtered_candidates[random.randint(0,len(filtered_candidates)-1)]


class RandomAiKnowGoodMove(Player):

    def next_move(self,board):
        known_good_moves = [[0,0],[0,7],[7,0],[7,7]]
        known_bad_moves = [[0,1],[1,0],[1,1],[0,6],[1,6],[1,7],[6,0],[6,1],[7,1],[7,6],[6,7],[6,6]]
        all_candidates = ReverseCommon.get_puttable_points(board,self._color)
        good_moves = list(filter(lambda good_move:good_move in known_good_moves,all_candidates))
        if len(good_moves) > 0:
            return good_moves[random.randint(0,len(good_moves)-1)]
        not_bad_moves = list(filter(lambda not_bad_move:not_bad_move not in (known_good_moves+known_bad_moves),all_candidates))
        if len(not_bad_moves) > 0:
            return not_bad_moves[random.randint(0,len(not_bad_moves)-1)]
        return all_candidates[random.randint(0,len(all_candidates)-1)]


#class AlphaBeta(Player):

#    def next_move(self,board):
        

class Human(Player):
    
    def next_move(self,board):
        all_candidates = ReverseCommon.get_puttable_points(board,self._color)
        while True:
            try:
                if self._color:
                    color = 'Black'
                else:
                    color = 'White'
                next_move_str = input(f'{color} -> ')
                next_move_str_split = next_move_str.split(',')
                if len(next_move_str_split) == 2:
                    next_move = [int(next_move_str_split[0]),int(next_move_str_split[1])]
                    if next_move in all_candidates:
                        return next_move
                    else:
                        print("can't put there.")
            except ValueError:
                print('format error.')
