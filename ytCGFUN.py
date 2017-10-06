from tkinter import *
import matplotlib.pyplot as plt
'''
此文件为图形学课堂展示软件的内部函数文件
'''


def exit_chile(child):
      child.destroy()
def pop_up_help():
      top = Toplevel()
      top.geometry('500x300')
      text = Text(top, font=(None, 13))
      text.insert(END, '图形学课堂展示软件\n 20154479\nacytoo@gmail.com\nAll right reserved\n')
      b1 = Button(text,text='知道了',command=lambda m = top :exit_chile(m))
      text.pack()
      text.window_create(INSERT,window=b1)
    
class Chapter():
    def __init__(self, a):
        print(a)
        self.tk = Toplevel(takefocus = True)
        self.tk.lift(aboveThis=None)
        self.tk.title('第一章')
        self.tk.geometry('200x300')
        self.tk.iconbitmap('yt.ico')
        self.tk.mainloop()

      


def Ch(c):
      print(c)
      Chapter(c)      


'''
画直线
'''

def DAA():
      print('DAA')
      pass


class line():
      def __init__(self):
            self.tk = Toplevel(takefocus = True)
            self.tk.lift(aboveThis = None)
            self.tk.title('直线的画法')
            self.tk.geometry('200x300')
            self.tk.iconbitmap('yt.ico')
            Button(self.tk, text = 'DAA', command = DAA).pack()

            
            self.tk.mainloop()
