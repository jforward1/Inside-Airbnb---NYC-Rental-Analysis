"""
Statistical analysis functions for Inside Airbnb dataset.

This module provides functions for calculating rental statistics,
comparing boroughs, and analyzing seasonal trends.
"""

import pandas as pd
import numpy as np
from typing import Optional


def calculate_rental_stats(df: pd.DataFrame, 
                          groupby_col: str = 'month_num',
                          price_col: str = 'price') -> pd.DataFrame:
    """
    Calculate rental statistics (count, mean, median, std) grouped by a column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with price data
    groupby_col : str, default='month_num'
        Column to group by (e.g., 'month_num' for monthly stats)
    price_col : str, default='price'
        Name of the price column
        
    Returns
    -------
    pd.DataFrame
        Statistics dataframe with count, mean, median, std columns
    """
    stats = (
        df.groupby(groupby_col)[price_col]
        .agg(['count', 'mean', 'median', 'std'])
        .sort_index()
    )
    
    # Add month names if grouping by month_num
    if groupby_col == 'month_num':
        stats['month'] = stats.index.map(
            lambda x: pd.to_datetime(str(x), format='%m').month_name()
        )
    
    return stats


def compare_boroughs(df: pd.DataFrame, 
                    borough_col: str = 'neighbourhood_group_cleansed',
                    target_borough: str = 'Manhattan',
                    price_col: str = 'price') -> pd.DataFrame:
    """
    Compare average prices between a target borough and all other boroughs.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    borough_col : str, default='neighbourhood_group_cleansed'
        Name of the borough column
    target_borough : str, default='Manhattan'
        Borough to compare against others
    price_col : str, default='price'
        Name of the price column
        
    Returns
    -------
    pd.DataFrame
        Comparison dataframe with average prices and ratio
        
    Examples
    --------
    >>> comparison = compare_boroughs(df, target_borough='Manhattan')
    """
    target_avg = df[df[borough_col] == target_borough][price_col].mean()
    other_avg = df[df[borough_col] != target_borough][price_col].mean()
    
    comparison = pd.DataFrame({
        f"{target_borough}_avg_price": [target_avg],
        "Other_boroughs_avg_price": [other_avg],
        "Ratio": [target_avg / other_avg]
    })
    
    return comparison


def count_luxury_listings(df: pd.DataFrame, 
                         price_threshold: float = 1000.0,
                         groupby_col: Optional[str] = None,
                         price_col: str = 'price') -> pd.Series:
    """
    Count listings above a price threshold, optionally grouped by a column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    price_threshold : float, default=1000.0
        Price threshold for "luxury" listings
    groupby_col : str, optional
        Column to group by (e.g., 'neighbourhood_group_cleansed')
    price_col : str, default='price'
        Name of the price column
        
    Returns
    -------
    pd.Series or int
        Count of luxury listings (grouped if groupby_col provided)
    """
    luxury_df = df[df[price_col] > price_threshold]
    
    if groupby_col:
        return luxury_df.groupby(groupby_col).size()
    else:
        return len(luxury_df)


def calculate_seasonal_range(df: pd.DataFrame,
                            groupby_col: str = 'month_num',
                            price_col: str = 'price') -> dict:
    """
    Calculate seasonal price variation statistics.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    groupby_col : str, default='month_num'
        Column to group by (typically month_num for seasonal analysis)
    price_col : str, default='price'
        Name of the price column
        
    Returns
    -------
    dict
        Dictionary with min, max, range, and percentage range
    """
    monthly_avg = df.groupby(groupby_col)[price_col].mean()
    
    min_price = monthly_avg.min()
    max_price = monthly_avg.max()
    price_range = max_price - min_price
    pct_range = (price_range / min_price) * 100
    
    return {
        'min_price': min_price,
        'max_price': max_price,
        'range': price_range,
        'pct_range': pct_range
    }
