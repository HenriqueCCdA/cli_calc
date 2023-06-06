import typer
from rich import print

from calc.operation import InvalidOperation, add, div, mult, sub

app = typer.Typer(add_completion=False)


@app.command(name="add")
def addition(a: float, b: float):
    """Adicionando dois números"""
    result = add(a, b)
    print(f"{a} + {b} = {result}")


@app.command(name="sub")
def subtraction(a: float, b: float):
    """Subtraindo dois números"""
    result = sub(a, b)
    print(f"{a} - {b} = {result}")


@app.command(name="mul")
def multiplication(a: float, b: float):
    """Multiplicando dois números"""
    result = mult(a, b)
    print(f"{a} * {b} = {result}")


@app.command(name="div")
def division(a: float, b: float):
    """Dividindo dois números"""
    try:
        result = div(a, b)
        print(f"{a} / {b} = {result}")
    except InvalidOperation as e:
        print(f"[red]Error[/red]: {e}")
