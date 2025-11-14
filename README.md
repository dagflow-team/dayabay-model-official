# dayabay-model-official

[![python](https://img.shields.io/badge/python-3.11-purple.svg)](https://www.python.org/)
[![pipeline](https://git.jinr.ru/dagflow-team/dayabay-model-official/badges/main/pipeline.svg)](https://git.jinr.ru/dagflow-team/dayabay-model-official/commits/main)
[![coverage report](https://git.jinr.ru/dagflow-team/dayabay-model-official/badges/main/coverage.svg)](https://git.jinr.ru/dagflow-team/dayabay-model-official/-/commits/main)

<!--- Uncomment here after adding docs!
[![pages](https://img.shields.io/badge/pages-link-white.svg)](http://dagflow-team.pages.jinr.ru/dayabay-model-official)
-->

The model of the Daya Bay reactor antineutrino experiment dedicated to work with official Daya Bay dataset and perform neutrino oscillation analysis based on gadolinium capture data.

## Content

- [Repositories](#repository)
- [Minimal working example](#minimal-working-example)
  - [Preparation](#preparation)
  - [Simple run](#simple-run)
  - [Custom path to model data](#custom-path-to-model-data)
  - [Switch between real and asimov data](#switch-between-real-and-asimov-data)

## Repositories

- Development/CI: https://git.jinr.ru/dagflow-team/dayabay-model-official
- Contact/pypi/mirror: https://github.com/dagflow-team/dayabay-model-official
- PYPI: https://pypi.org/project/dayabay-model-official

## Working with the model

The typical workflow considers installation of the Daya Bay model via PYPI and using it in the analysis from within python. Minimal usage examples may be found in this repository while more comprehensive cases of the fits and statsitical analysis are provided in a dedicated [dayabay-analysis](https://github.com/dagflow-team/dayabay-analysis) repository.

### Minimal working examples

The minimal working exampls are located in the folder `extras/mwe` folder. In order to run them clone this repository :
```bash
git clone https://github.com/dagflow-team/dayabay-model-official 
cd dayabay-model-official
````
However, you can just copy examples that are listed below and run them where you want after installation of package and several others steps:

### Installation

The first steps are to obtain the code and the data:

```bash
# install the package
pip install dayabay-model-official
# obtain the dataset in a preferred format
# the file is shared via email at this stage
# download dayabay_data_v2-npz.zip # note: to be updated
# inpack the data
unzip /path/to/dayabay_data_v2-npz.zip -d ./
mv npz/ data/
# setup environment variables
export PYTHONPATH=$PHYTHONPATH:$PWD
```

<!-- **Alternative**: set variable value when you are running example: `PYTHONPATH=PWD python ./extras/...` -->

#### Simple run

Assuming the environment variables are set, the

1. Run script
  ```bash
  ./extras/mwe/run.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run.py
  ```
  Text of script is above
  ```python
  from dayabay_model_official import model_dayabay

  model = model_dayabay()
  print(model.storage["outputs.statistic.full.covmat.chi2cnp"].data)
  ```
  within `python`
  ```bash
  python extras/mwe/run.py
  ```
2. Check output in console, it might be something like below
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

#### Custom path to model data

Sometimes it is useful to load data model from specific directory. For this aim you may want to use `path_data` parameter of `model_dayabay`.

1. Also, you may pass custom path to data, if you put `path_data` parameter to model. For example,
  ```python
  from dayabay_model_official import model_dayabay

  model = model_dayabay(path_data="dayabay-data-official/npz")
  print(model.storage["outputs.statistic.full.pull.chi2cnp"].data)
  ```
  Example can be executed:
  ```bash
  python extras/mwe/run-custom-data-path.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run-custom-data-path.py
  ```
2. Example can be executed:
  ```bash
  python extras/mwe/run-custom-data-path.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run-custom-data-path.py
  ```
3. **Warning**: before running this example, make sure that you have put data in `dayabay-data-official/npz`. You can do it with `data/` from previous example. Run commands:
  ```bash
  mkdir dayabay-data-official/
  mv data/ dayabay-data-official/npz/
  ```

#### Switch between real and Asimov data

`real` data is loaded to model by default. However, it is possible to switch between `real` and `Asmov` datasets.

Short note:
- `real` means that will be loaded IBD candidates after selection;
- `asimov` means that data will be replaced with mean observation of model under assumption of mean parameters.

1. If you want to switch between Asimov and observed data, you need to switch input in the next way
  ```python
  from dayabay_model_official import model_dayabay

  model = model_dayabay(path_data="dayabay-data-official/npz")

  print("CNP chi-squared (default data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

  model.switch_data("real")
  print("CNP chi-squared (real data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)

  model.switch_data("asimov")
  print("CNP chi-squared (asimov data):", model.storage["outputs.statistic.full.pull.chi2cnp"].data)
  ```
2. Example can be executed: 
  ```bash
  python extras/mwe/run-switch-asimov-real-data.py
  ```
  or
  ```bash
  PYTHONPATH=PWD python extras/mwe/run-switch-asimov-real-data.py
  ```
