# Topsis-Raghav-102203745

A Python package to implement the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision-making problems.

---

## Features

- Rank alternatives based on multiple criteria.
- Handle positive and negative impacts of criteria.
- Simple to use with CSV input/output.
- Fully customizable weights and impacts.

---

## Installation

Install the package directly from PyPI:

```bash
pip install Topsis-Raghav-102203754
```

---

## How to Use

The package can be used through the command line or imported into a Python script.

### **Command-Line Usage**

The basic syntax for using the package via the command line:

```bash
python -m topsis <input_file> <weights> <impacts> <output_file>
```

#### **Parameters:**
- `input_file`: CSV file containing the decision matrix.
- `weights`: Comma-separated values representing the importance of each criterion (e.g., `1,1,2,3`).
- `impacts`: Comma-separated values representing the impact of each criterion (`+` for positive, `-` for negative).
- `output_file`: Name of the CSV file where the results will be saved.

#### **Example:**

```bash
python -m topsis data.csv "1,1,2,3" "+,+,-,+" result.csv
```

#### **Input File Format:**

The input file must be a CSV file with the following structure:

| Alternatives | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|--------------|-------------|-------------|-------------|-------------|
| A1           | 250         | 16          | 12          | 5           |
| A2           | 200         | 18          | 8           | 3           |
| A3           | 300         | 14          | 16          | 7           |
| A4           | 275         | 17          | 10          | 4           |

- The first column contains alternative names (e.g., A1, A2, etc.).
- From the second column onwards, numeric values for each criterion are provided.

#### **Output File Format:**

The output file will include the input data along with two additional columns:

| Alternatives | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 | Topsis Score | Rank |
|--------------|-------------|-------------|-------------|-------------|--------------|------|
| A1           | 250         | 16          | 12          | 5           | 0.65         | 2    |
| A2           | 200         | 18          | 8           | 3           | 0.45         | 4    |
| A3           | 300         | 14          | 16          | 7           | 0.78         | 1    |
| A4           | 275         | 17          | 10          | 4           | 0.52         | 3    |

---

### **Python Script Usage**

You can also import and use the package in your Python scripts:

```python
from topsis_raghav_102203754 import topsis

topsis(
    input_file="data.csv",
    weights="1,1,2,3",
    impacts="+,+,-,+",
    output_file="result.csv"
)
```

---

## Validation and Error Handling

The package includes robust error handling to ensure correct inputs:

1. **File Not Found:**
   - If the input file does not exist, an appropriate error message is shown.

2. **Invalid Parameters:**
   - The number of weights, impacts, and criteria must match.

3. **Non-Numeric Values:**
   - From the second column onwards, only numeric values are allowed.

4. **Invalid Impacts:**
   - Impacts must be either `+` or `-`.

5. **Minimum Column Requirement:**
   - The input file must have at least three columns.

---

## Example Files

You can test the package using the following example files:

### Input File (`data.csv`):

| Alternatives | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|--------------|-------------|-------------|-------------|-------------|
| A1           | 250         | 16          | 12          | 5           |
| A2           | 200         | 18          | 8           | 3           |
| A3           | 300         | 14          | 16          | 7           |
| A4           | 275         | 17          | 10          | 4           |

### Output File (`result.csv`):

| Alternatives | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 | Topsis Score | Rank |
|--------------|-------------|-------------|-------------|-------------|--------------|------|
| A1           | 250         | 16          | 12          | 5           | 0.65         | 2    |
| A2           | 200         | 18          | 8           | 3           | 0.45         | 4    |
| A3           | 300         | 14          | 16          | 7           | 0.78         | 1    |
| A4           | 275         | 17          | 10          | 4           | 0.52         | 3    |

---

## Author

Developed by **Raghav Jindal (Roll Number: 102203745)**.
