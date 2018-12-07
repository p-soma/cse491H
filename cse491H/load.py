"""
file: load.py
author: Paul Soma
description: Functions for loading the data
"""

import os
from definitions import ROOT_DIR
import pandas as pd
from ta import *


def load_basic():
    """

    :return: df of date, open, hi, low, close, adj close, volume
    """

    fpath = os.path.join(ROOT_DIR, 'data', 'dji.csv')
    df = pd.read_csv(fpath)

    df = df.drop('Adj Close', axis=1)
    df['Date'] = pd.to_datetime(df['Date'])

    return df

def load_all_features():

    df = load_basic()

    df = add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume",
                             fillna=True)

    return df




