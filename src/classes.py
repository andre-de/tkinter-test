from tkinter import Tk, BOTH, Canvas
import time


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

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._xtlc = None
        self._ytlc = None
        self._xbrc = None
        self._ybrc = None
        self._win = win

    def draw(self, xtlc, ytlc, xbrc, ybrc):
        if self._win is None:
            return
        self._xtlc = xtlc
        self._ytlc = ytlc
        self._xbrc = xbrc
        self._ybrc = ybrc

        if self.has_left_wall:
            left_wall = Line(Point(self._xtlc, self._ytlc), Point(self._xtlc, self._ybrc))
            self._win.draw_line(left_wall, "black")

        if self.has_right_wall:
            right_wall = Line(Point(self._xbrc, self._ytlc), Point(self._xbrc, self._ybrc))
            self._win.draw_line(right_wall, "black")

        if self.has_top_wall:
            top_wall = Line(Point(self._xtlc, self._ytlc), Point(self._xbrc, self._ytlc))
            self._win.draw_line(top_wall, "black")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._xtlc, self._ybrc), Point(self._xbrc, self._ybrc))
            self._win.draw_line(bottom_wall, "black")
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        line = Line(Point((self._xtlc+self._xbrc)//2, (self._ytlc + self._ybrc)//2), 
                     Point((to_cell._xtlc+to_cell._xbrc)//2, (to_cell._ytlc + to_cell._ybrc)//2))
        self._win.draw_line(line, fill_color)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)


    
