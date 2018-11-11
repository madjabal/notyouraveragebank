import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


def find_still_cash(dataframe, give=False):
    stddev = dataframe['Balance'].std()
    min = dataframe['Balance'].min()
    still_cash = round(min - stddev, 2)

    if not give:
        print("Cash safe to be invested over the past 2 months: " + str(still_cash))
        print("This could have yielded: " + str(still_cash * (1.01)**2))
        print("Or an extra " + str(still_cash * (1.01)**2 - still_cash))
    else:
        return still_cash


def plot(dataframe):
    sns.lineplot(x=dataframe['Date'], y=dataframe['Balance'])
    plt.show()


def check_savings(dataframe, give=False):
    x = list(range(len(dataframe['Balance'])))
    y = np.array(dataframe['Balance'])
    x = sm.add_constant(x)
    mod = sm.OLS(y, x)
    res = mod.fit()
    r2 = round(res.rsquared, 3)

    returnstring = ''

    b1 = .4
    b2 = .2
    b3 = .1

    if r2 > b1:
        returnstring = "Extra income is high, consider a monthly deposit to investments or savings, score from " \
                       "-1 to 1: " + str(r2)
    elif b1 >= r2 >= b2:
        returnstring = "Savings are strong, consider a monthly deposit to investments or savings, score from " \
                       "-1 to 1: " + str(r2)
    elif b2 > r2 >= b3:
        returnstring = "Fair strength savings, consider monthly contribution to investments, score from " \
                       "-1 to 1: " + str(r2)
    elif b3 > r2 >= 0:
        returnstring = "Savings are fair, if you don't have a savings account, consider re-budgeting, score from " \
                       "-1 to 1: " + str(r2)
    elif 0 > r2 >= -b3:
        returnstring = "Savings are somewhat weak, if you don't have a savings account, consider re-budgeting, " \
                       "score from -1 to 1: " + str(r2)
    elif -b3 > r2 >= -b2:
        returnstring = "Savings are fairly weak, consider re-budgeting, score from " \
                       "-1 to 1: " + str(r2)
    elif -b2 > r2 >= -b1:
        returnstring = "Weak savings, strongly consider re-budgeting, score from " \
                       "-1 to 1: " + str(r2)
    else:
        returnstring = "Account in need of severe re-budgeting, score from  " \
                       "-1 to 1: " + str(r2)
    if not give:
        print(returnstring)
    else:
        return r2, returnstring


# def stability(dataframe, give=False):

account_history = pd.read_csv('account_history.csv')

# print(account_history.describe())

# print(check_savings(account_history))

# print(account_history)

# print(find_still_cash(account_history))

print("Use pd.read_csv() to enter account history")
print("Methods: find_still_cash(), plot(), check_savings()")
