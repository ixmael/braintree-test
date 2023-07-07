# Calculate the accounts' balances from a file
This script reads a file and calculate the balance of the accounts.

## Setup
This project use Poetry to manage the packages.

```bash
# Install the dependencies and generate the python environment
poetry install
```

## Run
The script reads a file or the content of the *STDIN*.

```bash
# Set the file name
poetry run python processing.py test_file.txt

# Redirect the STDIN to the script
poetry run python processing.py < test_file.txt
```

## Tests
This project implements some unit tests.

```bash
# Run tests
poetry run python -m unittest
```