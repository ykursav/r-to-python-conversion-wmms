import numpy as np
import pandas as pd

#' @title Data checking
#'
#' @description Checks the integrity of the inputed data before computing the
#' Euclidian Minimum Spanning Tree (EMST)
#'
#' @param x a \code{matrix} or \code{data.frame}.
#'
#' @details \code{data_check} is called from inside
#'     \code{\link[emstreeR]{ComputeMST}} before the computation begins. First,
#'     it evaluates the object format. Afterwards, it checks whether the
#'     inputed data has at least two columns and tries to coerce all columns
#'     into numeric, beyond removing all rows containing \code{NA} entries.
#'
#' @return a \code{matrix} containing the cleaned data after running the
#'     necessary checks.
#'
#' @keywords internal
#' @noRd


def data_check(x):
    # 1) matrix/data.frame verification

    try:
        if not isinstance(x, pd.DataFrame):
            x = pd.DataFrame(x)
    except Exception as e:
        print("Error: Not a matrix or data.frame.")
        print(e)
        return None

    # 2) multivariate data verification

    if len(x) < 2:
        print("Error: Your data should have more than 1 column.")
        return None

    # 3) numeric cols verification

    try:
        x = x.astype(np.float)
    except Exception as e:
        print("Error: Could not transform your data columns into numeric.")
        print(e)

    # 4) only NA'S in a column verification (e.g. when all entries of a column
    # .. have characters)
    na_count = x.isna().sum()
    if any(na_count == x.shape[0]):
        print(
            "Error after transforming your columns into numeric: one or more columns end up having only NA's as entries."
        )
        return None

    # 5) removing NA's verification
    if any(na_count) > 0:
        try:
            x = x.dropna()
        except Exception as e:
            print("Error: Could not remove your NA's entries.")
            print(e)

    return x
