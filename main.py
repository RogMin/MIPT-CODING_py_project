import sys

import matplotlib as plt
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import model
from ui.design import Ui_MainWindow

plt.use('Qt5Agg')


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=115):
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
        self.modl = model.Model()
        self.themes = self.themes = ['bmh', 'classic', 'dark_background', 'fast',
               'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
               'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
               'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
               'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
               'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
               'Solarize_Light2', 'tableau-colorblind10']
        self.setupUi(self)
        self.openCSVButton.clicked.connect(self.get_csv_file)
        self.stylesDropdown.addItems(self.themes)
        self.stylesDropdown.currentIndexChanged['QString'].connect(self.set_theme)
        self.x_to_y_button.clicked.connect(self.modl.x_to_y)
        self.y1_to_y2_button.clicked.connect(self.modl.y1_to_y2)
        self.x1_to_y2_button.clicked.connect(self.modl.x1_to_y2)
        self.x_label_inp.editingFinished.connect(self.set_x_label)
        self.y_label_inp.editingFinished.connect(self.set_y_label)
        self.x1_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.x2_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.y1_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.y2_line_edit.editingFinished.connect(self.get_x_y_arrays)
        self.toggleButton.clicked.connect(self.change_marker_bool)
        self.markerSizeSlider.sliderReleased.connect(self.set_marker_size)
        self.modl.set_vertical_lay(self.verticalLayout)
        self.modl.init_graphs()

    def change_marker_bool(self):
        self.modl.change_marker_bool()

    def set_marker_size(self):
        self.modl.set_marker_size(self.markerSizeSlider.sliderPosition())

    def set_theme(self):
        self.modl.set_theme(self.themes[self.stylesDropdown.currentIndex()])

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
