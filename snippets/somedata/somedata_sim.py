import pandas as pd
import matplotlib.pyplot as plt

data_dir = "somedata.csv"

rainfall = pd.read_csv(data_dir)

rainfall.dropna(inplace=True)

rainfall_annual = rainfall["Annual"]
year = rainfall["Year"]

print(rainfall_annual.describe())

plt.plot(year, rainfall_annual, alpha=0.5, c="black")
plt.scatter(year, rainfall_annual, c=rainfall_annual, cmap="YlGnBu")
plt.xlabel("Year")
plt.ylabel("Rainfall(mm)")
plt.ylim(0, 3000)
plt.colorbar()
plt.show()
