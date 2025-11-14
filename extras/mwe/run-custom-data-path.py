#!/usr/bin/env python

from dayabay_model_official import model_dayabay

model = model_dayabay(path_data="./data")
print("χ² (CNP) value:", model.storage["outputs.statistic.full.pull.chi2cnp"].data)
