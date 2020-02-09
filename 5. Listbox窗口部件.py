import tkinter as tk

window = tk.Tk()
window.title('aguang is handsome')
window.geometry('600x600')

# 创建变量，用var1用来接收鼠标点击具体选项的内容
var1 = tk.StringVar()
l = tk.Label(window, bg = 'green', fg = 'yellow', font = ('Arial', 14), width = 10, height = 2, textvariable = var1)
l.pack()

def print_selection():
    # 获取当前选中的文本
    value = lb.get(lb.curselection())
    # 为label设置值
    var1.set(value)

b1 = tk.Button(window, text = 'print selection', width = 15, height = 2, command = print_selection)
b1.pack()

var2 = tk.StringVar()
# 为变量var2设置值
var2.set((1,2,3,4))

# 创建Listbox并为其添加内容
# 将var2的值赋给Listbox
lb = tk.Listbox(window, listvariable = var2)

# 创建一个list并将值循环添加到Listbox控件中
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)

lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()