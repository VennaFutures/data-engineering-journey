age = 24
study_hours = 3

if age >= 18:
    print("Adult learner")
else:
    print("Minor")

if study_hours >= 3:
    print("On track with learning")
elif study_hours == 2:
    print("Need to increase effort")
else:
    print("Off track")

    age = 24
study_hours = 3

# Existing checks
if age >= 18:
    print("Adult learner")
else:
    print("Minor")

if study_hours >= 3:
    print("On track with learning")
elif study_hours == 2:
    print("Need to increase effort")
else:
    print("Off track")

# New variables
goal = "Data Engineer"
commitment_level = 4

# Commitment logic
if commitment_level >= 4:
    print("High commitment")
else:
    print("Needs improvement")

# Context sentence tying it together
print("Goal:", goal, "| Study hours:", study_hours, "| Commitment:", commitment_level)

if (age >= 18) and (study_hours >= 3):
    print("Adult learner on track")
elif (age >= 18) and (study_hours < 3):
    print("Adult learner — adjust schedule")
else:
    print("Minor — ensure guidance and support")