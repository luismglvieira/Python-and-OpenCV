# -*- coding: utf-8 -*-

class rps:
    def __init__(self, ans):
        self.__ans = ans
    
    def set_ans(self, value):
        self.__ans = value
    def get_ans(self):            
        return self.__ans
    
    def get_res(self):
        if self.get_ans() == 'rock':
            self._res = 1
        elif self.get_ans() == 'paper':
            self._res = 2
        elif self.get_ans() == 'scissor':
            self._res = 3
        else:
            self._res = 0
        return self._res

# 
class rps_res:
    def __init__(self, p1, p2):
        self.p1 = p1
#        print(self.p1)
        self.p2 = p2
#        print(self.p2)
        
    def get_res(self):
        if self.p1 == 1: #rock
            if self.p2 == 1:
                return 'tie'
            elif self.p2 == 2:
                return 'p1 loss'
            elif self.p2 == 3:
                return 'p1 win'
            else:
                return 'invalid'
        elif self.p1 == 2: #paper
            if self.p2 == 1:
                return 'p1 win'
            elif self.p2 == 2:
                return 'tie'
            elif self.p2 == 3:
                return 'p1 loss'
            else:
                return 'invalid'        
        elif self.p1 == 3: #scissor
            if self.p2 == 1:
                return 'p1 loss'
            elif self.p2 == 2:
                return 'p1 win'
            elif self.p2 == 3:
                return 'tie'
            else:
                return 'invalid'           
        else:
            return 'invalid'
        
player_1 = rps('rock')
player_2 = rps('rock')

print('Player 1: ' + str(player_1.get_ans()))
print('Player 2: ' + str(player_2.get_ans()))

result = rps_res(player_1.get_res(),player_2.get_res())
print(result.get_res())
