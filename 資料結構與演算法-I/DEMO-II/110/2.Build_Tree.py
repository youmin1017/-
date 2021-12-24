import tkinter as tk
from tkinter import END
import turtle

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preorder: list, inorder: list,
              start: int, end: int):
    if start > end: return None

    TNode = Node(preorder[buildTree.i])
    buildTree.i+=1
    if start == end: return TNode

    index = search(inorder, start, end, TNode.data)
    TNode.left  = buildTree(preorder, inorder, start, index-1 )
    TNode.right = buildTree(preorder, inorder, index+1, end   )

    return TNode

def search(arr, start, end, value) -> int:
    for i in range(start, end + 1):
        if arr[i] == value:
            return i
    return -1 

def onPressGetTree():
    setUpTurtle()
    buildTree.i = 0
    preorder = entryPreorder.get().replace(',', ' ').split()
    inorder  = entryInorder.get().replace(',', ' ').split()
    bTree = buildTree(preorder, inorder, 0, len(preorder)-1)
    drawTree(bTree)
    t.hideturtle()

RADIUS = 20
FONT_SIZE = 14
FONT = ("Arial", FONT_SIZE, "normal")
GRID_SIZE = 50
def draw_node(turtle, text, x, y):
    t.fillcolor('gray')
    t.up()
    turtle.goto(x - RADIUS, y)
    turtle.down()
    t.begin_fill()
    turtle.circle(RADIUS)
    t.end_fill()
    turtle.up()
    turtle.goto(x, y - RADIUS // 2)
    turtle.write(text, align="center", font=FONT)
    turtle.goto(x, y)
    turtle.pendown()

def drawTree(bTree, dis = 50, x = 0, y = 0) -> None:
    if bTree == None: return None
    t.down()
    t.goto(x * GRID_SIZE, y * GRID_SIZE + 250)
    drawTree(bTree.left,  dis, x-1, y-1)
    t.up()
    t.goto(x * GRID_SIZE, y * GRID_SIZE + 250)
    drawTree(bTree.right, dis, x+1, y-1)
    t.up()
    t.goto(x * GRID_SIZE, y * GRID_SIZE + 250)
    draw_node(t, bTree.data, t.xcor(), t.ycor())

def setUpTurtle() -> None:
    t.clear()
    t.pensize(2)
    t.penup()
    t.goto(0, 250)
    t.setheading(-90)
    t.pendown()

app = tk.Tk() 

labelWidth = tk.Label(app,
                    text = "前序走訪：")
labelWidth.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

labelHeight = tk.Label(app,
                    text = "中序走訪：")
labelHeight.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)

entryPreorder = tk.Entry(app, width=60)
entryPreorder.insert(END, 'A, B, D, E, C, F')
entryInorder = tk.Entry(app, width=60)
entryInorder.insert(END, 'D, B, E, A, C, F')

entryPreorder.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
entryInorder.grid(column=1, row=1, padx=10, pady=5, sticky=tk.S)

getTreeButton = tk.Button(app, text = 'Get Tree', command=onPressGetTree)
getTreeButton.grid(column=0, row=2, sticky=tk.W)

canvas = tk.Canvas(app, width=600, height=600)
canvas.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky='w')
t = turtle.RawTurtle(canvas)
app.mainloop()
