import matplotlib.pyplot as plt
import pandas as pd
import main
import draw


class Model:
    def __init__(self, color=0, xlabel="", ylabel="", df=None, theme="bmh", Graphs=[], vertical_lay=None,
                 markersize=5):
        self.Graphs = Graphs
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.df = df
        self.theme = theme
        self.marker_sz = markersize
        self.draw = draw.Draw()
        self.vertical_lay = vertical_lay
        self.marker_on_off = False

    def set_vertical_lay(self, lay):
        self.vertical_lay = lay
        print(self.vertical_lay)

    def change_marker_bool(self):
        self.marker_on_off = not self.marker_on_off
        self.update_graphs_data()

    def set_marker_size(self, markersize):
        self.marker_sz = markersize
        self.update_graphs_data()

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
        self.xlabel = label
        self.update_graphs_data()

    def set_y_label(self, label):
        self.ylabel = label
        self.update_graphs_data()

    def clear_frames(self):
        for graph in self.Graphs:
            print("remove frames")
            graph.vertical_lay.removeWidget(graph.frame)
            print("remove fra2s")

    def init_graphs(self):
        self.clear_frames()
        self.Graphs = []
        self.Graphs.append(Graph())
        self.Graphs.append(Hist())
        self.Graphs.append(Area())
        self.Graphs.append(Hexbin())
        self.Graphs.append(Box())

    def update_graphs_data(self):
        print("visualising started")
        print("graphs null")
        self.init_graphs()
        print("init graphs")
        for graph in self.Graphs:
            print("ЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫАЫА")
            graph.x_lbl = self.xlabel
            graph.y_lbl = self.ylabel
            graph.df = self.df
            graph.marker_size = self.marker_sz
            graph.theme = self.theme
            graph.vertical_lay = self.vertical_lay
            graph.canvas = main.MatplotlibCanvas(main.MainWindow())
            graph.marker_on_off = self.marker_on_off
        self.draw.visualise(self.Graphs, self)


class Graph:
    def __init__(self, marker_size=5, color=0, color2=0, fig_type=0, x_lbl="", y_lbl="", df=None, canvas=None,
                 theme="bmh", verticalLay=None, frame = None):
        self.marker_size = marker_size
        self.color = color
        self.color2 = color2
        self.fig_type = fig_type
        self.x_lbl = x_lbl
        self.y_lbl = y_lbl
        self.canvas = canvas
        self.df = df
        self.theme = theme
        self.vertical_lay = verticalLay
        self.marker_on_off = False
        self.frame = frame

    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot(ax=ax, style="o", ms=self.marker_size)
        else:
            self.df.plot(ax=ax)


class Hist(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.bar(ax=ax, style="o", ms=self.marker_size)
        else:
            self.df.plot.bar(ax=ax)


class Area(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.area(ax=ax, style="o", ms=self.marker_size)
        else:
            self.df.plot.area(ax=ax)


class Hexbin(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.hexbin(ax=ax, style="o", ms=self.marker_size)
        else:
            self.df.plot.hexbin(ax=ax)


class Box(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.box(ax=ax, style="o", ms = self.marker_size)
        else:
            self.df.plot.box(ax=ax)