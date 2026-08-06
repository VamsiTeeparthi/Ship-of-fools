from random import randint
class Die():
    def __init__(self):
        self.roll()
        self._value=1
    def get_value(self):
        #Return the score
        return self._value
    def roll(self):
        #roll the dice #
        self._value= randint(1,6)
class DiceCup():
    #roll the 5 dice until they are banked
    def __init__(self):
        self.die_rool=[False,False,False,False,False]
        self.die_no1=Die()
        self.die_no2=Die()
        self.die_no3=Die()
        self.die_no4=Die()
        self.die_no5=Die()
        self.die_rools=[self.die_no1,self.die_no2,self.die_no3,self.die_no4,self.die_no5]
    def roll(self):
        for dice in self.die_rools:
            rool=self.die_rools.index(dice)
            if self.die_rool[rool]==False:
                self.die_rools[rool].roll()
    def value(self,index):
        #value of the 5 dice based on index
        return self.die_rools[index].get_value()
    def bank(self,index):
        #banking the values
        self.die_rool[index]=True
    def is_banked(self,index):
        #banking Ship,captain and crew
        if self.die_rool[index]==True:
            print('banked')
            print()
        else:
            print('not banked')
    def release(self,index):
        #release for perticular index
        self.die_rool[index]=False
    def release_all(self):
        #release all 
        for i in range(5):
            self.die_rool[i]=False

class PlayRoom():
    #checks if any player reached the required score
    def __init__(self):
        self.start_game=ShipOfFoolsGame()
        self.play_game=[]
        self.player_score=[0,0]       
    def add_player(self,player):
        #adding players
        self.player=player
        self.play_game.append(self.player)
        return self.play_game
    def reset_scores(self):
        #resets scores
        for i in range(2):
            self.play_game[i].reset_score()
    def play_round(self):
        #play a single round
        for i in range(2):
            self.play_game[i].play_round(self.start_game)
            print(self.play_game[i].player_name,":", self.play_game[i]._score)  
    def game_finished(self):
            #checks if any player reached the required score
            if max(self.player_score) >= self.start_game.required_score:
                return True
            else:
                return False
    def print_scores(self):
        #final scores
        print("scores")
        for i in range(len(self.play_game)):
            self.player_score[i]=self.play_game[i]._score
            print(self.play_game[i].player_name," :", self.play_game[i]._score)
    def print_winner(self):
        #final winner
        if self.play_game[0]._score == self.play_game[1]._score:
            print(f"This match is a draw")
        else:
            self.player_name=self.play_game[self.player_score.index(max(self.player_score))].player_name
            print(self.player_name," won the game with the score",max(self.player_score))
class ShipOfFoolsGame():
    #Game logic
    def __init__(self):
            self.Dicecup=DiceCup()
            self.required_score=25
    def round(self) :
        #Play a round
        has_ship = False
        has_captain = False
        has_crew = False
        self.crew = 0

# Repeat the loop for three times
        for round in range(3):
                self.Dicecup.roll()
                self.cup_rool=[self.Dicecup.die_no1.get_value(),self.Dicecup.die_no2.get_value(),self.Dicecup.die_no3.get_value(),self.Dicecup.die_no4.get_value(),self.Dicecup.die_no5.get_value()]
                print(self.cup_rool)
                if not has_ship and 6 in self.cup_rool:
                    self.Dicecup.bank(self.cup_rool.index(6))
                    has_ship = True
                if has_ship and not has_captain and 5 in self.cup_rool:
        # ship is banked but not captain
                    self.Dicecup.bank(self.cup_rool.index(5))
                    has_captain = True
                if has_captain and not has_crew and 4 in self.cup_rool:
        # The ship and captain are baked but the crew is not 
                    self.Dicecup.bank(self.cup_rool.index(4))
                    has_crew=True
                if has_ship and has_captain and has_crew:
        # Now we got all needed dice, and can bank the ones we like to save.   
                    for i in range(5):
                        if self.cup_rool[i]>3:
                            self.Dicecup.bank(i)
                    self.Dicecup.is_banked(self.cup_rool.index(6))
# If we have a ship, captain and crew (sum 15), 
# calculate the sum of the two remaining.
        if has_ship and has_captain and has_crew:
                self.crew = sum(self.cup_rool)-15
        self.Dicecup.release_all()

class Player():
    #play a round of a game then The gained score is accumulated in the attribute _score
    def __init__(self,real_name):
        self.player_name=real_name
        self._score=0
    def reset_score(self):
        # we can reset the score
        self._score=0
    def play_round(self,ShipOfFools):
        #play a round 
        self.game_play=ShipOfFools
        self.game_play.round()
        self._score+=self.game_play.crew

if __name__ == "__main__":
    room = PlayRoom()
    room.add_player(Player("vamsi"))
    room.add_player(Player('krishna'))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()