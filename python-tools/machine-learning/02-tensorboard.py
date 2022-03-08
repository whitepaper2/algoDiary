#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/07 16:32:53
@Author  : pengyuan.li
@File    : 02-tensorboard.py
@Software: VSCode
'''

# here put the import lib
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(root="data",
                                      train=True,
                                      download=True,
                                      transform=ToTensor())

test_data = datasets.FashionMNIST(root="data",
                                  train=False,
                                  download=True,
                                  transform=ToTensor())
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
train_features, train_labels = next(iter(train_dataloader))

print(train_features.shape, train_labels.shape)

# conda install tensorboard
# from torch.utils.tensorboard import SummaryWriter
# writer = SummaryWriter(log_dir="./board/mnist01")

# writer.add_image('01',train_features)
