def md_nre_single_sample (y=0, y_hat=0, n=2, p=1):
    y, y_hat, n, p = float(y), float(y_hat), int(n), int(p)   # casting all inputs from string to numbers
    return print(">>",(y**(1/n) - y_hat**(1/n))**p)

if __name__ == '__main__':
    y = input("Enter y = ")
    y_hat = input("Enter y_hat = ")
    n = input("Enter n_th order root = ")
    p = input("Enter order of the loss, p = ")
    md_nre_single_sample(y=y, y_hat=y_hat, n=n, p=p)    # show result
