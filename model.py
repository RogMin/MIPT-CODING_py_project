import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import draw


class Model:
    def __init__(self, color=0, xlabel="", ylabel="", df=pd.series(), theme="", Graphs=[]):
        self.Graphs = Graphs
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.df = df
        self.theme = theme
        self.draw = draw.Draw()

    def set_x_y(self, df):
        self.df = df
        self.update_graphs_data()


    def csv_to_pd(self, df):
        self.df = df
        self.update_graphs_data()

    def set_theme(self, theme):
        self.theme = theme
        self.update_graphs_data()

    def x_to_y(self):
        # (...)
        self.update_graphs_data()

    def y1_to_y2(self):
        # (...)
        self.update_graphs_data()

    def x1_to_y2(self):
        # (...)
        self.update_graphs_data()

    def set_x_label(self, label):
        self.xlabel = label
        self.update_graphs_data()

    def set_y_label(self, label):
        self.ylabel = label
        self.update_graphs_data()

    def init_graphs(self):
        pass

    def update_graphs_data(self):
        for graph in self.Graphs:
            graph.x_lbl = self.xlabel
            graph.y_lbl = self.ylabel
            # (...)
        self.draw.visualise(self.Graphs)
        print("visualising started")



class Graph:
    def __init__(self, marker_size=0, color=0, color2=0, fig_type=0, x_lbl="", y_lbl="", x=[np.ones(5), 5 * np.ones(5)],
                 y=[5 * np.ones(5), np.ones(5)]):
        self.marker_size = marker_size
        self.color = color
        self.color2 = color2
        self.fig_type = fig_type
        self.x_lbl = x_lbl
        self.y_lbl = y_lbl
        self.x = x
        self.y = y

   def draw():
       pass



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
