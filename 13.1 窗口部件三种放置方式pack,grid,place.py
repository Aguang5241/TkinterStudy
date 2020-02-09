'''
grid 是方格, 所以所有的内容会被放在这些规律的方格中
'''
import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，grid 放置方法
# 以下的代码就是创建一个三行三列的表格，其实 grid 就是用表格的形式定位的
# 这里的参数 row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，
# ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距
for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
 
# 第5步，主窗口循环显示
window.mainloop()