import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis("off")

# 节点位置定义 (x, y)
positions = {
    "Input": (0, 0),
    "Shared_Linear": (2, 0),
    "BN": (3.5, 0),
    "ReLU1": (5, 0),
    "Dropout1": (6.5, 0),
    "Residual1": (8.5, 1),
    "Residual2": (10.5, 1),
    "Shared_Output": (12.5, 0),
    "Binary": (15, 2),
    "Regression": (15, 0),
    "Multiclass": (15, -2),
}

# 节点文本
labels = {
    "Input": "输入\n(input_dim)",
    "Shared_Linear": "Linear\n(input_dim→hidden_dim)",
    "BN": "BatchNorm1d",
    "ReLU1": "ReLU",
    "Dropout1": "Dropout(0.3)",
    "Residual1": "ResidualBlock×1",
    "Residual2": "ResidualBlock×2",
    "Shared_Output": "共享特征\n(hidden_dim)",
    "Binary": "Binary Head\n→ (1)",
    "Regression": "Regression Head\n→ (1)",
    "Multiclass": "Multiclass Head\n→ (K)",
}

# 绘制矩形节点
for key, (x, y) in positions.items():
    box = mpatches.FancyBboxPatch(
        (x-0.7, y-0.4), 1.4, 0.8,
        boxstyle="round,pad=0.1", fc="lightblue", ec="black", lw=1.2
    )
    ax.add_patch(box)
    ax.text(x, y, labels[key], ha="center", va="center", fontsize=9)

# 绘制连线（顺序连接）
edges = [
    ("Input", "Shared_Linear"),
    ("Shared_Linear", "BN"),
    ("BN", "ReLU1"),
    ("ReLU1", "Dropout1"),
    ("Dropout1", "Residual1"),
    ("Residual1", "Residual2"),
    ("Residual2", "Shared_Output"),
    ("Shared_Output", "Binary"),
    ("Shared_Output", "Regression"),
    ("Shared_Output", "Multiclass"),
]

for start, end in edges:
    x1, y1 = positions[start]
    x2, y2 = positions[end]
    ax.annotate("",
                xy=(x2-0.7, y2), xytext=(x1+0.7, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2))

plt.title("MultiTaskModel 网络结构图", fontsize=12, weight="bold")
plt.show()
