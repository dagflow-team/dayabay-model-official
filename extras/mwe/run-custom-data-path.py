from dayabay_model_official import model_dayabay

model = model_dayabay(path_data="dayabay-model-official/npz")
print(model.storage["outputs.statistic.full.pull.chi2p"].data)
