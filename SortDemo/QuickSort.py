import tkinter as tk
from random import randint
from time import sleep

def init():
    global rect, pos, lst, step
    count = 300
    rect, pos = [0] * count, []
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

def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            cv.move(rect[i], (j - i) * step, 0)
            cv.move(rect[j], (i - j) * step, 0)
            rect[i], rect[j] = rect[j], rect[i]
            cv.itemconfig(rect[i], fill='red')
            cv.itemconfig(rect[j], fill='red')
            cv.update()
            sleep(0.01)
            cv.itemconfig(rect[i], fill='royalblue')
            cv.itemconfig(rect[j], fill='royalblue')
            cv.update()
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    cv.move(rect[i + 1], (high - i - 1) * step, 0)
    cv.move(rect[high], (i + 1 - high) * step, 0)
    rect[i + 1], rect[high] = rect[high], rect[i + 1]
    return i + 1

def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)

def sort():
    global lst
    btn2.configure(state=tk.DISABLED)
    quick_sort(lst, 0, len(lst) - 1)
    btn1.configure(state=tk.NORMAL)

def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('快速排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=sort, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()

if __name__ == "__main__":
    app = main()