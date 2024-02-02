# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Pandas_dataframe__2_ = dataiku.Dataset("Pandas_dataframe__2_")
Pandas_dataframe__2__df = Pandas_dataframe__2_.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_df = Pandas_dataframe__2__df # For this sample code, simply copy input to output

import time
time.sleep(300)

# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(test_df)
