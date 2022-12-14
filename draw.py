import matplotlib as plt
from matplotlib import style
import main
plt.use('Qt5Agg')


class Draw:

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
            except:
                continue
        self.change_theme(graphs[0].theme)
        model.Graphs = graphs

    def change_theme(self, theme):
        plt.style.use(theme)