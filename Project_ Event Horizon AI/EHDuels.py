#Event Horizon Battle Determination
IS = {"HP": 0,
         "Atk": 0,
         "Spd": 0,
         "Def": 0,
         "Res": 0}
IA = {"color": 0,
               "type": 0,
               "defensive": 0}

DS = {"HP": 0,
         "Atk": 0,
         "Spd": 0,
         "Def": 0,
         "Res": 0}
DA = {"color": 0,
               "type": 0,
               "defensive": 0}

def damage(Istats, Iattributes, Dstats, Dattributes):
    IDef = 0
    DDef = 0
    ITri = 0
    DTri = 0
    if Iattributes["defensive"] == "True":
        IDef = round(Dstats["Atk"] * 0.3, 0)
    if Dattributes["defensive"] == "True":
        DDef = round(Istats["Atk"] * 0.3, 0)
    if (Iattributes["color"] == "R" and Dattributes["color"] == "G") or (Iattributes["color"] == "B" and Dattributes["color"] == "R") or (Iattributes["color"] == "G" and Dattributes["color"] == "B"):
        ITri = round(Istats["Atk"] * 0.2, 0)
        DTri = round(Dstats["Atk"] * -0.2, 0)
    elif (Dattributes["color"] == "R" and Iattributes["color"] == "G") or (Dattributes["color"] == "B" and Iattributes["color"] == "R") or (Dattributes["color"] == "G" and Iattributes["color"] == "B"):
        DTri = round(Istats["Atk"] * 0.2, 0)
        ITri = round(Dstats["Atk"] * -0.2, 0)
    DDmg = Dstats["HP"] - ((Istats["Atk"] - DDef + ITri) - Dstats["Def"])
    IDmg = Istats["HP"] - ((Dstats["Atk"] - IDef + DTri) - Istats["Def"])
    return [DDmg, IDmg]

#Color: R/G/B/W
#Type: True (Phys) or False (Mag)
#Defensive: True or False

#Advantage/Disadvantage:
##Eff: 50%
##Defense: 30%
##TA: 20%

for stat in IS.keys():
    IS[stat] = int(input("Enter initiator's " + stat + ": "))
for attribute in IA.keys():
    IA[attribute] = input("Enter initiator's " + attribute + ": ").strip().title()

print()

for stat in DS.keys():
    DS[stat] = int(input("Enter defender's " + stat + ": "))
for attribute in DA.keys():
    DA[attribute] = input("Enter defender's " + attribute + ": ").strip().title()

print()

print(IS)
print(IA)
print(DS)
print(DA)

print()

while IS["HP"] > 0 and DS["HP"] > 0:
    Dmg = damage(IS, IA, DS,DA)
    if IS["HP"] > 0:
        DS["HP"] = DS["HP"] - Dmg[1]
        print("Defender took " + str(Dmg[1]) + " damage! It has " + str(DS["HP"]) + " HP left!")
    if DS["HP"] > 0:
        IS["HP"] = IS["HP"] - Dmg[0]
        print("Initiator took " + str(Dmg[0]) + " damage! It has " + str(IS["HP"]) + " HP left!")

if IS["HP"] > 0 and DS["HP"] <= 0:
    print("Initiator wins! Defender was slain.")
elif DS["HP"] > 0 and IS["HP"] <= 0:
    print("Defender wins! Initiator was slain.")
else:
    print("Something got fucked up")
