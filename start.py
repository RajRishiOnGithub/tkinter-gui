import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("700x500")
        self.title("Treasure Hunt")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def close(self):
        self.destroy()
        


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame=tk.Frame(self)
        
        self.label=tk.Label(self.frame,text="WELCOME TO INFOTREK'19",fg="green")
        self.label.config(font=("ARDESTINE",20))
        self.label.pack(fill="x",padx=5,pady=10)

        self.frame.pack()

        self.bottomframe=tk.Frame(self)

        self.button1=tk.Button(self.bottomframe,text="LOGIN",width=10,command=lambda:controller.show_frame("PageOne"))
        self.button1.grid(row=0,padx=5,pady=350)

        self.button2=tk.Button(self.bottomframe,text="REGISTER",width=10,command=lambda:controller.show_frame("PageTwo"))
        self.button2.grid(row=0,column=1,padx=5,pady=350)
        
        self.button3 = tk.Button(self.bottomframe, text="EXIT",
                            command=lambda: controller.close())
        self.button3.grid(row=0,column=2,padx=5,pady=350)

        self.bottomframe.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frame=tk.Frame(self)
        
        self.label=tk.Label(self.frame,text="LOG IN",fg="black")
        self.label.config(font=("ARDESTINE",25))
        self.label.pack(fill='x',padx=5,pady=20)

        self.frame.pack()

        self.bottomframe=tk.Frame(self)
        
        self.label1=tk.Label(self.bottomframe,text="ROLL NO : ",fg="blue")
        self.label1.grid(row=0,column=0,padx=5,pady=50)
        
        self.entry1=tk.Entry(self.bottomframe)
        self.entry1.grid(row=0,column=1,padx=5,pady=20)

        self.label2=tk.Label(self.bottomframe,text="PASSWORD : ",fg="blue")
        self.label2.grid(row=1,padx=50,pady=55)
        
        self.entry2=tk.Entry(self.bottomframe)
        self.entry2.grid(row=1,column=1,padx=5,pady=55)

        self.button1=tk.Button(self.bottomframe,text="SUBMIT",width=10,command='')#lambda:controller.show_frame( ))
        self.button1.grid(row=2,column=0,padx=5,pady=70)

        self.button2=tk.Button(self.bottomframe,text="HOME",width=10,command=lambda:controller.show_frame("StartPage"))
        self.button2.grid(row=2,column=1,padx=5,pady=70)


        self.bottomframe.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frame=tk.Frame(self)
        self.label=tk.Label(self.frame,text="SIGNUP",fg="black")
        self.label.config(font=("ARDESTINE",25))
        self.label.pack(fill='x',padx=5,pady=20)

        self.frame.pack()

        self.bottomframe=tk.Frame(self)

        self.label0=tk.Label(self.bottomframe,text="NAME : ",fg="blue")
        self.label0.grid(row=0,padx=5,pady=5)

        self.entry0=tk.Entry(self.bottomframe)
        self.entry0.grid(row=0,column=1,padx=5,pady=5)
                         
        
        self.label1=tk.Label(self.bottomframe,text="ROLL NO : ",fg="blue")
        self.label1.grid(row=1,column=0,padx=5,pady=5)
        
        self.entry1=tk.Entry(self.bottomframe)
        self.entry1.grid(row=1,column=1,padx=5,pady=5)

        self.label2=tk.Label(self.bottomframe,text="PASSWORD : ",fg="blue")
        self.label2.grid(row=2,padx=5,pady=5)
        
        self.entry2=tk.Entry(self.bottomframe)
        self.entry2.grid(row=2,column=1,padx=5,pady=5)

        self.button1=tk.Button(self.bottomframe,text="SUBMIT",width=10,command=' ')
        self.button1.grid(row=3,column=0,padx=5,pady=70)

        self.button2=tk.Button(self.bottomframe,text="HOME",width=10,command=lambda:controller.show_frame("StartPage"))
        self.button2.grid(row=3,column=1,padx=5,pady=70)


        self.bottomframe.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
