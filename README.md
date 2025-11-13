# dayabay-model-official

[![python](https://img.shields.io/badge/python-3.11-purple.svg)](https://www.python.org/)
[![pipeline](https://git.jinr.ru/dagflow-team/dayabay-model-official/badges/main/pipeline.svg)](https://git.jinr.ru/dagflow-team/dayabay-model-official/commits/main)
[![coverage report](https://git.jinr.ru/dagflow-team/dayabay-model-official/badges/main/coverage.svg)](https://git.jinr.ru/dagflow-team/dayabay-model-official/-/commits/main)

<!--- Uncomment here after adding docs!
[![pages](https://img.shields.io/badge/pages-link-white.svg)](http://dagflow-team.pages.jinr.ru/dayabay-model-official)
-->

Official model of the Daya Bay reactor antineutrino experiment for neutrino oscillation analysis based on gadolinium capture data.

## Content

- [Repositories](#repository)
- [Minimal working example](minimal-working-example)


## Repositories

- Development/CI: https://git.jinr.ru/dagflow-team/dayabay-model-official
- Contact/pypi/mirror: https://github.com/dagflow-team/dayabay-model-official
- PYPI: https://pypi.org/project/dayabay-model-official

## Minimal working example

If you want to run examples from `extras/mwe`, clone this repository `git clone https://github.com/dagflow-team/dayabay-model-official` and change position to cloned reposiotry `cd dayabay-model-official`.
However, you can just copy examples that are listed below and run them where you want after installation of package and several others steps:

1. Install package `pip install dayabay-model-official`
2. Install required packages: `pip install -r requirements`
3. Download archive from the provided storages by email (check email from Maxim Gonchar 13 November 2025) and unpack it
  - Download archive `dayabay_data_v2-npz.zip`
  - Unpack archive `dayabay_data_v2-npz.zip`: via GUI or just run command `unzip /path/to/dayabay_data_v2-npz.zip -d ./`. **WARNING**: unpacking might cause overwritting of `README.md`. Ignore it and press `N`+`Enter`
  - Rename data directory from `npz/` to `data/` via GUI or  just run command `mv npz/ data/`
4. Update `PYTHONPATH` variable to the current directory: `export PYTHONPATH=$PHYTHONPATH:$PWD`. **Alternative**: set variable value when you are running example: `PYTHONPATH=PWD python ./extras/...`
6. Run script `python extras/mwe/run.py` or `PYTHONPATH=PWD python extras/mwe/run.py`
```python
from dayabay_model_official import model_dayabay

model = model_dayabay()
print(model.storage["outputs.statistic.full.covmat.chi2cnp"].data)
```
within `python`
```bash
python extras/mwe/run.py
```
7. Check output in console, it might be something like below
```bash
INFO: Model version: model_dayabay
INFO: Source type: npz
INFO: Data path: data
INFO: Concatenation mode: detector_period
INFO: Spectrum correction mode: exponential
INFO: Spectrum correction location: before integration
[705.12741983]
```
It shows non-zero value of chi-squared function because by default it loads `real` data. About choosing `real`/`asimov` data read above.
8. Also, you may pass custom path to data, if you put `path_data` parameter to model. For example,
```python
from dayabay_model_official import model_dayabay

model = model_dayabay(path_data="dayabay-data-official/npz")
print(model.storage["outputs.statistic.full.pull.chi2cnp"].data)
```
Example can be executed: `python extras/mwe/run-custom-data-path.py` or `PYTHONPATH=PWD python extras/mwe/run-custom-data-path.py`
**Warning**: before running this example, make sure that you have put data in `dayabay-data-official/npz`. You can do it with `data/` from previous example. Run commands:
```bash
mkdir dayabay-data-official/
mv data/ dayabay-data-official/npz/
```

9. If you want to switch between Asimov and observed data, you need to switch input in the next way
```python
from dayabay_model_official import model_dayabay

model = model_dayabay(path_data="dayabay-data-official/npz")

print("CNP chi-squared (default data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

model.switch_data("real")
print("CNP chi-squared (real data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

model.switch_data("asimov")
print("CNP chi-squared (asimov data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)
```
Example can be executed: `python extras/mwe/run-switch-asimov-real-data.py` or `PYTHONPATH=PWD python extras/mwe/run-switch-asimov-real-data.py`
