# %%  Import necessary module
import numpy as np
import Own_Regression_module as m_
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# %%  Data Processing
df = pd.read_csv('SimpleLinearRegression.csv')
df.head()

# %%
print(df.isnull().sum())
df.drop_duplicates(inplace=True)

# %%
X_year = df['YearsExperience']
Y_salary = df['Salary']

# %%
X_train, X_test, Y_train, Y_test = train_test_split(
    X_year, Y_salary, test_size=0.20, random_state=0)

# %%
x = np.array(X_train)
y = np.array(Y_train)

# %%
a = m_.a_value_2(x, y)  # 26780.099150628186
b = m_.b_value_2(x, y)  # 9312.575126729187

# %%  Train Set
y_pred = []
for i in range(len(x)):
    y_pred.append(a + (b*x[i]))

# %%
print("Test set result evalutation matrix")
print('MAE value:       ', m_.mae_2(y, y_pred))
print('MSE value:       ', m_.mse_2(y, y_pred))
print('R-squared value: ', m_.r_squared_2(y, y_pred))

# %% Test Set
x1 = np.array(X_test)
y1 = np.array(Y_test)

# %%
y_pred1 = []
for i in range(len(x1)):
    y_pred1.append(a + (b*x1[i]))

# %%
print("Train set result evalutation matrix")
print('MAE value:       ', m_.mae_2(y1, y_pred1))
print('MSE value:       ', m_.mse_2(y1, y_pred1))
print('R-squared value: ', m_.r_squared_2(y1, y_pred1))


# %%
plt.figure()
plt.xlabel('Year')
plt.ylabel('Salary')
plt.scatter(X_year, Y_salary)
plt.plot(x1, y_pred1, color="black")

# %%
