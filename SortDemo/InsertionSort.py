import tkinter as tk
from random import randint
from time import sleep

def init():
    global rect, font, pos, lst, step
    count = 300
    rect, font, pos = [0] * count, [0] * count, []
    lst = [randint(1, 300) for _ in range(count)]
    x, y = 45, 610
    width, step = 2, 2.8
    cv.delete('all')
    for i in range(count):
        pos.append((x + i * step, y - lst[i] * width, x + i * step + width, y))
        rect[i] = cv.create_rectangle(pos[i], fill='royalblue')
        cv.update()
        sleep(0.01)
    btn2.configure(state=tk.NORMAL)
    btn1.configure(state=tk.DISABLED)

def insertion():
    global cv, rect, pos, lst, step
    L = len(lst)
    btn2.configure(state=tk.DISABLED)
    for i in range(1, L):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            cv.move(rect[j], step, 0)
            cv.move(rect[j + 1], -step, 0)
            rect[j], rect[j + 1] = rect[j + 1], rect[j]
            pos[j], pos[j+1] = pos[j+1], pos[j]
            cv.update()
            sleep(0)
            j -= 1
        lst[j + 1] = key
        cv.itemconfig(rect[i], fill='green')
        cv.update()
        cv.itemconfig(rect[i], fill='royalblue')

    btn1.configure(state=tk.NORMAL)

def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('插入排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=insertion, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()

if __name__ == "__main__":
    app = main()