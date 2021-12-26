import tkinter as tk
import turtle

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None
        self.x = -1
        self.y = -1

def deleteNode(root, key: int):
    if not root :
        return None
    elif key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)     
    elif root.data == key :
        if not root.left :
            return root.right
        if not root.right :
            return root.left
        else :
            root.data = findmin(root.right)
            root.right = deleteNode(root.right, root.data)       
    return root
    
def findmin(node) -> int :
    while node.left :
        node = node.left
    return node.data

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


def knuth_layout(tree, depth = 0):
    if tree.left: 
        knuth_layout(tree.left, depth-1)
    tree.x = knuth_layout.i
    tree.y = depth
    knuth_layout.i += 1
    if tree.right: 
        knuth_layout(tree.right, depth-1)


def onPressGetTree():
    setUpTurtle()
    buildTree.i = 0
    knuth_layout.i = -8
    preorder = entryData.get().replace(',', ' ').split()
    T = buildTree(preorder)
    deleteNode(T, int(entryTarget.get()))
    knuth_layout(T)
    drawTree(T)
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

def drawTree(T) -> None:
    if T == None: return None
    t.down() if T.y != 0 else t.up()
    t.goto(T.x * GRID_SIZE, T.y * GRID_SIZE + 250)
    drawTree(T.left)
    t.up()
    t.goto(T.x * GRID_SIZE, T.y * GRID_SIZE + 250)
    drawTree(T.right)
    t.up()
    t.goto(T.x * GRID_SIZE, T.y * GRID_SIZE + 250)
    draw_node(t, T.data, t.xcor(), t.ycor())

def setUpTurtle() -> None:
    t.clear()
    t.pensize(2)
    t.penup()
    t.goto(0, 250)
    t.setheading(-90)
    t.pendown()

app = tk.Tk() 

labelWidth = tk.Label(app,
                    text = "資料：")
labelWidth.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

entryData = tk.Entry(app, width=110)
entryData.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

labelWidth = tk.Label(app,
                    text = "目標：")
labelWidth.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.N)

entryTarget = tk.Entry(app, width=10)
entryTarget.grid(column=1, row=1, padx=10, pady=5, sticky='w')

findBstButton = tk.Button(app, text = 'Find', command=onPressGetTree)
findBstButton.grid(column=0, row=2, sticky=tk.W)

canvas = tk.Canvas(app, width=1000, height=600)
canvas.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky='w')
t = turtle.RawTurtle(canvas)

app.mainloop()
