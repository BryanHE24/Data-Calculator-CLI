# Data Calculator CLI

A professional-grade command-line tool for statistical analysis and matrix operations. Built with Python, Click, and NumPy following Clean Code principles.

## Features

* **Descriptive Statistics**: Calculate Mean, Median, Mode, Variance, and Standard Deviation.
* **Linear Algebra**: Perform Matrix Transpose and Dot Products using NumPy.
* **Data Normalization**: Preprocess data for AI with Min-Max and Z-Score scaling.
* **Robust I/O**: Handles CSV files and standard error reporting.

## Installation

**Prerequisites:** Python 3.10+

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd data_calculator

# 2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt
```

## Usage

### 1. Statistics & Normalization

```bash
# Run stats on a CSV file
python -m calculator.cli stats --file data/sample.csv

# Normalize data (Min-Max)
python -m calculator.cli normalize --file data/sample.csv --type min-max
```

### 2. Matrix Operations

```bash
# Transpose a 2x2 Matrix
python -m calculator.cli matrix transpose "[[1, 2], [3, 4]]"

# Calculate Dot Product
python -m calculator.cli matrix dot "[[1, 2]]" "[[1], [2]]"
```

## Testing

This project uses `pytest` for automated logic verification.

```bash
python -m pytest -v
```

## Project Structure

```
data_calculator/
├── calculator/
│   ├── cli.py       # Entry point & Interface
│   ├── stats.py     # Pure Statistics Logic
│   ├── matrix.py    # Pure Matrix Logic (NumPy)
│   └── utils.py     # File I/O
├── tests/           # Automated Unit Tests
├── data/            # Sample Datasets
└── requirements.txt # Dependencies
```

## Methodology (BMAD)

This project was built using the Breakthrough Method for Agile AI-Driven Development (BMAD).

* **Cycle 1**: Python Foundations.
* **Focus**: Separation of Concerns, Pure Functions, and Explainable Code.

---
