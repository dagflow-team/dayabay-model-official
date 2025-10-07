from dayabay_model_official import model_dayabay

ASIMOV_INPUT_INDEX = 0
OBSERVED_INPUT_INDEX = 1

model = model_dayabay(path_data="dayabay-model-official/npz")

print(model.storage["outputs.statistic.full.pull.chi2p"].data)

model.switch_data("real")
print(model.storage["outputs.statistic.full.pull.chi2p"].data)

model.switch_data("asimov")
print(model.storage["outputs.statistic.full.pull.chi2p"].data)
