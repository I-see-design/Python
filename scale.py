import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scale")
        self.geometry("600x350")
        self.minsize(600, 350)
        self.configure(fg_color='#242222')


        self.main = Scale(self)


        self.mainloop()



class Scale(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master = master, width=500, height=250, fg_color='#474545',
                         corner_radius=8)

        self.unit_lb = ctk.CTkLabel(master=self,
                                    text="Deg to F\n\n",
                                    text_color='#e8e2e1',
                                    font=('Helvetica', 25, 'bold'))
        self.unit_lb.pack(pady=30)

        self.scale = ctk.CTkSlider(master=self,
                                   from_=0,
                                   to=100,
                                   hover=True,
                                   button_hover_color='#657c82',
                                   button_color='#a5c0c7',
                                   command=self.convert)
        self.scale.pack(expand = True, fill = 'x', padx = 20)


        self.pack(expand = True)
        self.pack_propagate(False)


    def convert(self, value):
        deg = value * 33.8
        self.unit_lb.configure(text=f'Deg to F\n\n{round(value, 1)}Deg = {round(deg, 1)}F')


App()