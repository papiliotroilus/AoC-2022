puzzleinput = open("input.txt", "r")
puzzleinput_data = puzzleinput.read()
guide = puzzleinput_data.split("\n")
guide.pop(-1)
score1 = 0
for round in guide:
    if round[2] == "X":
        score1 = score1 + 1
        if round[0] == "A":
            score1 = score1 + 3
        elif round[0] == "B":
            score1 = score1 + 0
        elif round[0] == "C":
            score1 = score1 + 6
    elif round[2] == "Y":
        score1 = score1 + 2
        if round[0] == "A":
            score1 = score1 + 6
        elif round[0] == "B":
            score1 = score1 + 3
        elif round[0] == "C":
            score1 = score1 + 0
    elif round[2] == "Z":
        score1 = score1 + 3
        if round[0] == "A":
            score1 = score1 + 0
        elif round[0] == "B":
            score1 = score1 + 6
        elif round[0] == "C":
            score1 = score1 + 3
score2 = 0
for round in guide:
    if round[2] == "X":
        score2 = score2 + 0
        if round[0] == "A":
            score2 = score2 + 3
        elif round[0] == "B":
            score2 = score2 + 1
        elif round[0] == "C":
            score2 = score2 + 2
    elif round[2] == "Y":
        score2 = score2 + 3
        if round[0] == "A":
            score2 = score2 + 1
        elif round[0] == "B":
            score2 = score2 + 2
        elif round[0] == "C":
            score2 = score2 + 3
    elif round[2] == "Z":
        score2 = score2 + 6
        if round[0] == "A":
            score2 = score2 + 2
        elif round[0] == "B":
            score2 = score2 + 3
        elif round[0] == "C":
            score2 = score2 + 1
print("The solution to part 1 is", score1)
print("The solution to part 2 is", score2)
