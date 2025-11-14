#!/usr/bin/env python

from dayabay_model_official import model_dayabay

model = model_dayabay(path_data="data")

print("χ² CNP (default data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

model.switch_data("real")
print("χ² CNP (real data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

model.switch_data("asimov")
print("χ² CNP (asimov data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)
