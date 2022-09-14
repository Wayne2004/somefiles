import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
import tests
import os

root = tk.Tk()
img = (Image.open("photos\\svobackground.png"))
resized_image= img.resize((550,300))
background = tk.PhotoImage(file="photos\\svobackground.png")


root.title('Auto Broadcast SVO MELAKA')
root.geometry('550x600+20+0')
root.minsize(550,600)
root.maxsize(550,600)

label1 = tk.Label(root,image=background)
label1.place(x=0,y=0)

ids = []
if os.path.exists('credentials.txt'):
    with open('credentials.txt','r+') as f:
        stuf = f.readlines()
        ids.append(stuf[0].replace('\n',''))
        ids.append(stuf[1])

else:
    with open('credentials.txt','w+') as f:
        pass
label2 = tk.Label(root,text='Facebook Email/Phone Number')
label2.place(x=0,y=300)
label3 = tk.Label(root,text='Facebook Password')
label3.place(x=0,y=350)
label4 = tk.Label(root,text='MESSAGE TO BROADCAST')
label4.place(x=0,y=400)

entry1 = tk.Entry(root,width=30,selectbackground='black',
                  bd=0)
entry1.place(x=0,y=320)
entry2 = tk.Entry(root,width=30,selectbackground='black',
                  bd=0)
entry2.place(x=0,y=370)


if len(ids)>1:
    entry1.insert(0,ids[0])
    entry2.insert(0,ids[1])
textbox = tk.Text(root,width=68,height=11)
textbox.place(x=0,y=420)

pictureselected = False
def addpicture():
    global pictureselected
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a Picture!",
                                          filetypes=[("all files","*.*")])
    pictureselected = True
    AddpicButt.configure(text='Change Picture')

def broadcast():
    with open('credentials.txt','w') as f:
        f.write(entry1.get()+'\n')
        f.write(entry2.get())
    if pictureselected:
        tests.startprocess(entry1.get(),entry2.get(),textbox.get('1.0','end'),filename)
    else:
        tests.startprocess(entry1.get(),entry2.get(),textbox.get('1.0','end'))




AddpicButt = tk.Button(root,text='Add Picture',command=addpicture)
AddpicButt.place(x=460,y=395)

StartButton = tk.Button(root,text='开始',command=broadcast)
StartButton.place(x=515,y=300)



root.mainloop()