import torch
from torch import nn
import torch
from torchsummary import summary

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class LeNet5(nn.Module):
    def __init__(self, n_classes):
        super(LeNet5, self).__init__()
        self.Conv_1 = nn.Conv2d(
            in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=0)
        self.Sigmoid_1 = nn.Sigmoid()
        self.pooling_1 = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)
        self.Conv_2 = nn.Conv2d(
            in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0)
        self.Sigmoid_2 = nn.Sigmoid()
        self.pooling_2 = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)
        self.Fc_1 = nn.Linear(16*5*5, 120)
        self.Sigmoid_3 = nn.Sigmoid()
        self.Fc_2 = nn.Linear(120, 84)
        self.Sigmoid_4 = nn.Sigmoid()
        self.Fc_3 = nn.Linear(84, n_classes)

    def forward(self, x):
        x = self.Conv_1(x)
        x = self.Sigmoid_1(x)
        x = self.pooling_1(x)
        x = self.Conv_2(x)
        x = self.Sigmoid_2(x)
        x = self.pooling_2(x)
        x = x.view(x.size(0), -1)
        x = self.Fc_1(x)
        x = self.Sigmoid_3(x)
        x = self.Fc_2(x)
        x = self.Sigmoid_4(x)
        x = self.Fc_3(x)
        return x


if __name__ == '__main__':
    model = LeNet5(10).to(device)
    print(model)
    summary(model, input_size=(1, 32, 32))
    x = model(torch.randn((2, 1, 32, 32)).to(device))
    print(x)
