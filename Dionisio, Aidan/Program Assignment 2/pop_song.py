#pop_song.py
#Python 3.7.0
#Written by Aidan Dionisio
#September 12, 2018
#Print the lyrics to "99 Bottles of Pop on the Wall"

bottles = list(range(1,100))
bottles.reverse()

for bottle in bottles:
    print(str(bottle) + " bottles of pop on the wall, "
          + str(bottle) + " bottles of pop. You take one down, pass it around,  "
          + str(bottle - 1) + " bottles of pop on the wall.")
