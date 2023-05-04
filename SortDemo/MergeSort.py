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

def merge_sort(lst, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(lst, left, mid)
    merge_sort(lst, mid + 1, right)

    # Merge the sorted sub-arrays
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if lst[i] < lst[j]:
            temp.append(lst[i])
            i += 1
        else:
            temp.append(lst[j])
            j += 1
    while i <= mid:
        temp.append(lst[i])
        i += 1
    while j <= right:
        temp.append(lst[j])
        j += 1

    # Copy the temp array back to lst
    for i, val in enumerate(temp):
        lst[left + i] = val

    # Update the visualization
    for i in range(left, right + 1):
        cv.itemconfig(rect[i], fill='red')
        cv.coords(rect[i], pos[i][0], 610, pos[i][2], 610 - lst[i] * 2)
        cv.itemconfig(rect[i], fill='royalblue')
        cv.update()
        sleep(0.01)

def merge():
    global cv, rect, pos, lst, step
    L, R = 0, len(lst) - 1
    btn2.configure(state=tk.DISABLED)
    merge_sort(lst, L, R)
    btn1.configure(state=tk.NORMAL)

def main():
    global cv, btn1, btn2
    root = tk.Tk()
    root.geometry('940x700')
    root.title('归并排序')
    root.resizable(False, False)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)
    btn1.place(x=360, y=640)
    btn2 = tk.Button(root, text='排序', command=merge, state=tk.DISABLED)
    btn2.place(x=520, y=640)
    root.mainloop()

if __name__ == "__main__":
    app = main()