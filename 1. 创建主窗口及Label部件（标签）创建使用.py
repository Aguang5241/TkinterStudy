import tkinter as tk
# 实例化object，建立窗口window
window = tk.Tk()
# 窗口名
window.title('图片转化')
# 设置窗口大小
window.geometry('600x600')
# 界面设置标签
l = tk.Label(window, text = '阿光（v1.0）', bg = 'green', font = ('Times New Roman', 14), width = 30, height = 2)
# 放置标签
# 方法有：l.pack();l.place()
l.pack()
# 窗口主循环显示
window.mainloop()