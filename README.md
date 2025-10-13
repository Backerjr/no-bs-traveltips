# no-bs-traveltips

A tiny, dependency-light command line tool that prints no-nonsense tips for popular destinations.

## Getting started

Create a virtual environment (optional but recommended) and install the testing dependency:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

List supported destinations:

```bash
python -m traveltips.cli
```

Look up tips for a specific city:

```bash
python -m traveltips.cli "Tokyo"
```

Search the catalog:

```bash
python -m traveltips.cli --search yo
```

## Tests

Run the automated test suite with:

```bash
pytest
```
