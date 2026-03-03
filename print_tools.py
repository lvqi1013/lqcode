import torch
import matplotlib.pyplot as plt


def print_device(device):
    """
    打印训练设备的信息。
    :param device: 获取的设备
    :return: 无
    """
    print('==============所用训练设备============')
    print(f'设备：{device}')
    if device.type == 'cuda':
        print(f'设备名称为：{torch.cuda.get_device_name(0)}')
    print('====================================')
    print()


def lineOutput(data):
    """
    把可迭代对象中的每一个数据按行进行输出。
    """
    print("=============开始输出===========")
    for i in data:
        print(i)
    print("=============输出结束===========")
