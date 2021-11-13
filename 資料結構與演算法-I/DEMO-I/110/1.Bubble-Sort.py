import tkinter as tk
from tkinter import END
from pycnnum import num2cn


root = tk.Tk()
root.title('Bubble Sort')

def Bubble_Sort(Nums: list[int]):
    Result, Flag, Count = '', True, 1
    while Flag == True:
        Flag = False 
        for i in range(len(Nums)-1):
            if Nums[i] > Nums[i+1]:
                # Swap two number
                Nums[i], Nums[i+1] = Nums[i+1], Nums[i]
                Flag = True
        Result = ''.join(map(lambda x: str(x) + ',', Nums))[:-1]
        # Display the result in the window 
        if Flag == True:
            Text.insert(END, f'第{num2cn(Count)}輪排序結果：{Result}\n')
        Count += 1
    Text.insert(END, f'最終排序結果：{Result}\n')

def pressHandler():
    nums = Input.get().replace(' ', '').split(',')
    if all(x.isnumeric() for x in nums):
        Text.delete('1.0', 'end')
        Text.insert(END, f'原始未經排序資料：{Input.get()}\n')
        nums = list(map(int, nums)) # Convert number string list to int list
        Bubble_Sort(nums)
    else:
        Input.delete(0, 'end')
        Input.insert(0, "請輸入正確的輸入！")
        Input.configure(fg='red')

def clear_text(event):
    Input.delete(0, 'end')
    Input.configure(fg='black')

Input = tk.Entry(root, width=50)
Input.pack()
Input.bind('<FocusIn>', clear_text)
Input.bind('<Button-1>', clear_text)

Button = tk.Button(root, text="Start", command=pressHandler)
Button.pack()

Text = tk.Text(root)
Text.pack()

root.mainloop()
