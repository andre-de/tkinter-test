from classes import Window, Point, Line, Cell, Maze
import sys

def main():
    

    '''
    point1 = Point(100, 100)
    point2 = Point(200, 200)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")

    point3 = Point(500, 10)
    point4 = Point(10, 500)
    line2 = Line(point3, point4)
    win.draw_line(line2, "red")
    
    cell1 = Cell(win)
    cell1.draw(100, 100, 200, 200)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(300, 100, 400, 200)

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.has_bottom_wall = False
    cell3.draw(500, 100, 600, 200)

    cell1.draw_move(cell2)
    '''
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


if __name__ == "__main__":
    main()