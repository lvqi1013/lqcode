# -*- coding:utf-8 -*-
"""
@file name  : img_tools.py
@author     : LQ
@date       : 2025/05/07
@brief      : Brief description of the file
"""

import cv2


def imread(filename,flags = cv2.IMREAD_COLOR):
    img = cv2.imread(filename,flags)
    assert img is not None,"图片加载失败！请注意路径中是否存在中文！或路径是否正确！"
    return img

