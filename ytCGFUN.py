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
    

'''
画直线
'''
def LINE():
      line()


class line():

      def __init__(self):
            self.tk = Toplevel(takefocus = True)
            self.tk.lift(aboveThis = None)
            self.tk.title('直线的画法')
            #self.tk.geometry('500x600')
            self.tk.iconbitmap('yt.ico')
            self.p1x = StringVar()
            self.p1y = StringVar()
            self.p2x = StringVar()
            self.p2y = StringVar()
            self.is_number = self.tk.register(self.isnum)
            #self._DAA = self.tk.register(self.DAA)
            Label(self.tk, text = '请输入线段的两个端点').grid(row = 0, column = 0, padx = 5, pady= 3, columnspan = 3)
            Label(self.tk, text = '点1').grid(row = 1, column = 0)
            e1x=Entry(self.tk, textvariable=self.p1x, validate='key', validatecommand = (self.is_number, '%P'))\
                           .grid(row = 1, column=1, padx = 5, pady= 3)
            e1y=Entry(self.tk, textvariable=self.p1y, validate='key', validatecommand = (self.is_number, '%P'))\
                           .grid(row = 1, column=2, padx = 5, pady= 3)
            Label(self.tk, text = '点2').grid(row = 2, column = 0, padx = 5, pady= 3)
            e2x=Entry(self.tk, textvariable=self.p2x, validate='key', validatecommand = (self.is_number, '%P'))\
                           .grid(row = 2, column=1, padx = 5, pady= 3)
            e2y=Entry(self.tk, textvariable=self.p2y, validate='key', validatecommand = (self.is_number, '%P'))\
                           .grid(row = 2, column=2, padx = 5, pady= 3)            
            Label(self.tk, text = '请选择算法').grid(row = 3, column = 0, padx = 5, pady= 3, columnspan = 3)           
            Button(self.tk, text = 'DAA', command = self.DAA, width = 15, height = 2).grid(row = 4, column = 0, padx = 3, pady = 3, ipadx = 2, ipady = 2, columnspan = 3)
            #print('Here is the content: ', self.p1x.get())
            self.tk.mainloop()


      #因为传递的额外的参数，所以验证函数需要注册
      def isnum(self, s):
            #s = s.get()
            #print(s,'iwascalled')
            try:
                  float(s)
                  return True
            except ValueError:
                  pass
 
            try:
                  import unicodedata
                  unicodedata.numeric(s)
                  return True
            except (TypeError, ValueError):
                  pass
            return False

      def DAA(self):
            x1 = float(self.p1x.get())
            y1 = float(self.p1y.get())
            x2 = float(self.p2x.get())
            y2 = float(self.p2y.get())
            deltax = x2 - x1
            deltay = y2 - y1
            k = deltay/deltax
            x=[]
            y=[]
            x.append(x1)
            y.append(y1)
            i = 0
            while i <= deltax:
                  x.append(x1+i)
                  y.append(y1+i*k)
                  i+=1            
            #print(x)
            #print(y)
            plt.scatter(x,y)
            plt.grid(True)  #加上网格
            plt.show()

