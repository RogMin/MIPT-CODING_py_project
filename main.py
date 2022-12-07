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

        self.x_to_y_button.clicked.connect(self.x_to_y)
        self.y1_to_y2_button.clicked.connect(self.y1_to_y2)
        self.x1_to_y2_button.clicked.connect(self.x1_to_y2)
        self.x_label_inp.editingFinished.connect(self.set_x_label)
        self.y_label_inp.editingFinished.connect(self.set_y_label)

        self.x1_line_edit.editingFinished.connect(self.inputTest)
    # self.x2_line_edit.editingFinished.connect()
    # self.y1_line_edit.editingFinished.connect()
    # self.y2_line_edit.editingFinished.connect()

    def x_to_y(self):
        f = 0
        for frame in self.frames:
            if not f:
                print("x_to_y:", "x", frame.graph.y, "y", frame.graph.y)
                f = 1

            if frame.graph.y and frame.graph.y:
                frame.graph.x, frame.graph.y = frame.graph.y, frame.graph.x
        print("x", frame.graph.x, "y", frame.graph.y)
        # pass

    def y1_to_y2(self):
        f = 0
        for frame in self.frames:
            if not f:
                print("y1_to_y2", "y1", frame.graph.y[0], "y2", frame.graph.y[1])
                f = 1

            if frame.graph.y[0] and frame.graph.y[1]:
                frame.graph.y[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.y[0]
        print("y1", frame.graph.y[0], "y2", frame.graph.y[1])
        # pass

    def x1_to_y2(self):
        #
        f = 0
        for frame in self.frames:
            if not f:
                print("x1_to_y2", "x1", frame.graph.x[0], "y2", frame.graph.y[1])
                f = 1
            if frame.graph.x[0] and frame.graph.y[1]:
                frame.graph.x[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.x[0]
        print("x1", frame.graph.x[0], "y2", frame.graph.y[1])
        # pass

    def inputTest(self):
        for frame in self.frames:
            df["x1"] = pd.series(self.x1_line_edit.text())
            print(frame.graph.x)

    def set_x_label(self):
        if len(self.frames) > 0:
            for frame in self.frames:
                frame.graph.x_lbl = self.x_label_inp.text()
            self.Update()

    def set_y_label(self):
        if len(self.frames) > 0:
            for frame in self.frames:
                frame.graph.y_lbl = self.y_label_inp.text()
            self.Update()

    def x_to_y(self):
        print("x y")
        # pass
        f = 0
        for frame in self.frames:
            if not f:
                print("x_to_y:", "x", frame.graph.y, "y", frame.graph.y)
                f = 1

            if frame.graph.y and frame.graph.y:
                frame.graph.x, frame.graph.y = frame.graph.y, frame.graph.x
        print("x", frame.graph.x, "y", frame.graph.y)
        # pass

    def y1_to_y2(self):
        print("y1 y2")
        # pass
        f = 0
        for frame in self.frames:
            if not f:
                print("y1_to_y2", "y1", frame.graph.y[0], "y2", frame.graph.y[1])
                f = 1

            if frame.graph.y[0] and frame.graph.y[1]:
                frame.graph.y[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.y[0]
        print("y1", frame.graph.y[0], "y2", frame.graph.y[1])
        # pass

    def x1_to_y2(self):
        print("x1 y2")
        # pass
        #
        f = 0
        for frame in self.frames:
            if not f:
                print("x1_to_y2", "x1", frame.graph.x[0], "y2", frame.graph.y[1])
                f = 1
            if frame.graph.x[0] and frame.graph.y[1]:
                frame.graph.x[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.x[0]
        print("x1", frame.graph.x[0], "y2", frame.graph.y[1])
        # pass

    def inputTest(self):
        print(self.x1_line_edit.text())

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

    def read_data(self, filename):
        """reads the file from the link"""
        self.df = pd.read_csv(filename, encoding='utf-8').fillna(0)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #self.df = pd.Series([1,2,3,4],[4,3,2,1])
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
