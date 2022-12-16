import matplotlib as plt
from matplotlib import style
import main
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Navi

plt.use('Qt5Agg')


class Draw:
    """Draws graphs from model

        :graphs: a graph from an array of graphs from model(not changed)
        :model: link to model
    """
    def visualise(self, graphs, model):
        self.change_theme(graphs[0].theme)
        for graph in graphs:
            try:
                graph.frame = main.QtWidgets.QFrame()  # Create new frame
                lay = main.QtWidgets.QStackedLayout(graph.frame)  # Set frame layout
                lay.addWidget(graph.canvas)
                graph.frame.setMinimumHeight(graph.canvas.get_width_height()[1])  # Set minimum height to graphic frame
                graph.vertical_lay.addWidget(graph.frame)
                ax = graph.canvas.axes
                ax.cla()
                ax.set_xlabel(graph.x_lbl)
                ax.set_ylabel(graph.y_lbl)
                legend = ax.legend()
                legend.set_draggable(True)
                graph.draw(ax)
                self.draw_toolbar(graph)
                if graph.toolbar.canvas is None:
                    print("Application cannot draw this plot. The plot is empty")
            except:
                graph.vertical_lay.removeWidget(graph.frame)
                graph.vertical_lay.removeWidget(graph.toolbar)
                graph.vertical_lay.update()
                graphs.remove(graph)
                continue
        model.Graphs = graphs

    def draw_toolbar(self, graph):
        """Draws nav2tools from matplotlib

        :graph: a graph from an array of graphs from model
        """
        graph.toolbar = Navi(graph.canvas, graph.frame)
        graph.vertical_lay.addWidget(graph.toolbar)


    def change_theme(self, theme):
        """Sets the theme in matplotlib

        :theme: matplotlib theme as a string
        """
        plt.style.use(theme)
