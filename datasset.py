# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:46:00 2020

@author: 91603
"""

import pandas as pd
import pandas_profiling
import csv
data = pd.read_csv('mean.csv')
data.profile_report(title = 'dataset')