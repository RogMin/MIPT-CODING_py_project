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
        self.openCSVButton.clicked.connect(self.get_file)
        self.stylesDropdown.addItems(self.themes)
        self.stylesDropdown.currentIndexChanged['QString'].connect(self.Update)

    def clear_frames(self):
        print("s")
        for frame in self.frames:
            print("l")
            self.verticalLayout.removeItem(frame.test)
            print("ll")
            self.frames.pop(frame)
        print("s")

    def create_frame(self):
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())
        self.frames.append(data.Frame())

    def Update(self, value):
        """clears old, draws new"""
        self.clear_frames()
        self.create_frame()
        plt.style.use('dark_background')
        for frame in self.frames:
            frame.canvas = MatplotlibCanvas(self)
            canv = frame.canvas
            w = canv.get_width_height()
            a = QtWidgets.QFrame(self)
            a.setStyleSheet("QFrame{background_color: rgb(0, 0, 0, 0)}")
            a_l = QtWidgets.QStackedLayout(a)
            a_l.addWidget(canv)
            a.setMinimumHeight(w[1])
            self.verticalLayout.addWidget(a)
            canv.axes.cla()
            ax = canv.axes
            self.df.plot(ax=ax)
            legend = ax.legend()
            legend.set_draggable(True)
            fr = data.Frame()
            ax.set_xlabel(fr.graph.x_lbl)
            ax.set_ylabel(fr.graph.y_lbl)
            canv.draw()
        print("end")

        # self.toolbar = Navi(self.canv, self.centralwidget)
        # self.horizontalLayout.addWidget(self.toolbar)

    def read_data(self, filename):
        """reads the file from the link"""
        self.df = pd.read_csv(filename, encoding='utf-8').fillna(0)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("-1")
        self.Update(self.themes[0])

    def get_file(self):
        """sends a link to the file"""
        print("ЫА1")
        self.read_data(QFileDialog.getOpenFileName(filter="csv (*.csv)")[0])
        print("ЫА2")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


