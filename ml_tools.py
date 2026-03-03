import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay


def get_confusion_matrix_and_heatmap(y_true, y_pred, labels=None, normalize=None,
                                     title=None, cmap=plt.cm.Blues, save_dir=None):
    # 检查 normalize 参数是否合法
    assert normalize in [None, 'true', 'pred', 'all'], \
        "normalize 必须是 None, 'true', 'pred' 或 'all'\n 'true'表示按真实标签标准化，\n 'pred'表示按预测标签标准化 \n 'all'表示整个矩阵标准化"
    
    
    # 绘制图像
    disp = ConfusionMatrixDisplay.from_predictions(
        y_true=y_true,
        y_pred=y_pred,
        labels=labels,
        cmap=cmap,
        normalize=normalize
    )
    disp.ax_.set_title(title if title else "Confusion Matrix")
    
    cm = disp.confusion_matrix

    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(os.path.join(save_dir, f'{title if title else "confusion_matrix"}.png'))
    plt.close()
    
    return cm.tolist()

def print_confusion_matrix(y_true, y_pred, type='binary', labels=None):
    """
    打印混淆矩阵，带中文说明和DataFrame表格展示
    
    参数:
    - y_true: 实际标签
    - y_pred: 预测标签
    - type: 'binary' 或 'multiclass'
    - labels: 标签列表（多分类时使用，保证行列顺序一致）
    """
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    if type == 'binary':
        # 检查输入是否为2x2矩阵
        if cm.shape != (2, 2):
            raise ValueError("二分类任务时，混淆矩阵必须是2x2的")
        
        # 展开混淆矩阵
        tn, fp, fn, tp = cm.ravel()
        
        print("混淆矩阵结果如下：")
        print(f" 真负 (TN): {tn} —— 实际为负类，预测也为负类")
        print(f" 假正 (FP): {fp} —— 实际为负类，但预测为正类（误报）")
        print(f" 假负 (FN): {fn} —— 实际为正类，但预测为负类（漏报）")
        print(f" 真正 (TP): {tp} —— 实际为正类，预测也为正类")
        
        # 用DataFrame展示混淆矩阵表格
        print("\n混淆矩阵表格：")
        df = pd.DataFrame(
            [[tn, fp], [fn, tp]],
            index=["实际负类", "实际正类"],
            columns=["预测负类", "预测正类"]
        )
        print(df)

    elif type == 'multiclass':
        if labels is None:
            # 自动从 y_true 和 y_pred 中获取所有类别
            labels = sorted(list(set(y_true) | set(y_pred)))
        
        print("多分类混淆矩阵结果如下：")
        print("行：实际类别，列：预测类别\n")
        
        # 用DataFrame展示
        df = pd.DataFrame(cm, index=[f"实际:{l}" for l in labels],
                             columns=[f"预测:{l}" for l in labels])
        print(df)
    else:
        raise ValueError("type 只能是 'binary' 或 'multiclass'")

    # 返回DataFrame供后续使用
    return df
