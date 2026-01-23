"""
Data loading utilities for Inside Airbnb dataset.

This module provides functions to load and combine monthly CSV files
from the Inside Airbnb NYC dataset.
"""

from pathlib import Path
from typing import List
import pandas as pd


def load_monthly_listings(data_folder: Path, year: int = 2025) -> pd.DataFrame:
    """
    Load and combine all monthly listing CSV files for a given year.
    
    Parameters
    ----------
    data_folder : Path
        Path to the folder containing the CSV files
    year : int, default=2025
        Year of the data files to load
        
    Returns
    -------
    pd.DataFrame
        Combined dataframe with all monthly listings, including a 'month' column
    """
    files = sorted(data_folder.glob(f"listings_*_{year}.csv"))
    
    if not files:
        raise FileNotFoundError(
            f"No listing files found in {data_folder} for year {year}. "
            f"Expected pattern: listings_*_{year}.csv"
        )
    
    dfs = []
    loaded_files = []
    
    for f in files:
        # Extract the month name between "listings_" and "_2025"
        month_str = f.stem.split("_")[1]
        
        df = pd.read_csv(f)
        df["month"] = month_str
        dfs.append(df)
        loaded_files.append(f.name)
    
    # Combine all dataframes
    full_df = pd.concat(dfs, ignore_index=True)
    
    print(f"Loaded {len(files)} files:")
    for f in loaded_files:
        print(f" - {f}")
    print(f"\nFinal combined shape: {full_df.shape}")
    
    return full_df
