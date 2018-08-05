# functions

from .imports import *


def display_all(df):
    """displays wider view of a pandas data frame df"""
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        display(df)


def make_submission(df_columns, labels):
    """Takes two the same length lists of columns and labels.
        Creates a data frame with colums: df_columns
        and labels: labels, in order of labels list,
        return the pd.DataFrame created. Used to create a
        submission frame"""
    data = {key:val for (key, val) in zip(labels, df_columns)}
    return pd.DataFrame(data, columns=labels)

def get_sample(df, size):
    """returns sample of size size from  dataframe df"""
    return df[:size].copy()




