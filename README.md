# Inside Airbnb Analysis - NYC Rental Prices

This project analyzes NYC Airbnb rental prices through the year 2025. It starts with exploratory data analysis and preprocessing to remove outlier/scam listings and computes key summary statistics to understand how the data is distributed. Trends across seasons and boroughs is examined and displayed in meaningful graphs.

## Project Structure

```
.
├── src/
│   └── inside_airbnb/          # Main package
│       ├── __init__.py
│       ├── data_loading.py     # Functions to load CSV files
│       ├── preprocessing.py    # Data cleaning and preprocessing
│       ├── analysis.py         # Statistical analysis functions
│       └── visualization.py   # Plotting functions
├── notebooks/                  # Jupyter notebooks
│   ├── InsideAirbnbAnalysis.ipynb  # Original notebook
│   └── example_refactored_analysis.py  # Example using refactored code
├── data/
│   ├── raw/                    # Raw CSV files (gitignored)
│   └── processed/              # Processed data (gitignored)
├── reports/
│   └── figures/                # Saved visualizations
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
└── .gitignore
```

## Quick Start

### 1. Install the Package

```bash
pip install -e .
```

**Alternative:**

```bash
pip install -r requirements.txt
```

Note: If you use the alternative method, you'll need to manually add the `src` directory to your Python path (see example below).

### 2. Using the Refactored Code

**If you installed with `pip install -e .`** (recommended), you can directly import:

```python
from inside_airbnb import data_loading, preprocessing, analysis, visualization
```

**If you only installed dependencies** (using `pip install -r requirements.txt`), you need to add the src directory to your path:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd() / "src"))

from inside_airbnb import data_loading, preprocessing, analysis, visualization
```

## Key Improvements

### ✅ **Modular Code Structure**
- Data loading logic extracted to `data_loading.py`
- Preprocessing steps in `preprocessing.py`
- Analysis functions in `analysis.py`
- Visualization functions in `visualization.py`

### ✅ **Reusable Functions**
- All functions are well-documented with docstrings
- Functions can be imported and reused across notebooks
- Easy to test and maintain

### ✅ **Better Organization**
- Clear separation of concerns
- Follows Python package best practices
- Easy to extend with new functionality

### ✅ **Professional Setup**
- `setup.py` for package installation
- `.gitignore` to exclude data files and outputs
- Proper directory structure

## Module Documentation

### `data_loading.py`
- `load_monthly_listings()`: Load and combine monthly CSV files

### `preprocessing.py`
- `clean_price_column()`: Remove currency symbols, convert to numeric
- `add_month_number()`: Convert month names to numbers (1-12)
- `filter_price_outliers()`: Remove listings above price threshold
- `preprocess_data()`: Complete preprocessing pipeline

### `analysis.py`
- `calculate_rental_stats()`: Calculate count, mean, median, std
- `compare_boroughs()`: Compare prices between boroughs
- `count_luxury_listings()`: Count listings above threshold
- `calculate_seasonal_range()`: Calculate seasonal price variation

### `visualization.py`
- `plot_price_histograms_by_borough()`: Price histograms by borough
- `plot_price_histogram_log_scale()`: Log-scale histograms
- `plot_manhattan_neighborhood_prices()`: Manhattan neighborhood analysis
- `plot_manhattan_boxplot()`: Boxplots by neighborhood
- `plot_correlation_heatmap()`: Feature correlation matrix
- `plot_seasonal_trends()`: Monthly price trends

## Next Steps

1. **Update your notebook**: Replace inline code with function calls from the modules
2. **Add tests**: Create unit tests for your functions (e.g., `tests/test_preprocessing.py`)
3. **Add configuration**: Create a `config.py` for parameters like `max_price`, file paths, etc.
4. **Documentation**: Add more detailed docstrings and examples

## Research Questions

1. How do rental prices vary seasonally?
2. What is the price distribution across different NYC boroughs?
3. How do prices vary within Manhattan neighborhoods?
4. Which features correlate most strongly with price?

## Data Source

Inside Airbnb NYC dataset (January-October 2025)
- Website: http://insideairbnb.com
- Data includes listings, reviews, and calendar data
