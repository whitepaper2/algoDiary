#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/07 17:01:53
@Author  : pengyuan.li
@File    : 03-resnet.py
@Software: VSCode
'''

# here put the import lib

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import torch.optim as optim


class ResBlock(nn.Module):

    def __init__(self) -> None:
        super().__init__()

    def forward():
        pass


class ResNet(nn.Module):

    def __init__(self) -> None:
        super().__init__()

    def forward():
        pass


def trainModel(train, test):
    resnet = ResNet()
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.SGD(params=resnet.parameters(),lr=1e-2,momentum=0.2)
    epoches = 10 # 轮次
    for epoch in range(epoches):
        for i, (imgs,labels) in enumerate(train):
            # i = [0,937] ,60000/64=937
            print(i)
            
    pass


if __name__ == "__main__":
    training_data = datasets.FashionMNIST(root="data",
                                          train=True,
                                          download=True,
                                          transform=ToTensor())

    test_data = datasets.FashionMNIST(root="data",
                                      train=False,
                                      download=True,
                                      transform=ToTensor())
    train = DataLoader(training_data, batch_size=64, shuffle=True)
    test = DataLoader(test_data, batch_size=64, shuffle=True)
    trainModel(train, test)
    pass