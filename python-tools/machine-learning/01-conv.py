#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/07 13:52:25
@Author  : pengyuan.li
@File    : 01-conv.py
@Software: VSCode
'''

# here put the import lib
import torch

in_channels = 3  #输入通道数量
out_channels = 64  #输出通道数量
width = 100  #每个输入通道上的卷积尺寸的宽
heigth = 100  #每个输入通道上的卷积尺寸的高
kernel_size = 3  #每个输入通道上的卷积尺寸
batch_size = 1  #批数量

input = torch.randn(batch_size, in_channels, width, heigth)
conv_layer = torch.nn.Conv2d(in_channels,
                             out_channels,
                             kernel_size=kernel_size)

out_put = conv_layer(input)

print(input.shape)
print(out_put.shape)
print(conv_layer.weight.shape)
# torch.Size([1, 3, 100, 100])
# torch.Size([1, 64, 98, 98])
# torch.Size([64, 3, 3, 3])
