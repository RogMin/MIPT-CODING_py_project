import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Model:
    def __init__(self, color=0, xlabel="", ylabel="", df=pd.series(),theme = "",Graphs =[]):
        self.Graphs = Graphs
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.df = df
        self.theme = theme

    def set_x_y(self,df):
        if not self.df.empty:
            self.df = df


    def csv_to_pd(self,df):
        self.df = df

    def set_theme(self,theme):
        theme = self.theme


    def x_to_y(self):
        for frame in self.frames:
            if frame.graph.y and frame.graph.y:
                frame.graph.x, frame.graph.y = frame.graph.y, frame.graph.x
        print("x", frame.graph.x, "y", frame.graph.y)

    def y1_to_y2(self):
        for frame in self.frames:
            if frame.graph.y[0] and frame.graph.y[1]:
                frame.graph.y[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.y[0]
        print("y1", frame.graph.y[0], "y2", frame.graph.y[1])

    def x1_to_y2(self):
        for frame in self.frames:
            if frame.graph.x[0] and frame.graph.y[1]:
                frame.graph.x[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.x[0]
        print("x1", frame.graph.x[0], "y2", frame.graph.y[1])

    def set_x_label(self, label):
        if len(self.frames) > 0:
            for frame in self.frames:
                frame.graph.x_lbl = label
            self.Update()

    def set_y_label(self, label):
        if len(self.frames) > 0:
            for frame in self.frames:
                frame.graph.y_lbl = self.y_label_inp.text()
            self.Update()

    def update_graphs_data(self):
        pass

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
