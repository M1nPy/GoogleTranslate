import tkinter as tk
#from concurrent.futures import ThreadPoolExecutor
import sys
import time
import subprocess
import urllib.parse
from tkinter import font

#tpe=ThreadPoolExecutor(max_workers=1)
worldlist=["ja","en","ru","zh-CN","eo","de","la","sw","ar","ka"]
# tpe.submit()
root=tk.Tk()
root.title('honyakukonyaku')
root.resizable(0,0)
root.geometry("800x500")
menubar = tk.Menu(root)
menu_selw1=tk.Menu(menubar,tearoff=False)
menu_selw2=tk.Menu(menubar,tearoff=False)
menu_selw_=tk.Menu(menubar,tearoff=False)
root.config(menu=menubar)

menubar.add_cascade(label="Source",menu=menu_selw1)
Wvar1=tk.IntVar()
Wvar1.set(1)#初期状態

menu_selw1.add_radiobutton(label="jp",variable=Wvar1,value=0)
menu_selw1.add_radiobutton(label="en",variable=Wvar1,value=1)
menu_selw1.add_radiobutton(label="ru",variable=Wvar1,value=2)
menu_selw1.add_radiobutton(label="cn",variable=Wvar1,value=3)
menu_selw1.add_radiobutton(label="eo",variable=Wvar1,value=4)
menu_selw1.add_radiobutton(label="du",variable=Wvar1,value=5)
menu_selw1.add_radiobutton(label="la",variable=Wvar1,value=6)
menu_selw1.add_radiobutton(label="sw",variable=Wvar1,value=7)
menu_selw1.add_radiobutton(label="ar",variable=Wvar1,value=8)
menu_selw1.add_radiobutton(label="ka",variable=Wvar1,value=9)

menubar.add_cascade(label="to",menu=menu_selw_)

menubar.add_cascade(label="Destination",menu=menu_selw2)
Wvar2=tk.IntVar()
Wvar2.set(0)#初期状態
menu_selw2.add_radiobutton(label="jp",variable=Wvar2,value=0)
menu_selw2.add_radiobutton(label="en",variable=Wvar2,value=1)
menu_selw2.add_radiobutton(label="ru",variable=Wvar2,value=2)
menu_selw2.add_radiobutton(label="cn",variable=Wvar2,value=3)
menu_selw2.add_radiobutton(label="eo",variable=Wvar2,value=4)
menu_selw2.add_radiobutton(label="du",variable=Wvar2,value=5)
menu_selw2.add_radiobutton(label="la",variable=Wvar2,value=6)
menu_selw2.add_radiobutton(label="sw",variable=Wvar2,value=7)
menu_selw2.add_radiobutton(label="ar",variable=Wvar2,value=8)
menu_selw2.add_radiobutton(label="ka",variable=Wvar2,value=9)

toptext = font.Font(size=27, weight='bold')
sectext = font.Font(size=14, weight='bold')
top = tk.Label(root, text="Please enter the text to translate here.",fg="#444", font=toptext)
top.place(x=80, y=5)

entrylabel = tk.Label(text='input')
entrylabel.place(x=30, y=70)

entrybox = tk.Entry(width=90)
entrybox.place(x=80, y=70)
entrybox.insert(tk.END,"Hello,World!")

currentlabel = tk.Label(text='output')
currentlabel.place(x=30, y=130)
currentbox = tk.Text(width=90,height=17)
currentbox.place(x=80, y=130)

def cmd(n,s):
    if entrybox.get() == "":
        s.delete("1.0","end")
        s.insert("end","Please enter text to Entrybox.")
        return 0
    elif str(Wvar1.get()) == str(Wvar2.get()):
        s.delete("1.0","end")
        s.insert("end","language are the same.")
        return 0
    else:
        n[1] = "&source="+worldlist[int(Wvar1.get())]+"&target="+worldlist[int(Wvar2.get())]
        n[2] = urllib.parse.quote(str(entrybox.get()))

    subprocess.call(n)
    
    with open("translate.txt" ,"r",encoding="utf-8") as trans:
        s.delete("1.0","end")
        text = trans.read()
        s.insert("end",text)

def vers(n,s):
    text_temp=str(s.get("1.0","end"))
    n.delete(0,tk.END)
    n.insert(tk.END,text_temp)

commandlist=["main_C.exe","&source="+worldlist[int(Wvar1.get())]+"&target="+worldlist[int(Wvar2.get())],str(entrybox.get())]
letsgo = tk.Button(root, text='Translate',width=25,height=3,bg="#1a73e8",font=sectext, command=lambda:cmd(commandlist,currentbox))
letsgoo = tk.Button(root, text='Copy entry',width=25,height=3,bg="#1a73e8",font=sectext, command=lambda:vers(entrybox,currentbox))
letsgo.place(x=80, y=380)
letsgoo.place(x=400, y=380)

root.mainloop()