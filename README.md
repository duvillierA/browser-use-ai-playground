# Browser Use Demo

A Python application that demonstrates automated browser interactions using LangChain and OpenAI.

## Prerequisites

- Python 3.11 or later
- OpenAI API key
- Poetry (optional, for Poetry installation method)

## Installation

1. **Clone the repository:**

```
git clone https://github.com/your-username/browser-use-demo.git
cd browser-use-demo
```

2. **Install dependencies:**

Via poetry:

```
curl -sSL https://install.python-poetry.org | python3 -
poetry install --no-root
poetry run playwright install
```

Via pip:

```
pip install -r requirements.txt
playwright install
```

3. **Run app:**

Via poetry:

```
poetry run python app/init.py
```

Via pip:

```
python app/init.py
```

