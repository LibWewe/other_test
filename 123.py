#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 123.py
# @Time: 2018/2/2 19:48
# @Last Modified time: 2018/2/2 19:48
# @Explain: This file is for a test

import numpy as np
import os
from matplotlib.pyplot import *


def test_function():
    x_stick = np.linspace(-5, 5, 11)
    y_stick = np.linspace(-5, 5, 11)
    x, y = np.meshgrid(x_stick, y_stick)
    print(x, y)


if __name__ == '__main__':
    test_function()
