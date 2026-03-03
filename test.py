import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义函数
def f(x1, x2):
    return (x1 - 1)**2 + x2 - 2

# 创建数据点
x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
x1, x2 = np.meshgrid(x1, x2)
z = f(x1, x2)

# 创建图形
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 绘制3D表面图
surf = ax.plot_surface(x1, x2, z, cmap='viridis')

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 设置标签
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('f(X1, X2)')

# 显示图形
plt.show()