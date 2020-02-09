'''
再接下来我们来看place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的
(50, 100)，就是将这个部件放在坐标为(x=50, y=100)的这个位置, 后面的参数 
anchor='nw'，就是前面所讲的锚定点是西北角
'''
import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，place 放置方法（精准的放置到指定坐标点的位置上）
tk.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')
 
# 第5步，主窗口循环显示
window.mainloop()