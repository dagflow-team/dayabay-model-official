from dayabay_model_official import model_dayabay

ASIMOV_INPUT_INDEX = 0
OBSERVED_INPUT_INDEX = 1

model = model_dayabay(path_data="dayabay-model-official/npz")

print(model.storage["outputs.statistic.full.pull.chi2p"].data)

model.storage["nodes.data.proxy"].switch_input(OBSERVED_INPUT_INDEX)
print(model.storage["outputs.statistic.full.pull.chi2p"].data)

model.storage["nodes.data.proxy"].switch_input(ASIMOV_INPUT_INDEX)
print(model.storage["outputs.statistic.full.pull.chi2p"].data)
