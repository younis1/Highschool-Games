
from tkinter import *
mywindow = Tk()
mywindow.geometry("500x500+230+230") # size(a x b) and position on screen
mywindow.title("bas6aweesee")


def greeting():
    from tkinter import Label
    b  = a.get()
    greet = Label(text = " welcome to younis first GUI program ",bg = "pink",fg = "red").pack()
    inp = Label(text = b,bg = "darkblue",fg = "white").pack()

def bye():
    from tkinter import Label
    byebye = Label(text =" Why do you wonna leave me ? :/ ",fg = "white", bg = "black",font =  ("arial",25,"bold")).pack()#type,size,(Italic or Bold)

def save():
    from tkinter import messagebox
    messagebox.showinfo(message = " SAVED", title = " save file ")

def quitgui():
    from tkinter import messagebox
    a = messagebox.askyesno(message = " Do you wonna quit ?", title = " make a decision  ... ")
    if a == 1:
        mywindow.destroy()

def openfile():
    try:
        
        from tkinter import Label, filedialog
        askfile = filedialog.askopenfile()
        filename = askfile.name
        file = open(filename)
        filelabel = Label(text = file.read(), bg = "yellow", fg = "green", font = ("arial",20,"italic")).pack()

    except AttributeError:
        pass
def count(label):
    from tkinter import Label
    def counting():
        global counter, out
        
        if out %  2== 1:
            return None
        counter += 1
        s = str(counter)
        label.config(text = s)       
        label.after(1000,counting)
    if out% 2 == 1:
        return None
    counting()

def stopcounting():
    global out 
    out += 1
    count(countlabel)

def inputcolor():
    from tkinter import colorchooser
    color = colorchooser.askcolor()
    colorlabel = Label(text = "color you have choosen is the background of this label", bg = color[1], width = 40).pack() 


out = 0
counter =0


choosecolorbutton = Button(mywindow,width = 25 , bg = "black", fg = "white", command = inputcolor,text = "choose a color").pack()
stopcount = Button(mywindow,width = 40 , fg = "white", bg = "red",text = "STOP / Continue",command = stopcounting)
stopcount.pack()

countlabel = Label(mywindow,fg = "black", bg = "light blue",width = 50)
countlabel.pack() #if stored in variable with something.pack() .. then None is returned
count(countlabel)



radiolabel = Label(mywindow,text =" Chooose your programming language",font = ("arial",20,"bold")).pack(anchor = "center")
radioresult = IntVar()
radioresult.set(1)
Radiobutton(mywindow,text = "python",padx = 40,variable = radioresult,value = 1).pack(anchor = "center")
Radiobutton(mywindow,text = "matlab",padx = 40,variable = radioresult,value = 2).pack(anchor = "center")
Radiobutton(mywindow,text = "C ++",padx = 40,variable = radioresult,value = 3).pack(anchor = "center")
Radiobutton(mywindow,text = "java",padx = 40,variable = radioresult,value = 4).pack(anchor = "center")



a = StringVar()#string holder
my_menu = Menu()
filelist = Menu()
filelist.add_command(label ="New file")
filelist.add_command(label = "Open file", command = openfile,font = ("arial",20,"italic") )
filelist.add_command(label = "Save file",command = save, font = ("arial",20,"italic"))
formatlist = Menu()
formatlist.add_command(label = "Edit")
formatlist.add_command(label = "italic")
formatlist.add_command(label = "Bond")
helplist = Menu()
helplist.add_command(label = "modules")
helplist.add_command(label = "functions")
helplist.add_command(label = "datatypes")
options = Menu()
options.add_command(label = " setting")
options.add_command(label = "running")
options.add_command(label = "debugging" , font = ("arial",20,"italic"),command = bye)
options.add_command(label = "quit", command = quitgui, font = ("arial",20,"italic"))

my_menu.add_cascade(label= "File",menu = filelist)
my_menu.add_cascade(label= "Format",menu = formatlist)
my_menu.add_cascade(label= "Help",menu = helplist)
my_menu.add_cascade(label= "Options",menu = options)
textbox = Entry(textvariable = a).pack()#textbox
label = Label(text = "Hi everyone  .....",fg = "white",bg = "blue").pack()          #.place(x = 100,y = 100) # can use .pack() for normal setting (in middle) or  .grid(row = ... , column = ...,) may use sticky = direction to solve overlapping i guess which is "w " or "e" or "s","n"
button = Button(text = " enter",fg = "yellow",bg = "green",font = 10,command = greeting).pack()    #for some reason .. font = 10 is not the right way to initialise the font size need to import stuff
#note that command = function with no brackets because we dont need its returned value .. we just need it to be passed
#good practice to pass the object name first in any label buttom etc ...  in this example Entry(mywindow, ....) .. especially when u have more than 1 window .. default goes to the first initialised


mywindow.config(menu = my_menu)
mainloop() # does not close immediately when its open from windows
#fg is front ground , bg back ground
