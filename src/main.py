from classes import Window, Point, Line, Cell

def main():
    win = Window(800, 600)

    '''
    point1 = Point(100, 100)
    point2 = Point(200, 200)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")

    point3 = Point(500, 10)
    point4 = Point(10, 500)
    line2 = Line(point3, point4)
    win.draw_line(line2, "red")
    '''
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
    
    win.wait_for_close()





if __name__ == "__main__":
    main()