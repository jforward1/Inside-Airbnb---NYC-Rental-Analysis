"""
Data preprocessing utilities for Inside Airbnb dataset.

This module provides functions to clean and preprocess the raw Airbnb data,
including price cleaning, month mapping, and outlier filtering.
"""

import pandas as pd
from typing import Optional


# Month name to number mapping
MONTH_MAPPING = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 
    'May': 5, 'June': 6, 'July': 7, 'August': 8, 
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}


def clean_price_column(df: pd.DataFrame, price_col: str = 'price') -> pd.DataFrame:
    """
    Clean the price column by removing currency symbols and converting to numeric.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with price column
    price_col : str, default='price'
        Name of the price column to clean
        
    Returns
    -------
    pd.DataFrame
        Dataframe with cleaned price column (numeric)
    """
    df = df.copy()
    
    # Remove dollar signs and commas, convert to numeric
    df[price_col] = (
        df[price_col]
        .astype(str)
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
    )
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
    
    return df


def add_month_number(df: pd.DataFrame, month_col: str = 'month', 
                     month_num_col: str = 'month_num') -> pd.DataFrame:
    """
    Add a numeric month column (1-12) from month name column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with month name column
    month_col : str, default='month'
        Name of the month name column
    month_num_col : str, default='month_num'
        Name for the new numeric month column
        
    Returns
    -------
    pd.DataFrame
        Dataframe with added month_num column
    """
    df = df.copy()
    df[month_num_col] = df[month_col].map(MONTH_MAPPING)
    return df


def filter_price_outliers(df: pd.DataFrame, max_price: float = 5000.0, 
                         price_col: str = 'price', 
                         verbose: bool = True) -> pd.DataFrame:
    """
    Filter out listings with prices above a threshold.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    max_price : float, default=5000.0
        Maximum price threshold (exclusive)
    price_col : str, default='price'
        Name of the price column
    verbose : bool, default=True
        Whether to print filtering statistics
        
    Returns
    -------
    pd.DataFrame
        Filtered dataframe
    """
    original_count = len(df)
    df_filtered = df[df[price_col] < max_price].copy()
    filtered_count = len(df_filtered)
    removed_count = original_count - filtered_count
    
    if verbose:
        print(f"Filtered out {removed_count:,} listings with price >= ${max_price:,.0f}")
        print(f"Remaining: {filtered_count:,} listings ({filtered_count/original_count*100:.1f}%)")
    
    return df_filtered


def preprocess_data(df: pd.DataFrame, max_price: float = 5000.0, 
                   verbose: bool = True) -> pd.DataFrame:
    """
    Complete preprocessing pipeline: clean prices, add month numbers, filter outliers.
    
    Parameters
    ----------
    df : pd.DataFrame
        Raw dataframe from load_monthly_listings
    max_price : float, default=5000.0
        Maximum price threshold for outlier filtering
    verbose : bool, default=True
        Whether to print progress information
        
    Returns
    -------
    pd.DataFrame
        Preprocessed dataframe ready for analysis
    """
    if verbose:
        print("Preprocessing data...")
        print(f"  Original shape: {df.shape}")
    
    # Clean price column
    df = clean_price_column(df)
    
    # Add month number
    df = add_month_number(df)
    
    # Filter outliers
    df = filter_price_outliers(df, max_price=max_price, verbose=verbose)
    
    if verbose:
        print(f"  Final shape: {df.shape}")
    
    return df
