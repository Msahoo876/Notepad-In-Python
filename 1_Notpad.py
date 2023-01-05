from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile,askopenfile
from datetime import datetime

def new():
    win.title("Untitled - Notepad")
    t1.delete(1.0,END)

def save():
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')]
    file1 = asksaveasfile(mode='w',initialfile='Untitled.txt',filetypes=files,defaultextension = files)
    save = str(t1.get(0.0,END))
    file1.write(save)
    file1.close()
    t1.delete(0.0,END)

def open():
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')]
    file1 = askopenfile(mode='r',filetypes=files)
    if file1 is not None:
        content = file1.read()
        t1.insert(END,content)

def exit():
    win.quit()

def cut():
    t1.event_generate("<<Cut>>")

def copy():
    t1.event_generate("<<Copy>>")

def paste():
    t1.event_generate("<<Paste>>")

def delete():
    t1.delete(1.0,END)

# def fonti():
#     a = QFontDialog.getFont()
#     t1.delete(0.0,END)
#     t1.insert(END,a)

# def bcolor():
#     rgb_color = colorchooser.askcolor(parent=win,initialcolor=(255, 0, 0))
#     t1.delete(0.0,END)
#     t1.insert(END,rgb_color)

def datetime1():
    a = datetime.now()
    t1.delete(0.0,END)
    t1.insert(END,a)

def select_all(event):
    t1.select_range(0.0,END)

def view():
    s = "Notepad is a very basic text editor that has been part of Windows for a very long time. It is excellent for writing relatively short text documents that you want to save as plain text, and that is not all you can do with it. If you have not used Notepad much, you may be surprised by how easy it is to work with. Let's take a new look at this old desktop app for Windows, what it is, and what it does"
    t1.delete(0.0,END)
    t1.insert(END,str(s))

def about():
    s = "Notepad is a simple text editor for Microsoft Windows and a basic text-editing program which enables computer users to create documents. It was first released as a mouse-based MS-DOS program in 1983, and has been included in all versions of Microsoft Windows since Windows 1.0 in 1985."
    t1.delete(0.0,END)
    t1.insert(END,str(s))
    

    
win =  Tk()
win.title("Untitled - Notepad")
win.geometry("600x700")


m1 = Menu(win)

filem1 =Menu(m1,tearoff=0)
filem1.add_command(label="New",command=new)
filem1.add_separator()
filem1.add_command(label="Open",command=open)
filem1.add_separator()
filem1.add_command(label="Save",command=save)
filem1.add_separator()
filem1.add_command(label="Save as...",command=save)
filem1.add_separator()
filem1.add_command(label="Exit",command=exit)
m1.add_cascade(label="File", menu=filem1)

editm1 = Menu(m1,tearoff=0)
m1.add_cascade(label="Edit",menu=editm1)
editm1.add_command(label="Cut",command=cut)
editm1.add_separator()
editm1.add_command(label="Copy",command=copy)
editm1.add_separator()
editm1.add_command(label="Paste",command=paste)
editm1.add_separator()
editm1.add_command(label="Delete",command=delete)
editm1.add_separator()
editm1.add_command(label="Time/Date",command=datetime1)
editm1.add_separator()
editm1.add_command(label="UNDO")

# formatm1 = Menu(m1,tearoff=0)
# m1.add_cascade(label="Format",menu=formatm1)
# formatm1.add_command(label="Font..",command=fonti)
# formatm1.add_separator()
# formatm1.add_command(label="BackColor",command=bcolor)

helpm1 = Menu(m1,tearoff=0)
m1.add_cascade(label="Help",menu=helpm1)
helpm1.add_command(label="View Help",command=view)
helpm1.add_separator()
helpm1.add_command(label="About Notpad",command=about)


win.config(menu=m1)

t1 = Text(win)
t1.place(x=0,y=0,width=600,height=700)
t1.bind("<Control-a>",select_all)


win.mainloop()