"""
file: ann_regression_model.py
author: Paul Soma
"""
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from ta import *
import cse491H.load as load
import cse491H.preproc as preproc



def model_1(input_shape):
    model = keras.Sequential([
        keras.layers.Dense(64, activation=tf.nn.relu,
                           input_shape=(input_shape,)),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(64, activation=tf.nn.relu),
        keras.layers.Dense(1)
    ])

    optimizer = tf.train.AdamOptimizer(0.001)

    model.compile(loss='mae',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])
    return model


def model_2(input_shape):
    model = keras.Sequential([
        keras.layers.Dense(128, activation=tf.nn.relu,
                           input_shape=(input_shape,)),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(64, activation=tf.nn.relu),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(32, activation=tf.nn.relu),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(8, activation=tf.nn.relu),
        keras.layers.Dense(1)
    ])

    optimizer = tf.train.AdamOptimizer(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mse', 'mae'])
    return model



if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    df = load.load_basic()
    df = preproc.add_shifted_price_col(df,'NextDay',-1)

    print(df.head())
    train, test = preproc.train_test(df)

    train, test = preproc.scale(train, test)

    num_epochs = 1000

#    model = construct_model()
#    history = fit_model(model)



