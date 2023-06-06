from typer.testing import CliRunner

from src.calc.cli import app

runner = CliRunner()


def test_add():
    result = runner.invoke(app, ["add", "5", "9"])

    assert result.exit_code == 0
    assert result.stdout == "5.0 + 9.0 = 14.0\n"


def test_sub():
    result = runner.invoke(app, ["sub", "5", "9"])

    assert result.exit_code == 0
    assert result.stdout == "5.0 - 9.0 = -4.0\n"


def test_mul():
    result = runner.invoke(app, ["mul", "5", "9"])

    assert result.exit_code == 0
    assert result.stdout == "5.0 * 9.0 = 45.0\n"


def test_div():
    result = runner.invoke(app, ["div", "9", "5"])

    assert result.exit_code == 0
    assert result.stdout == "9.0 / 5.0 = 1.8\n"


def test_div_by_zero():
    result = runner.invoke(app, ["div", "9", "0"])

    assert result.exit_code == 0
    assert result.stdout == "Error: Denominator must be not null!\n"
