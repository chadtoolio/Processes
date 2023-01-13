from tkinter import *
from tkinter import filedialog

window = Tk()
window.option_add('*Font' , '35')
window.geometry('400x180')
window.title("Total MINI & BMW Processes and Procedures")


def openFile():


    tech_proc = filedialog.askopenfilename(initialdir="C:\\tmb_ammended_projects\\Processes\\Technician Processes",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt, *.docx"),
                                          ("all files","*.*")))
    file = open(tech_proc,'r')
    print(file.read())
    file.close()


button = Button(text="Tech Procedures",command=openFile)
button.pack(padx=10, pady=10)


def openFile():
    sa_proc = filedialog.askopenfilename(initialdir="C:\\tmb_ammended_projects\\Processes\\Service advisor Processes",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt, *.docx"),
                                          ("all files","*.*")))
    file = open(sa_proc,'r')
    print(file.read())
    file.close()

button = Button(text="Service Advisor Procedures",command=openFile)
button.pack(padx=10, pady=10)

def openFile():
    sa_proc = filedialog.askopenfilename(initialdir="C:\\tmb_ammended_projects\\Processes\\TMB Posted policy",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt, *.docx"),
                                          ("all files","*.*")))
    file = open(sa_proc,'r')
    print(file.read())
    file.close()

button = Button(text="TMB Posted Policy",command=openFile)
button.pack(padx=10, pady=10)


window.mainloop()