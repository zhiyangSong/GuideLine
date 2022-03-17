import numpy as np
import os, sys
import random
import torch
import time
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter
from net import BCNet


class BCAgent():
    def __init__(self, input_size, output_size, args):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = args.lr
        self.batch_size = args.batch_size
        self.args = args
        
        self.features, self.labels = self.getData()
        
        self.net = BCNet(self.input_size, self.output_size, args)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=self.learning_rate)
        self.loss_function = nn.MSELoss()

        
        time_now = time.strftime('%y%m_%d%H%M')
        self.save_dir = "{}/{}".format(args.save_dir, time_now)
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
        self.log_dir = "./{}/{}".format(args.log_dir,time_now)
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)


    
    def getData(self):
        features = np.load("./data/fectures.npy")
        labels = np.load("./data/labels.npy")
        return features, labels


    def data_iter(self, batch_size, features, labels):
        num_examples = len(features)
        indices = list(range(num_examples))
        random.shuffle(indices)  # 样本的读取顺序是随机的
        for i in range(0, num_examples, batch_size):
            j = torch.LongTensor(indices[i: min(i + batch_size, num_examples)]) # 最后一次可能不足一个batch
            yield  features.index_select(0, j), labels.index_select(0, j)

    def train(self):
        writer = SummaryWriter(self.log_dir)
        # https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
        for epoch in range(self.args.episodes_num):
            # for X, y in self.data_iter(self.batch_size, self.features, self.labels): 
            for X, y in zip(self.features, self.labels):
                X = torch.FloatTensor(X).view(1, -1)
                y = torch.FloatTensor(y).view(1, -1)
                pred = self.net(X)
                loss = self.loss_function(pred, y)
                writer.add_scalar("loss:", loss, epoch)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
            
            if epoch%self.args.save_interval == 0:
                self.save(epoch)
            print(f"epoch: {epoch:<4} loss: {loss:>7f}")


    def save(self, episodes):
        dir = '{}/episodes_{}.pth'.format(self.save_dir,episodes)
        torch.save(self.net.state_dict(), dir)
        
    def load(self, path):
        self.net.load_state_dict(torch.load(path))
        print('load network successed')


