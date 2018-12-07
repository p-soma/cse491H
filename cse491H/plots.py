import matplotlib.pyplot as plt
import numpy as np


def plot_history(history, metric, figname=None):
    plt.figure()

    train_mae = np.array(history.history[metric])
    val_mae = np.array(history.history['val_' + metric])

    train_label = 'Training '
    val_label = 'Validation '

    plt.plot(history.epoch, train_mae,
             label=train_label)
    plt.plot(history.epoch, val_mae,
             label=val_label)

    ymin = np.min([np.min(train_mae), np.min(val_mae), 0])
    ymax = np.max([np.max(train_mae), np.max(val_mae)])

    plt.ylim([ymin, ymax])

    plt.title(metric)
    plt.xlabel('Epoch')
    plt.ylabel(metric)

    plt.legend()

    if figname is not None:
        plt.savefig(figname)


def plot_prediction(actual, predicted, figname=None):
    """

    :param actual: actual next day closing price in USD
    :param predicted: predicted next day closing price in USd
    :return:
    """
    plt.figure()

    plt.title('')

    xvals = range(actual.shape[0])

    plt.plot(xvals, actual,
             label='Actual')
    plt.plot(xvals, predicted,
             label='Predicted')

    ymin = np.min([np.min(actual), np.min(predicted)]) - 500
    ymax = np.max([np.max(actual), np.max(predicted)]) + 500

    plt.ylim([ymin, ymax])

    plt.title('Closing Price')
    plt.xlabel('t')
    plt.ylabel('$USD')

    plt.legend()

    if figname is not None:
        plt.savefig(figname)
