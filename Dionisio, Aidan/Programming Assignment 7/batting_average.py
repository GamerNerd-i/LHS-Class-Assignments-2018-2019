#batting_average.py
#Python 3.7.0
#Written by Aidan Dionisio
#March 25, 2019
#Display a line graph of a player's (Manny Machado) batting average per year.

import csv
from matplotlib import pyplot as plt

filename = "Batting.csv"

#Get data
with open(filename) as input_file:
    reader = csv.reader(input_file)
    header_row = next(reader)
    year = []
    batting_avg = []
    
    for row in reader:
        if row[0] == "machama01":
            year.append(int(row[1]))
            batting_avg.append(int(row[8])/int(row[6]))

#Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(year, batting_avg, c = "#052140", marker = ".")

#Format plot
plt.title("Manny Machado's Career Batting Average", fontsize = 24)
plt.xlabel("Year", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Batting Average", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)
plt.tick_params(axis = "x", which = "both", labelsize = 8)

plt.xticks(year)
plt.xlim(year[0],year[-1])
plt.show()

