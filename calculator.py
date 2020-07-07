from tkinter import *

wind=Tk()

wind.geometry("312x324")

wind.title("Calculator")

wind.resizable(0,0)


def button_click(item):
    global expression
    expression=expression+str(item)
    input_string.set(expression)

def button_clear():
    global expression
    expression=""
    input_string.set("")

def button_equal():
    global expression
    result = str(eval(expression)) 
    input_string.set(result)
    expression=""

expression=""

input_string=StringVar()
    
input_frame = Frame(wind, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black" ,highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ("arial", 18, "bold"), textvariable = input_string, width = 50, bg = "black",fg="white", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

button_frame=Frame(wind,width="312",height="273",bg="black")
button_frame.pack()

clear = Button(button_frame, text = "C", fg = "white", width = 32, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: button_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide=Button(button_frame,text="/",width=10,height=3,bd=0,bg="grey",fg="white",cursor="hand2",command= lambda: button_click("/")).grid(row=0,column=3,padx=1,pady=1)

button_seven=Button(button_frame,text="7",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("7")).grid(row=1,column=0,padx=1,pady=1)
button_eight=Button(button_frame,text="8",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("8")).grid(row=1,column=1,padx=1,pady=1)
button_nine=Button(button_frame,text="9",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("9")).grid(row=1,column=2,padx=1,pady=1)
multiply=button_seven=Button(button_frame,text="*",width=10,height=3,bd=0,bg="grey",fg="white",cursor="hand2",command= lambda: button_click("*")).grid(row=1,column=3,padx=1,pady=1)

button_four=Button(button_frame,text="4",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("4")).grid(row=2,column=0,padx=1,pady=1)
button_five=Button(button_frame,text="5",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("5")).grid(row=2,column=1,padx=1,pady=1)
button_six=Button(button_frame,text="6",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("6")).grid(row=2,column=2,padx=1,pady=1)
subract=Button(button_frame,text="-",width=10,height=3,bd=0,bg="grey",fg="white",cursor="hand2",command= lambda: button_click("-")).grid(row=2,column=3,padx=1,pady=1)

button_one=Button(button_frame,text="1",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command=lambda: button_click("1")).grid(row=3,column=0,padx=1,pady=1)
button_two=Button(button_frame,text="2",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command=lambda: button_click("2")).grid(row=3,column=1,padx=1,pady=1)
button_three=Button(button_frame,text="3",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command=lambda: button_click("3")).grid(row=3,column=2,padx=1,pady=1)
add=Button(button_frame,text="+",width=10,height=3,bd=0,bg="grey",fg="white",cursor="hand2",command= lambda:button_click("+")).grid(row=3,column=3,padx=1,pady=1)

modulus=Button(button_frame,text="%",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda : button_click("%")).grid(row=4,column=0,padx=1,pady=1)
button_zero=Button(button_frame,text="0",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click("0")).grid(row=4,column=1,padx=1,pady=1)
dot=Button(button_frame,text=".",width=10,height=3,bd=0,bg="black",fg="white",cursor="hand2",command= lambda: button_click(".")).grid(row=4,column=2,padx=1,pady=1)
equal=Button(button_frame,text="=",width=10,height=3,bd=0,bg="grey",fg="white",cursor="hand2",command= lambda: button_equal()).grid(row=4,column=3,padx=1,pady=1)


wind.mainloop()
