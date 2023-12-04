### User Ship Placement:
1. **`create_welcome_window():`**
   - Creates a Tkinter window for the welcome screen.
   - Takes user's name input.

2. **`get_player_name_start_game(playerName, root):`**
   - Processes the entered player name and starts the game.

3. **`create_grid(canvas, cell_size):`**
   - Creates a grid on the given canvas with specified cell size.

4. **`is_valid_placement(ship_length, start_row, start_col, direction, board):`**
   - Checks if a ship can be placed at the specified location on the board.

5. **`show_temporary_label(text, duration):`**
   - Displays a temporary label with the provided text for a specified duration.

6. **`clear_temporary_label():`**
   - Clears the temporary label.

7. **`draw_ship_on_canvas(canvas, ship_length, start_row, start_col, direction):`**
   - Draws a ship on the canvas based on its length, starting position, and direction.

8. **`on_user_canvas_click(event):`**
   - Handles the user's click on the user canvas during ship placement.

### CPU Opponent:
9. **`place_cpu_ships_on_board(enemy_game_board):`**
   - Places CPU ships on the game board.

10. **`place_ships(grid, ships_to_place, placement_stack):`**
    - Recursively places ships on the grid, ensuring valid placement.

11. **`can_place_ship(grid, x, y, ship_size, orientation):`**
    - Checks if a ship can be placed at the specified location.

12. **`place_ship(grid, x, y, ship_size, orientation):`**
    - Places a ship on the grid at the specified location.

13. **`remove_ship(grid, x, y, ship_size, orientation):`**
    - Removes a ship from the grid.

14. **`all_ships_placed(grid):`**
    - Checks if all ships have been placed on the grid.

### Battle Phase:
15. **`cpu_turn():`**
    - Executes the CPU's turn.

16. **`get_random_shot():`**
    - Gets a random shot for the CPU.

17. **`get_targeted_shot(last_hit):`**
    - Gets a targeted shot for the CPU based on the last hit position.

18. **`process_cpu_shot(row, col):`**
    - Processes a CPU shot and updates the game board.

19. **`process_shot(row, col):`**
    - Processes a user's shot and updates the enemy game board.

20. **`display_hit_or_miss(canvas, col, row, result):`**
    - Displays a hit or miss on the canvas based on the result.

### Game Management:
21. **`create_ranking_system():`**
    - Creates a ranking system for tracking player performance.

22. **`display_rankings(ranking_system):`**
    - Displays player rankings in a new Tkinter window.

23. **`restart_game():`**
    - Restarts the game by saving data and running the `finaltest.py` script.

