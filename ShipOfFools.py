from random import randint
class Die:
    def __init__(self):
        self._value = 1
        self.roll()
    def get_value(self):
        return self._value
    def roll(self):
        self._value = randint(1, 6)
class DiceCup:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.banked = [False] * 5
    def roll(self):
        for i in range(5):
            if not self.banked[i]:
                self.dice[i].roll()
    def values(self):
        return [die.get_value() for die in self.dice]
    def bank(self, index):
        self.banked[index] = True
    def is_banked(self, index):
        return self.banked[index]
    def release(self, index):
        self.banked[index] = False
    def release_all(self):
        self.banked = [False] * 5
class ShipOfFoolsGame:
    def __init__(self):
        self.dice_cup = DiceCup()
        self.required_score = 25
        self.round_score = 0
    def round(self):
        has_ship = False
        has_captain = False
        has_crew = False
        self.round_score = 0
        self.dice_cup.release_all()
        print("\n--- New Turn ---")
        for turn in range(3):
            print(f"\nRoll {turn + 1} of 3")
            self.dice_cup.roll()
            values = self.dice_cup.values()
            print("Dice:", values)
            # Find ship (6)
            if not has_ship and 6 in values:
                index = values.index(6)
                self.dice_cup.bank(index)
                has_ship = True
                print("🚢 Ship found!")
            # Find captain (5)
            if has_ship and not has_captain and 5 in values:
                index = values.index(5)
                # Make sure this die is not already banked
                if not self.dice_cup.is_banked(index):
                    self.dice_cup.bank(index)
                    has_captain = True
                    print("👨‍✈️ Captain found!")

            # Find crew (4)
            if has_ship and has_captain and not has_crew and 4 in values:
                index = values.index(4)
                if not self.dice_cup.is_banked(index):
                    self.dice_cup.bank(index)
                    has_crew = True
                    print("👷 Crew found!")
            # Once ship, captain and crew are found
            if has_ship and has_captain and has_crew:
                print("Ship, Captain and Crew collected!")
                # Bank all dice greater than 3
                for i in range(5):
                    if values[i] > 3:
                        self.dice_cup.bank(i)
                # Ask player if they want to bank additional dice
                self.ask_to_bank(values)
            else:
                print("You still need:")
                if not has_ship:
                    print("- Ship (6)")
                if not has_captain:
                    print("- Captain (5)")
                if not has_crew:
                    print("- Crew (4)")
        # Calculate score
        if has_ship and has_captain and has_crew:
            final_values = self.dice_cup.values()
            # The 6, 5 and 4 are worth 15
            self.round_score = sum(final_values) - 15
            print("\nTurn score:", self.round_score)
        else:
            print("\nYou did not collect Ship, Captain and Crew.")
            self.round_score = 0
        self.dice_cup.release_all()
    def ask_to_bank(self, values):
        print("\nCurrent dice:", values)
        while True:
            choice = input(
                "Enter dice numbers to bank (1-5), separated by spaces, "
                "or press ENTER to continue: "
            ).strip()
            if choice == "":
                break
            try:
                indexes = [int(x) - 1 for x in choice.split()]
                valid = True
                for index in indexes:
                    if index < 0 or index >= 5:
                        valid = False
                if not valid:
                    print("Please enter numbers from 1 to 5.")
                    continue
                for index in indexes:
                    self.dice_cup.bank(index)
                print("Banked dice:", [
                    values[i] for i in range(5)
                    if self.dice_cup.is_banked(i)
                ])
                break
            except ValueError:
                print("Please enter valid numbers.")
class Player:
    def __init__(self, name):
        self.player_name = name
        self._score = 0
    def reset_score(self):
        self._score = 0
    def play_round(self, game):
        print("\n" + "=" * 40)
        print(f"{self.player_name}'s turn")
        print("=" * 40)
        game.round()
        self._score += game.round_score
        print(f"{self.player_name}'s total score: {self._score}")
class PlayRoom:
    def __init__(self):
        self.game = ShipOfFoolsGame()
        self.players = []
    def add_player(self, player):
        self.players.append(player)
    def reset_scores(self):
        for player in self.players:
            player.reset_score()
    def play_round(self):
        for player in self.players:
            # Each player gets one turn.
            # The turn itself contains 3 dice rolls.
            player.play_round(self.game)
            input("\nPress ENTER for the next player...")
    def game_finished(self):
        for player in self.players:
            if player._score >= self.game.required_score:
                return True
        return False
    def print_scores(self):
        print("\n" + "=" * 40)
        print("CURRENT SCORES")
        print("=" * 40)
        for player in self.players:
            print(f"{player.player_name}: {player._score}")
        print("=" * 40)
    def print_winner(self):
        highest_score = max(player._score for player in self.players)
        winners = [
            player for player in self.players
            if player._score == highest_score
        ]
        print("\n" + "=" * 40)
        print("GAME OVER")
        print("=" * 40)
        if len(winners) > 1:
            print("It's a draw!")
            print("Players:")
            for player in winners:
                print(f"- {player.player_name}")
            print("Score:", highest_score)
        else:
            winner = winners[0]
            print(
                f"{winner.player_name} won the game "
                f"with {winner._score} points!"
            )
def get_number_of_players():
    while True:
        try:
            number = int(input("How many players? "))
            if number >= 2:
                return number
            print("Please enter at least 2 players.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    print("=" * 40)
    print("       SHIP OF FOOLS")
    print("=" * 40)
    room = PlayRoom()
    # Ask for number of players
    number_of_players = get_number_of_players()
    # Ask for player names
    for i in range(number_of_players):
        while True:
            name = input(f"Enter name for Player {i + 1}: ").strip()
            if name:
                room.add_player(Player(name))
                break
            print("Name cannot be empty.")
    room.reset_scores()
    print("\nPlayers:")
    for player in room.players:
        print("-", player.player_name)
    input("\nPress ENTER to start the game...")
    # Continue playing until somebody reaches 25
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()