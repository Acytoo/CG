from ytCGFUN import *
'''
写一个图形学展示程序，分章展示所学算法，每一章一个弹出窗口
下面是基本界面，构造每一章的入口
下面是一个帮助，并排一个退出
'''

def Ch1():
    pass



root = Tk()
#root.geometry('303x600')
root.title('图形学')
root.iconbitmap('yt.ico')

Button(root, text='直线', width = 13, command = line)\
             .grid(row = 0, column = 1, padx = 10, pady = 5)
Button(root, text='第二章', width = 13, command = pop_up_help)\
             .grid(row = 1, column = 1, padx = 10, pady = 5)
Button(root, text='第三章', width = 13, command = pop_up_help)\
             .grid(row = 2, column = 1, padx = 10, pady = 5)
Button(root, text='第四章', width = 13, command = pop_up_help)\
             .grid(row = 3, column = 1, padx = 10, pady = 5)
Button(root, text='第五章', width = 13, command = pop_up_help)\
             .grid(row = 4, column = 1, padx = 10, pady = 5)
Button(root, text='第六章', width = 13, command = pop_up_help)\
             .grid(row = 5, column = 1, padx = 10, pady = 5)
Button(root, text='第七章', width = 13, command = pop_up_help)\
             .grid(row = 6, column = 1, padx = 10, pady = 5)
Button(root, text='第八章', width = 13, command = pop_up_help)\
             .grid(row = 7, column = 1, padx = 10, pady = 5)
Button(root, text='帮助', width = 9, command = pop_up_help)\
             .grid(row = 8, column = 0, padx = 10, pady = 5)
Button(root, text='退出', width = 9, command = root.destroy)\
             .grid(row = 8, column = 2, padx = 10, pady = 5)

root.mainloop()


