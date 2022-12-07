import model
class Input:
    def x_to_y(self):
        f = 0
        for frame in self.frames:
            if not f:
                print("x_to_y:", "x", frame.graph.y, "y", frame.graph.y)
                f = 1

            if frame.graph.y and frame.graph.y:
                frame.graph.x, frame.graph.y = frame.graph.y, frame.graph.x
        print("x", frame.graph.x, "y", frame.graph.y)
        # pass

    def y1_to_y2(self):
        f = 0
        for frame in self.frames:
            if not f:
                print("y1_to_y2", "y1", frame.graph.y[0], "y2", frame.graph.y[1])
                f = 1

            if frame.graph.y[0] and frame.graph.y[1]:
                frame.graph.y[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.y[0]
        print("y1", frame.graph.y[0], "y2", frame.graph.y[1])
        # pass

    def x1_to_y2(self):
        #
        f = 0
        for frame in self.frames:
            if not f:
                print("x1_to_y2", "x1", frame.graph.x[0], "y2", frame.graph.y[1])
                f = 1
            if frame.graph.x[0] and frame.graph.y[1]:
                frame.graph.x[0], frame.graph.y[1] = frame.graph.y[1], frame.graph.x[0]
        print("x1", frame.graph.x[0], "y2", frame.graph.y[1])
        # pass

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
