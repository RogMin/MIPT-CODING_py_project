import matplotlib.pyplot as plt
import pandas as pd

import draw


class Model:
    def __init__(self, color=0, xlabel="", ylabel="", df=pd.Series(), theme="", Graphs=[], vertical_lay=None):
        self.Graphs = Graphs
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.df = df
        self.theme = theme
        self.draw = draw.Draw()
        self.vertical_lay = vertical_lay

    def set_x_y(self, df):
        print("seting_x_y")
        self.df = df
        self.update_graphs_data()

    def csv_to_pd(self, df):
        print("csving_to_pd")
        self.df = df
        self.update_graphs_data()

    def set_theme(self, theme):
        print("setting theme")
        self.theme = theme
        self.update_graphs_data()

    def x_to_y(self):
        print("changing_x_to_y")
        # (...)
        self.update_graphs_data()

    def y1_to_y2(self):
        print("changing_y1_to_y2")
        # (...)
        self.update_graphs_data()

    def x1_to_y2(self):
        print("changing_x1_to_y2")
        # (...)
        self.update_graphs_data()

    def set_x_label(self, label):
        print("setting_x_label")
        self.xlabel = label
        self.update_graphs_data()

    def get_vert_layout(self):
        return self.vertical_lay

    def set_y_label(self, label):
        print("setting_y_label")
        self.ylabel = label
        self.update_graphs_data()

    def init_graphs(self):
        pass

    def update_graphs_data(self):
        print("visualising started")
        for graph in self.Graphs:
            graph.x_lbl = self.xlabel
            graph.y_lbl = self.ylabel
            # (...)
        self.draw.visualise(self.Graphs)


class Graph:
    def __init__(self, marker_size=0, color=0, color2=0, fig_type=0, x_lbl="", y_lbl="", df=None, canvas=None):
        self.marker_size = marker_size
        self.color = color
        self.color2 = color2
        self.fig_type = fig_type
        self.x_lbl = x_lbl
        self.y_lbl = y_lbl
        self.canvas = canvas
        self.df = df

    def draw(self):
        x, y = None
        return x, y


class Hist(Graph):
    def draw(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.bar(self.x, self.y, c=self.color)


class Line(Graph):
    def draw(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.x, self.y, c=self.color)
