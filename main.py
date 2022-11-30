import tkinter as tk
import tkinter.messagebox
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import os
import pandas as pd

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):

    APP_NAME = "Easy plot"
    WIDTH = 900
    HEIGHT = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)
        self.maxsize(App.WIDTH, App.HEIGHT)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # load image with PIL and convert to PhotoImage
        #image = Image.open(PATH + "/test_images/bg_gradient.jpg").resize((self.WIDTH, self.HEIGHT))
        #self.bg_image = ImageTk.PhotoImage(image)

        #self.image_label = tkinter.Label(master=self, image=self.bg_image)
       # self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.app = customtkinter.CTk()

        self.frame = customtkinter.CTkFrame(master=self,
                                            width=300,
                                            height=App.HEIGHT,
                                            corner_radius=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.graph_frame = customtkinter.CTkFrame(master=self,
                                            width=100,
                                            height=100,
                                            corner_radius=0)
        self.graph_frame.place(relx=0, rely=0, anchor=tkinter.CENTER)

        self.label_1 = customtkinter.CTkLabel(master=self.frame, width=200, height=60,
                                              fg_color=("gray70", "gray25"), text="CustomTkinter\ninterface example")
        self.label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame, corner_radius=6, width=200, placeholder_text="username")
        self.entry_1.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame, corner_radius=6, width=200, show="*", placeholder_text="password")
        self.entry_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.button_2 = customtkinter.CTkButton(master=self.frame, text="Login",
                                                corner_radius=6, command=self.button_event, width=200)
        self.button_2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


        #canvas = FigureCanvasTkAgg(plt.plot(np.linspace(0,100,10),np.linspace(0,100,10)), self.graph_frame)
       # canvas.get_tk_widget().place(x=0, y=0, width=100, height=100)
  #  plt.figure.
        data1 = {'country': ['A', 'B', 'C', 'D', 'E'],
                 'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
                 }
        df1 = pd.DataFrame(data1)
        root = self.app

        figure1 = plt.Figure(figsize=(5, 5), dpi=100)
        ax1 = figure1.add_subplot(222)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack()
        df1.plot(kind='bar', legend=True, ax=ax1)
        canvas = customtkinter.CTkCanvas(root, width=200, height=200, bg='white')
        #canvas.
        canvas.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        ax1.set_title('Country Vs. GDP Per Capita')
        root.mainloop()



    def button_event(self):
        print("Login pressed - username:", self.entry_1.get(), "password:", self.entry_2.get())

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()