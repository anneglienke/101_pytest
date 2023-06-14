Create a virtual environment
'python3 -m venv .venv'
Activace
'source /Users/anneglienke/Work/101_pytest/.venv/bin/activate'

### Running locally
To run locally, you will need Python 3.11 or newer installed in your local environment. Then, just install the dependencies and execute the `main.py` file:

Create a virtual environment:
```
$ python3 -m venv .venv
```

Activate local environment:
```
$ source /Users/anneglienke/Work/101_pytest/.venv/bin/activate
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
$ python ./main.py
```


mypy = help ensure that you're using variables and functions in your code correctly
ruff = analyze a program's source code to detect various problems such as syntax errors, programming mistakes, style violations, and more
black = formats code
pre-commit = run tests before commit