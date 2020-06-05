# -*- coding: utf-8 -*-

class rps:
    def __init__(self, ans):
        self.__ans = ans
    
    def set_ans(self, value):
        self.__ans = value
    def get_ans(self):            
        return self.__ans
    
    def get_res(self):
        if self.get_ans() == 'r':   # rock
            self._res = 1
        elif self.get_ans() == 'p': # paper
            self._res = 2
        elif self.get_ans() == 's': # scissor
            self._res = 3
        else:
            self._res = 0
        return self._res
    
    def get_string(self):
        if self.get_ans() == 'r':   # rock
            return 'rock'
        elif self.get_ans() == 'p': # paper
            return 'paper'
        elif self.get_ans() == 's': # scissor
            return 'scissors'
        else:
            return 'invalid'
# 
class rps_res:
    def __init__(self, p1, p2):
        self.p1 = p1 # values of 1, 2 or 3. Zero if input from player is wrong.
        self.p2 = p2
        
    def get_res(self):
        if self.p1 == 1: #rock
            if self.p2 == 1:
                return "It's a tie."
            elif self.p2 == 2:
                return 'Player 2 wins.'
            elif self.p2 == 3:
                return 'Player 1 wins.'
            else:
                return 'Invalid result.'
            
        elif self.p1 == 2: #paper
            if self.p2 == 1:
                return 'Player 1 wins.'
            elif self.p2 == 2:
                return "It's a tie."
            elif self.p2 == 3:
                return 'Player 2 wins.'
            else:
                return 'Invalid result.'
            
        elif self.p1 == 3: #scissor
            if self.p2 == 1:
                return 'Player 2 wins.'
            elif self.p2 == 2:
                return 'Player 1 wins.'
            elif self.p2 == 3:
                return "It's a tie."
            else:
                return 'Invalid result.'

        else:
            return 'Invalid result.'

   
player_1 = rps(str.lower(input("Player 1: Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")))
player_2 = rps(str.lower(input("Player 2: Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")))

print()
print('Player 1: ' + str(player_1.get_string()))
print('Player 2: ' + str(player_2.get_string()))
print()
result = rps_res(player_1.get_res(),player_2.get_res())
print(result.get_res())
