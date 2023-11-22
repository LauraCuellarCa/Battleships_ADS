import tkinter as tk

# DEFINITION: Canvas is an addon from tkinter which is a blank slate or a drawing area in a Tkinter window.
#             Basically a window.
def create_grid(canvas, cell_size):
    line_width = 2
    line_color = "blue"

    # Creates all vertical lines
    for i in range(11):
        canvas.create_line([(i * cell_size, cell_size), (i * cell_size, 11 * cell_size)], width=line_width, fill=line_color, tag='grid_line')

    # Creates all horizontal lines
    for i in range(11):
        canvas.create_line([(0, i * cell_size), (11 * cell_size, i * cell_size)], width=line_width, fill=line_color, tag='grid_line')

    for i in range(10):
        canvas.create_text((i * cell_size + cell_size * 3 / 2, cell_size * 3 / 4), text=chr(65 + i), fill="red", font=("Helvetica", 14))

    # Label the rows (1-10)
    # Adding an offset to teh y-coordinate to avoid overlap with letters
    for i in range(10):
        canvas.create_text((cell_size / 2, i * cell_size + cell_size * 5/4), text=str(i+1), fill="red", font=("Helvetica", 14))

cell_size = 50
def on_enemy_canvas_click(event):
    cell_clicked(event, "Enemy's Board")

def on_user_canvas_click(event):
    cell_clicked(event, "User Ships")

def cell_clicked(event, canvas_name):
    x = (event.x - cell_size) // cell_size
    y = (event.y - cell_size) // cell_size
    if 0 <= x < 10 and 0 <= y < 10:  # Checks if the click is within the grid bounds
        print(f"Cell clicked on {canvas_name} at: ({x}, {y})") # this is outputted to the console

# Initialize the main Tkinter window
root = tk.Tk()
root.title('Battleship Game')


enemy_canvas = tk.Canvas(root, height=(cell_size * 11), width=(cell_size * 11), bg='white')
user_canvas = tk.Canvas(root, height=(cell_size * 11), width=(cell_size * 11), bg='white')


# Putting the canvases (windows) next to each other
enemy_canvas.grid(row=0, column=0, padx=(10, 0), pady=10)
enemy_canvas.bind('<Button-1>', on_enemy_canvas_click) # <Button-1>: Left mouse button click
user_canvas.grid(row=0, column=1, padx=(10, 0), pady=10)
user_canvas.bind('<Button-1>', on_user_canvas_click)


# Place the canvases on the MAIN window
enemy_canvas.grid(row=0, column=0, padx=(10, 0), pady=10) # padx and pady adds space around the canvases, so they're
                                                          # not stuck together
user_canvas.grid(row=0, column=1, padx=(10, 0), pady=10)

# Now actually create the grids on both canvases
create_grid(enemy_canvas, cell_size)
create_grid(user_canvas, cell_size)

# Add labels for the boards
tk.Label(root, text="ENEMY'S BOARD", fg="white", font=("Helvetica", 16)).grid(row=1, column=0)
tk.Label(root, text="USER SHIPS", fg="white", font=("Helvetica", 16)).grid(row=1, column=1)

root.mainloop()
