i = 0
team = input("Team: ")
for character in team:
    print("Give me a " + team[i].upper() + "!")
    i = i + 1
print("What does that spell? " + team.upper() + "!")