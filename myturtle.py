import turtle
import math

# 定义三条边的长度
a = 100
b = 150
c = 200

# 计算角度
angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
angle_C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

# 创建turtle对象
t = turtle.Turtle()

# 绘制三角形
t.forward(a)
t.left(180 - angle_C)
t.forward(b)
t.left(180 - angle_A)
t.forward(c)

# 结束绘制
turtle.done()
