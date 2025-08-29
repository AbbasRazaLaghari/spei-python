# spei-python
Compute & plot SPEI (scales 3, 6, 9, 12) with Python

This repository contains a simple Python script that computes the **Standardized Precipitation Evapotranspiration Index (SPEI)** from monthly precipitation and PET data, and plots the result.

The script uses a single variable at the top of the file to set the SPEI timescale (in months):

```py
SPEI_SCALE = 9   # change to 3, 6, 9, or 12 months

# Install required Python packages

Linux (open terminal and paste):
pip install --upgrade pip
pip install pandas numpy matplotlib climate-indices

Windows (open CMD and paste):
pip install pandas numpy matplotlib climate-indices


