import sys

from ui.design import Ui_MainWindow
import matplotlib as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
from matplotlib import style
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import main

plt.use('Qt5Agg')


class Draw:
    def visualise(self, graphs, model):
        print("draw start")
        for graph in graphs:
            plt.style.use(graph.theme)
            print(graph.canvas)
            print("connected with graph")
            w = graph.canvas.get_width_height()
            frame = main.QtWidgets.QFrame()
            print(frame)
            frame.setStyleSheet("QFrame{background_color: rgb(0, 0, 0, 0)}")
            a_l = main.QtWidgets.QStackedLayout(frame)
            a_l.addWidget(graph.canvas)
            print("before set frame")
            frame.setMinimumHeight(w[1])
            print("minimum height")
            print(graph.vertical_lay)
            graph.vertical_lay.addWidget(frame)
            print("vert")
            graph.canvas.axes.cla()
            print("legend")
            ax = graph.canvas.axes
            print("ax")
            graph.df.plot(ax=ax)
            print("set legend draw")
            legend = ax.legend()
            legend.set_draggable(True)
            ax.set_xlabel(graph.x_lbl)
            ax.set_ylabel(graph.y_lbl)
            graph.canvas.draw()
            model.set_frames(frame)
            print("printing started")
        print("end")

    # self.toolbar = Navi(self.canv, self.centralwidget)
    # self.horizontalLayout.addWidget(self.toolbar)
