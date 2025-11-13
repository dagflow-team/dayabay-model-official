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
- [Minimal working example](#minimal-working-example)
  - [Preparation](#preparation)
  - [Simple run](#simple-run)
  - [Custom path to data](#custom-path-to-data)
  - [Switch between real and asimov data](#switch-between-real-and-asimov-data)

66:### Simple run
101:### Custom path to model data
134:### Switch between real and Asimov data

## Repositories

- Development/CI: https://git.jinr.ru/dagflow-team/dayabay-model-official
- Contact/pypi/mirror: https://github.com/dagflow-team/dayabay-model-official
- PYPI: https://pypi.org/project/dayabay-model-official

## Daya Bay analysis repository

Several examples of scripts for fitting and plotting results are stored in [dayabay-analysis](https://github.com/dagflow-team/dayabay-analysis). Do steps from [preparation section](section) before going to the repository with analysis examples.

## Minimal working example

If you want to run examples from `extras/mwe`, clone this repository `git clone https://github.com/dagflow-team/dayabay-model-official` and change position to cloned reposiotry `cd dayabay-model-official`.
However, you can just copy examples that are listed below and run them where you want after installation of package and several others steps:

### Preparation

Here are described several points of how to start work with `dayabay-official-data` and how to run MWE. Same steps might be useful for [dayabay-analysis](https://github.com/dagflow-team/dayabay-analysis).

1. Install package
```bash
pip install dayabay-model-official
```
2. Download archive from the provided storages by email (check email from Maxim Gonchar 13 November 2025) and unpack it
  - Download archive
    ```bash
    dayabay_data_v2-npz.zip
    ```
  - Unpack archive `dayabay_data_v2-npz.zip`: via GUI or just run command
    ```bash
    unzip /path/to/dayabay_data_v2-npz.zip -d ./
    ```
    **WARNING**: unpacking might cause overwritting of `README.md`. Ignore it and press `N`+`Enter`
  - Rename data directory from `npz/` to `data/` via GUI or  just run command
    ```bash
    mv npz/ data/
    ```
3. Update `PYTHONPATH` variable to the current directory:
  ```bash
  export PYTHONPATH=$PHYTHONPATH:$PWD
  ```
  **Alternative**: set variable value when you are running example: `PYTHONPATH=PWD python ./extras/...`

### Simple run

Let's run model without any additional parameters. AS it is from box.

1. Run script
  ```bash
  python extras/mwe/run.py
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

### Custom path to model data

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

### Switch between real and Asimov data

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
