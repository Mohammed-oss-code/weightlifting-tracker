workouts = []

while True:
    print("\nWeightlifting Tracker")
    print("1. Add workout")
    print("2. View workouts")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        exercise = input("Exercise name: ")
        sets = input("Sets: ")
        reps = input("Reps: ")
        weight = input("Weight: ")

        workout = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }

        workouts.append(workout)
        print("Workout added.")

    elif choice == "2":
        for workout in workouts:
            print(workout)

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
