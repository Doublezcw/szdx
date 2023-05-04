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
        sleep(0.01)
        rect[i] = cv.create_rectangle(pos[i], fill='royalblue')

        cv.update()
    btn2.configure(state=tk.NORMAL)
    btn1.configure(state=tk.DISABLED)

def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                # Update the visualization
                cv.itemconfig(rect[j], fill='red')
                cv.coords(rect[j], pos[j][0], 610, pos[j][2], 610 - lst[j] * 2)
                cv.itemconfig(rect[j], fill='royalblue')
                cv.update()
                sleep(0.01)
                j -= gap
            lst[j] = temp
            # Update the visualization
            cv.itemconfig(rect[j], fill='red')
            cv.coords(rect[j], pos[j][0], 610, pos[j][2], 610 - lst[j] * 2)
            cv.itemconfig(rect[j], fill='royalblue')
            cv.update()
        gap //= 2

def shell():
    global cv, rect, pos, lst, step
    btn2.configure(state=tk.DISABLED)
    shell_sort(lst)
    btn1.configure(state=tk.NORMAL)

def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('希尔排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=shell, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()

if __name__ == "__main__":
    app = main()