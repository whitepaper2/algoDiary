#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2022/03/09 15:02:02
@Author  : pengyuan.li
@File    : 04-modifyModel.py
@Software: VSCode
'''

# here put the import lib
from torchvision.models import vgg11
from torch import nn
vggnet = vgg11(pretrained=False)
print(vggnet)
vggnet.classifier.add_module('linear',nn.Linear(in_features=1000,out_features=10))
print('-'*50,vggnet)
vggnet.classifier[6]=nn.Linear(in_features=1000,out_features=10)
print('-'*50,vggnet)