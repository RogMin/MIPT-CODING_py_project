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
        for graph in graphs:
            try:
                plt.style.use(graph.theme)
                frame = main.QtWidgets.QFrame()  # Create new frame
                frame.setStyleSheet("QFrame{background_color: rgb(0, 0, 0, 0)}")
                lay = main.QtWidgets.QStackedLayout(frame)  # Set frame layout
                lay.addWidget(graph.canvas)
                frame.setMinimumHeight(graph.canvas.get_width_height()[1])  # Set minimum height to graphic frame
                graph.vertical_lay.addWidget(frame)
                ax = graph.canvas.axes
                ax.cla()
                graph.draw(ax)
                legend = ax.legend()
                legend.set_draggable(True)
                ax.set_xlabel(graph.x_lbl)
                ax.set_ylabel(graph.y_lbl)
                graph.frame = frame
            except:
                continue
        model.Graphs = graphs
