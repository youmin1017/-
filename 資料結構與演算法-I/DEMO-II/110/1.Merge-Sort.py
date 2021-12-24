import tkinter as tk
from tkinter import END
from pycnnum import num2cn

root = tk.Tk()
root.title('Merge Sort')

def merge(nums: list[int], front, end):
    l, r, mid, Max  = 0, 0, (front+end)//2, max(nums)
    l_sub = nums[front:mid+1]
    r_sub = nums[mid+1:end+1]
    l_sub.append(Max + 1)
    r_sub.append(Max + 1)
    for i in range(front, end+1):
        if l_sub[l] <= r_sub[r]:
            nums[i], l = l_sub[l], l+1
        else:
            nums[i], r = r_sub[r], r+1
    if end == len(nums)-1:
        result = ','.join([str(x) for x in nums])
        Text.insert(END, f'第{num2cn(merge.count)}輪排序結果：{result}\n')
        merge.count += 1
merge.count = 1

def merge_sort(nums: list[int], front: int, end: int):
    mid = (front + end)//2
    if front < end:
        merge_sort(nums, front, mid)
        merge_sort(nums, mid+1, end)
        merge(nums, front, end)

def pressHandler():
    nums = Input.get().replace(',', ' ').split()
    if all(x.isnumeric() for x in nums):
        Text.delete('1.0', 'end')
        Text.insert(END, f'原始未經排序資料：{Input.get()}\n')
        nums = list(map(int, nums)) # Convert number string list to int list
        merge_sort(nums, 0, len(nums)-1)
        result = ','.join([str(x) for x in nums])
        Text.insert(END, f'最終排序結果：{result}\n')
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
