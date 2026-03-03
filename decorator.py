# -*- coding:utf-8 -*-
"""
@file name  : decorator.py
@author     : LQ
@date       : 2025/12/09
@brief      : 用于存放自己写的装饰器的代码
"""

import time
from functools import wraps
"""
decirtor是一种在不修改原函数代码的前提下，为其添加额外的功能的工具。

本质上是一个以函数作为参数，并返回一个新函数的函数。

装饰器的核心思想：给函数套上一层外壳，在函数执行前后做一些额外的操作，它不会改变原函数的内容，也不会改变函数的调用方式.

functools.wraps 的作用不使用@wraps(func)时，装饰后的函数wrapper会覆盖原函数的__name__、__doc__等元信息（比如test_func.__name__会变成wrapper），导致调试 / 反射时出错，务必加上。

"""
def lq_decorator(func):
    @wraps(func)
    def wrapper():
        print('函数执行前')
        func()
        print('函数执行后')
        
    return wrapper()

def lq_timer(func):
    """
    基础班耗时统计装饰器    
    :param func: 需要计时的函数
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        # 1.record the start time
        start_time = time.perf_counter()
        print(f'====== function {func.__name__} start')

        # 2.operate the orginal function
        result = func(*args,**kwargs)

        # 3. record the ending time and calculate the waste time
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        # 4. print the waste time
        print(f'====== function {func.__name__} waste time:{elapsed_time:.4f} seconds')

        # 5. 返回原函数的结果（关键：不影响原函数使用
        return result

    return wrapper


class Lq_Timer:
    def __init__(self,title = None):
        self.name = title
    
    def __enter__(self):
        print(f'start {self.name} and time')
        self.start_time = time.time()
        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time
        print(f'exhaulst :{self.duration:.2f} seconds')
        print('end')    

if __name__ == '__main__':
    # @lq_decorator
    # def say_hello():
    #     """
    #     say_hello 的 Docstring
    #     """
    #     print('hello')
    # @lq_timer  # 直接装饰目标函数
    with Lq_Timer(title='计时'):
        def test_func(n):
            """示例函数：计算1到n的累加"""
            total = 0
            for i in range(n):
                total += i
            return total
    
        test_func(10000000)