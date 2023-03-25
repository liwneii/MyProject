# import numpy as np
# import torch
# from torch.autograd import Variable
# import torch.nn as nn
# import torch.nn.functional as f
# import torch.optim as optim
# import matplotlib.pyplot as plt
#
#
#
# def create_2n_csv():
#     a = np.random.random((100,2))
#     np.savetxt('GradDes.csv',a,delimiter = ',', fmt='%10.5f')
#
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
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#
#     net = Net()
#     print(net)
#     for param in net.parameters():
#         print(param.size())
#     x = torch.randn(NUM)
#     input = Variable(x)
#
#     target = Variable(0.5 * x + 0.3)
#
#     optimizer = optim.SGD(net.parameters(), lr=0.01)
#     loss_list = []
#     step = 500
#     for epoch in range(step):
#         optimizer.zero_grad()  # 参数梯度清零，因为会叠加
#         out = net(input)
#         loss = nn.MSELoss()(out, target)
#         loss_list.append(loss)
#         loss.backward()
#         optimizer.step()
#
#     print('loss 的层级--------->')
#     t = loss.grad_fn
#     while t:
#         print(t)
#         t = t.next_functions[0][0]
#
#     print('target--->', target)
#     out1 = net(input)
#     print('out1------>', out1)
#     print(nn.MSELoss()(out1, target))
#
#     plt.figure(1)
#     plt.plot(range(1, NUM + 1), target.detach().numpy().tolist(), '*', ms=10, lw=1, color='black')  # question:detach()
#     plt.plot(range(1, NUM + 1), out1.detach().numpy().tolist(), 'o', ms=3, lw=1, color='red')
#     plt.show()
#     plt.figure(2)
#     plt.plot(range(1, step + 1), loss_list, 'o-', ms=3, lw=1, color='black')
#     plt.show()
#     # create_2n_csv()
#     # points = np.genfromtxt('GradDes.csv',delimiter=",")
#     # learning_rate = 0.0001
#     #
#     # help(np.savetxt)
#
#
#
#
#     # print(sklearn.__version__)
#     # % matplotlib inline  # 用于确保展示图形
#     # plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示乱码问题
#     # plt.rcParams['axes.unicode_minus'] = False  # 解决符号显示乱码问题
#     #
#     # series_1 = pd.Series([2.8, 3.01, 8.99, 8.59, 5.18])
#     # print(series_1, type(series_1))
#
#     # 图形显示及相关参数
#     # x = np.linspace(0, 100, 1000)
#     # y = np.sin(x)
#     # plt.plot(x, y, c='red', lw=2, ls='-', marker='o', markersize=1, markeredgecolor='blue', markerfacecolor='black',
#     #          label='x和y')
#     # plt.legend(loc='center')
#     # plt.show()
#     #
#     # df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
#     #                    "date": pd.date_range('20130102', periods=6),
#     #                    "city": ['Beijin g ', 'SH', ' guang zhou ', 'Shen zhen', 'shang hai', 'BEI JING '],
#     #                    "age": [23, 44, 54, 32, 34, 32],
#     #                    "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
#     #                    "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
#     #                   columns=['id', 'date', 'city', 'category', 'age', 'price'])
#     #
#     #
#     #
#     # print_hi('PyCharm')
#     # print('使用列表生成一维数组')
#     # data = [1, 2, 3, 4, 5, 6]
#     # x = np.array(data)
#     # print(x)  # 打印数组
#     # print(x.dtype)  # 打印数组元素的类型
#     # print(tf.__version__)
#     #
#     # print(torch.__version__)
#     #
#     # tf.compat.v1.disable_eager_execution()
#     # hello = tf.constant('hello,tensorflow')
#     # sess = tf.compat.v1.Session()
#     # print(sess.run(hello))
#     # x = torch.rand(5, 3)
#     # print(x)
#
#
#
#
