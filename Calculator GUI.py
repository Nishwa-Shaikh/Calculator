#Making calculator GUI
from tkinter import Tk, Button, Entry
Calc = Tk()
Calc.title('Calculator')
Calc.geometry('500x600')
Calc.configure(bg='white')
entry = Entry(Calc, fg='black', bg='light grey', font=('none', 18))
entry.place(x=175, y=65)

def button_click(number):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert('end', str(current) + str(number))

def clear_entry():
    entry.delete(0, 'end')

def evaluate():
    result = eval(entry.get())
    entry.delete(0, 'end')
    entry.insert(0, str(result))

buttonC = Button(Calc, text='C', fg='Black', bg="light grey", font=("none", 30), command=clear_entry)
buttonC.place(x=180,y=150)
button_Plus = Button(Calc, text='+', fg="black", bg='light grey', font=("none", 30), command=lambda: button_click('+'))
button_Plus.place(x=180, y=240)
button_minus = Button(Calc, text='-', fg="black", bg='light grey', font=("none", 31), command=lambda: button_click('-'))
button_minus.place(x=180, y=330)
buttonX = Button(Calc, text='x', fg="black", bg='light grey', font=("none", 28), command=lambda: button_click('*'))
buttonX.place(x=180, y=420)
button_divide = Button(Calc, text='/', fg="black", bg='light grey', font=("none", 30), command=lambda: button_click('/'))
button_divide.place(x=180, y=515)
button_point = Button(Calc, text='.', fg="black", bg='light grey', font=("none", 30), command=lambda: button_click('.'))
button_point.place(x=250, y=420)
button_equal = Button(Calc, text='=', fg="black", bg='light grey', font=("none", 30), command=evaluate)
button_equal.place(x=310, y=420)
button_ans = Button(Calc, text='ANS', fg="black", bg='light grey', font=("none", 30))
button_ans.place(x=255, y=515)

button1=Button(Calc, text='1', fg='black', bg='light grey', font=('none', 30), command=lambda:button_click(1))
button1.place(x=250,y=150)
button2=Button(Calc, text='2', fg='black', bg='light grey', font=('none', 30), command=lambda:button_click(2))
button2.place(x=310,y=150)
button3=Button(Calc, text='3', fg='black', bg='Light grey', font=('none', 30),command=lambda:button_click(3))
button3.place(x=370, y=150)
button4=Button(Calc, text='4', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(4))
button4.place(x=250, y=240)
button5=Button(Calc, text='5', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(5))
button5.place(x=310, y=240)
button6=Button(Calc, text='6', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(6))
button6.place(x=370, y=240)
button7=Button(Calc, text='7', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(7))
button7.place(x=250, y=330)
button8=Button(Calc, text='8', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(8))
button8.place(x=310, y=330)
button9=Button(Calc, text='9', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(9))
button9.place(x=370, y=330)
button0=Button(Calc, text='0', fg='black', bg='Light grey', font=('none', 30), command=lambda:button_click(0))
button0.place(x=370, y=420)
Calc.mainloop()