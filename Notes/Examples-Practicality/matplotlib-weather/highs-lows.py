import csv
from matplotlib import pyplot as plt
from datetime import datetime

#csv = comma separated values
#Our .csv for this example is weather data for Sitka, Alaska.

filename = "sitka_weather_2014.csv"

with open(filename) as input_file:
    reader = csv.reader(input_file)
    header_row = next(reader)
#row = row/day, index = column
    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))

#Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = "red", alpha = 0.5)
plt.plot(dates, lows, c = "blue", alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)

#Format plot
plt.title("Daily high and low temperatures, July 2014", fontsize = 24)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)
plt.tick_params(axis = "x", which = "both", labelsize = 8)
#plt.xticks(dates)

plt.xlim(dates[0],dates[-1])
plt.show()
