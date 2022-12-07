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
import model

plt.use('Qt5Agg')


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.themes = plt.style.available
        self.frames = []
        self.df = None
        self.setupUi(self)
        self.openCSVButton.clicked.connect(self.get_csv_file)
        self.stylesDropdown.addItems(self.themes)
        self.stylesDropdown.currentIndexChanged['QString'].connect(self.Update)
        self.modl = model.Model()
        self.x_to_y_button.clicked.connect(self.modl.x_to_y)
        self.y1_to_y2_button.clicked.connect(self.modl.y1_to_y2)
        self.x1_to_y2_button.clicked.connect(self.modl.x1_to_y2)
        self.x_label_inp.editingFinished.connect(self.set_x_label)
        self.y_label_inp.editingFinished.connect(self.set_y_label)
        self.x1_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.x2_line_edit.editingFinished.connect()


    #
    # self.y1_line_edit.editingFinished['QString'].connect()
    # self.y2_line_edit.editingFinished['QString'].connect()

    def set_x_label(self):
        self.modl.set_x_label(self.x_label_inp.text())

    def set_y_label(self):
        self.modl.set_y_label(self.y_label_inp.text())

    def inputTest(self):
        for frame in self.frames:
            frame.graph.x = self.x1_line_edit.text()
            print(frame.graph.x)

    def clear_frames(self):
        for frame in self.frames:
            self.verticalLayout.removeWidget(frame.test)
        self.frames = []

    def create_frame(self):
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())

    def Update(self, value = "bmh"):
        """clears old, draws new"""
        self.clear_frames()
        self.create_frame()
        plt.style.use(value)
        for frame in self.frames:
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
        print("end")

        # self.toolbar = Navi(self.canv, self.centralwidget)
        # self.horizontalLayout.addWidget(self.toolbar)

    def get_x_y_arrays(self):

    def get_csv_file(self):
        """sends df to model"""
        self.modl.csv_to_pd(pd.read_csv(QFileDialog.getOpenFileName(filter="csv (*.csv)")[0], encoding='utf-8').fillna(0))


        # self.modl.set_x_y()
        # self.df = pd.Series([1,2,3,4],[4,3,2,1])
        #self.Update(self.themes[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
