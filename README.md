# coin-tracker

A small Python utility to fetch, format and export Ethereum transaction data. The project provides python command to fetch Ethereum transactions and generate CSV file.

## Contents

- `api_client/` — low-level API client(s) (e.g., `ethereum_api_client.py`) for talking to blockchain/external APIs.
- `factory/` — factories for creating transaction fetchers (`transaction_fetcher_factory.py`).
- `formatter/` — transaction formatters (for normalizing API payloads into CSV-ready rows).
- `service/` — high-level services : fetching, formatting and exporting transactions (`ethereum_transactions.py`, `transactions_csv.py`).
- `utils/` — helper utilities (e.g., `csv_parser.py`).
- `exports/` — sample or generated CSV exports.
- `generate_report.py` — small runner script to generate a report (example usage below).
- `env.sample` — example environment variables file.
- `requirement.txt` — Python dependencies.

## Features

- Fetch Ethereum transaction data via pluggable API client(s).
- Normalize and format transactions into CSV rows.
- Export transaction reports to CSV with timestamped filenames.
- Simple factory pattern to choose different fetchers/backends.

## Quick start

1. Create a virtual environment (recommended):

	python3 -m venv .venv
	source .venv/bin/activate

2. Install dependencies:

	pip install -r requirement.txt

3. Copy environment sample and provide real values:

	env.sample (edit env.sample and update api_key and base_url)

4. Run the example report generator:

	python generate_report.py -a address

The runner will use default settings (or values from `.env`) and create a CSV in the `exports/` folder.


## Project layout and important files

- `api_client/ethereum_api_client.py` — the place to add or modify low-level API calls to blockchain providers.
- `factory/transaction_fetcher_factory.py` — choose which fetcher (implementation) to use based on configuration.
- `formatter/ethereum_transaction_formatter.py` — normalizes API payloads into a consistent CSV-ready structure.
- `service/ethereum_transactions.py` — orchestrates fetching, formatting and preparing data for export.
- `service/transactions_csv.py` — contains CSV export helpers (filename format, headers).
- `utils/csv_parser.py` — small helpers for reading/parsing CSV files used in tests or import flows.
