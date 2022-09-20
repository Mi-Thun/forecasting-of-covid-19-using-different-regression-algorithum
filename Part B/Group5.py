import math

def countDF(df):   # count dataframe
    dict = {}
    for i in df:
        c = 0
        for r in df[i]:
            b = isinstance(r, str)
            if b == True:
                c += 1
            else:
                if math.isnan(r):
                    continue
                else:
                    c += 1
        dict[i] = c
        # print(f'{i}        {c}')
    return dict


def count_2(List):   # count series
    c = 0
    for i in List:
        if math.isnan(i):
            continue
        else:
            c += 1
    return c


def describeDF(a):  # describe df
    dic = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            # print(i)
            # describe_2(list)
            dic[i] = describe_2(list)
    return dic


def describe_2(s):     # describe series
    des_dic = {"count": count_2(s), "mean": mean_2(s), "std": std_2(s),
               "min": min_2(s), "25%": quantile_2(s, .25),
               "50%": quantile_2(s, .50), "75%": quantile_2(s, .75), 
               "max": max_2(s)
               }
    return des_dic


def maxDF(df):  # max dataframe
    dic = {}
    for i in df:
        max = float('-inf')
        for r in df[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                if r > max:
                    max = r
        # print(f'{i}        {max}')
        dic[i] = max
    return dic


def max_2(s):    # max serirs
    max = float('-inf')
    for i in s:
        if i > max:
            max = i
    return max


def minDF(df):  # Min dataframe
    dic = {}
    for i in df:
        min = float('inf')
        for r in df[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            if r < min:
                min = r
        # print(f'{i}        {min}')
        dic[i] = min
    return dic

def min_2(s):    # min series
    min = float('inf')
    for i in s:
        if i < min:
            min = i
    return min


def argmax_2(s):  # index of max series
    c = 0
    max = max_2(s)
    for i in s:
        if i != max:
            c += 1
        else:
            return c


def argmin_2(s):  # index of mim series
    c = 0
    min = min_2(s)
    for i in s:
        if i != min:
            c += 1
        else:
            return c


def idxmax_2(list):  # index lebel at which maximum lies series
    max = max_2(list)
    indx = -1
    for i in list:
        indx += 1
        if i == max:
            return indx

    # or just write bellow 2 line of code
    # max = max_2(list)
    # return argmax_2(list)


def idxmin_2(List):  # index lebel at which minimum lies series
    min = List[0]
    indx = 0
    for i in range(len_2(List)):
        if List[i] < min:
            min = List[i]
            indx = i
    return indx


def quantile_2(a, x):   # quantile series
    b = isinstance(a, list)
    if b:
        a.sort()
    else:
        a = a.sort_values()
        a.reset_index(inplace=True, drop=True)
    total = len_2(a)
    quan = math.ceil(int(total*x))
    for i in range(len_2(a)):
        if i == quan:
            return a[i]


def quantileDF(df, x):   # quantile dataframe
    dic = {}
    for i in df:
        list = []
        for r in df[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        # print(f'{i}        {quantile_2(list, x)}')
        q = quantile_2(list, x)
        dic[i] = q
    return dic


def len_2(List):  # length
    n = 0
    for i in List:
        n += 1
    return n


def sum_2(a):  # sum
    s = 0
    for i in a:
        s += i
    return s


def sumDF(a):  # sum df
    dic = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            dic[i] = round(sum_2(list), 3)
    return dic


def meanDF(a):  # Mean DF
    dict = {}
    for i in a:
        sum = 0
        c = 0
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                sum += r
                c += 1
        if sum != 0:
            # print(f'{i}         {sum/c}')
            dict[i] = round(sum/c, 6)
    return dict


def mean_2(a):  # Mean
    sum = sum_2(a)
    n = len_2(a)
    return sum/n


def medianDF(a):  # median df
    dict = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            # print(f'{i}        {median_2(list)}')
            dict[i] = round(median_2(list), 3)
    return dict


def median_2(a):  # median series
    b = isinstance(a, list)
    if b:
        a.sort()
    else:
        a = a.sort_values()
        a.reset_index(inplace=True, drop=True)
    l = len_2(a)
    if l % 2 == 0:
        return (a[math.ceil((l/2)-1)]+a[math.ceil(l/2)])/2
    else:
        return a[l//2 + 1]


def madDF(a):  # MAD df
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            meam = mean_2(list)
            x = [round(abs(number-meam), 2) for number in list]
            print(f'{i}        {mean_2(x)}')


def mad_2(a):  # MAD series
    n = len_2(a)
    m = mean_2(a)
    x = 0
    for i in range(n):
        x += abs(a[i]-m)
    return x/n


def prodDF(a):  # prod df
    dict = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            j = 1
            for k in list:
                j *= k
            dict[i] = "{:e}".format(j)
            # print(f'{i}        {"{:e}".format(j)}')
    return dict


def prod_2(a):  # prod series
    p = 1
    for i in a:
        p *= i
    return "{:e}".format(p)


def var_2(list):  # var list
    mean = mean_2(list)
    deviations = [(x - mean) ** 2 for x in list]
    return sum(deviations) / (len(deviations)-1)


def varDF(a):  # var df
    dict = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            dict[i] = round(var_2(list), 6)
            # print(f'{i}            {round(var_2(list), 6)}')
    return dict


def std_2(a):  # std series
    return math.sqrt(var_2(a))


def stdDF(a):  # std df
    dict = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            dict[i] = round(std_2(list), 6)
            # print(f'{i}            {std_2(list)}')
    return dict


def skew_2(list):  # skew list
    m = mean_2(list)
    deviations = [(x - m)**3 for x in list]
    x = ((math.sqrt(((var_2(list)*(len(deviations)))/len(deviations))))**3)
    s = sum(deviations)
    return round(s / ((len(deviations)-1) * x), 6)


def skewDF(a):  # skew df
    dict = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            dict[i] = round(skew_2(list), 6)
            # print(f'{i}            {skew_2(list)}')
    return dict


def kurt_2(list):  # kurt list
    m = mean_2(list)
    deviations = [(x - m)**4 for x in list]
    x = ((math.sqrt(((var_2(list)*(len_2(deviations)))/len_2(deviations))))**4)
    return round(sum_2(deviations) / ((len(deviations)-1) * x), 6)


def kurtDF(a):  # kurt df
    dict = {}
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        if list:
            dict[i] = round(kurt_2(list), 6)
            # print(f'{i}            {kurt_2(list)}')
    return dict


def cumsum_2(s):   # cumsum
    cumS = 0
    list = []
    for i in s:
        cumS += i
        list.append(round(cumS, 2))
    return list


def cummin_2(s):     # cummin
    min = s[0]
    list = []
    for i in s:
        if i < min:
            min = i
        list.append(round(min, 2))
    return list


def cummax_2(s):   # cummax
    max = s[0]
    list = []
    for i in s:
        if i > max:
            max = i
        list.append(max)
    return list


def cumprod_2(s):  # cumprod
    cum = 1
    p = []
    for i in s:
        cum *= i
        p.append(cum)
    return p


def diff_2(s):  # diff
    diff = math.nan
    difference = []
    for i in s:
        diff = round((i-diff), 2)
        difference.append(diff)
        diff = i
    return difference


def pct_change_2(s):   # pct_change
    pct = math.nan
    percentage = []
    for i in s:
        pct = round((i/pct)-1, 6)
        percentage.append(pct)
        pct = i
    return percentage


def weighted_mean_2(List, weight):  # weighted_mean
    total = sum_2([(List[i]*weight[i]) for i in range(len_2(List))])
    return total/sum_2(weight)


def dispersion_2(List):   # dispersion
    return max_2(List)-min_2(List)


def range_2(List):   # Range
    return f'{max_2(List)} - {min_2(List)}'


def iqr(a):  # interquantile range
    return quantile_2(a, .75) - quantile_2(a, .25)


def z_score_2(List):   # zscore
    list = []
    for i in List:
        list.append(round((i-(mean_2(List)))/(std_2(List)), 4))
    return list


def standard_error_2(a):   # Standard Error
    return (std_2(a)/math.sqrt(len_2(a)))


def zscore_2(a, b):  # zscore
    z = (a-mean_2(b))/std_2(b)
    return z


def mode_2(List):  # mode
    max = 0
    for i in range(len_2(List)):
            frq = 0
            for j in range(len_2(List)):
                if List[i] == List[j]:
                    frq += 1
            if(frq >= max):
                max = frq
    return max


def median_absulate_devationDF(a):
    for i in a:
        list = []
        for r in a[i]:
            b = isinstance(r, str)
            if b == True:
                continue
            else:
                list.append(r)
        list.sort()
        if list:

            median_value = round(median_2(list), 2)
            x = [round(abs(number-median_value), 2) for number in list]
            x.sort()
            print(f'{i}        {median_2(x)}')
