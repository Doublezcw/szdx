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
        sleep(0.01) #控制创建动画时长
        rect[i] = cv.create_rectangle(pos[i], fill='royalblue')

        cv.update()
    btn2.configure(state=tk.NORMAL)
    btn1.configure(state=tk.DISABLED)

def selection():
    global cv, rect, pos, lst, step
    L = len(lst)
    btn2.configure(state=tk.DISABLED)
    for i in range(L-1):
        min_idx = i
        for j in range(i+1, L):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        cv.move(rect[i], (min_idx-i)*step, 0)
        cv.move(rect[min_idx], (i-min_idx)*step, 0)
        rect[i], rect[min_idx] = rect[min_idx], rect[i]
        cv.itemconfig(rect[i], fill='red')
        cv.itemconfig(rect[min_idx], fill='red')
        cv.update()
        sleep(0.01) # 控制排序动画快慢
        cv.itemconfig(rect[i], fill='royalblue')
        cv.itemconfig(rect[min_idx], fill='royalblue')
        cv.update()
    btn1.configure(state=tk.NORMAL)

def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('选择排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=selection, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()

if __name__ == "__main__":
    app = main()