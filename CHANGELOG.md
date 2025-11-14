# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.4.2] - 2025-11-

- feature: a script to plot neutrino rate daily data.
- chore: update variable names, labels, units. TODO

## [1.4.1] - 2025-11-08

- feature: add `mc_parameters` field to determine wich normalized parameters will be used to produce Monte-Carlo samples. It works with names of parameters from the storage, not their covariance uncertainties aliases.

## [1.4.0] - 2025-11-07

- feature: official data now uses total weekly neutrino rate from each reactor.
- feature: remove test for checking reactor data plots.

## [1.3.2] - 2025-11-02

- hotfix: `full.covmat.chi2cnp` was removed to avoid confusions. `full.covmat.chi2cnp_alt` wes renamed to `full.covmat.chi2cnp`, it is defined as (18)-(19) equations from the [arXiv: 1903.07185](https://arxiv.org/pdf/1903.07185). Only `v1a` and `v1a_distorted` were updated.

## [1.3.1] - 2025-11-02

- hotfix: add `absolute_efficiency` gruop for covariance matrix and pull terms. Works with model `v1a`, and `v1a_distorted`.

## [1.3.0] - 2025-10-31

- feature: add `covariance_groups` parameter to control passed nuisance parameters to covarince matrix, works only with `strict=False`.
- feature: add `pull_groups` parameter to control passed nuisance parameters to `nuisance.pull_extra`.
- feature: add `is_absolute_efficiency_fixed` parameter to switch between fixed/variable absolute correlated detector efficiency.
- feature: prepare code for reading variable periods of reactor data.

## [1.2.1] - 2025-10-16

- feature: validate the data version from `data_information.yaml` and use it to determine the `source_type` (data format).
- feature: check that overridden indices exist.
- fix: apply `Abs` transformation to scaled fission fractions.
- chore: minor fixes and updates.

## [1.2.0] - 2025-10-07

- feature: add `detector_selected` index to select detectors for the χ² construction.
- feature: Add `switch_data` method. It can switch model output between real data (`real`) and Asimov (`asimov`).
- feature: Support all the inputs via `uproot` (`ROOT` is supported just as before).
- update: auto detection of source type skip `parameters` directory natively. Docstring was added.

## [1.1.1] - 2025-10-02

- feature: enable uproot only operation (no ROOT required).
- chore: antineutrino spectrum parametrization edges are stored in a text file instead of python.

## [1.1.0] - 2025-09-25

- feature: example scripts.
- chore: automatic data type detection.
- chore: clean data format.

## [1.0.0] - 2025-09-08

- First public PYPI version. The model is based on v1 from [dgm-dayabay-dev](https://github.com/dagflow-team/dgm-dayabay-dev).
