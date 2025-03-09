

from tkinter import *
from tkinter import messagebox

win = Tk()
#========================================
win.geometry("200x200")
win.title("امام علی")
win.resizable(0,0)
#========================================
def done():
    g = 0
    if py.get() == 1:
        g+=2000
    if c.get() == 1:
        g+=2300
    if jv.get() == 1:
        g+=1500
    messagebox.showinfo("شهریه",f"شهریه شما {g}است.")
    # s = 0
    # g = 0
    # dic = {"py":2000,"c":2300,"jv":1500}
    # name = ["py","c","jv"]
    # lst = [py.get(),c.get(),jv.get()]
    # for i in lst:
    #     if i == 1:
    #         g += dic[name[s]]
    #     s+=1
    # messagebox.showinfo("شهریه",f"شهریه شما {g}است.")
#========================================
py = IntVar()
c = IntVar()
jv = IntVar()
chb_python = Checkbutton(win,text="python",variable=py)
chb_csharp = Checkbutton(win,text="C#",variable=c)
chb_java = Checkbutton(win,text="Java",variable=jv)

btn_done = Button(win,text="Done",command=done)

chb_python.grid(row=0,column=0)
chb_csharp.grid(row=0,column=1,padx=10)
chb_java.grid(row=0,column=2)

btn_done.grid(row=1,column=1)


win.mainloop()





















































win.mainloop()