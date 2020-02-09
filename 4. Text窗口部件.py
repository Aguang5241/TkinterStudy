import tkinter as tk

window = tk.Tk()
window.title('图像转换器')
window.geometry('600x600')

e = tk.Entry(window, show = None)
e.pack()

# 定义两个触发事件时的函数insert_point和insert_end
# 注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面
def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)

# 创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text = '插入内容', width = 10, height = 2, command = insert_point)
b1.pack()

b2 = tk.Button(window, text = '末尾添加', width = 10, height = 2, command = insert_end)
b2.pack()

# 创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height = 3)
t.pack()

window.mainloop()