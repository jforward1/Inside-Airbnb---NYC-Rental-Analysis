"""
Visualization utilities for Inside Airbnb dataset.

This module provides functions for creating plots and visualizations
of Airbnb rental price data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional, List


# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100


def plot_price_histograms_by_borough(df: pd.DataFrame,
                                     borough_col: str = 'neighbourhood_group_cleansed',
                                     price_col: str = 'price',
                                     figsize: tuple = (10, 6),
                                     bins: int = 50,
                                     save_path: Optional[Path] = None) -> None:
    """
    Plot overlapping histograms of prices by borough.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    borough_col : str, default='neighbourhood_group_cleansed'
        Name of the borough column
    price_col : str, default='price'
        Name of the price column
    figsize : tuple, default=(10, 6)
        Figure size
    bins : int, default=50
        Number of histogram bins
    save_path : Path, optional
        Path to save the figure
    """
    plt.figure(figsize=figsize)
    
    for group in df[borough_col].unique():
        subset = df[df[borough_col] == group]
        plt.hist(subset[price_col].dropna(), bins=bins, alpha=0.5, label=group)
    
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.title("Price Histograms by Neighborhood Group (Borough)")
    plt.legend()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_price_histogram_log_scale(df: pd.DataFrame,
                                   borough_col: str = 'neighbourhood_group_cleansed',
                                   price_col: str = 'price',
                                   figsize: tuple = (10, 6),
                                   bins: int = 50,
                                   save_path: Optional[Path] = None) -> None:
    """
    Plot overlapping histograms of log(price) by borough.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    borough_col : str, default='neighbourhood_group_cleansed'
        Name of the borough column
    price_col : str, default='price'
        Name of the price column
    figsize : tuple, default=(10, 6)
        Figure size
    bins : int, default=50
        Number of histogram bins
    save_path : Path, optional
        Path to save the figure
    """
    plt.figure(figsize=figsize)
    
    for group in df[borough_col].unique():
        subset = df[df[borough_col] == group]
        plt.hist(np.log(subset[price_col]), bins=bins, alpha=0.5, label=group)
    
    plt.xlabel("log(price)")
    plt.ylabel("Count")
    plt.title("Histogram of Prices (Log Scale)")
    plt.legend()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_manhattan_neighborhood_prices(df: pd.DataFrame,
                                      borough_col: str = 'neighbourhood_group_cleansed',
                                      neighborhood_col: str = 'neighbourhood_cleansed',
                                      price_col: str = 'price',
                                      top_n: Optional[int] = None,
                                      figsize: tuple = (14, 10),
                                      save_path: Optional[Path] = None) -> None:
    """
    Plot average prices by neighborhood in Manhattan.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    borough_col : str, default='neighbourhood_group_cleansed'
        Name of the borough column
    neighborhood_col : str, default='neighbourhood_cleansed'
        Name of the neighborhood column
    price_col : str, default='price'
        Name of the price column
    top_n : int, optional
        Show only top N neighborhoods by average price
    figsize : tuple, default=(14, 10)
        Figure size
    save_path : Path, optional
        Path to save the figure
    """
    manhattan_df = df[df[borough_col] == 'Manhattan'].copy()
    
    # Calculate average prices by neighborhood
    neighborhood_avg = (
        manhattan_df.groupby(neighborhood_col)[price_col]
        .mean()
        .sort_values(descending=True)
    )
    
    if top_n:
        neighborhood_avg = neighborhood_avg.head(top_n)
    
    plt.figure(figsize=figsize)
    sns.barplot(
        x=neighborhood_avg.values,
        y=neighborhood_avg.index,
        palette='viridis'
    )
    plt.title('Average Price by Neighborhood in Manhattan', fontsize=16)
    plt.xlabel('Average Price', fontsize=12)
    plt.ylabel('Neighborhood', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_manhattan_boxplot(df: pd.DataFrame,
                           borough_col: str = 'neighbourhood_group_cleansed',
                           neighborhood_col: str = 'neighbourhood_cleansed',
                           price_col: str = 'price',
                           figsize: tuple = (12, 8),
                           save_path: Optional[Path] = None) -> None:
    """
    Plot boxplot of price distribution by Manhattan neighborhood (log scale).
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    borough_col : str, default='neighbourhood_group_cleansed'
        Name of the borough column
    neighborhood_col : str, default='neighbourhood_cleansed'
        Name of the neighborhood column
    price_col : str, default='price'
        Name of the price column
    figsize : tuple, default=(12, 8)
        Figure size
    save_path : Path, optional
        Path to save the figure
    """
    manhattan_df = df[df[borough_col] == 'Manhattan'].copy()
    manhattan_df['log_price'] = np.log(manhattan_df[price_col])
    
    plt.figure(figsize=figsize)
    sns.boxplot(data=manhattan_df, x='log_price', y=neighborhood_col)
    plt.title("Price Distribution by Manhattan Neighborhood (Log Scale)")
    plt.xlabel("Log(Price)")
    plt.ylabel("Neighborhood")
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame,
                            columns: List[str],
                            figsize: tuple = (10, 6),
                            save_path: Optional[Path] = None) -> None:
    """
    Plot correlation heatmap for specified columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    columns : List[str]
        List of column names to include in correlation
    figsize : tuple, default=(10, 6)
        Figure size
    save_path : Path, optional
        Path to save the figure
    """
    corr = df[columns].corr()
    
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='bwr', center=0,
                square=True, linewidths=0.5)
    plt.title('Correlation Matrix for Features of Interest')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_seasonal_trends(df: pd.DataFrame,
                        groupby_col: str = 'month_num',
                        price_col: str = 'price',
                        figsize: tuple = (10, 6),
                        save_path: Optional[Path] = None) -> None:
    """
    Plot average price trends over months.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    groupby_col : str, default='month_num'
        Column to group by (typically month_num)
    price_col : str, default='price'
        Name of the price column
    figsize : tuple, default=(10, 6)
        Figure size
    save_path : Path, optional
        Path to save the figure
    """
    monthly_avg = df.groupby(groupby_col)[price_col].mean().sort_index()
    
    plt.figure(figsize=figsize)
    plt.plot(monthly_avg.index, monthly_avg.values, marker='o', linewidth=2, markersize=8)
    plt.xlabel('Month')
    plt.ylabel('Average Price ($)')
    plt.title('Average Price Changes Over Months')
    plt.grid(True, alpha=0.3)
    plt.xticks(monthly_avg.index)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
