import tkinter as tk
from time import sleep
import threading
from random import sample

# 全局变量
rect, pos, lst, step = [], [], [], 2.8 # rect: 矩形对象列表，pos: 矩形坐标，lst: 排序数据，step: 每个矩形的水平间隔
cv, btn1, btn2, algo_var = None, None, None, None  # 画布、按钮、算法选择变量
count = 300  # 排序元素数量

# 初始化数据和画布
# 创建初始的无序数据，并在画布上绘制对应的矩形条
# 每次点击"创建"按钮时调用
# 会禁用"创建"按钮，启用"排序"按钮
# 并以动画方式绘制所有矩形

def init():
    global rect, pos, lst, step
    rect, pos = [0] * count, []
    lst = sample(range(1, count + 1), count)  # 生成1~300的无重复随机排列
    x, y = 45, 610  # 起始坐标
    width, step = 2, 2.8  # 矩形宽度和水平间隔
    cv.delete('all')  # 清空画布
    for i in range(count):
        pos.append((x + i * step, y - lst[i] * width, x + i * step + width, y))  # 计算每个矩形的坐标
        rect[i] = cv.create_rectangle(pos[i], fill='green')  # 绘制矩形
        cv.update()
        sleep(0.01)  # 动画延时
    btn2.configure(state=tk.NORMAL)  # 启用"排序"按钮
    btn1.configure(state=tk.DISABLED)  # 禁用"创建"按钮

# 冒泡排序动画
# 每次相邻元素比较并交换，交换时高亮显示
# 排序完成后启用"创建"按钮

def bubble_sort_anim():
    global rect, pos, lst, step
    L = len(lst) - 1
    btn2.configure(state=tk.DISABLED)  # 排序过程中禁用"排序"按钮
    for i in range(L):
        for j in range(L - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 交换数据
                cv.move(rect[j], step, 0)  # 右移
                cv.move(rect[j + 1], -step, 0)  # 左移
                rect[j], rect[j + 1] = rect[j + 1], rect[j]  # 交换矩形对象
                cv.itemconfig(rect[j], fill='red')  # 高亮显示
                cv.itemconfig(rect[j + 1], fill='red')
                cv.update()
                cv.itemconfig(rect[j], fill='green')  # 恢复颜色
                cv.itemconfig(rect[j + 1], fill='green')
                cv.update()
    btn1.configure(state=tk.NORMAL)  # 排序完成后启用"创建"按钮

# 快速排序动画
# 递归分区，每次交换时高亮显示
# 排序完成后启用"创建"按钮

def quick_sort_anim():
    # 分区函数，返回枢轴位置
    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]  # 交换数据
                cv.move(rect[i], (j - i) * step, 0)
                cv.move(rect[j], (i - j) * step, 0)
                rect[i], rect[j] = rect[j], rect[i]  # 交换矩形对象
                cv.itemconfig(rect[i], fill='red')
                cv.itemconfig(rect[j], fill='red')
                cv.update()
                sleep(0.005)
                cv.itemconfig(rect[i], fill='green')
                cv.itemconfig(rect[j], fill='green')
                cv.update()
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        cv.move(rect[i + 1], (high - i - 1) * step, 0)
        cv.move(rect[high], (i + 1 - high) * step, 0)
        rect[i + 1], rect[high] = rect[high], rect[i + 1]
        return i + 1
    # 快速排序递归实现
    def quick_sort(lst, low, high):
        if low < high:
            pi = partition(lst, low, high)
            quick_sort(lst, low, pi - 1)
            quick_sort(lst, pi + 1, high)
    btn2.configure(state=tk.DISABLED)
    quick_sort(lst, 0, len(lst) - 1)
    btn1.configure(state=tk.NORMAL)

# 选择排序动画
# 每次选择最小值与当前位置交换，交换时高亮显示

def selection_sort_anim():
    global rect, pos, lst, step
    L = len(lst)
    btn2.configure(state=tk.DISABLED)
    for i in range(L-1):
        min_idx = i
        for j in range(i+1, L):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]  # 交换数据
        cv.move(rect[i], (min_idx-i)*step, 0)
        cv.move(rect[min_idx], (i-min_idx)*step, 0)
        rect[i], rect[min_idx] = rect[min_idx], rect[i]  # 交换矩形对象
        cv.itemconfig(rect[i], fill='red')
        cv.itemconfig(rect[min_idx], fill='red')
        cv.update()
        sleep(0.005)
        cv.itemconfig(rect[i], fill='green')
        cv.itemconfig(rect[min_idx], fill='green')
        cv.update()
    btn1.configure(state=tk.NORMAL)

# 归并排序动画
# 递归分治，合并时更新矩形高度并高亮

def merge_sort_anim():
    # 归并排序递归实现
    def merge_sort(lst, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
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
        for k, val in enumerate(temp):
            lst[left + k] = val  # 合并回原数组
        for k in range(left, right + 1):
            cv.itemconfig(rect[k], fill='red')  # 高亮
            cv.coords(rect[k], pos[k][0], 610, pos[k][2], 610 - lst[k] * 2)  # 更新高度
            cv.itemconfig(rect[k], fill='green')
            cv.update()
            sleep(0.005)
    btn2.configure(state=tk.DISABLED)
    merge_sort(lst, 0, len(lst) - 1)
    btn1.configure(state=tk.NORMAL)

# 希尔排序动画
# 分组插入排序，移动时更新高度并高亮

def shell_sort_anim():
    global rect, pos, lst, step
    n = len(lst)
    gap = n // 2  # 初始步长
    btn2.configure(state=tk.DISABLED)
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                cv.itemconfig(rect[j], fill='red')
                cv.coords(rect[j], pos[j][0], 610, pos[j][2], 610 - lst[j] * 2)
                cv.itemconfig(rect[j], fill='green')
                cv.update()
                sleep(0.005)
                j -= gap
            lst[j] = temp
            cv.itemconfig(rect[j], fill='red')
            cv.coords(rect[j], pos[j][0], 610, pos[j][2], 610 - lst[j] * 2)
            cv.itemconfig(rect[j], fill='green')
            cv.update()
        gap //= 2  # 缩小步长
    btn1.configure(state=tk.NORMAL)

# 插入排序动画
# 每次插入时移动矩形并高亮

def insertion_sort_anim():
    global rect, pos, lst, step
    L = len(lst)
    btn2.configure(state=tk.DISABLED)
    for i in range(1, L):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            cv.move(rect[j], step, 0)
            cv.move(rect[j + 1], -step, 0)
            rect[j], rect[j + 1] = rect[j + 1], rect[j]  # 交换矩形对象
            pos[j], pos[j+1] = pos[j+1], pos[j]  # 交换坐标
            cv.update()
            sleep(0.001)
            j -= 1
        lst[j + 1] = key
        cv.itemconfig(rect[i], fill='red')  # 插入位置高亮
        cv.update()
        cv.itemconfig(rect[i], fill='green')
    btn1.configure(state=tk.NORMAL)

# 堆排序动画
# 构建大顶堆，每次取出堆顶元素与末尾交换，交换时高亮

def heap_sort_anim():
    global rect, pos, lst, step
    L = len(lst)
    btn2.configure(state=tk.DISABLED)
    # 堆化过程
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
            sleep(0.002)
            cv.itemconfig(rect[i], fill='green')
            cv.itemconfig(rect[largest], fill='green')
            cv.update()
            heapify(n, largest)
    # 构建初始大顶堆
    for i in range(L // 2 - 1, -1, -1):
        heapify(L, i)
    # 依次将堆顶元素与末尾交换，并重新堆化
    for i in range(L - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        cv.move(rect[0], step * (i - 0), 0)
        cv.move(rect[i], -step * (i - 0), 0)
        rect[0], rect[i] = rect[i], rect[0]
        cv.itemconfig(rect[0], fill='red')
        cv.itemconfig(rect[i], fill='red')
        cv.update()
        sleep(0.005)
        cv.itemconfig(rect[0], fill='green')
        cv.itemconfig(rect[i], fill='green')
        cv.update()
        heapify(i, 0)
    btn1.configure(state=tk.NORMAL)

# 算法名称与函数映射
# 根据下拉菜单选择返回对应的排序动画函数

def get_sort_func(name):
    return {
        "冒泡排序": bubble_sort_anim,
        "快速排序": quick_sort_anim,
        "选择排序": selection_sort_anim,
        "归并排序": merge_sort_anim,
        "希尔排序": shell_sort_anim,
        "插入排序": insertion_sort_anim,
        "堆排序": heap_sort_anim,
    }[name]

# 启动排序动画线程，防止界面卡死

def start_sort():
    # 多线程防止界面卡死
    threading.Thread(target=get_sort_func(algo_var.get())).start()

# 主函数，构建界面
# 包括下拉菜单、画布、按钮等
# 绑定按钮事件

def main():
    global cv, btn1, btn2, algo_var
    root = tk.Tk()  # 创建主窗口
    root.geometry('940x700')  # 设置窗口大小
    root.title('排序算法动画演示')  # 设置窗口标题
    root.resizable(False, False)  # 固定窗口大小
    algo_var = tk.StringVar(value="冒泡排序")  # 算法选择变量，默认冒泡排序
    tk.Label(root, text="").place(x=200, y=10)  # 占位标签
    algo_menu = tk.OptionMenu(root, algo_var, "冒泡排序", "快速排序", "选择排序", "归并排序", "希尔排序", "插入排序", "堆排序")  # 算法下拉菜单
    algo_menu.place(x=200, y=640)
    cv = tk.Canvas(root, width=940, height=610, bg='aliceblue')  # 创建画布
    cv.pack()
    btn1 = tk.Button(root, text='创建', command=init)  # 创建按钮
    btn1.place(x=470, y=640)
    btn2 = tk.Button(root, text='排序', command=start_sort, state=tk.DISABLED)  # 排序按钮
    btn2.place(x=705, y=640)
    root.mainloop()  # 进入主循环

# 程序入口
if __name__ == "__main__":
    main() 