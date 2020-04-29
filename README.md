# Fuzzy Word Matcher

FuzzyMatcher is a a python package exposed through a flask app that suggests **correct** dictionary words for a given "word" or word part.


## Use cases



## Dev

### Setup

To setup development environment, follow these steps:

```bash
git clone https://github.com/sebasibarguen/fuzzy_matcher.git
cd fuzzy_matcher
python3 -m venv venv
. venv/bin/activate
```

### Run 

```bash
export FLASK_APP=web/run:app
export FLASK_ENV=development
flask run
```

### Run tests

In top direcotyr, run `python -m pytest`

