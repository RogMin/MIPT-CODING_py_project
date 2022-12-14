import sys
import matplotlib as plt
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import model
from ui.design import Ui_MainWindow

plt.use('Qt5Agg')


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=112):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        width = 846
        height = 510
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
        self.x_label_inp.editingFinished.connect(self.set_x_label)
        self.y_label_inp.editingFinished.connect(self.set_y_label)
        self.toggleButton.clicked.connect(self.change_marker_bool)
        self.markerSizeSlider.sliderReleased.connect(self.set_marker_size)
        self.modl.set_vertical_lay(self.verticalLayout)
        self.triangleMarkerTypeButton.clicked.connect(self.triangle_button)
        self.circleMarkerTypeButton.clicked.connect(self.circle_button)
        self.squareMarketTypeButton.clicked.connect(self.square_button)
        self.grayLineColorButton.clicked.connect(self.change_color_to_gray)
        self.blueLineColorButton.clicked.connect(self.change_color_to_blue)
        self.whiteLineColorButton.clicked.connect(self.change_color_to_white)
        self.brownLineColorButton.clicked.connect(self.change_color_to_brown)
        self.yellowLlineColorButton.clicked.connect(self.change_color_to_yellow)
        self.redLineColorButton.clicked.connect(self.change_color_to_red)
        self.ResetButton.clicked.connect(self.reset)
        self.setWindowTitle("Easy Plot")
    """Push and drop event"""

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            for url in e.mimeData().urls():
                fname = str(url.toLocalFile())
            self.readData(fname)
        else:
            e.ignore()

    def readData(self, name):
        self.modl.csv_to_pd(pd.read_csv(name, encoding='utf-8').fillna(0))

    """Change variables in model"""
    def reset(self):
        self.modl.reset()

    def triangle_button(self):
        self.modl.set_line_type('-')

    def circle_button(self):
        self.modl.set_line_type('bs-')

    def square_button(self):
        self.modl.set_line_type('ro-')

    def change_color_to_gray(self):
        self.modl.change_color("GRAY")

    def change_color_to_red(self):
        self.modl.change_color("RED")

    def change_color_to_white(self):
        self.modl.change_color("WHITE")

    def change_color_to_yellow(self):
        self.modl.change_color("YELLOW")

    def change_color_to_brown(self):
        self.modl.change_color("BROWN")

    def change_color_to_blue(self):
        self.modl.change_color("BLUE")

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

    def get_csv_file(self):
        """send dataframe to model"""
        self.modl.csv_to_pd(
            pd.read_csv(QFileDialog.getOpenFileName(filter="csv (*.csv)")[0], encoding='utf-8').fillna(0))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
