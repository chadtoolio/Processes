from tkinter import *
from tkinter import filedialog

def openFile():
    tech_proc = filedialog.askopenfilename(initialdir="C:\\tmb_ammended_projects\\Processes\\Technician Processes",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt, *.docx"),
                                          ("all files","*.*")))
    file = open(tech_proc,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Tech Procedures",command=openFile)
button.pack()

def openFile():
    sa_proc = filedialog.askopenfilename(initialdir="C:\\tmb_ammended_projects\\Processes\\Service advisor Processes",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt, *.docx"),
                                          ("all files","*.*")))
    file = open(sa_proc,'r')
    print(file.read())
    file.close()

button = Button(text="Service Advisor Procedures",command=openFile)
button.grid_slaves(row= 0, column= 0)

def openFile():
    sa_proc = filedialog.askopenfilename(initialdir="C:\\tmb_ammended_projects\\Processes\\TMB Posted policy",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt, *.docx"),
                                          ("all files","*.*")))
    file = open(sa_proc,'r')
    print(file.read())
    file.close()

button = Button(text="TMB Posted Policy",command=openFile)
button.grid_slaves(row=1, column=0)


window.mainloop()