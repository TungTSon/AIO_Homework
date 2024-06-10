import math
# Given function
def is_number(n):
    try:
        float(n)   # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def ex2_ActivationFunction():
    x = input("Input x = ")
    if is_number(x):
        actfunc = input("Input activation Function (sigmoid | relu |elu): ")
        print(activation_function(actfunc, float(x)))
    else:
        print("x must be number")


def activation_function(actfunc, x):
    if actfunc == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif actfunc == 'relu':
        return max(0, x)
    elif actfunc == 'elu':
        alpha = .01
        return x if x > 0 else alpha * (math.exp(x) - 1)
    else:
        return f"{actfunc} is not supported"


if __name__ == "__main__":
    ex2_ActivationFunction()