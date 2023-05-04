import tkinter as tk
from random import randint
from time import sleep

def init():
    global rect, font, pos, lst, step
    count = 300
    rect, font, pos = [0] * count, [0] * count, []
    lst = [randint(1, 300) for _ in range(count)]
    x, y = 45,610
    width, step = 2,2.8
    cv.delete('all')
    for i in range(count):
        pos.append((x + i * step, y - lst[i] * width, x + i * step + width, y))
        sleep(0.01)
        rect[i] = cv.create_rectangle(pos[i], fill='royalblue')

        cv.update()
    btn2.configure(state=tk.NORMAL)
    btn1.configure(state=tk.DISABLED)

def bubble():
    global cv, rect, pos, lst, step
    L = len(lst) - 1
    btn2.configure(state=tk.DISABLED)
    for i in range(L):
        for j in range(L - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cv.move(rect[j], step, 0)
                cv.move(rect[j + 1], -step, 0)
                rect[j], rect[j + 1] = rect[j + 1], rect[j]
                cv.itemconfig(rect[j], fill='red')
                cv.itemconfig(rect[j + 1], fill='red')
                cv.update()
                sleep(0) #控制动画快慢，数值越小越快
                cv.itemconfig(rect[j], fill='royalblue')
                cv.itemconfig(rect[j + 1], fill='royalblue')
                cv.update()
                btn1.configure(state=tk.NORMAL)

def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('冒泡排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=bubble, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()

if __name__ == "__main__":
    app = main()