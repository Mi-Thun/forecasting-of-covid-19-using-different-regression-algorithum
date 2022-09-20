# %%  Import necessary module
import numpy as np
import Own_Regression_module as m_
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns

# %%  Data Pre Processing
covid_dataset = pd.read_excel('covid_dataset.xlsx')
covid_dataset['Day'] = pd.to_datetime(covid_dataset['Day'])
covid_dataset.set_index('Day', inplace=True)

covid_first_dose = pd.read_excel('covid_first_dose.xlsx')
covid_first_dose['Day'] = pd.to_datetime(covid_first_dose['Day'])
covid_first_dose.set_index('Day', inplace=True)

covid_second_dose = pd.read_excel('covid_second_dose.xlsx')
covid_second_dose['Day'] = pd.to_datetime(covid_second_dose['Day'])
covid_second_dose.set_index('Day', inplace=True)

df = pd.concat([covid_dataset, covid_first_dose, covid_second_dose],
               axis=1, ignore_index=True)
df.rename(columns={0: "Lab Test", 1: "Confirmed Case",
                   2: "Death Case", 3: "First Dose", 4: "Second Dose"}, inplace=True)


# %%
df['bias'] = 1
print(df.head(5))

# %%
df.isnull().sum()
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)


# %%
corr = df.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(corr, square=True, fmt='.2f',
            annot=True, cmap='Reds')

# %%
a, b = 0, 0
for i in range(df.shape[0]):
    a += df.iloc[i, 3]
    df.iloc[i, 3] = a
    b += df.iloc[i, 4]
    df.iloc[i, 4] = b


# %%
corr = df.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(corr, square=True, fmt='.2f',
            annot=True, cmap='Reds')

# %%
# Death Case
x_death = df.drop(columns=['Death Case', 'First Dose', 'Second Dose'])
y_death = df[['Death Case']]

x_death['L2'] = (df['Lab Test']*df['Lab Test'])
x_death['C2'] = (df['Confirmed Case']*df['Confirmed Case'])

# %%
X_train, X_test, Y_train, Y_test = train_test_split(
    x_death, y_death, test_size=0.20, random_state=0)

# %%
x = np.array(X_train)
y = np.array(Y_train)

# %%
w = m_.weight_2(x, y)
y_pred = m_.dot_2(x, w)

# %%


def evalutation(y, y_pred):
    print('MAE value:       ', m_.mae_2(y, y_pred))
    print('MSE value:       ', m_.mse_2(y, y_pred))
    print('R-squared value: ', m_.r_squared_2(y, y_pred))


# %%
print("Train set result evalutation matrix")
evalutation(y, y_pred)

# %% test data set
x = np.array(X_test)
y = np.array(Y_test)

# %%
y_pred = m_.dot_2(x, w)

# %%
print("Test set result evalutation matrix")
evalutation(y, y_pred)

# %%
# Confirm Case
x_confirmed = df.drop(columns=['Confirmed Case', 'Death Case'])
y_confirmed = df[['Confirmed Case']]

x_confirmed['L2'] = (df['Lab Test']*df['Lab Test'])
x_confirmed['F2'] = (df['First Dose']*df['First Dose'])
x_confirmed['S2'] = (df['Second Dose']*df['Second Dose'])

# %%
X_train, X_test, Y_train, Y_test = train_test_split(
    x_confirmed, y_confirmed, test_size=0.20, random_state=0)

# %%
x = np.array(X_train)
y = np.array(Y_train)

# %%
w = m_.weight_2(x, y)
y_pred = m_.dot_2(x, w)

# %%
print("Train set result evalutation matrix")
evalutation(y, y_pred)

# %% test data set
x = np.array(X_test)
y = np.array(Y_test)

# %%
y_pred = m_.dot_2(x, w)

# %%
print("Test set result evalutation matrix")
evalutation(y, y_pred)
