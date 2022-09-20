def count_2(x):      # Length
    count = 0
    for i in x:
        count += 1
    return count


def sum_2(x):      # Sum
    sum = 0
    for i in x:
        sum += i
    return sum


def mean_2(x):   # Mean
    return sum_2(x)/count_2(x)


def r_squared_2(y, ypred):  # R-squared
    residual = []
    sum = []
    for i, j in zip(y, ypred):
        residual.append((i-j)**2)
    rss = sum_2(residual)
    for i in y:
        sum.append((i-mean_2(y))**2)
    tss = sum_2(sum)
    return 1-(rss/tss)


def mse_2(y, ypred):   # MSE(Mean Squared Error)
    error = []
    for i, j in zip(y, ypred):
        error.append((i-j)**2)
    return (1/count_2(y))*sum_2(error)


def abs_2(a):  # Absolute
    return ((a*a)**0.5)


def mae_2(y, ypred):   # MAE(Mean Absolute Error)
    error = list()
    for i, j in zip(y, ypred):
        error.append(abs_2(i-j))
    return (1/count_2(y))*sum_2(error)


def cov_2(x, y):
    m = mean_2(x)
    list = []
    for i, j in zip(x, y):
        list.append((i-m)*(j-m))
    return sum_2(list)/(count_2(x)-1)


def var_2(x):
    m = mean_2(x)
    list = []
    for i in x:
        list.append((i-m)**2)
    return sum_2(list)/(count_2(x)-1)


def a_value_2(x, y):
    return mean_2(y)-(b_value_2(x, y)*mean_2(x))


def b_value_2(x, y):
    return cov_2(x, y)/var_2(x)
