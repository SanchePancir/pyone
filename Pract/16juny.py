### Игра в кости

from tkinter import *
import random, time


def bros():
    x = random.choice([
        'C:\\Users\\snovs\\Desktop\\кости\\b1.png',
        'C:\\Users\\snovs\\Desktop\\кости\\b2.png',
        'C:\\Users\\snovs\\Desktop\\кости\\b3.png',
        'C:\\Users\\snovs\\Desktop\\кости\\b4.png',
        'C:\\Users\\snovs\\Desktop\\кости\\b5.png',
        'C:\\Users\\snovs\\Desktop\\кости\\b6.png'
    ])
    return x


def img(event):
    global b1, b2
    for i in range(12):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.1)


root = Tk()
root.geometry('800x400')
root.title('Игра в кости от Саши! Сделай бросок))))')
root.resizable(height=False, width=False)
root.iconphoto(
    True, PhotoImage(file=('C:\\Users\\snovs\\Desktop\\кости\\icon1.png')))

font = PhotoImage(file=('C:\\Users\\snovs\\Desktop\\кости\\fon.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

#Button(root, text = 'Бросок', command = img).pack()
root.bind('<1>', img)
img('event')

root.mainloop()