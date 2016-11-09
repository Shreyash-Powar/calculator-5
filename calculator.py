from tkinter import *
import math
def operandfinal1():
         global operand1
         if dot not in operand1:
            operand1=int("".join(operand1))
         else:
            operand1=float("".join(operand1))
def val1():
    txt.insert(INSERT,"7")
    if not operation:
        global operand1
        operand1.append('7')
    else:
        global operand2
        operand2.append('7')
def val2():
    txt.insert(INSERT,"8")
    if not operation:
        global operand1
        operand1.append('8')
    else:
        global operand2
        operand2.append('8')
def val3():
    txt.insert(INSERT,"9")
    if not operation:
        global operand1
        operand1.append('9')
    else:
        global operand2
        operand2.append('8')
def val4():
    txt.insert(INSERT,"4")
    if not operation:
        global operand1
        operand1.append('4')
    else:
        global operand2
        operand2.append('4')
def val5():
    txt.insert(INSERT,"5")
    if not operation:
        global operand1
        operand1.append('5')
    else:
        global operand2
        operand2.append('5')
def val6():
    txt.insert(INSERT,"6")
    if not operation:
        global operand1
        operand1.append('6')
    else:
        global operand2
        operand2.append('6')
def val7():
    txt.insert(INSERT,"1")
    if not operation:
        global operand1
        operand1.append('1')
    else:
        global operand2
        operand2.append('1')
def val8():
    txt.insert(INSERT,"2")
    if not operation:
        global operand1
        operand1.append('2')
    else:
        global operand2
        operand2.append('2')
def val9():
    txt.insert(INSERT,"3")
    if not operation:
        global operand1
        operand1.append('3')
    else:
        global operand2
        operand2.append('3')
    
def val10():
    txt.insert(INSERT,"0")
    if not operation:
        global operand1
        operand1.append('0')
    else:
        global operand2
        operand2.append('0')
def val11():
    if not operation:
        global operand1
        if dot not in operand1:
            txt.insert(INSERT,".")
            operand1.append('.')
        else:
            pass
    else:
        global operand2
        if dot not in operand2:
            txt.insert(INSERT,".")
            operand2.append('.')
        else:
            pass
def sol():
    txt.delete("1.0",END)
    global operand1
    global solution
    global operand2
    if operation <=4:
        if dot not in operand2:
            operand2=int("".join(operand2))
        else:
            operand2=float("".join(operand2))
    if operation==1:
            s=operand1+operand2
            txt.insert(INSERT,s)
    elif operation==2:
            diff=operand1-operand2
            txt.insert(INSERT,diff)
    elif operation==3:
            pro=operand1*operand2
            txt.insert(INSERT,pro)
    elif operation==4:
            div=operand1/operand2
            txt.insert(INSERT,div)
    elif operation==19:
       txt.delete("1.0",END)
       log=math.log10(operand1)
       txt.insert(INSERT,log)
    elif operation==17:
        txt.delete("1.0",END)
        sqrt=math.sqrt(operand1)
        txt.insert(INSERT,sqrt)
    elif operation==18:
       txt.delete("1.0",END)
       exp=math.exp(operand1)
       txt.insert(INSERT,exp)
"""elif operation==5:
            txt.delete("1.0",END)
            sine=math.sin(math.radians(operand1))
            txt.insert(INSERT,sine)
    elif operation==6:
            txt.delete("1.0",END)
            cosine=math.cos(math.radians(operand1))
            txt.insert(INSERT,cosine)
    elif operation==7:
            txt.delete("1.0",END)
            tangent=math.sin(math.radians(operand1))/math.cos(math.radians(operand1))
            txt.insert(INSERT,tangent)
    elif operation==8:
            txt.delete("1.0",END)
            co=math.cosec(math.radians(operand1))
            txt.insert(INSERT,co)
    elif operation==9:
            txt.delete("1.0",END)
            secant=math.sec(math.radians(operand1))
            txt.insert(INSERT,secant)
    elif operation==10:
            txt.delete("1.0",END)
            cotengent=math.cot(math.radians(operand1))
            txt.insert(INSERT,cotengent)"""
  #  else:
          #  txt.insert(INSERT,"error")
def opt1():
    global operand1
    global operation
    if not operation:
        operation=1
        txt.insert(INSERT,"+")
        operandfinal1()
   
    else:
            pass
def opt2():
    global operand1
    global operation
    if not operation:
        txt.insert(INSERT,"-")
        operation=2
        operandfinal1()
    
    else:
            pass
def opt3():
    global operand1
    global operation
    if not operation:
        operation=3
        txt.insert(INSERT,"*")
        operandfinal1()
    else:
            pass
def opt4():
    global operand1
    global operation
    if not operation:
        operation=4
        txt.insert(INSERT,"/")
        operandfinal1()
    else:
            pass
"""def opt5():
    global operand1
    global operation
    if not operation:
        operation=5
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"sin(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt6():
    global operand1
    global operation
    if not operation:
        operation=6
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"cos(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
        pass
def opt7():
    global operand1
    global operation
    if not operation:
        operation=7
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"tan(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt8():
    global operand1
    global operation
    if not operation:
        operation=8
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"cosec(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt9():
    global operand1
    global operation
    if not operation:
        operation=9
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"sec(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt10():
    global operand1
    global operation
    if not operation:
        operation=10
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"cot(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt11():
    global operand1
    global operation
    if not operation:
        operation=11
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass"""
def opt17():
    global operand1
    global operation
    if not operation:
        operation=17
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"sqrt")
        txt.insert(INSERT,"(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt18():
    global operand1
    global operation
    if not operation:
        operation=18
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"e**")
        txt.insert(INSERT,"(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass
def opt19():
    global operand1
    global operation
    if not operation:
        operation=19
        operandfinal1()
        txt.delete("1.0",END)
        txt.insert(INSERT,"log10")
        txt.insert(INSERT,"(")
        txt.insert(INSERT,operand1)
        txt.insert(INSERT,")")
    else:
            pass





def clr():
    global operand1
    global operand2
    global operation
    txt.delete("1.0",END)
    operation=0
    operand1=[]
    operand2=[]
    
operand1=[]
operand2=[]
dot='.'
operation=0
t=Tk()
t.title("Calculator")
t.geometry("220x290")
txt=Text(width=20,height=2)
txt.grid(row=0,column=0,columnspan=6,rowspan=2)
button1=Button(t,text='7' ,font=60,height=2,width=5,command=val1).grid(row=4,column=2)
button2=Button(text='8',font=60,height=2,width=5,command=val2).grid(row=4,column=3)
button3=Button(text='9',font=60,height=2,width=5,command=val3).grid(row=4,column=4)
op1=Button(text='+',font=60,height=2,width=5,command=opt1).grid(row=4,column=5)
button4=Button(text='4',font=60,height=2,width=5,command=val4).grid(row=5,column=2)
button5=Button(text='5',font=60,height=2,width=5,command=val5).grid(row=5,column=3)
button6=Button(text='6',font=60,height=2,width=5,command=val6).grid(row=5,column=4)
op2=Button(text='-',font=60,height=2,width=5,command=opt2).grid(row=5,column=5)
button7=Button(text='1',font=60,height=2,width=5,command=val7).grid(row=6,column=2)
button8=Button(text='2',font=60,height=2,width=5,command=val8).grid(row=6,column=3)
button9=Button(text='3',font=60,height=2,width=5,command=val9).grid(row=6,column=4)
op3=Button(text='*',font=60,height=2,width=5,command=opt3).grid(row=6,column=5)
button10=Button(text='0',font=60,height=2,width=5,command=val10).grid(row=7,column=2)
op4=Button(text='/',font=60,height=2,width=5,command=opt4).grid(row=7,column=3)
button10=Button(text='.',font=60,height=2,width=5,command=val11).grid(row=7,column=4)
button10=Button(text='=',font=60,height=2,width=5,command=sol).grid(row=7,column=5)
op17=Button(text='SQRT',font=60,height=2,width=5,command=opt17).grid(row=3,column=2)
op18=Button(text='EXP',font=60,height=2,width=5,command=opt18).grid(row=3,column=3)
op19=Button(text='log10',font=60,height=2,width=5,command=opt19).grid(row=3,column=4)
clrbutton=Button(text='CLR',font=60,height=2,width=5,command=clr).grid(row=3,column=5)
"""op5=Button(text='sin',font=60,height=2,width=5,command=opt5).grid(row=2,column=0)
op6=Button(text='cos',font=60,height=2,width=5,command=opt6).grid(row=2,column=1)
op7=Button(text='tan',font=60,height=2,width=5,command=opt7).grid(row=2,column=2)
op8=Button(text='cosec',font=60,height=2,width=5,command=opt8).grid(row=2,column=3)
op9=Button(text='sec',font=60,height=2,width=5,command=opt9).grid(row=2,column=4)
op10=Button(text='cot',font=60,height=2,width=5,command=opt10).grid(row=2,column=5)
op11=Button(text='1/sin',font=60,height=2,width=5,command=opt11).grid(row=3,column=0)
op12=Button(text='1/cos',font=60,height=2,width=5,command=opt12).grid(row=3,column=1)
op13=Button(text='1/tan',font=60,height=2,width=5,command=opt13).grid(row=3,column=2)
op14=Button(text='1/cosec',font=60,height=2,width=5,command=opt14).grid(row=3,column=3)
op15=Button(text='1/sec',font=60,height=2,width=5,command=opt15).grid(row=3,column=4)
op16=Button(text='1/cot',font=60,height=2,width=5,command=opt16).grid(row=3,column=5)"""
t.mainloop()





