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


def heap_sort():
    global cv, rect, pos, lst, step
    L = len(lst)
    btn2.configure(state=tk.DISABLED)

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and lst[largest] < lst[l]:
            largest = l

        if r < n and lst[largest] < lst[r]:
            largest = r

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            cv.move(rect[i], step * (largest - i), 0)
            cv.move(rect[largest], -step * (largest - i), 0)
            rect[i], rect[largest] = rect[largest], rect[i]
            cv.itemconfig(rect[i], fill='red')
            cv.itemconfig(rect[largest], fill='red')
            cv.update()
            sleep(0)
            cv.itemconfig(rect[i], fill='royalblue')
            cv.itemconfig(rect[largest], fill='royalblue')
            cv.update()
            heapify(n, largest)

    for i in range(L // 2 - 1, -1, -1):
        heapify(L, i)

    for i in range(L - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        cv.move(rect[0], step * (i - 0), 0)
        cv.move(rect[i], -step * (i - 0), 0)
        rect[0], rect[i] = rect[i], rect[0]
        cv.itemconfig(rect[0], fill='red')
        cv.itemconfig(rect[i], fill='red')
        cv.update()
        sleep(0)
        cv.itemconfig(rect[0], fill='royalblue')
        cv.itemconfig(rect[i], fill='royalblue')
        cv.update()

        heapify(i, 0)

    btn1.configure(state=tk.NORMAL)


def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('堆排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=heap_sort, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()


if __name__ == "__main__":
    app = main()