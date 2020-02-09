import tkinter as tk

window = tk.Tk()
window.title('图片格式转换')
window.geometry('600x600')

# 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
var = tk.StringVar()
# bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高
l = tk.Label(window, textvariable = var, bg = 'green', fg = 'white', font = ('Arial', 14), width = 30, height = 2)
l.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('别点了')
    else:
        on_hit = False
        var.set('')

# 在窗口界面设置放置Button按键
b = tk.Button(window, text = '点击我！', font = ('Arial', 12), width = 10, height = 1, command = hit_me)
b.pack()

window.mainloop()