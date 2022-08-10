from tkinter import *

# Grid dimensions (display width is 150 pixels more)
WIDTH, HEIGHT = 1200, 600

# Number of cells in a row
n = 24

EMPTY_COLOUR = "lightgreen"
WALL_COLOUR = "gray"
START_COLOUR = "green"
FINISH_COLOUR = "red"

if EMPTY_COLOUR == WALL_COLOUR or EMPTY_COLOUR == START_COLOUR or EMPTY_COLOUR == FINISH_COLOUR or \
        WALL_COLOUR == START_COLOUR or WALL_COLOUR == FINISH_COLOUR or START_COLOUR == FINISH_COLOUR:
    raise Exception("Cell colours need to be different! Please check lines 9-12.")

FONT = "Comic Sans MS"

EMPTY = False
WALL = True

# User selection : 0 = wall, 1 = start, 2 = finish, -1 = None
selection = -1

grid = [[EMPTY for i in range(n)] for j in range(HEIGHT//n)]

root = Tk()
root.title("Maze")
root.resizable(0, 0)

canvas = Canvas(root, width=WIDTH+150, height=HEIGHT)
canvas.pack()


def display(board):
    global coord
    coord = []
    # Display grid
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]:
                canvas.create_rectangle(WIDTH / n * x + 2, WIDTH / n * y + 2, WIDTH / n * x + WIDTH / n,
                                        WIDTH / n * y + WIDTH / n, fill=WALL_COLOUR)
                coord.append([WIDTH / n * x + 2, WIDTH / n * y + 2, WIDTH / n * x + WIDTH / n,
                              WIDTH / n * y + WIDTH / n, WALL_COLOUR])
            else:
                canvas.create_rectangle(WIDTH / n * x + 2, WIDTH / n * y + 2, WIDTH / n * x + WIDTH / n,
                                        WIDTH / n * y + WIDTH / n, fill=EMPTY_COLOUR)
                coord.append([WIDTH / n * x + 2, WIDTH / n * y + 2, WIDTH / n * x + WIDTH / n,
                              WIDTH / n * y + WIDTH / n, EMPTY_COLOUR])


def select_colour(event):
    global cell_colour
    cx, cy = event.x, event.y
    for cell in coord:
        # Maybe add a clicked_on_cell function that returns which cell has been clicked on to fix problem with removing start and finish when user clicks on white
        # Remove existing Start or Finish
        if (cell[4] == START_COLOUR and selection == 1) or (cell[4] == FINISH_COLOUR and selection == 2):
            canvas.create_rectangle(cell[0], cell[1], cell[2], cell[3], fill=EMPTY_COLOUR)
            cell[4] = EMPTY_COLOUR

        if cell[0] <= cx <= cell[2] and cell[1] <= cy <= cell[3]:
            if selection == 0:
                if cell[4] == EMPTY_COLOUR:
                    cell_colour = WALL_COLOUR
                else:
                    cell_colour = EMPTY_COLOUR
                canvas.create_rectangle(cell[0], cell[1], cell[2], cell[3], fill=cell_colour)
                cell[4] = cell_colour
            elif selection == 1:
                canvas.create_rectangle(cell[0], cell[1], cell[2], cell[3], fill=START_COLOUR)
                cell[4] = START_COLOUR
            elif selection == 2:
                canvas.create_rectangle(cell[0], cell[1], cell[2], cell[3], fill=FINISH_COLOUR)
                cell[4] = FINISH_COLOUR


def motion(event):
    if selection == 0:
        cx, cy = event.x, event.y
        for cell in coord:
            if cell[0] <= cx <= cell[2] and cell[1] <= cy <= cell[3]:
                canvas.create_rectangle(cell[0], cell[1], cell[2], cell[3], fill=cell_colour)
                cell[4] = cell_colour


def select(i):
    global selection
    selection = i


def clear_grid():
    global grid
    grid = [[EMPTY for i in range(n)] for j in range(HEIGHT//n)]
    display(grid)


display(grid)

draw_wall = Button(root, text="Wall", font=(FONT, 8), bg="yellow", width=4, height=2, command=lambda: select(0))
draw_wall.place(x=WIDTH+10, y=20)

draw_start = Button(root, text="Start", font=(FONT, 8), bg="green", width=4, height=2, command=lambda: select(1))
draw_start.place(x=WIDTH+60, y=20)

draw_finish = Button(root, text="Finish", font=(FONT, 8), bg="red", width=4, height=2, command=lambda: select(2))
draw_finish.place(x=WIDTH+110, y=20)

clear_button = Button(root, text="Clear", font=(FONT, 8), bg="lightgray", width=8, height=1, command=clear_grid)
clear_button.place(x=WIDTH+46, y=80)

canvas.bind("<B1-Motion>", motion)
canvas.bind("<Button-1>", select_colour)

root.mainloop()
