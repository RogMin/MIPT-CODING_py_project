import data
import matplotlib.pyplot as plt
class Model:
    def __init__(self, color=0, xlabel="", ylabel="", x=[np.ones(5), 5 * np.ones(5)],
                 y=[5 * np.ones(5), np.ones(5)]):
        self.color = color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x = x
        self.y = y

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

    def set_x_label(self):
        if len(self.frames) > 0:
            for frame in self.frames:
                frame.graph.x_lbl = self.x_label_inp.text()
            self.Update()

    def set_y_label(self):
        if len(self.frames) > 0:
            for frame in self.frames:
                frame.graph.y_lbl = self.y_label_inp.text()
            self.Update()

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
