"""
Example refactored notebook showing how to use the inside_airbnb package.

This demonstrates the improved structure with functions extracted to modules.
Copy this pattern into your Jupyter notebook cells.
"""

# Cell 1: Imports
from pathlib import Path
import sys

# Add src to path so we can import our package
sys.path.insert(0, str(Path(__file__).parent.parent))

from inside_airbnb import data_loading, preprocessing, analysis, visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cell 2: Load data
data_folder = Path("../")  # Adjust path as needed
full_df = data_loading.load_monthly_listings(data_folder, year=2025)

# Cell 3: Preprocess data
full_df = preprocessing.preprocess_data(full_df, max_price=5000.0, verbose=True)

# Cell 4: Calculate monthly statistics
monthly_stats = analysis.calculate_rental_stats(full_df)
display(
    monthly_stats.style
        .format({'count':'{:,.0f}', 'mean':'{:,.2f}', 'median':'{:,.2f}', 'std':'{:,.2f}'})
        .background_gradient(cmap='Blues', subset=['median'])
        .background_gradient(cmap='Greens', subset=['mean'])
)

# Cell 5: Compare boroughs
comparison = analysis.compare_boroughs(full_df, target_borough='Manhattan')
print("Borough Comparison:")
print(comparison)

# Cell 6: Count luxury listings
luxury_by_borough = analysis.count_luxury_listings(
    full_df, 
    price_threshold=1000.0,
    groupby_col='neighbourhood_group_cleansed'
)
print("\nLuxury listings (>$1000) by borough:")
print(luxury_by_borough)

# Cell 7: Visualizations
visualization.plot_price_histograms_by_borough(full_df)
visualization.plot_price_histogram_log_scale(full_df)
visualization.plot_manhattan_neighborhood_prices(full_df, top_n=20)
visualization.plot_manhattan_boxplot(full_df)

# Cell 8: Correlation analysis
cols_of_interest = [
    'price', 'minimum_nights', 'number_of_reviews', 
    'reviews_per_month', 'calculated_host_listings_count', 'bedrooms'
]
visualization.plot_correlation_heatmap(full_df, cols_of_interest)

# Cell 9: Seasonal trends
visualization.plot_seasonal_trends(full_df)
seasonal_stats = analysis.calculate_seasonal_range(full_df)
print(f"\nSeasonal Price Range: ${seasonal_stats['range']:.2f}")
print(f"Percentage Range: {seasonal_stats['pct_range']:.1f}%")
