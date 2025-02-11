Calculadora//250x330//

global btn_click
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
global btn_clear
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

global btn_equal
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

global expression
expression = ""
global input_text
input_text = StringVar()

#*Create the buttons*
Button(app_window, text="C", command=btn_clear).place(x=10, y=30, width=50, height=50)
Button(app_window, text="1", command=lambda: btn_click(1)).place(x=10, y=90, width=50, height=50)
Button(app_window, text="2", command=lambda: btn_click(2)).place(x=70, y=90, width=50, height=50)
Button(app_window, text="3", command=lambda: btn_click(3)).place(x=130, y=90, width=50, height=50)
Button(app_window, text="+", command=lambda: btn_click('+')).place(x=190, y=90, width=50, height=50)

Button(app_window, text="4", command=lambda: btn_click(4)).place(x=10, y=150, width=50, height=50)
Button(app_window, text="5", command=lambda: btn_click(5)).place(x=70, y=150, width=50, height=50)
Button(app_window, text="6", command=lambda: btn_click(6)).place(x=130, y=150, width=50, height=50)
Button(app_window, text="-", command=lambda: btn_click('-')).place(x=190, y=150, width=50, height=50)

Button(app_window, text="7", command=lambda: btn_click(7)).place(x=10, y=210, width=50, height=50)
Button(app_window, text="8", command=lambda: btn_click(8)).place(x=70, y=210, width=50, height=50)
Button(app_window, text="9", command=lambda: btn_click(9)).place(x=130, y=210, width=50, height=50)
Button(app_window, text="*", command=lambda: btn_click('*')).place(x=190, y=210, width=50, height=50)

Button(app_window, text="0", command=lambda: btn_click(0)).place(x=10, y=270, width=50, height=50)
Button(app_window, text="=", command=btn_equal).place(x=70, y=270, width=110, height=50)
Button(app_window, text="/", command=lambda: btn_click('/')).place(x=190, y=270, width=50, height=50)

#*Create the input field*
entry_field = Entry(app_window, textvariable=input_text)
entry_field.place(x=70, y=30, width=170, height=50)


