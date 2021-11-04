import tkinter as tk
from tkinter import END
from pycnnum import num2cn

root = tk.Tk()
root.title('Selection Sort')

def Selection_Sort(Nums: list[int]) -> None:
    Result = ' '
    for i in range(len(Nums)-1):
        MinIndex = i
        for x in range(i, len(Nums)):
            if Nums[x] < Nums[MinIndex]: #find the smallest element
                MinIndex = x
        Nums[i], Nums[MinIndex] = Nums[MinIndex], Nums[i] # swap two elements
        # Convert list[int] to str and split all elements by ','
        Result = ' '.join(map(lambda s: str(s) + ',', Nums))[:-1] 
        Text.insert(END, f'第{num2cn(i+1)}輪排序結果：{Result}\n')
    Text.insert(END, f'最終排序結果：{Result}\n')

def pressHandler():
    Nums = Input.get().replace(' ', '').split(',')
    if all(x.isnumeric() for x in Nums):
        Text.delete('1.0', 'end')
        Text.insert(END, f'原始未經排序資料：{Input.get()}\n')
        Nums = list(map(int, Nums)) # Convert number string list to int list
        Selection_Sort(Nums)
    else:
        Input.delete(0, 'end')
        Input.insert(0, "請輸入正確的輸入！")
        Input.configure(fg='red')

def clear_text(e):
    Input.delete(0, END)
    Input.configure(fg='black')

Input = tk.Entry(root, width=50)
Input.pack()
Input.bind('<Button-1>', clear_text)
Input.bind('<FocusIn>', clear_text)

Button = tk.Button(root, text='Start', command=pressHandler)
Button.pack()

Text = tk.Text(root)
Text.pack()

root.mainloop()
