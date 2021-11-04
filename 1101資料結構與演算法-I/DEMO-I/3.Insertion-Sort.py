import tkinter as tk
from tkinter import END
from pycnnum import num2cn

root = tk.Tk()
root.title('Insertion Sort')

def Insertion_Sort(Nums: list[int]):
    Result = ''
    n = len(Nums)
    
    for i in range(1, n):
        key = Nums[i]
        j = i-1
        while j >= 0 and Nums[j] > key:
            Nums[j+1] = Nums[j]
            j -= 1
        Nums[j+1] = key
        Result = ' '.join(map(lambda x: str(x) + ',', Nums))[:-1]
        Text.insert(END, f'第{num2cn(i)}輪排序結果：{Result}\n')
    Text.insert(END, f'最終排序結果：{Result}\n')

def pressHandler():
    nums = Nums.get().replace(' ', '').split(',')
    if all(x.isnumeric() for x in nums):
        Text.delete('1.0', 'end')
        Text.insert(END, f'原始未經排序資料：{Nums.get()}\n')
        nums = list(map(int, nums)) # Convert number string list to int list
        Insertion_Sort(nums)
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
