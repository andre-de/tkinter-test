from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._root = Tk()
        self._root.title("Title")
        self._root.geometry(str(width)+"x"+str(height))
        self._canvas = Canvas(self._root)
        self._canvas.pack(fill=BOTH, expand=True)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
    
    def close(self):
        self._running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self._p1.x, self._p1.y, self._p2.x, self._p2.y, fill=fill_color, width = 2)

