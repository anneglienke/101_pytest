## 1 Purpose of this repo
The purpose of this repo is mainly to explore [pytest](https://docs.pytest.org/en/7.3.x/). Tests can be found in [tests](tests). 

It also introduces [pre-commit](https://pre-commit.com/) and some very cool checks/formatting that aim to ensure code quality and consistency, using [black](https://pypi.org/project/black/), [ruff](https://pypi.org/project/ruff/0.0.89/) and [mypy](https://mypy.readthedocs.io/en/stable/).

## 2 Running locally
To run locally, you will need Python 3.11 or newer installed in your local environment. Then, just install the dependencies and execute the `main.py` file:

Create a virtual environment:
```
$ python3 -m venv .venv
```

Activate local environment:
```
$ source .venv/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```

Install git hooks
```
$ pre-commit install
```

Run script:
```
$ python src/main.py
```

## 3 What is pre-commit?

`pre-commit` is a framework commonly used to execute code checks and tasks before committing changes to a version control system like Git. It allows developers to define a configuration file specifying various checks such as linters, code formatters, static analyzers, and custom scripts. These checks are run automatically when a commit is made, helping ensure code quality and consistency. If any checks fail, the commit process is interrupted, and errors or warnings are displayed to the developer. Pre-commit provides a practical way to enforce coding standards, catch potential issues early, and maintain a high level of code quality in a project.

To use `pre-commit`in your projects, don't forget to configure the [pre-commit config file](.pre-commit-config.yaml) and the [pyproject.toml](pyproject.toml). 

The `pyproject.toml` file is used as a configuration file that specifies various settings and dependencies for the project (metadata, build configurations, and tool settings).

### 3.1 What is it checking?

`black` = automatically formats code to adhere to a consistent style guide, known as "black formatting." By applying opinionated rules, Black helps ensure that code has a consistent layout, making it easier to read and maintain. 

`ruff` = analyzes a program's source code to detect various problems such as syntax errors, programming mistakes, style violations, and so on.

`mypy` = analyzes the types of variables, expressions, and function signature  correctly for potential type errors before runtime. By using type hints, Mypy can catch common programming mistakes, improve code quality, and provide better editor autocompletion and documentation. 

