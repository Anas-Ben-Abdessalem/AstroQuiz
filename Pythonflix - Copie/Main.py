from tkinter import *
color = "#2ecc72"

class App(Tk):
    def __init__(self,*args,**kwrgs):
        Tk.__init__(self,*args,**kwrgs)
        Tk.configure(self, bg = color)
        container = Frame(self)
        container.pack(side = "top",fill = "both",expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        self.frames = {}
        for F in (StartPage, PageOne):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self,parent, controller):
        self.controller = controller
        Frame.__init__(self,parent,)
        Tk.configure(self,  bg=color)
        self.frame1 = Frame(self, padx=(self.winfo_screenwidth() - 608) / 3,
                            pady=(self.winfo_screenheight() - 180) / 2.5, bg=color)
        self.frame1.pack()
        self.button_user = Button(self.frame1, text = "Create an account" ,bg = "#E74292", bd = 0,
                                 font = "Arial 20", fg = "white",  width = 20)
        self.button_user.pack()
        spacer = Label(self.frame1,height = 0 ,bg = color )
        spacer.pack()
        self.button_login = Button(self.frame1, text = "Log In" ,bg = "#E74292", bd = 0,width = 20,
                                 font = "Arial 20", fg = "white")
        self.button_login.pack()
        self.frame0 = Frame(self,bg = color, pady = 70)
        self.frame0 .pack(side =TOP, fill = 'both')
        self.label12 = Label(self.frame0,text = "",bg = "blue",font = Large_Font,fg = "white",
                             pady = 20, padx = 20)
        self.label12.pack()

class PageOne(Frame):
    def __init__(self,parent, controller):
        self.controller = controller
        Frame.__init__(self,parent)
        Tk.configure(self,  bg=color)


app = App()
app.update()
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
x = 0
y = 0
app.geometry("%dx%d+%d+%d" % (width,height,x,y))
app.mainloop()
app.mainloop()