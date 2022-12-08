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
            try:
                plt.style.use(graph.theme)
                print(graph.canvas)
                w = graph.canvas.get_width_height()
                frame = main.QtWidgets.QFrame()
                frame.setStyleSheet("QFrame{background_color: rgb(0, 0, 0, 0)}")
                a_l = main.QtWidgets.QStackedLayout(frame)
                a_l.addWidget(graph.canvas)
                frame.setMinimumHeight(w[1])
                graph.vertical_lay.addWidget(frame)
                graph.canvas.axes.cla()
                print("legend")
                ax = graph.canvas.axes
                print("ax")
                graph.draw(ax)
                print("set legend draw")
                try:
                    legend = ax.legend()
                    legend.set_draggable(True)
                except:
                    print("")
                ax.set_xlabel(graph.x_lbl)
                ax.set_ylabel(graph.y_lbl)
                graph.canvas.draw()
                graph.frame = frame
            except:
                continue
            print("printing started")
        print("end")

    # self.toolbar = Navi(self.canv, self.centralwidget)
    # self.horizontalLayout.addWidget(self.toolbar)
