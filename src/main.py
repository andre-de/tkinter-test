from classes import Window, Point, Line

def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(200, 200)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")

    point3 = Point(500, 10)
    point4 = Point(10, 500)
    line2 = Line(point3, point4)
    win.draw_line(line2, "red")

    
    win.wait_for_close()





if __name__ == "__main__":
    main()