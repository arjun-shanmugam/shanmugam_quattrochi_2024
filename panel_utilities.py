import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from constants import Variables, Analysis
from typing import List, Union


def get_value_variable_names(df, analysis: str):
    value_columns = pd.Series([f'{month}_{analysis}' for month in Analysis.months], index=range(1, len(Analysis.months) + 1))
    int_to_period_dictionary = value_columns.str.replace(f"_{analysis}", "", regex=False).to_dict()
    period_to_int_dictionary = {v: k for k, v in list(int_to_period_dictionary.items())}
    return value_columns.tolist(), period_to_int_dictionary, int_to_period_dictionary


def prepare_df_for_DiD(df: pd.DataFrame, analysis: str, treatment_date_variable: str,
                       pre_treatment_covariates: List[str],
                       value_vars: List[str],
                       period_to_int_dictionary):
    # Reshape from wide to long.
    df = pd.melt(df,
                 id_vars=['case_number', treatment_date_variable, 'judgment_for_plaintiff'] + pre_treatment_covariates,
                 value_vars=value_vars, var_name='month', value_name=analysis)
    df = df.sort_values(by=['case_number', 'month'])

    # Convert months from string format to integer format.
    df.loc[:, 'month'] = (df['month'].str.replace(f"_{analysis}", '', regex=False)
                          .replace(period_to_int_dictionary)
                          .astype(int))
    df.loc[:, treatment_date_variable] = df[treatment_date_variable].replace(period_to_int_dictionary)

    # Set treatment month to 0 for untreated observations.
    never_treated_mask = (df['judgment_for_plaintiff'] == 0)
    df.loc[never_treated_mask, treatment_date_variable] = 0

    # Generate numeric version of case_number.
    df.loc[:, 'case_number_numeric'] = df['case_number'].astype('category').cat.codes.astype(int)
    df.loc[:, 'case_number_numeric'] = df['case_number_numeric'] + 1
    return df
