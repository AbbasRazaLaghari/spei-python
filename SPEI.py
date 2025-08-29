import os
os.environ["NUMBA_DISABLE_JIT"] = "1"\

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from climate_indices import indices
from climate_indices.compute import Periodicity

FILENAME = "data.txt"

SPEI_SCALE = 9
data = pd.read_csv(FILENAME, sep="\t")
start_year = int(data["Year"].iloc[0])
end_year = int(data["Year"].iloc[-1])

spei_array = indices.spei(
    precips_mm= data["preci"].to_numpy(dtype=np.float64),
    pet_mm= data["PET"].to_numpy(dtype=np.float64),
    scale= SPEI_SCALE,
    distribution= indices.Distribution.pearson,
    periodicity= Periodicity.monthly,
    data_start_year= start_year,
    calibration_year_initial= start_year,
    calibration_year_final= end_year,
    fitting_params= None
)
spei_values = np.array(spei_array, dtype=np.float32)
data.to_csv("SPEI_output.csv", index=False)

dates = pd.date_range(start=f"{start_year}-01", periods=len(spei_values),freq="M")

colors = ["skyblue" if v >=0 else "red" for v in spei_values]

plt.figure(figsize=(15, 5))
plt.bar(dates, spei_values, color=colors, width=25)
plt.axhline(0, color="black", linewidth=0.8)
plt.ylabel("SPEI")
plt.xlabel("Time")
plt.title("Standardized Precipitation Evapotranspiration Index (SPEI)")
plt.gca().xaxis.set_major_locator(mdates.YearLocator(5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
