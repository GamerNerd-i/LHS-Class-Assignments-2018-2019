#Player dictionary test

players = {"Kei": {"stats": {"HP": 22,
                              "Atk": 17,
                              "Mag": 3,
                              "Spd": 10,
                              "Def": 13,
                              "Res": 7},
                   "growth": {"HP": 90,
                              "Atk": 75,
                              "Mag": 25,
                              "Spd": 60,
                              "Def": 70,
                              "Res": 30},
                   "attributes" : {"color": "R",
                                   "type": True,
                                   "defensive": False}},
           "Sarah": {"stats": {"HP": 16,
                              "Atk": 6,
                              "Mag": 13,
                              "Spd": 12,
                              "Def": 9,
                              "Res": 13},
                   "growth": {"HP": 80,
                              "Atk": 20,
                              "Mag": 55,
                              "Spd": 70,
                              "Def": 60,
                              "Res": 65},
                   "attributes" : {"color": "G",
                                   "type": False,
                                   "defensive": False}},
           "Aurelius": {"stats": {"HP": 18,
                              "Atk": 10,
                              "Mag": 13,
                              "Spd": 12,
                              "Def": 9,
                              "Res": 13},
                   "growth": {"HP": 20,
                              "Atk": 45,
                              "Mag": 72,
                              "Spd": 71,
                              "Def": 71,
                              "Res": 71},
                   "attributes" : {"color": "B",
                                   "type": False,
                                   "defensive": False}}}

def damage(initiator, defender):
    IDef = 0
    DDef = 0
    ITri = 0
    DTri = 0
    if players[initiator]["attributes"]["defensive"] == "True":
        IDef = round(players[defender]["stats"]["Atk"] * 0.3, 0)
    if players[defender]["attributes"]["defensive"] == "True":
        DDef = round(players[initiator]["stats"]["Atk"] * 0.3, 0)
    if (players[initiator]["attributes"]["color"] == "R" and players[defender]["attributes"]["color"] == "G") or (players[initiator]["attributes"]["color"] == "B" and players[defender]["attributes"]["color"] == "R") or (players[initiator]["attributes"]["color"] == "G" and players[defender]["attributes"]["color"] == "B"):
        ITri = round(players[initiator]["stats"]["Atk"] * 0.2, 0)
        DTri = round(players[defender]["stats"]["Atk"] * -0.2, 0)
    elif (players[defender]["attributes"]["color"] == "R" and players[initiator]["attributes"]["color"] == "G") or (players[defender]["attributes"]["color"] == "B" and players[initiator]["attributes"]["color"] == "R") or (players[defender]["attributes"]["color"] == "G" and players[initiator]["attributes"]["color"] == "B"):
        DTri = round(players[initiator]["stats"]["Atk"] * 0.2, 0)
        ITri = round(players[defender]["stats"]["Atk"] * -0.2, 0)
    DDmg = players[defender]["stats"]["HP"] - ((players[initiator]["stats"]["Atk"] - DDef + ITri) - players[defender]["stats"]["Def"])
    IDmg = players[initiator]["stats"]["HP"] - ((players[defender]["stats"]["Atk"] - IDef + DTri) - players[initiator]["stats"]["Def"])
    return [DDmg, IDmg]

def battle(initiator, defender):
    print("Fight!")
    while players[initiator]["stats"]["HP"] > 0 and players[defender]["stats"]["HP"] > 0:
        Dmg = damage(initiator, defender)
        if players[initiator]["stats"]["HP"] > 0:
            players[defender]["stats"]["HP"] = players[defender]["stats"]["HP"] - Dmg[1]
            print(defender + " took " + str(Dmg[1]) + " damage! " + defender + " has " +
                  str(players[defender]["stats"]["HP"]) + " HP left!")
        if players[defender]["stats"]["HP"] > 0:
            players[initiator]["stats"]["HP"] = players[initiator]["stats"]["HP"] - Dmg[0]
            print(initiator + " took " + str(Dmg[0]) + " damage! " + initiator + " has " +
                  str(players[initiator]["stats"]["HP"]) + " HP left!")
    if players[initiator]["stats"]["HP"] > 0 and players[defender]["stats"]["HP"] <= 0:
        print(initiator+ " wins! " + defender + " was slain.")
        del players[defender]
    elif players[defender]["stats"]["HP"] > 0 and players[initiator]["stats"]["HP"] <= 0:
        print(defender + " wins! " + initiator + " was slain.")
        del players[initiator]
    else:
        print("Something got fucked up")

initiator = input("Who initiates the attack? ").strip().title()
defender = input("Who is " + initiator + " attacking? ").strip().title()

battle(initiator, defender)

print(players.keys())
