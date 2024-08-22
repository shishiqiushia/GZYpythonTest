import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



# 创建一个3D坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义立方体的顶点坐标
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# 定义立方体的面
faces = [
    (0, 1, 5, 4),
    (1, 2, 6, 5),
    (2, 3, 7, 6),
    (3, 0, 4, 7),
    (0, 1, 2, 3),
    (4, 5, 6, 7)
]

# # 绘制立方体的面
# for face in faces:
#     ax.add_collection3d(plt.Polygon(vertices[face]))


# 绘制立方体的面
for face in faces:
    vertices_for_face = [vertices[i] for i in face]  # 使用列表推导式从 vertices 中提取顶点
    polygon = Poly3DCollection([vertices_for_face], alpha=0.5)
    polygon.set_color('blue')
    ax.add_collection3d(polygon)


# 设置坐标轴范围和标签
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()