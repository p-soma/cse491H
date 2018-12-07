import tensorflow as tf
from tensorflow import keras
import pandas as pd
from ta import *
import cse491H.load as load
import cse491H.preproc as preproc
import cse491H.ann_regression_model as regression


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    # load model
    df = load.load_basic()

    # add features
    df = preproc.add_daily_change(df)

    train, test = preproc.train_test(df)

    train, test = preproc.scale(train, test)

    num_epochs = 1000

    model = regression.construct_model()
    history = regression.fit_model(model)
