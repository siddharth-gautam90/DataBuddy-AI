# DataBuddy AI

DataBuddy AI is a Python-based data analysis dashboard that helps users explore CSV datasets, inspect data quality, view statistical summaries, and create interactive visualizations.

## Features

- Upload CSV datasets.
- View dataset dimensions and preview rows.
- Identify missing values and duplicate rows.
- Inspect column data types and unique values.
- Generate statistical summaries for numeric columns.
- Visualize numeric data using histograms and box plots.
- Download a data quality report as a CSV file.
- Handle common CSV reading errors.

## Built With

- Python
- Streamlit
- Pandas
- Plotly Express

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/siddharth-gautam90/DataBuddy-AI.git
cd DataBuddy-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install streamlit pandas plotly
```

## Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the dashboard.

## How to Use

1. Launch the application.
2. Upload a CSV file.
3. Explore the dataset preview and overview.
4. Review the data quality report.
5. Inspect statistical summaries.
6. Select a numeric column and visualization type.
7. Download the data quality report.

## Current Limitations

- CSV files are supported; other file formats are not currently supported.
- Visualizations are available only for numeric columns.
- The downloadable report currently contains data quality information, not the complete statistical analysis.

## Future Improvements

- Support additional chart types.
- Add downloadable statistical summaries.
- Provide options for handling missing values.
- Improve validation for large and unusual CSV files.

## Author

Siddharth Gautam

GitHub: [siddharth-gautam90](https://github.com/siddharth-gautam90)
