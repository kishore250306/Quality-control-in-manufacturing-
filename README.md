# Quality Control Report Generator

This Python script performs a basic quality control (QC) check on product diameters. It compares each measurement against a target value within a specified tolerance and generates a CSV report showing whether each product passes or fails.

## Features

- Compares product diameters to a target with tolerance
- Identifies products that are out of spec
- Outputs results to a `qc_report.csv` file

## How to Use

1. Make sure you have Python 3 installed.

2. Run the script:

```bash
python qc_report_generator.py
```

3. A file named `qc_report.csv` will be created in the same directory.

## Output Format

The generated CSV report includes:

- **Product ID**
- **Diameter**
- **Status** (PASS or FAIL)

Example:
```
Product ID,Diameter,Status
1,50.2,PASS
2,49.6,PASS
3,50.0,PASS
4,50.6,FAIL
5,49.4,FAIL
```

## Configuration

You can change the target diameter, tolerance, and product data directly in the script:

```python
TARGET_DIAMETER = 50.0  # mm
TOLERANCE = 0.5         # mm
```
