from tkinter import *
from pyDictionary import pyDictionary  #import not working here

#creating a dictionary object:
dictionary=pyDictionary()
root=Tk()

root.geometry("400*400")
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

#add necessary buttons and labels:
label(root, text='Dictionary', font=('Helvetica 20 bold'), fg='green').pack(pady=10)

#first frame:
frame=frame(root)

label(frame, text='Type word', font=(' Helvetica 15 bold')).pack(side=LEFT)
word=Entry(frame, font=('Helvetica 15 bold'))
word.pack()
frame.pack(pady=10)

#second frame
frame1=Frame(root)
label(frame1, text='meaning:-', font=('Helvetica 10 bold')).pack(side=LEFT)
meaning=Label(frame1, text=' ', font=('Helvetica 10'))
meaning.pack()
frame1.pack(pady=10)

#third frame:
frame2=Frame(root)
label(frame2, text='Synonym', font=('Helvetica 10 bold')).pack(side=LEFT)
synonym=Label(frame2, text=' ', font=('Helvetica 10'))
synonym.pack()
frame2.pack(pady=10)

#fourth frame:
frame3=Frame(root)
label(frame3, text='Antonym', font=('Helvetica 10 bold')).pack(side=LEFT)
antonym=Label(frame3, text=' ', font=('Helvetica 10'))
antonym.pack()
frame3.pack(pady=10)

#end button:
Button(root, text='Submit', font=('Helvetica 15 bold'), command=dict).pack()




root.mainloop()
