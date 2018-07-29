# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import torch
import numpy as np
from torch.autograd import Variable

#%% test if torch GPU works
a = torch.Tensor([[1,2],[3,4]])
if torch.cuda.is_available():
    cuda_a = a.cuda()
    print(cuda_a)
else:
    print(a)

#%% test numpy <-> tensor

b = torch.randn((4,5))
c = torch.zeros((4,5))
c[0,0] = 20
d = np.array([[1,2],[4,6]])
numpy_c = c.numpy()
torch_d = torch.from_numpy(d)
print('b = {} ; \nc = {} ; \nnumpy_c = {}; \n torch_d = {}'.format(b,c,numpy_c,torch_d))

#%% different types of tensor

e = torch.LongTensor([[1,2],[3,4],[5,6]]) #LongTensor,ShortTensor,IntTensor,FloatTensor,DoubleTensor
f = torch.Tensor([[1,2],[3,4]]) # FloatTensor
print('e = {};\n f = {}'.format(e,f))

#%% Variable

x = Variable(torch.Tensor([1]), requires_grad = True)
w = Variable(torch.Tensor([2]), requires_grad = True)
b = Variable(torch.Tensor([3]), requires_grad = True)

y = w * x + b

y.backward()
print(x.grad)
print(w.grad)
print(b.grad)

#%% matrix variable

x = torch.randn((3,3))
x = Variable(x, requires_grad = True)
b = Variable(torch.Tensor([0.35]), requires_grad = True)

y = 2 * x + b
print(y)
y.backward(torch.Tensor([1, 0.1, 0.01]))
print(x.grad)
print(b.grad)

#%% load dataset

from torch.utils.data import Dataset, Dataloader
import pandas as pd

class myDataset(Dataset):
    def __init__(self, csv_file, txt_file, root_dir, other_file):
        self.csv_data = pd.read_csv(csv_file)
        with open(txt_file, 'r') as f:
            data_list = f.readlines()
        self.txt_data = data_list
        self.root_dir = root_dir
        
    def __len__(self):
        return len(self.csv_data)
        
    def __getitem__(self, idx):
        data = (self.csv_data[idx], self.txt_data[idx])
        return data
        
dataiter = Dataloader(myDataset, batch_size = 32, shuffle = True)

#%% module
from torch import nn, from_numpy
from torch.autograd import Variable
class net(nn.Module):
    def __init__(self, other_args):
        super(net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size)
        # other network layers
        
    def forward(self, x):
        x = self.conv1(x)
        return x
    
w = np.random.randint(0,10,(3,3))
x = torch.randn((3,3))
x = Variable(x, requires_grad = True)
output = 3*x + Variable(torch.Tensor([10]), requires_grad = True)
torch_target = Variable(torch.LongTensor([0,0,0]), requires_grad = True)
criterion = nn.CrossEntropyLoss()
loss = criterion(output, torch_target)
print(loss)