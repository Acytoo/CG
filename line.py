import matplotlib.pyplot as plt
'''
x=[1,2,3,4,5,6,7]
y = [2,3,4,5,6,7,8]
plt.scatter(x,y)
plt.show()
'''
#先画直线，再画园，使用不同的算法，先写完基本功能，再加上图形界面
# DAA 算法 数值微分算法 digital differential analyzer


'''
print
("Please enter the points of the line")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

deltax = c - a
deltay = d - b
k = deltay/deltax
#print(str(k) + " " +  str(deltax) + " " + str(deltay))
# (a, b) (c, d)

x=[]
y=[]
x.append(a)
y.append(b)
i = 0

while i <= deltax:
      x.append(a+i)
      y.append(b+i*k)
      i+=1
      #print(i)

print(x)
print(y)
plt.scatter(x,y)
plt.grid(True)  #加上网格
plt.show()
'''
# 中点Bresenham算法画圆

r = int(input('Please enter the radius of the circle\n'))

d = 1 - r
x = 0
y = r
X = [x]
Y = [y]

while x < y:   
      if d <= 0:
            d = d + 2*x + 3
            x = x + 1
            X.extend([x, y, y, x, -x, -y, -y, -x])
            Y.extend([y, x, -x, -y, -y, -x, x, y]) 
      else:
            d = d + 2*(x-y) + 5
            x = x + 1
            y = y - 1
            X.extend([x, y, y, x, -x, -y, -y, -x])
            Y.extend([y, x, -x, -y, -y, -x, x, y]) 

plt.scatter(X,Y)
##plt.xlim(-20, 20)
##plt.ylim(-20, 20)
plt.axis('equal')
plt.grid()
plt.show()


