from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
from random import *
import numpy as np
color = "purple"
Large_Font = "Arial"
white = "white"
score = 0
score_sys = 0
num = ""
a = 0

def remove (o,string):
    list1 = list(string)
    v = list1.count(o)
    for i in range(v):
        list1.remove(o)
    return''.join(list1)


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
        self.list3 = []
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
        self.image = self.image1.resize((self.winfo_screenwidth() -20, self.winfo_screenheight() -80), Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image = self.render, bd = 0)
        self.img.image = self.render
        self.img.place(x = 0, y = 0)
        self.label11 = Label(self, text = "Créé par Anas Ben Abdisselem" , font = "Arial 20" ,
                           padx = 20,pady = 20, bg = color , fg = white)
        self.label11.place(x = (self.winfo_screenwidth() - 20 - 393)/2,
                         y =  (self.winfo_screenheight() - 80 - 476)/4)
        self.label = Label(self, text = "Assosciation Jeunes Science" , font = "Arial 20" ,
                           padx = 20,pady = 20, bg = color , fg = white)
        self.label.place(x = (self.winfo_screenwidth() - 20 - 373)/2,
                         y =  (self.winfo_screenheight() - 80 - 76)/4)
        self.label1 = Label(self, text = "Informatique et\nAstronomie", font = "Arial 60", bg = "black",fg = "white", padx = 10,pady=10)
        self.label1.place(x = (self.winfo_screenwidth() - 20 - 373 - 130)/2,
                         y =  (self.winfo_screenheight() - 80 - 76 + 340)/4)
        self.frame2 = Frame(self, bg = "purple", padx = 10, pady = 5)
        self.frame2.place(x = (self.winfo_screenwidth() - 20 - 373 - 25 - 160)/2,
                         y =  (self.winfo_screenheight() - 80 - 76 + 340 + 887)/4)
        self.label2 = Label(self.frame2,text = "Combien de quetions veux-tu répondre de 25 ?" , font = "Arial 20" ,
                            bg = color , fg = "white" , pady = 5)
        self.label2.pack(side=TOP)
        self.frame5= Frame(self.frame2 ,pady = 5 , bg = color)
        self.frame5.pack(side = TOP )
        self.entry = ttk.Entry(self.frame5 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = TOP)
        self.label4 = Label(self.frame5, bg = color ,text = "", font = "Arial 15", fg = "#67E6DC" )
        self.label4.pack(side = TOP)
        self.frame4 = Frame(self.frame2, bg = color , pady = 5)
        self.frame4.pack(side = TOP)


        self.button = Button(self.frame4, text = "Commencer", font = "Arial 20", bd = 2, padx = 10,pady=10, width = 10 ,bg = "#8B78E6", fg = white,
                             relief = "solid", command = self.start )
        self.button.pack(side = TOP)

    def start(self):
        global num
        global score_sys
        global app
        global a
        num = self.entry.get()
        num = remove(" ", num)
        score_sys = 100 / int(num)
        if int(num) < 26:
            if int(num) < 10:
                self.label4['text'] = "Monsieur! le minimum des questions est 10"
            else:
                while True:
                    page = choice(np.array([Page1 , Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page8, Page9, Page10, Page11, Page12,
                                         Page13,Page14,Page15, Page16, Page17, Page18, Page19, Page20,
                                         Page21, Page22, Page23, Page24, Page25]))
                    if page not in app.list3:
                        app.list3.append(page)
                    if len(app.list3) == int(num):
                        app.list3.append(QuitPage)
                        frame = app.list3[a](app.container,app)
                        app.frames[app.list3[a]] = frame
                        frame.grid(row = 0, column = 0, sticky = "nsew")
                        self.controller.show_frame(app.list3[a])
                        break
                        
        elif int(num) > 25 :
            self.label4['text'] = "Monsieur! le maximum des questions est 25"




class Page1(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
De quoi est composée la terre?

1- Azote , fer ,souffre , 
oxygéne , silicium , aluminium
et de dioxyde de carbone

2- Fer, oxygène, souffre,
nickel, calcium, aluminium,
maniésium et de silicium

3- Dioxyde de carbone, oxygène,
magnésium, aluminium, calcium
et de silicium 

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1
        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2":
            score += score_sys
            o()
            if o() == True:
                self.controller.show_frame(app.list3[a])
                self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])






class Page2(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg = color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quel est le satellite naturel de la terre ?
1- Titan

2- Lo

3- Lune

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1
        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])




class Page3(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Comment s'appelle notre galaxie ?
1- Androméde

2- Tournesol

3- Voie Lactée

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1
        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])






class Page4(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Combien y a t-il des planètes ? 

1- 7

2- 6

3- 8

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])



class Page5(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quelle et la plus grande planéte ?

1- Neptune

2- Saturne

3- Jupiter

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1

        if info == "3" :
            score += score_sys
        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])




class Page6(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Qu' est ce qu'une galaxie

1- Ensemble d'étoiles

2- Ensemble de trous noir

3- Ensemble de planéte

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])



class Page7(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quelle est la différnce entre une étoile 
et une planéte ?

1- Une étoile produit de
la lumière , tandis qu'une planète
reflète celle de Soleil

2- Les étoiles sont plus grandes 
que les planètes

3-  Une planéte produit de
la lumière , tandis qu'une étoile
reflète celle de Soleil

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])




class Page8(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quelle est la planète la plus chaude

1- Mercure

2- Mars

3- Vénus

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])



class Page9(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Qu'appelle t-on "l'étoile du berger" ?
1- Terre

2- Vénus

3- Jupiter

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])


class Page10(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Qu'appelle t-on "unité astronomique" ?

1- Unité utilisée pour mesurer 
les distances entre les objets 
du systéme solaire et notre planète

2- Une unité utilisée pour
mesurer les distances entre
les objets du systéme solaire

3- Unité utilisée pour mesurer
la distance entre Terre et Lune 
ou soleil

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])




class Page11(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Qu' est ce qu'un Trou noir ?

1- Une exoplanéte 

2- Région de l'espace tellement dense
qu'aucun rayonnement n' en sort

3- Région de l'espace tellement dense
que tous rayonnement n' en sort 

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])




class Page12(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quelle sont les planète qui 
possèdent des anneaux ?

1- Uranus, Jupiter,
Neptune et saturne
 
2- Uranus, Mercure,
Neptune et Saturne

3- Mercure, Vénus,
Neptune et Sature

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0

        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])


class Page13(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Pourquoi les étoiles brillent-elles ?

1- Elles brillent grâce au
rayonnement du soleil

2- Elles brillent grâce aux 
satellites naturels  

3- Elles brillent car leurs
surface est composée de gaz 
ionisé de haute température

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page14(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quels sont les phases de la lune

1- La Nouvelle lune ,
le premier croissant,le premier quartier, 
la lune gibbeuse décroissante,
le Dernier quartier,le Dernier croissant

2- La Nouvelle Lune, le Premier quartier,
le Dernier quartier,la plaine Lune

3- La Nouvelle Lune, le Premier croissant,
le Dernier croissant, la plaine Lune

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page15(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Où se trouve la ceinture d'astéroides ?

1- A côté du Trou Noir

2- Entre terre et Vénus

3- Entre Mars et Jupiter

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page16(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Cembien de temps met la lumière 
du soleil à nous parvenir ?

1- 15 min

2- 8 min

3- 10 min

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page17(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Comment s'appellent les 5 planètes ?

1- Europe, Ganymède, 
Pluton, Titan 
et Arial

2- lo, Andromède,
Makémaké, Eris 
et Pluton 

3- Cérès, Pluton,
Hauméa, Makémaké
et Eris

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page18(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quelle est la planète la plus proche de la nôtre ?

1- Titan

2- Andromède

3- Grand Nuage de Magellan

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])
class Page19(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quels est les trois type de 
transmission de chaleur ?

1- Par radiation ,
par convection et 
par contact 

2- Par radiation ,
par lumière et 
par contact 

3- Par radiation ,
par plazma et 
par contact 

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])


class Page20(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Qu'est-ce-qu'un Plasma ? 

1- Gaz ionisé à haute température

2- Une étoile

3- Une galaxie

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page21(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Dans quel état une étoile comme le soleil 
finie sa 'vie' ?

1- Elle refoidit 
jusqu'à s'éteindre 

2- Elle s'échauffe
jusqu'à s'éteindre

3- Elle s'échauffe 
jusqu'à s'explose

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])
class Page22(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quelle est la forme de notre galaxie ?

1- Spirale barré

2- Cerclée

3- Elliptique

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "1" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])

class Page23(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Où se trouve le plus grand volcan du
systeme Solaire?
 
1- Vénus

2- Mars

3- Mercure

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])
class Page24(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quels sont les quatres satellites 
galiléens du Jupiter ?

1- Titan, Europe,
Andromède et lo

2- lo, Europe,
Ganymède et Callisto

3- Callisto, Arial,
Triton et Titan

Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1


        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "2" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])


class Page25(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.configure(bg=color)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() - 20, self.winfo_screenheight() - 80),
                                        Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image=self.render, bd=0)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.frame1 = Frame(self,bg = color)
        self.frame1.place(x = 20,
                         y = 20)
        self.label = Label(self.frame1, text="""Choisie une suggession de 1 - 3 
Quels sont les 6 types de lumière?

1-  Rayons Z, Rayon U,
Ultra-Violets, Visible,
Infra-rouge

2- Rayons M, Rayon A,
Ultra-Violets, Visible,
Infra-rouge 

3- Rayons Y, Rayon X,
Ultra-Violets, Visible,
Infra-rouge
 
Saisie 1 , 2 , 3 pour répondre""", font="Arial 20",padx=20, pady=10, bg=color, fg=white , justify = LEFT)
        self.label.pack(side = TOP)
        self.frame2 = Frame(self.frame1, bg = color , padx = 20)
        self.frame2.pack(side = TOP, fill = "both")
        self.label1 = Label(self.frame2,text = "Deviner:", font = "Arial 20" , bg = color , fg = "white" , pady = 10 )
        self.label1.pack(side = LEFT)
        self.entry = ttk.Entry(self.frame2 , font = "Arial 15" , width = 8 )
        self.entry.pack(side = LEFT)
        self.label2 = Label(self.frame2,text = "", font = "Arial 20" , bg = color , fg = "#EA7773" , pady = 10 )
        self.label2.pack(side=LEFT)
        self.button = Button(self, text="Suivant>>", font="Arial 30", bd = 0, padx= 5, pady= 5, width=10,
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
        anas = self.entry.get()
        info = remove(" ", anas)
        i = 0


        a += 1
        frame = app.list3[a](app.container,app)
        app.frames[app.list3[a]] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")

        def o():
            frame = app.list3[a](app.container,app)
            app.frames[app.list3[a]] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        if info == "3" :
           score += score_sys
           o()
           if o() == True :
               self.controller.show_frame(app.list3[a])
               self.entry.delete(0, END)
        elif int(info) > 3:
            self.label2['text'] = "Mr saisie 1,2 où 3"
            a -= 1
        else:
            o()
            self.controller.show_frame(app.list3[a])



class QuitPage(Frame):

    def __init__(self,parent, controller):
        global score
        self.controller = controller
        Frame.__init__(self,parent)
        self.image1 = Image.open("BG.jpg")
        self.image = self.image1.resize((self.winfo_screenwidth() -20, self.winfo_screenheight() -80), Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.image)
        self.img = Label(self, image = self.render, bd = 0)
        self.img.image = self.render
        self.img.place(x = 0, y = 0)
        if int(score) > 50 :
            if int(score) > 80 :
                mark = "était bon nous (l'Assosciation) sommes fiers de toi et de tes efforts\n"
            else :
                mark = "était +- bon pour un menbre des Jeunes Sciences!\n"
        else:
            mark = "N'était pas bon pour un menbre des Jeunes Sciences!\n" \
                   "Allez améliorer votre pensée astronomique \n" \
                   "Et essayez le jeux une autre fois"
        self.frame1 = Frame(self, bg = color)
        self.frame1.place(x = (self.winfo_screenwidth() - 20 - 573)/2,
                         y =  (self.winfo_screenheight() - 80 - 76)/4)
        self.label = Label(self.frame1, text = f"Ok tu as répondu à {str(int(score))}% des questions et ça \n{mark}" , font = "Arial 20" ,
                           padx = 20,pady = 20, bg = color , fg = white)
        self.label.pack(side = TOP)
        self.label1 = Label(self, text = "Créé par Anas Ben Abdisselem " , bg = color, fg = "white" , font= "Arial 20")
        self.label1.place(x = (self.winfo_screenwidth() - 20 - 373)/2,
                         y =  (self.winfo_screenheight() - 80 - 276)/4)


app = SeaofBTCapp()

app.title("Anas Quiz")
app.update()
width = app.winfo_screenwidth() - 20
height = app.winfo_screenheight() - 80

x = 0
y = 0
app.geometry("%dx%d+%d+%d" % (width,height,x,y))
app.resizable(width = False, height = False)
app.mainloop()

