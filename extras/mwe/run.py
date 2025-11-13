#!/usr/bin/env python

from dayabay_model_official import model_dayabay

model = model_dayabay()
print("χ² CNP value:", model.storage["outputs.statistic.full.covmat.chi2p"].data)
