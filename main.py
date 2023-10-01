from tkinter import *
from youchat import you_message
import pyttsx3
from functools import partial
import re
import os

cwd = os.getcwd()

root = Tk()
root.geometry("700x400")
root.title("Alphabetical Tech Facts (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

cmd = Text(root, width="85", height="11")
cmd.place(x=10, y=200)

def chat(letter):
    text = f"one short Tech fact related to the letter {letter}"

    ans = you_message(text=text, out_type="string")
    ans = re.sub("\(.*?\)", "", ans)
    cmd.insert(END, ans+"\n")
    print(ans)

    pyttsx3.speak(ans)

Label(root, text="Choose the Alphabet of your Choice", font=("Raleway", 20), bg="black", fg="white", height="1").place(x=130, y=1)

Button(root, text="A", command=partial(chat, "A"), width="5", height="1").place(x=20, y=65)
Button(root, text="B", command=partial(chat, "B"), width="5", height="1").place(x=80, y=65)
Button(root, text="C", command=partial(chat, "C"), width="5", height="1").place(x=140, y=65)
Button(root, text="D", command=partial(chat, "D"), width="5", height="1").place(x=200, y=65)
Button(root, text="E", command=partial(chat, "E"), width="5", height="1").place(x=260, y=65)
Button(root, text="F", command=partial(chat, "F"), width="5", height="1").place(x=320, y=65)
Button(root, text="G", command=partial(chat, "G"), width="5", height="1").place(x=380, y=65)
Button(root, text="H", command=partial(chat, "H"), width="5", height="1").place(x=440, y=65)
Button(root, text="I", command=partial(chat, "I"), width="5", height="1").place(x=500, y=65)
Button(root, text="J", command=partial(chat, "J"), width="5", height="1").place(x=560, y=65)
Button(root, text="K", command=partial(chat, "K"), width="5", height="1").place(x=620, y=65)
Button(root, text="L", command=partial(chat, "L"), width="5", height="1").place(x=20, y=100)
Button(root, text="M", command=partial(chat, "M"), width="5", height="1").place(x=80, y=100)
Button(root, text="N", command=partial(chat, "N"), width="5", height="1").place(x=140, y=100)
Button(root, text="O", command=partial(chat, "O"), width="5", height="1").place(x=200, y=100)
Button(root, text="P", command=partial(chat, "P"), width="5", height="1").place(x=260, y=100)
Button(root, text="Q", command=partial(chat, "Q"), width="5", height="1").place(x=320, y=100)
Button(root, text="R", command=partial(chat, "R"), width="5", height="1").place(x=380, y=100)
Button(root, text="S", command=partial(chat, "S"), width="5", height="1").place(x=440, y=100)
Button(root, text="T", command=partial(chat, "T"), width="5", height="1").place(x=500, y=100)
Button(root, text="U", command=partial(chat, "U"), width="5", height="1").place(x=560, y=100)
Button(root, text="V", command=partial(chat, "V"), width="5", height="1").place(x=620, y=100)
Button(root, text="W", command=partial(chat, "W"), width="5", height="1").place(x=200, y=136)
Button(root, text="X", command=partial(chat, "X"), width="5", height="1").place(x=260, y=135)
Button(root, text="Y", command=partial(chat, "Y"), width="5", height="1").place(x=320, y=135)
Button(root, text="Z", command=partial(chat, "Z"), width="5", height="1").place(x=380, y=135)

root.mainloop()