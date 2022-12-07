import sys

from ui.design import Ui_MainWindow
import matplotlib as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
from matplotlib import style
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import data
import draw
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
            frame.canvas = MatplotlibCanvas(self)
            canv = frame.canvas
            w = canv.get_width_height()
            a = QtWidgets.QFrame(self)
            a.setStyleSheet("QFrame{background_color: rgb(0, 0, 0, 0)}")
            a_l = QtWidgets.QStackedLayout(a)
            a_l.addWidget(canv)
            a.setMinimumHeight(w[1])
            frame.test = a
            self.verticalLayout.addWidget(a)
            canv.axes.cla()
            ax = canv.axes
            self.df.plot(ax=ax)
            legend = ax.legend()
            legend.set_draggable(True)
            ax.set_xlabel(frame.graph.x_lbl)
            ax.set_ylabel(frame.graph.y_lbl)
            canv.draw()

            # plt.figure(figsize=(8, 6), dpi=300)  # размер графика
            # plt.xlabel(self.xlabel)  # подписи к осям
            # plt.ylabel(self.ylabel)
            # plt.grid(True, linestyle="--")  # пунктирная сетка
            # plt.plot(self.x, self.y, c=self.color)
            #
            # plt.bar(self.x, self.y, c=self.color)
            # plt.plot(self.x, self.y, c=self.color)
            #
            # plt.legend()
            # plt.show()
    print("end")

    # self.toolbar = Navi(self.canv, self.centralwidget)
    # self.horizontalLayout.addWidget(self.toolbar)
