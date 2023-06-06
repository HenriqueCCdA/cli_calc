# Projeto de calculador usando o typer

```console
poetry new --src . --name calc
```

Instalando dependencias

```console
poetry add typer
```

```console
poetry add --group dev pytest ruff black pre-commit
```

## Instalação

Instalando o ambiente de desenvolvimento como editavel

```console
poetry install
```

Instalando sem o ambiente de desenvolvimento

```console
poetry install --without dev
```

## Build

Fazendo a `build` do pacote

```console
poetry build
```

## Insalando o pacote

```console
pip install calc-0.1.0-py3-none-any.whl
```

## Uso

```console
calc add 8 8
8.0 + 8.0 = 16.0
```

```console
calc sub 8 9
8.0 - 9.0 = -1.0
```

```console
calc mul 8 9
8.0 * 9.0 = 72.0
```

```console
calc div 8 9
8.0 / 9.0 = 0.8888888888888888
```

```console
calc div 8 0
Error: Denominator must be not null!
```
