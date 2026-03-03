import numpy as np
import matplotlib.pyplot as plt

def plot_loss_curve(losses:list,title:str,save_path:str = None):
    """
    功能：绘制并可选保存损失曲线图

    参数:
        losses (list): 每个 epoch 的平均损失
        title (str): 图像标题
        save_path (str or None): 如果提供路径，则保存图像
    """
    plt.figure(figsize=(8,5))
    plt.plot(range(1,len(losses) + 1), losses,marker = 'o')
    plt.title(title)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f'损失图像已保存至{save_path}')
    plt.close()
