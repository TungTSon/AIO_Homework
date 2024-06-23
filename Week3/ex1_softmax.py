import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x))


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        return exp_x / torch.sum(exp_x)


if __name__ == "__main__":
    # Examples
    data = torch.Tensor([1, 2, 3])

    # Using Softmax
    softmax = Softmax()
    output = softmax.forward(data)
    print(">>", output)  # print out the result

    # Using SoftmaxStable
    softmax_stable = SoftmaxStable()
    output_stable = softmax_stable.forward(data)
    print(">>", output_stable)  # print out the result

    # this part is for Multiple Choice questions ---------------------
    data2 = torch.Tensor([5, 2, 4])
    data3 = torch.Tensor([1, 2, 300000000])
    # Using Softmax
    softmax2 = Softmax()
    output2 = softmax2.forward(data2)
    print(">>", output2)  # print out the result
    softmax3 = Softmax()
    output3 = softmax3.forward(data2)
    print(">>", output3)  # print out the result
