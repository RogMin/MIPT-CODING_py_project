import sys

from ui.design import Ui_MainWindow
import matplotlib as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
from matplotlib import style
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import model
import numpy as np

class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)


class Draw:
    def visualise(self,graphs):
        plt.style.use(graphs[0].theme)
        for graph in graphs:
            graph.canvas = MatplotlibCanvas(self)
            print("connected with graph")
            w = graph.canvas.get_width_height()
            frame = QtWidgets.QFrame(self)
            frame.setStyleSheet("QFrame{background_color: rgb(0, 0, 0, 0)}")
            a_l = QtWidgets.QStackedLayout(frame)
            a_l.addWidget(graph.canvas)
            frame.setMinimumHeight(w[1])
            model.Model.get_vert_layout().addWidget(frame)
            graph.canvas.axes.cla()
            ax = graph.canvas.axes
            graph.df.plot(ax=ax)
            legend = ax.legend()
            legend.set_draggable(True)
            ax.set_xlabel(graph.x_lbl)
            ax.set_ylabel(graph.y_lbl)
            graph.canvas.draw()
            print("printing started")
    print("end")

    # self.toolbar = Navi(self.canv, self.centralwidget)
    # self.horizontalLayout.addWidget(self.toolbar)
