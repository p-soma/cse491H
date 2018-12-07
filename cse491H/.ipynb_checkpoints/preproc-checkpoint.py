"""
file: preproc.py
author: Paul Soma
"""


def train_test(df):
    """
    split into train and test set
        train contains Jan 1, 2018 through July 31, 2018
        test contains August 1, 2018 through
    :param df:
    :return:
    """
    df = df[df['Date'] >= '2018-01-01']

    train = df[df['Date'] < '2018-08-01']

    test = df[df['Date'] >= '2018-08-01']
    test = test[test['Date'] < '2018-09-28']

    return [train, test]

def feat_target(df):
    """
    split into features and target
    :param df:
    :return:
    """
    X = df.drop('Change', axis=1)
    y = df.Change

    return [X,y]


def normalize(train,test):
    """
    normalize each column individually based on mean and std deviation of
    training data
    :param train: training dataframe
    :param test: test dataframe
    :return:
    """

    mean = train.mean(axis=0)
    std = train.std(axis=0)

    train = (train - mean) / std
    test = (train - mean) / std

    return [train,test]


def add_daily_change(df):
    """
    function to compute daily change in price and add to the dataframe
        change = (price on day t) - (price on day t+1)
        used as the target variable
    :return:
    """
    Change = df.Close - df.Close.shift(1)
    Change = Change.shift(-1)

    df['Change'] = Change

    return df


