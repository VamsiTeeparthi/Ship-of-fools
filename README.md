# Ship of Fools - Python Dice Game

## Overview
This project is a Python-based implementation of the classic **Ship of Fools** dice game using Object-Oriented Programming (OOP) principles. It simulates a two-player game where participants roll five dice to secure a Ship, Captain, and Crew, aiming to accumulate the highest cargo score.

## Game Rules
The goal of the game is to reach a target score of **25 points** before your opponent. 

During a player's turn, they have up to **3 rolls** of five dice to achieve the following in order:
1. **Ship (6)**: Must be banked first.
2. **Captain (5)**: Can only be banked if a Ship is already secured.
3. **Crew (4)**: Can only be banked if both a Ship and Captain are secured.

Once the 6, 5, and 4 are banked, the sum of the remaining two dice represents the "Cargo" (your score for that round). If a player rolls all three required dice early, they can choose to re-roll the remaining cargo dice to try and get a higher score. If they fail to get a Ship, Captain, and Crew by the end of their 3 rolls, they score 0 for that round.

## Project Structure
The game is structured using modular classes:
* **`Die`**: Simulates a standard 6-sided die with randomized rolling mechanics.
* **`DiceCup`**: Manages a collection of 5 `Die` instances. It handles banking (saving) specific dice indices and re-rolling the unbanked ones.
* **`ShipOfFoolsGame`**: Contains the core logic for a single round of the game, including the conditional rules for banking the 6, 5, and 4.
* **`Player`**: Represents a game participant, tracking their real name and total accumulated score.
* **`PlayRoom`**: The main game controller. It adds players, manages the game loop, tracks rounds, prints scores, and determines the winner.

## How to Run
1. Ensure you have Python 3.x installed on your system.
2. Save the script to a Python file (e.g., `ship_of_fools.py`).
3. Run the script from your terminal:
   ```bash
   python ship_of_fools.py
   ```
4. By default, the script will simulate a game between two players ("vamsi" and "krishna") and output the live rolls, banked statuses, running scores, and the final winner directly in the console.
