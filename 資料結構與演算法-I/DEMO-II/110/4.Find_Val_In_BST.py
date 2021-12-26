import tkinter as tk
from tkinter import END
import turtle

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None
        self.x = -1
        self.y = -1

def buildTree(data: list):
    BST = Node(data[0])
    for x in data[1:]:
        traversal(BST, int(x))
    return BST

    
def traversal(BST: Node, x):
    if  x < BST.data:
        if BST.left == None:
            BST.left = Node(x)
            return
        traversal(BST.left, x)
    elif x >= BST.data: 
        if BST.right == None:
            BST.right = Node(x)
            return
        traversal(BST.right, x)


def find(BST: Node, target: int):
    if BST == None: 
        find.result = []
        return
    find.result.append(BST.data)
    if target == BST.data: return
    if target <  BST.data: find(BST.left, target)
    if target >= BST.data: find(BST.right, target)


def onPressGetTree():
    buildTree.i = 0
    find.result = []
    data = entryData.get().replace(',', ' ').split()
    T = buildTree(data)
    find(T, int(entryTarget.get()))
    result.insert(END, str(find.result)+'\n')
  

app = tk.Tk() 

labelWidth = tk.Label(app,
                    text = "資料：")
labelWidth.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

entryData = tk.Entry(app, width=60)
entryData.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

labelWidth = tk.Label(app,
                    text = "目標：")
labelWidth.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.N)

entryTarget = tk.Entry(app, width=10)
entryTarget.grid(column=1, row=1, padx=10, pady=5, sticky='w')

findBstButton = tk.Button(app, text = 'Find', command=onPressGetTree)
findBstButton.grid(column=0, row=2, sticky=tk.W)

result = tk.Text(app)
result.grid(column=0, row=3, columnspan=2, sticky='w')


app.mainloop()
