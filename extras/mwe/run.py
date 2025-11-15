#!/usr/bin/env python

from dayabay_model import model_dayabay

model = model_dayabay()
print("χ² CNP value:", model.storage["outputs.statistic.full.covmat.chi2cnp"].data)
