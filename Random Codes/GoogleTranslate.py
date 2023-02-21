from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#Function to Translate the language you want to
def change1(text = "type",src = "English",dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src = src1,dest = dest1)
    return trans1.text

#Function to call in button which will actually show the translation
def data():
    s = combo_sor.get()
    d = combo_dest.get()
    msg = sor_txt.get(1.0,END)
    textget = change1(text = msg,src = s,dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)
    return dest_txt
    
#Creating Window for Google Translator
root = Tk()
root.title("TRANSLATOR")
root.geometry('500x700')
root.config(bg="red")

#Main Label TRANSLATOR
lab_txt = Label(root,text = "Translator",font = ("Verdana",30,"bold"),bg = "red")
lab_txt.place(x=100,y=30,height=100,width=300)

#Creating Frame for all Textboxes, Buttons and Comboboxes
frame = Frame(root).pack(side = BOTTOM)
lab_txt = Label(root,text = "Source Text",font = ("Verdana",15,"bold"),fg = "black",bg = "red")   #Source Label
lab_txt.place(x=100,y=110,height=20,width=300)

sor_txt = Text(frame,font = ("Verdana",20,"bold"),wrap = WORD)   #Source TextBox
sor_txt.place(x=10,y=140,height=100,width=480)

list_text = list(LANGUAGES.values())
combo_sor = ttk.Combobox(frame,value = list_text)     #Source Combobox
combo_sor.place(x=10,y=300,height=30,width=150)
combo_sor.set("English")

button_change = Button(frame,text = "Translate",relief = RAISED,command = data)     #Translate Button
button_change.place(x=170,y=300,height=30,width=150)

combo_dest = ttk.Combobox(frame,value = list_text)     #Destination Combobox
combo_dest.place(x=330,y=300,height=30,width=150)
combo_dest.set("English")

lab_txt = Label(root,text = "Destination Text",font = ("Verdana",15,"bold"),fg = "black",bg = "red")   #Destination Label
lab_txt.place(x=100,y=390,height=20,width=300)

dest_txt = Text(frame,font = ("Verdana",20,"bold"),wrap = WORD)    #Destination TextBox
dest_txt.place(x=10,y=420,height=100,width=480)

root.mainloop()
