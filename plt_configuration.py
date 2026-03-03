import matplotlib.pyplot as plt

def setTheFont2Chinese(font = 'KaiTi'):
    # 设置字体为支持中文的字体
    plt.rcParams['font.sans-serif'] = [font]  # 替换为你找到的字体名称
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
