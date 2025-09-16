import os
import subprocess


def run_script(script: str, args: list[str]) -> tuple[str, str, int]:
    print("Starting the test of the following script: ", script)
    result = subprocess.run(
        [script, *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode(), result.stderr.decode(), result.returncode


def test_run_dayabay_plot_all_nodes():
    parameter_path = "outputs.background"
    output_path = "output/plot-all-nodes-kinematics-ibd"
    node_path = "kinematics.ibd"
    stdout, stderr, code = run_script(
        "./extras/scripts/dayabay-plot-all-nodes.py",
        [
            "--print",
            parameter_path,
            "--plots",
            output_path,
            node_path,
        ],
    )

    assert code == 0
    assert stderr == ""
    assert parameter_path in stdout
    assert f"Write: {output_path}" in stdout
    assert os.path.exists(output_path)


def test_run_dayabay_plot_detector_data():
    parname = "survival_probability.DeltaMSq32"
    parvalue = "2.5e-3"
    output = "output/plot-detector-data-{type}.pdf"

    stdout, stderr, code = run_script(
        "./extras/scripts/dayabay-plot-detector-data.py",
        [
            "--par",
            parname,
            parvalue,
            "--output",
            output,
        ],
    )

    assert code == 0
    assert stderr == ""
    assert "Push survival_probability.DeltaMSq32=2.5e-3" in stdout
    for type in ["eff", "eff_livetime", "rate_accidentals"]:
        assert f"Save plot: {output.format(type=type)}" in stdout
        assert os.path.exists(output.format(type=type))


def test_run_dayabay_plot_reactor_data():
    parname = "survival_probability.DeltaMSq32"
    parvalue = "2.5e-3"
    output = "output/plot-detector-data-{type}.pdf"

    stdout, stderr, code = run_script(
        "./extras/scripts/dayabay-plot-reactor-data.py",
        [
            "--par",
            parname,
            parvalue,
            "--output",
            output,
        ],
    )

    assert code == 0
    assert stderr == ""
    assert f"Push {parname}={parvalue}" in stdout
    for type in ["power", "fission_fraction"]:
        assert f"Save plot: {output.format(type=type)}" in stdout
        assert os.path.exists(output.format(type=type))
