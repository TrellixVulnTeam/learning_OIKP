from tkinter import *
root = Tk()
root.option_add("*font",("FixedSys",14))
buffer = StringVar()
buffer.set( "")
e = Entry (root, textvariable = buffer)

#list box 연동
lb = Listbox(root)

#scroll bar 생성
sb1 = Scrollbar(root, orient='v',command =lb.yview)
sb2 = Scrollbar(root, orient='h', command =lb.xview)

#list박스 설정
lb.configure(yscrollcommand=sb1.set)
lb.configure(xscrollcommand=sb2.set)

#연산
def cals(event):
    expr = buffer.get()
    lb.insert('end', expr)
    lb.see('end')
    value = eval(expr)
    buffer.set(str(value))

#식 리턴받기
def get_expr(event):
    buffer.set(lb.get('active'))

#바인딩
e.bind('<Return>', cals)
lb.bind('<Double-1>',get_expr)

#grid
e.grid(row=0,columnspan = 2,sticky = 'ew')
lb.grid(row=1,column = 0,sticky = 'nsew')
sb1.grid(row=1,column = 1,sticky = 'nsew')
sb2.grid(row=2,column = 0,sticky = 'ew')

#포커스 설정
e.focus_set()
root.mainloop() #윈도우창 끄지.

