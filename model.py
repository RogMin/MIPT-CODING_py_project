import main
import draw


class Model:
    def __init__(self):
        self.Graphs = []
        self.marker_sz = 2
        self.theme = "bmh"
        self.color = ''
        self.xlabel = ""
        self.ylabel = ""
        self.line_type = ''
        self.df = None
        self.draw = draw.Draw()
        self.vertical_lay = None
        self.marker_on_off = False

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

    def clear_graphs(self):
        """Dell old graphics"""
        for graph in self.Graphs:
            graph.vertical_lay.removeWidget(graph.frame)
            graph.vertical_lay.removeWidget(graph.toolbar)
            graph.vertical_lay.update()
        self.Graphs = []

    def init_graphs(self):
        """Create graphics prefabs"""
        self.clear_graphs()
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
    def __init__(self):
        self.marker_size = 2
        self.x_lbl = ""
        self.y_lbl = ""
        self.theme = "bmh"
        self.line_type = ''
        self.color = ""
        self.vertical_lay = None
        self.canvas = None
        self.frame = None
        self.df = None
        self.toolbar = None
        self.marker_on_off = False

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
