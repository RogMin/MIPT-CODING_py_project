import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import main
import draw


class Model:
    def __init__(self, df=None, theme="bmh", vertical_lay=None, markersize=2):
        self.Graphs = []
        self.color = ''
        self.xlabel = ""
        self.ylabel = ""
        self.df = df
        self.theme = theme
        self.marker_sz = markersize
        self.draw = draw.Draw()
        self.vertical_lay = vertical_lay
        self.marker_on_off = False
        self.line_type = ''

    def save_graph(self, index):
        graph = self.Graphs[index]
        plt.style.use(graph.theme)
        ax = graph.canvas.axes
        ax.cla()
        graph.draw(ax)
        legend = ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel(graph.x_lbl)
        ax.set_ylabel(graph.y_lbl)

    def set_line_type(self, typ):
        self.line_type = typ
        self.update_graphs_data()

    def set_vertical_lay(self, lay):
        self.vertical_lay = lay

    def change_color(self, color):
        self.color = color
        self.update_graphs_data()

    def change_marker_bool(self):
        self.marker_on_off = not self.marker_on_off
        self.update_graphs_data()

    def set_marker_size(self, markersize):
        self.marker_sz = markersize
        self.update_graphs_data()

    def csv_to_pd(self, df):
        self.df = df
        self.update_graphs_data()

    def set_theme(self, theme):
        self.theme = theme
        self.update_graphs_data()

    def set_x_label(self, label):
        self.xlabel = label
        self.update_graphs_data()

    def set_y_label(self, label):
        self.ylabel = label
        self.update_graphs_data()

    def clear_frames(self):
        """Dell old graphics"""
        for graph in self.Graphs:
            graph.vertical_lay.removeWidget(graph.frame)
            del graph.frame
            graph.vertical_lay.update()
        self.Graphs = []

    def init_graphs(self):
        """Create graphics prefabs"""
        self.clear_frames()
        self.Graphs = []
        self.Graphs.append(Graph())
        self.Graphs.append(Hist())
        self.Graphs.append(Area())
        self.Graphs.append(StackedArea())
        self.Graphs.append(Hexbin())
        self.Graphs.append(Box())
        self.Graphs.append(BoxHoriz())
        self.Graphs.append(HistStacked())
        self.Graphs.append(HistHoriz())
        self.Graphs.append(HistHorizStacked())

    def update_graphs_data(self):
        """Set vars in graphics from class init"""
        self.init_graphs()
        for graph in self.Graphs:
            graph.x_lbl = self.xlabel
            graph.y_lbl = self.ylabel
            graph.df = self.df
            graph.marker_size = self.marker_sz
            graph.theme = self.theme
            graph.vertical_lay = self.vertical_lay
            graph.canvas = main.MatplotlibCanvas(main.MainWindow())
            graph.marker_on_off = self.marker_on_off
            graph.line_type = self.line_type
            graph.color = self.color
        self.draw.visualise(self.Graphs, self)


class Graph:
    def __init__(self, marker_size=2, x_lbl="", y_lbl="", df=None, canvas=None,
                 theme="bmh", verticalLay=None, frame=None):
        self.marker_size = marker_size
        self.x_lbl = x_lbl
        self.y_lbl = y_lbl
        self.canvas = canvas
        self.df = df
        self.theme = theme
        self.vertical_lay = verticalLay
        self.marker_on_off = False
        self.frame = frame
        self.line_type = ''
        self.color = ""

    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot(ax=ax, style="o", ms=self.marker_size)
        else:
            if self.color != "":
                self.df.plot(ax=ax, linewidth=self.marker_size, style=self.line_type, color=self.color)
            else:
                self.df.plot(ax=ax, linewidth=self.marker_size, style=self.line_type)


class HistHoriz(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.barh(ax=ax, style="o", ms=self.marker_size)
        else:
            if self.color != "":
                self.df.plot.barh(ax=ax, linewidth=self.marker_size, style=self.line_type, color=self.color)
            else:
                self.df.plot.barh(ax=ax, linewidth=self.marker_size, style=self.line_type)


class HistHorizStacked(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.barh(ax=ax, style="o", ms=self.marker_size, stacked=True)
        else:
            if self.color != "":
                self.df.plot.barh(ax=ax, stacked=True, linewidth=self.marker_size, style=self.line_type,
                                  color=self.color)
            else:
                self.df.plot.barh(ax=ax, stacked=True, linewidth=self.marker_size, style=self.line_type)


class Hist(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.bar(ax=ax, style="o", ms=self.marker_size)
        else:
            if self.color != "":
                self.df.plot.bar(ax=ax, linewidth=self.marker_size, style=self.line_type, color=self.color)
            else:
                self.df.plot.bar(ax=ax, linewidth=self.marker_size, style=self.line_type)


class HistStacked(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.bar(ax=ax, style="o", ms=self.marker_size, stacked=True)
        else:
            if self.color != "":
                self.df.plot.bar(ax=ax, stacked=True, linewidth=self.marker_size, style=self.line_type,
                                 color=self.color)
            else:
                self.df.plot.bar(ax=ax, stacked=True, linewidth=self.marker_size, style=self.line_type)


class Area(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.area(ax=ax, style="o", ms=self.marker_size)
        else:
            if self.color != "":
                self.df.plot.area(ax=ax, linewidth=self.marker_size, style=self.line_type, color=self.color)
            else:
                self.df.plot.area(ax=ax, linewidth=self.marker_size, style=self.line_type)


class StackedArea(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.area(stacked=True, ax=ax, style="o", ms=self.marker_size)
        else:
            if self.color != "":
                self.df.plot.area(stacked=True, ax=ax, linewidth=self.marker_size, style=self.line_type,
                                  color=self.color)
            else:
                self.df.plot.area(stacked=True, ax=ax, linewidth=self.marker_size, style=self.line_type)


class Hexbin(Graph):
    def draw(self, ax):
        if self.marker_on_off:
            self.df.plot.hexbin(ax=ax, style="o", ms=self.marker_size)
        else:
            if self.color != "":
                self.df.plot.hexbin(ax=ax, style=self.line_type, color=self.color)
            else:
                self.df.plot.hexbin(ax=ax, style=self.line_type)


class Box(Graph):
    def draw(self, ax):
        if not self.marker_on_off:
            self.df.plot.box(ax=ax, style=self.line_type, color=self.color)


class BoxHoriz(Graph):
    def draw(self, ax):
        if not self.marker_on_off:
            self.df.plot.box(vert=False, ax=ax, style=self.line_type, color=self.color)
