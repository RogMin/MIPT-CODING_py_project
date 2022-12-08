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

plt.use('Qt5Agg')


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Easy Plot")
        width = 941
        height = 552
        self.setFixedSize(width, height)

        self.themes = plt.style.available
        self.setupUi(self)
        self.openCSVButton.clicked.connect(self.get_csv_file)
        self.stylesDropdown.addItems(self.themes)
        self.stylesDropdown.currentIndexChanged['QString'].connect(self.set_theme())
        self.modl = model.Model()
        self.x_to_y_button.clicked.connect(self.modl.x_to_y)
        self.y1_to_y2_button.clicked.connect(self.modl.y1_to_y2)
        self.x1_to_y2_button.clicked.connect(self.modl.x1_to_y2)
        self.x_label_inp.editingFinished.connect(self.set_x_label)
        self.y_label_inp.editingFinished.connect(self.set_y_label)
        self.x1_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.x2_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.y1_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.y2_line_edit.editingFinished.connect(self.get_x_y_arrays)

    def set_theme(self):
        model.Model.set_theme(self.stylesDropdown.currentIndex())

    def set_x_label(self):
        self.modl.set_x_label(self.x_label_inp.text())

    def set_y_label(self):
        self.modl.set_y_label(self.y_label_inp.text())

    def get_x_y_arrays(self):
        df = pd.Series(self.x1_line_edit.text(), self.x1_line_edit.text(), self.y1_line_edit.text(),
                       self.y2_line_edit.text())
        self.modl.set_x_y(df)

    def get_csv_file(self):
        """sends df to model"""
        self.modl.csv_to_pd(
            pd.read_csv(QFileDialog.getOpenFileName(filter="csv (*.csv)")[0], encoding='utf-8').fillna(0))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
