from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import random
color = "purple"
Large_Font = "Arial"
white = "white"
score = 0
score_sys = 0
num = ""
a = 0
class SeaofBTCapp(Tk):
    def __init__(self,*args,**kwrgs):
        global num
        Tk.__init__(self,*args,**kwrgs)
        self.container = Frame(self)
        self.container.pack(side = "top",fill = "both",expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0,weight = 1)
        self.frames = {}
        self.list2 = [Start]
        self.list1 = []
        for F in self.list2:
            frame = F(self.container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(Start)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class Start(Frame):

    def __init__(self,parent, controller):

        self.controller = controller
        Frame.__init__(self,parent)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() -20, self.winfo_screenheight() -80), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image = self.render, bd = 0)
        self.img.image = self.render
        self.img.place(x = 0, y = 0)
        self.label = Label(self, text = "Assosciation Jeunes Science" , font = "Arial 20" ,
                           padx = 20,pady = 20, bg = color , fg = white)
        self.label.place(x = (self.winfo_screenwidth() - 20 - 373)/2,
                         y =  (self.winfo_screenheight() - 80 - 76)/4)
        self.label1 = Label(self, text = "Astronomie", font = "Arial 60", bg = "black",fg = "white", padx = 10,pady=10)
        self.label1.place(x = (self.winfo_screenwidth() - 20 - 373 - 25)/2,
                         y =  (self.winfo_screenheight() - 80 - 76 + 340)/4)
        self.frame2 = Frame(self, bg = "purple", padx = 10, pady = 5)
        self.frame2.place(x = (self.winfo_screenwidth() - 20 - 373 - 25 - 250)/2,
                         y =  (self.winfo_screenheight() - 80 - 76 + 340 + 487)/4)
        self.label2 = Label(self.frame2,text = "How many questions do you wanna answer from 25 ?" , font = "Arial 20" ,
                            bg = color , fg = "white" , pady = 5)
        self.label2.pack(side = TOP)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = TOP)


        self.button = Button(self, text = "Start", font = "Arial 30", bd = 2, padx = 10,pady=10, width = 10 ,bg = "#8B78E6", fg = white,
                             relief = "solid", command = self.start )
        self.button.place(x = (self.winfo_screenwidth() - 20 - 373 + 130)/2,
                         y =  (self.winfo_screenheight() - 80 - 76 + 1307)/4)
    def start(self):
        global num
        global score_sys
        global app
        num = self.entry.get()
        score_sys = 100 / int(num)
        while True:
            page = random.choice([Page1 , Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page8, Page9, Page10, Page11, Page12,
                                 Page13,Page14,Page15, Page16, Page17, Page18, Page19, Page20,
                                 Page21, Page22, Page23, Page24, Page25])
            if page not in app.list1:
                app.list1.append(page)
            if len(app.list1) == int(num):

                app.list1.append(QuitPage)
                for F in app.list1:
                    frame = F(app.container,app)
                    app.frames[F] = frame
                    frame.grid(row = 0, column = 0, sticky = "nsew")
                self.controller.show_frame(app.list1[0])
                break


class Page1(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list1[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page2(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page3(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page4(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page5(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page6(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page7(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page8(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page9(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page10(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page11(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page12(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page13(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page14(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page15(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page16(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page17(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page18(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page19(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page20(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "3":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page21(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page22(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page23(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1
class Page24(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "2":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1

class Page25(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choose a suggession from 1 - 3 
qsfz'rgdfbe
1-
2-
3-
Type 1 , 2 or 3 to answer""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack()
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(fill = "both")
        self.label1 = Label(self.frame2,text = "Guess:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Next >>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
                              bg = "#D63031", fg = "white" , command = self.Next)
        self.button.place(x = 1346 - 260,
                         y =  688 - 99)
        """self.button1 = Button(self, text="<< Previous ", font="Arial 30", bd = 0, padx = 5 , pady = 5 ,
                              bg = "#D63031" ,width=10, fg = "white")
        self.button1.place(x = 1346 - 260*2 -20,
                          y = 688 - 99)"""
    def Next(self):
        global score
        global score_sys
        global num
        global a
        info = self.entry.get()
        i = 0

        if info == "1":
            if i < 2 :
                self.controller.show_frame(app.list[a+1])
                score += score_sys
                self.entry.delete(0, END)
            else:
                self.controller.show_frame(app.list1[a+1])
        else:
            i += 1
            self.entry.delete(0, END)
            self.label2['text'] = "False! Try again"
        a += 1


class QuitPage(Frame):

    def __init__(self,parent, controller):
        global score
        self.controller = controller
        Frame.__init__(self,parent)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() -20, self.winfo_screenheight() -80), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image = self.render, bd = 0)
        self.img.image = self.render
        self.img.place(x = 0, y = 0)
        if int(score) > 50 :
            if int(score) > 80 :
                mark = "good man we (the Assosciation) are proud with your efforts"
            else :
                mark = "pretty good for a Jeunes Science member !"
        else:
            mark = "not good for a Jeunes Science member !\n" \
                   "Go and improve your knowlage in Astronomy\n" \
                   "and try the game up again"
        self.frame1 = Frame(self, bg = color)
        self.frame1.place(x = (self.winfo_screenwidth() - 20 - 373)/2,
                         y =  (self.winfo_screenheight() - 80 - 76)/4)
        self.label = Label(self.frame1, text = f"Ok you have answered {str(int(score))}% of the questions and that's {mark}" , font = "Arial 20" ,
                           padx = 20,pady = 20, bg = color , fg = white)
        self.label.pack(side = TOP)





app = SeaofBTCapp()

app.title("Q&A")
app.update()
width = app.winfo_screenwidth() -20
height = app.winfo_screenheight() - 80

x = 0
y = 0
app.geometry("%dx%d+%d+%d" % (width,height,x,y))
app.resizable(width = False, height = False)

app.mainloop()

