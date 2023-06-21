## 1 Purpose of this repo
The purpose of this repo is mainly to explore [pytest](https://docs.pytest.org/en/7.3.x/). Tests can be found in [tests](tests). 

To ensure code quality, this repository leverages the capabilities of pre-commit. If you're curious about pre-commit and want to explore its capabilities further, I recommend checking out this other repository: https://github.com/anneglienke/101_pre-commit

## 2 Running locally
To run locally, you will need Python 3.11 or newer installed in your local environment. Then, just install the dependencies and execute the `main.py` file:

Create a virtual environment:
```
python3 -m venv .venv
```

Activate local environment:
```
source .venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Install git hooks
```
pre-commit install
```

Run script:
```
python3 src/main.py
```

Run tests:
```
pytest -v tests
```
Run test coverage command to generate report locally:
```
pytest --cov --cov-report=html
```



