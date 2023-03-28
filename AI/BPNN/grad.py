# import torch
# from torch.autograd import Variable
# import torch.nn as nn
# import torch.nn.functional as f
# import torch.optim as optim
# import matplotlib.pyplot as plt
#
# NUM = 100
# hide_num = 300
#
#
# class Net(nn.Module):
#     def __init__(self):
#         super(Net, self).__init__()
#
#         self.fc1 = nn.Linear(NUM, hide_num)
#         self.fc2 = nn.Linear(hide_num, NUM)
#
#     def forward(self, x):
#         x = f.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x
#
#
# net = Net()
# print(net)
# for param in net.parameters():
#     print(param.size())
# x = torch.randn(NUM)
# input = Variable(x)
#
# target = Variable(0.5 * x + 0.3)
#
# optimizer = optim.SGD(net.parameters(), lr=0.01)
# loss_list = []
# step = 500
# for epoch in range(step):
#     optimizer.zero_grad()  # 参数梯度清零，因为会叠加
#     out = net(input)
#     loss = nn.MSELoss()(out, target)
#     loss_list.append(loss)
#     loss.backward()
#     optimizer.step()
#
# print('loss 的层级--------->')
# t = loss.grad_fn
# while t:
#     print(t)
#     t = t.next_functions[0][0]
#
# print('target--->', target)
# out1 = net(input)
# print('out1------>', out1)
# print(nn.MSELoss()(out1, target))
#
# plt.figure(1)
# plt.plot(range(1, NUM + 1), target.detach().numpy().tolist(), '*', ms=10, lw=1, color='black')  # question:detach()
# plt.plot(range(1, NUM + 1), out1.detach().numpy().tolist(), 'o', ms=3, lw=1, color='red')
# plt.show()
# plt.figure(2)
# plt.plot(range(1, step + 1), loss_list, 'o-', ms=3, lw=1, color='black')
# plt.show()