import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure


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


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)


class Color:
    GRAY = "gray"
    BLUE = "blue"
    RED = "red"


class Frame:
    def __init__(self, frame=None, canvas=None, test=None, graph=Graph()):
        self.graph = graph
        self.frame = frame
        self.test = test
