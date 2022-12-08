import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import draw


class Model:
    def __init__(self, color=0, xlabel="", ylabel="", df=pd.series(), theme="", Graphs=[], vertical_layout = None):
        self.Graphs = Graphs
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.df = df
        self.theme = theme
        self.draw = draw.Draw()
        self.vertical_layout = vertical_layout

    def get_vert_lay(self):
        return self.vertical_layout

    def set_x_y(self, df):
        self.df = df

    def csv_to_pd(self, df):
        self.df = df

    def set_theme(self, theme):
        self.theme = theme

    def x_to_y(self):
        pass

    def y1_to_y2(self):
        pass

    def x1_to_y2(self):
        pass

    def set_x_label(self, label):
        self.xlabel = label

    def set_y_label(self, label):
        self.ylabel = label

    def init_graphs(self):
        pass

    def update_graphs_data(self):
        for graph in self.Graphs:
            graph.x_lbl = self.xlabel
            graph.y_lbl = self.ylabel
            # (...)
        self.draw.visualise(self.Graphs)





class Hist(data.Graph):
    def draw(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.bar(self.x, self.y, c=self.color)


class Line(data.Graph):
    def draw(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.x, self.y, c=self.color)