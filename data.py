import numpy as np

class Graph:
    def __init__(self, marker_size=0, color=0, color2=0, fig_type=0, x_lbl="", y_lbl="", x=[np.ones(5), 5 * np.ones(5)],
                 y=[5 * np.ones(5), np.ones(5)]):
        self.marker_size = marker_size
        self.color = color
        self.color2 = color2
        self.fig_type = fig_type
        self.x_lbl = x_lbl
        self.y_lbl = y_lbl
        self.x = x
        self.y = y

   def draw():
       pass


class Color:
    GRAY = "gray"
    BLUE = "blue"
    RED = "red"

