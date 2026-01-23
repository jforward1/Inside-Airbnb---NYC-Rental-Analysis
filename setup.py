"""
Setup file for inside_airbnb package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README if it exists
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="inside-airbnb-analysis",
    version="0.1.0",
    description="Data science project for analyzing NYC Airbnb rental prices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jett Forward",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "geopandas>=0.13.0",
        "scikit-learn>=1.3.0",
        "jinja2>=3.0.0",
    ],
)
