"""
file: preproc.py
author: Paul Soma
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def train_test(df):
    """
    split into train and test set
        train contains Jan 1, 2018 through July 31, 2018
        test contains August 1, 2018 through September 28, 2018
    :param df:
    :return:
    """
    df = df[df['Date'] >= '2018-01-01']

    train = df[df['Date'] < '2018-08-01']

    test = df[df['Date'] >= '2018-08-01']
    test = test[test['Date'] < '2018-09-28']

    return [train, test]


def scale(train,test):
    """
    apply minmax scaling to training and testing sets separately
    only use for
    :param train: training dataframe
    :param test: test dataframe
    :return:
    """
    cols = train.columns

    scaler = MinMaxScaler()
    train_s = scaler.fit_transform(train)
    test_s = scaler.transform(test)

    train_df = pd.DataFrame(train_s,columns=cols, index=train.index)
    test_df = pd.DataFrame(test_s, columns=cols, index=test.index)


    return [scaler,train_df,test_df]


def shifted_price_col(df, colname, dt):
    """
    function to compute daily change in price and add to the dataframe
        change = (price on day t) - (price on day t+1)
        used as the target variable
    :param df: pd.DataFrame of stocks. should at least include a closing price
        columnn named 'Close'
    :param colname: the new column name
    :param dt: change in time. number of days to shift price for the
        new column.
        If dt=1, new column contains the next day's closing price (t+1),
            only used for the target
        If dt=-1, new column contains the previous day's closing price (t-1)
    :return:
    """
    new_col = df.Close.shift(dt)

    df[colname] = new_col

    return df



def class_target_col(df, colname):
    """
    function to add a target feature with value +1 if the DJI goes up on day
        t+1, and with value -1 if the DJI goes down on day t+1
    :param df:
    :param colname:
    :return:
    """

    pass

def shifted_pct_returns_col(df, colname, dt):
    """

    :param df:
    :param colname:
    :param dt:
    :return:
    """

    pass

if __name__ == '__main__':
    df = pd.DataFrame([[1,2],[3,4],[5,6]],columns=['Close','Open'])
    print(df)

    print(shifted_price_col(df,'a',-1))
