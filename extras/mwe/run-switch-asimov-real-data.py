from dayabay_model_official import model_dayabay


model = model_dayabay(path_data="dayabay-data-official/npz")

print("CNP chi-squared (default data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

model.switch_data("real")
print("CNP chi-squared (real data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

model.switch_data("asimov")
print("CNP chi-squared (asimov data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)
