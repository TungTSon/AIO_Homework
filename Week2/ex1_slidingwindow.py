import numpy as np
import random


def list_generate(n_sample):
    return [random.randint(-100, 100) for _ in range(n_sample)]


def max_in_window_list(input_list, k):
    output_list = []
    for i in range(len(input_list) - k + 1):
        sliding_window_list = input_list[i: i + k]
        output_list.append(np.max(sliding_window_list))
    return output_list


def prompt_user_input():
    k = input("Enter the size of sliding window list, k = ")
    if not k.isnumeric() or int(k) < 1:
        print("k must be a positive integer")
        exit()
    return int(k)


if __name__ == "__main__":
    input_list = list_generate(10)
    k = prompt_user_input()
    print(">> input num_list =", input_list)
    print(">> Output:", max_in_window_list(input_list, k))
