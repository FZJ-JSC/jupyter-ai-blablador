# jupyter_ai_blablador

`jupyter_ai_blablador` is a Jupyter AI module, a package
that registers additional model providers and slash commands for the Jupyter AI
extension.

## Requirements

- Python 3.8 - 3.12
- JupyterLab 4

## Install

To install the extension, execute:

```bash
pip install jupyter_ai_blablador
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyter_ai_blablador
```

## Contributing

### Development install

```bash
cd jupyter-ai-blablador
pip install -e "."
```

### Development uninstall

```bash
pip uninstall jupyter_ai_blablador
```

#### Backend tests

This package uses [Pytest](https://docs.pytest.org/) for Python testing.

Install test dependencies (needed only once):

```sh
cd jupyter-ai-blablador
pip install -e ".[test]"
```

To execute them, run:

```sh
pytest -vv -r ap --cov jupyter_ai_blablador
```
