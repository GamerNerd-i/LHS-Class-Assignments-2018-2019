import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "USC_weather_Feb2019.csv"

with open(filename) as input_file:
    reader = csv.reader(input_file)
    header_row = next(reader)
    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[8]))
        lows.append(int(row[9]))

#Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = "red", marker = ".", linestyle = "--")
plt.plot(dates, lows, c = "blue", marker = ".")

#Format plot
plt.title("Daily Highs and Lows, Los Angeles Feb 2019", fontsize = 24)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)
plt.tick_params(axis = "x", which = "both", labelsize = 8)
#plt.xticks(dates)

plt.xticks(dates)
plt.xlim(dates[0],dates[-1])
plt.show()



#date: 2, Tmax 8, Tmin 8
