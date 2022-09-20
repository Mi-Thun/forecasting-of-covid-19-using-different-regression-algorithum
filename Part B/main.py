# %%
import numpy as np
import pandas as pd
import Group5 as B_

df = pd.read_csv('cars.csv')

df.columns = ['car', 'mpg', 'cly', 'disp', 'hp',
              'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

series1 = df['mpg']
series2 = df['cly']

# %%
# Count
# Send hole dataFrame
print("Panda Output:", df.count())
print("Module Output:", B_.countDF(df))
# Send a series
print("Panda Output:", series1.count())
print("Module Output:", B_.count_2(series1))

# %%
# Describe
# Send hole dataFrame
print("Panda Output:", df.describe())
print("Module Output:", B_.describeDF(df))
# Send a series
print("Panda Output:", series1.describe())
print("Module Output:", B_.describe_2(series1))

# %%
# Max
# Send hole dataFrame
print("Panda Output:", df.max())
print("Module Output:", B_.maxDF(df))
# Send a series
print("Panda Output:", series1.max())
print("Module Output:", B_.max_2(series1))

# %%
# min
# Send hole dataFrame
print("Panda Output:", df.min())
print("Module Output:", B_.minDF(df))
# Send a series
print("Panda Output:", series1.min())
print("Module Output:", B_.min_2(series1))

# %%
# argmax
# Send a series
print("Panda Output:", series1.argmax())
print("Module Output:", B_.argmax_2(series1))

# %%
# argmin
# Send a series
print("Panda Output:", series1.argmin())
print("Module Output:", B_.argmin_2(series1))

# %%
# idxmax
# Send a series
print("Panda Output:", series1.idxmax())
print("Module Output:", B_.idxmax_2(series1))

# %%
# idxmin
# Send a series
print("Panda Output:", series1.idxmin())
print("Module Output:", B_.idxmin_2(series1))

# %%
# quantile
# Send a series
print("Panda Output:", series1.quantile(0.2))
print("Module Output:", B_.quantile_2(series1, 0.2))
# Send hole dataFrame
print("Panda Output:", df.quantile(0.2))
print("Module Output:", B_.quantileDF(df, .2))


# %%
# sum
# Send a series
print("Panda Output:", series1.sum())
print("Module Output:", B_.sum_2(series1))
# Send hole dataFrame
print("Panda Output:", df.sum())
print("Module Output:", B_.sumDF(df))

# %%
# mean
# Send a series
print("Panda Output:", series1.mean())
print("Module Output:", B_.mean_2(series1))
# Send hole dataFrame
print("Panda Output:", df.mean())
print("Module Output:", B_.meanDF(df))

# %%
# median
# Send a series
print("Panda Output:", series1.median())
print("Module Output:", B_.median_2(series1))
# Send hole dataFrame
print("Panda Output:", df.median())
print("Module Output:", B_.medianDF(df))

# %%
# mad
# Send a series
print("Panda Output:", series2.mad())
print("Module Output:", B_.mad_2(series2))
# Send hole dataFrame
print("Panda Output:", df.mad())
print("Module Output:", B_.madDF(df))

# %%
# prod
# Send a series
print("Panda Output:", series1.prod())
print("Module Output:", B_.prod_2(series1))
# Send hole dataFrame
print("Panda Output:", df.prod())
print("Module Output:", B_.prodDF(df))


# %%
# var
# Send a series
print("Panda Output:", series1.var())
print("Module Output:", B_.var_2(series1))
# Send hole dataFrame
print("Panda Output:", df.var())
print("Module Output:", B_.varDF(df))

# %%
# std
# Send a series
print("Panda Output:", series1.std())
print("Module Output:", B_.std_2(series1))
# Send hole dataFrame
print("Panda Output:", df.std())
print("Module Output:", B_.stdDF(df))

# %%
# skew
# Send a series
print("Panda Output:", series1.skew())
print("Module Output:", B_.skew_2(series1))
# Send hole dataFrame
print("Panda Output:", df.skew())
print("Module Output:", B_.skewDF(df))

# %%
# kurt
# Send a series
print("Panda Output:", series1.kurt())
print("Module Output:", B_.kurt_2(series1))
# Send hole dataFrame
print("Panda Output:", df.kurt())
print("Module Output:", B_.kurtDF(df))

# %%
# cumsum
# Send a series
print("Panda Output:", series1.cumsum())
print("Module Output:", B_.cumsum_2(series1))

# %%
# cummin
# Send a series
print("Panda Output:", series1.cummin())
print("Module Output:", B_.cummin_2(series1))

# %%
# cummax
# Send a series
print("Panda Output:", series1.cummax())
print("Module Output:", B_.cummax_2(series1))

# %%
# cumprod
# Send a series
print("Panda Output:", series1.cumprod())
print("Module Output:", B_.cumprod_2(series1))

# %%
# diff
# Send a series
print("Panda Output:", series1.diff())
print("Module Output:", B_.diff_2(series1))

# %%
# pct_changes
# Send a series
print("Panda Output:", series1.pct_change())
print("Module Output:", B_.pct_change_2(series1))

# %%
# weighted_mean
wt = np.random.randint(1, 5, len(series1)+1)
print('Module Output: ', B_.weighted_mean_2(series1, wt))

# %%
# dispersion
print('Module Output: ', B_.dispersion_2(series1))

# %%
# inter quantile range
print("Module Output:", B_.iqr(series1))

# %%
# z score
print('Module Output: ', B_.z_score_2(series1))

# %%
# range
print('Module Output: ', B_.range_2(series1))

# %%
# standard_error
print("Module Output:", B_.standard_error_2(series1))
# %%
# median_absulate_devation
print('Module Output: ', B_.median_absulate_devationDF(df))

# %%
