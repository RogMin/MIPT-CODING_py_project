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
=======

>>>>>>> origin/main
