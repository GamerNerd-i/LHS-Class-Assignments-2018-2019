#league_leaders.py
#Python 3.7.0
#Written by Aidan Dionisio
#March 27, 2019
#Print the league leaders for hits, home runs, and runs batted in for a year (1999).

import csv

batting = "Batting.csv"
people = "People.csv"

year = "1999"
hits = 0
hit_champ = ""
homers = 0
homer_champ = ""
runs_batted_in = 0
RBI_champ = ""

#Get data
with open(batting) as data:
    dataread = csv.reader(data)
    data_header = next(dataread)
    for row in dataread:
        if row[1] == year:
            if int(row[8]) > hits:
                hits = int(row[8])
                hit_champ = row[0]
            if int(row[11]) > homers:
                homers = int(row[11])
                homers_champ = row[0]
            if int(row[12]) > runs_batted_in:
                runs_batted_in = int(row[12])
                RBI_champ = row[0]

with open(people) as names:
    nameread = csv.reader(names)
    name_header = next(nameread)
    for row in nameread:
        if row[0] == hit_champ:
            hit_champ = row[13] + " " + row[14]
        if row[0] == homers_champ:
            homers_champ = row[13] + " " + row[14]
        if row[0] == RBI_champ:
            RBI_champ = row[13] + " " + row[14]

#Print data
print("The leader in " + year + " for hits was " + hit_champ + " with " + str(hits) + " hits!")
print("The leader in " + year + " for home runs was " + homers_champ + " with " +
      str(homers) + " home runs!")
print("The leader in " + year + " for runs batted in was " + RBI_champ + " with " +
      str(runs_batted_in) + " runs batted in!")
