import tkinter as tk
from googletrans import Translator
win = tk.Tk()
win.title("Translator")
win.geometry("300x100")
def translator():
    word=e1.get()
    t=Translator(service_urls=['translate.google.com'])
    translation=t.translate(word,dest="hi")
    label1=tk.Label(win,text=f"Translated Text= {translation.text}",bg="yellow")
    label1.grid(row=2,column=0)

label=tk.Label(win, text='Enter Text to Convert (Hindi)',fg="Red",)
label.grid(row=0,column=0)
e1 = tk.Entry(win,width=35)
e1.focus()
e1.grid(row=1, column=0)
button = tk.Button(win,text="Convert",command=translator)
button.grid(row=1, column=1)
win.mainloop()