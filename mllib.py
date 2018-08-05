# functions

from imports import *


def display_all(df):
    """displays wider view of a dataframe df"""
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        display(df)



