import random
import numpy as np
import math

def output_generate(n_sample):  # this function is to generate random values for y and y_pred
    y_target = np.array([random.uniform(0, 10) for _ in range(n_sample)])
    y_predict = np.array([random.uniform(0, 10) for _ in range(n_sample)])
    return y_target, y_predict


def loss_calcultion(loss_type, y_target, y_predict):    # compute the loss, based on loss type (case by case)
    if (loss_type == 'MAE' or loss_type == 'mae'):
        loss = np.abs(y_predict - y_target)
        total_loss = np.mean(loss)
    elif(loss_type == 'MSE' or loss_type == 'mse'):
        loss = [(p - t)**2 for p, t in zip(y_target, y_predict)]
        total_loss = sum(loss)/len(loss)
    elif (loss_type == 'RMSE' or loss_type == 'rmse'):
        loss = [(p - t)**2 for p, t in zip(y_target, y_predict)]
        total_loss = math.sqrt(sum(loss)/len(loss))
    return loss, total_loss


def n_sample_and_Loss_input():
    n_sample = input("Enter number of samples: ")
    if n_sample.isnumeric():  # check if number of sample is numeric, if not end the program
        y_target, y_predict = output_generate(
            int(n_sample))  # generate random values of target and predicted output value
        loss_type = input("Enter the loss type (MAE/MSE/RMSE): ")
        loss, total_loss = loss_calcultion(loss_type, y_target, y_predict)

        for i in range(int(n_sample)):  # print the result
            print(f"loss name: {loss_type}, sample: {i}, pred: {y_predict[i]}, target: {y_target[i]}, loss: {loss[i]}")
        print("Total loss:", total_loss)
    else:
        print("Number of samples must be an integer number")  # notify user of invalid entered value of
        # n_sample and end program


if __name__ == '__main__':
    n_sample_and_Loss_input()