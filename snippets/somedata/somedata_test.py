import pandas as pd
import matplotlib.pyplot as plt

data_dir = 'someplace.csv'

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

YearIn = ""
Year = 0
# isdigit()用于判断字符串是否仅由数字组成
while(YearIn.isdigit() and (Year > 1933 and Year < 2021)):
    print("Enter a year between 1888-2020 to display:")
    YearIn = input()
    Year = int(YearIn)


# Read the file
rainfall = pd.read_csv(data_dir)

# 去除空值
rainfall.dropna(inplace=True)

# Set the indexing column
rainfall_index = rainfall.set_index("Year", drop=False)

# Use annual data
rainfall_monthly = rainfall_index.loc[Year, months]
print(rainfall_monthly.describe())

plt.plot(months, rainfall_monthly, alpha=0.5, c="black")
plt.scatter(months, rainfall_monthly, c=rainfall_monthly, cmap="YlGnBu")
plt.xlabel("Year")
plt.ylabel("Rainfall(mm)")
plt.colorbar()
plt.show()
