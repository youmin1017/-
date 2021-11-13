import tkinter as tk
import turtle

def koch(dis: float, order: int) -> None:
    if order == 0:
        t.fd(dis)
    elif order > 0:
        for rotate in [60, -120, 60, 0]:
            koch(dis/3, order-1)
            t.lt(rotate)

def onPress() -> None:
    num = Input.get()
    if num == '' or int(num) not in [0,1,2,3,4,5,6]:
        Input.delete(0, 'end')
        Input.insert(0, "請輸入正確的輸入！")
        Input.configure(fg='red')
        return None
    t.clear()
    t.speed(1000)
    t.penup()
    t.goto(-150,50)
    t.setheading(0)
    t.pendown()
    # Draw triangle
    for _ in range(3):
        koch( 300, int(num) )
        t.rt(120)

def clear_text(event):
    Input.delete(0, 'end')
    Input.configure(fg='black')

window = tk.Tk()
window.title('Koch Curve')
window.geometry('600x650')

canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()
canvas.place(x=0, y=50)

t = turtle.RawTurtle(canvas)

Input = tk.Entry(window,width=15,justify="center")
Input.pack()
Input.bind('<FocusIn>', clear_text)
Input.bind('<Button-1>', clear_text)

button = tk.Button(window,text="START", command=onPress)
button.pack()
button.place(x=270,y=20)

window.mainloop()
