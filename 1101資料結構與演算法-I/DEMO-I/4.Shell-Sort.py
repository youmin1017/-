import tkinter as tk
from tkinter import END
from pycnnum import num2cn

root = tk.Tk()
root.title('Shell Sort')

def Shell_Sort(list: list[int]): 
    # 初始步長
    n = len(list)
    gap = n // 2
    Count = 1
    Result = ''
    while gap > 0:
        for i in range(gap, n):
            # 每个步長進行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= 0 and j-gap >= 0 and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步長
        gap = gap // 2
        Result = ' '.join(map(lambda s: str(s) + ',', list))
        Text.insert(END, f'第{num2cn(Count)}輪排序結果：{Result}\n')
        Count += 1
    Text.insert(END, f'最終排序結果：{Result}\n')

def pressHandler():
    nums = Nums.get().replace(' ', '').split(',')
    if all(x.isnumeric() for x in nums):
        Text.delete('1.0', 'end')
        Text.insert(END, f'原始未經排序資料：{Nums.get()}\n')
        nums = list(map(int, nums)) # Convert number string list to int list
        Shell_Sort(nums)
    else:
        Nums.delete(0, 'end')
        Nums.insert(0, "請輸入正確的輸入！")
        Nums.configure(fg='red')

def clear_text(event):
    Nums.delete(0, 'end')
    Nums.configure(fg='black')

Nums = tk.Entry(root, width=50)
Nums.pack()
Nums.bind('<FocusIn>', clear_text)
Nums.bind('<Button-1>', clear_text)

Button = tk.Button(root, text="Start", command=pressHandler)
Button.pack()

Text = tk.Text(root)
Text.pack()

root.mainloop()
