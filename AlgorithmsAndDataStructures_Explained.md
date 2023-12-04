# Battleships Algorithms and Data Structures
## Below you will find a more in-depth look at the algorithms and data structures that we chose to implement our game. 

### GREEDY ALGORITHM - CPU Hit System using probability and game logic
 ** clara and edou work here

### BACKTRACKING AND RECURSION - CPU Ship Placing Functionality
The CPU ship placement algorithm in the Battleships game employs a strategic backtracking and recursion approach to ensure a dynamic and changing placement of the CPUs ships on the board.

1. **Base Case**

-   If there are no more ships to place (not ships_to_place), the algorithm returns True, indicating successful placement.

2. **Randomization**

-   Randomly select the orientation (horizontal or vertical) for the current ship.

-   Randomly choose coordinates (x, y) on the game board.

3. **Recursive Calls**

-   If the selected position is valid for placing the ship, update the game board and proceed to the next ship.

-   Recursively call the place_ships function for the remaining ships.

4. **Backtracking**

-   If the recursive calls fail (indicating an invalid placement), the algorithm backtracks by removing the last placed ship by calling remove_ship and exploring alternative positions.

-   This process repeats until a valid placement for all ships is found.

5. **Helper Functions**

-   can_place_ship: Checks if a ship can be placed at a given position.

-   place_ship: Updates the game board with the placement of a ship.

-   remove_ship: Backtracks by removing a previously placed ship from the game board.

-   all_ships_placed: Checks if all ships are successfully placed on the game board.

### MERGE SORT - key aspect of our ranking system

We used this divide-and-conquer sorting algorithm by recursively dividing the player list into smaller halves until each subarray has only one sorted element. Then, it merges these sorted subarrays back together in a way that ensures the final merged array is sorted. The function is defined under the Rankings class. 

1. **Base Case:**
   - If the length of the `player_list` is greater than 1, the algorithm proceeds; otherwise, it considers the list already sorted.

2. **Divide:**
   - Find the middle index of the `player_list` (using integer division), creating two subarrays: `left_half` and `right_half`.

3. **Recursive Calls:**
   - Recursively apply the `merge_sort` function to both `left_half` and `right_half`. This step continues until the base case is reached for each subarray.

4. **Merge:**
   - Merge the sorted `left_half` and `right_half` back into the original `player_list`.
   - Initialize three indices: `i` for `left_half`, `j` for `right_half`, and `k` for the merged list.

5. **Comparisons and Merging:**
   - Compare the values at indices `i` and `j` in `left_half` and `right_half`, respectively.
   - If the element in `left_half` is greater, it is placed in the merged array at index `k`, and `i` is incremented.
   - If the element in `right_half` is greater or equal, it is placed in the merged array at index `k`, and `j` is incremented.
   - Increment `k` after placing an element in the merged array.

6. **Remaining Elements:**
   - After the above loop, one of the subarrays (`left_half` or `right_half`) may still have remaining elements.
   - Copy the remaining elements from both subarrays to the merged array.

The end result is that the `player_list` is now sorted based on the value of `['wins']` in the sub-dictionaries. The merging step ensures that the smaller sorted arrays are combined in a way that maintains overall order. This process is repeated until the entire list is sorted.
 
 **Code: (found in Rankings.py)**

       def merge_sort(self, player_list):    
           if len(player_list) > 1:
               mid = len(player_list) // 2
               left_half = player_list[:mid]
               right_half = player_list[mid:]
               self.merge_sort(left_half)
               self.merge_sort(right_half)
       
               i = j = k = 0
       
               while i < len(left_half) and j < len(right_half):
                   if left_half[i][1]['wins'] > right_half[j][1]['wins']:
                       player_list[k] = left_half[i]
                       i += 1
                   else:
                       player_list[k] = right_half[j]
                       j += 1
                   k += 1
       
               while i < len(left_half):
                   player_list[k] = left_half[i]
                   i += 1
                   k += 1
       
               while j < len(right_half):
                   player_list[k] = right_half[j]
                   j += 1
                   k += 1


### QUEUES - Used for User Ship Placement and Managing CPU hit Directions

**CPU HIT MANGAGEMENT**

In our game, queues are used for managing hit directions in the `CPU_Player` class. Specifically, the `hit_directions` attribute is defined as a `deque` (double-ended queue) from the `collections` module. Here's a breakdown of how queues are used in the code:

1. **Initialization:**
   - `self.hit_directions = deque()`: This line initializes an empty deque (`hit_directions`) that will be used to store the hit directions.

2. **Adding Hit Directions:**
   - The `determine_hit_directions` method is responsible for determining the possible hit directions for the CPU player to continue targeting a ship.
   - It iterates through possible directions and appends valid directions to the `hit_directions` deque.

3. **Switching Hit Direction:**
   - The `switch_hit_direction` method is called when a miss occurs, and the CPU player needs to switch to another hit direction.
   - It uses `popleft()` to remove the leftmost (oldest) direction from the deque. If there are no more directions, it means the CPU has exhausted all possible directions, and the `reset_target_mode` method is called.

4. **Choosing Shot:**
   - The `choose_shot` method is responsible for choosing the next shot based on the current targeting mode or taking a random shot if not in target mode.
   - If the CPU is in target mode (`self.target_mode` is `True`), it uses the hit directions deque to determine the next shot direction.

5. **Resetting Target Mode:**
   - The `reset_target_mode` method is called when the CPU needs to reset the target mode, clearing hit information, and preparing for a new round.

In summary, the deque (`hit_directions`) is used as a stack to manage hit directions during the targeting phase. It allows the CPU player to keep track of possible directions to target a ship and efficiently switch between directions when needed. Deques are advantageous for this purpose due to their O(1) append and pop operations from both ends.

**USER SHIP PLACEMENT**

In the provided Battleships game code, the `ship_queue` is a deque (double-ended queue) used to manage the order in which the user places ships on the board during the ship placement phase. Here's an explanation of how the `ship_queue` is utilized:

1. **Initialization:**
   - At the beginning of the game, the `ship_queue` is initialized with instances of the `Ship` class representing different types of ships with their respective lengths.
   - The `current_ship` variable is set to the first ship in the queue (`ship_queue[0]`).

   ```python
   ship_queue = deque([
       Ship("Aircraft Carrier", 5),
       Ship("Battleship", 4),
       Ship("Cruiser", 3),
       Ship("Submarine", 3),
       Ship("Destroyer", 2)
   ])
   current_ship = ship_queue[0] if ship_queue else None
   
2. **Ship Placement:**
 - During the ship placement phase (game_state == 'placement'), the user places ships on the board by clicking on the canvas. The on_user_canvas_click function is responsible for handling the user's clicks and placing the ships on the board. After a successful placement, the ship is removed from the front of the ship_queue using ship_queue.popleft().
 - The upcoming ship to be placed is displayed on the GUI
 - The queue length is consistantly checked. When the queue is empty, meaning all ships have been placed, battle mode is initiated.

   ```python
   def on_user_canvas_click(event):
    global current_ship, game_board, game_state, ship_queue

    # ...

    if game_state != 'placement':
        return

    # ...

    if 0 <= x < 10 and 0 <= y < 10 and current_ship:
        if is_valid_placement(current_ship.length, y, x, selected_direction, game_board):
            # If valid, draw the ship on canvas and update the game board
            draw_ship_on_canvas(user_canvas, current_ship.length, y, x, selected_direction)

            # ...

            # Remove the placed ship from the queue and update the label
            ship_queue.popleft()
            if ship_queue:
                current_ship = ship_queue[0]
                shipLabel_text.set(f"Next ship to place: {current_ship.name} (length: {current_ship.length})")
            else:
                # No more ships to place, switch to battle mode
                game_state = 'battle'
                # ...

        else:
            # If the placement is not valid, provide feedback to the user
            show_temporary_label("Invalid placement! Try a different location or direction.", 3000)

### STACKS - 

