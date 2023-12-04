# Battleships - Algorithms and Data Structures Fall 2023
### By Laura Cuellar, Clara Mouzannar, Els Vaks, and Edouard Picasso 

# Gameplay Flow 
## 1. Welcome Window:
   - The game starts with a welcome window prompting the player to enter their name.
   - The player enters their name and clicks the "Start Game" button.

## 2. Ship Placement (User):
   - The main game window is initialized with two canvases for the user and the enemy.
   - The user places their ships on the grid by clicking on the user canvas.
   - Ships are placed one by one in a specific order (Aircraft Carrier, Battleship, Cruiser, Submarine, Destroyer).
   - The player selects the direction (UP, DOWN, LEFT, RIGHT) for ship placement.
   - Invalid placements are handled with temporary labels displaying error messages.
   - Once all user ships are placed, the game transitions to the battle phase.

## 3. Ship Placement (CPU):
   - The CPU places its ships on the grid using a random placement strategy.
   - The CPU avoids overlapping placements and follows the rules of ship length and direction.
   - The placement is determined by random selection until all CPU ships are placed.

## 4. Battle Phase:
   - The game enters the battle phase after both the user and CPU have placed their ships.
   - The user is prompted to click on the enemy grid to attack.
   - The user's shot results in a hit or miss, displayed on the enemy canvas.
   - The CPU takes its turn, selecting random or targeted shots based on the strategy.
   - The CPU's shot results are displayed on the user canvas.

## 5. Game End:
   - The game continues with alternating turns until either the user or CPU sinks all opponent ships.
   - The game declares the winner and displays a corresponding message.
   - The rankings are updated based on the game result (win or loss).
   - The player is given the option to view rankings or play again.

## 6. Rankings Display:
   - Player rankings are displayed in a new window.
   - Rankings include the player's name, number of plays, and number of wins.
   - The player is provided with a "Play Again" button to restart the game.

## 7. Restarting the Game:
   - If the player chooses to play again, the game restarts with ship placement and battle phases.
   - The player's name is retained, and the rankings are updated accordingly.

