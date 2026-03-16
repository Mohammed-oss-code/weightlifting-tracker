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
        if not workouts:
            print("No workouts saved yet.")
        else:
            print("\nSaved Workouts:")
            for i, workout in enumerate(workouts, start=1):
                print(f"{i}. {workout['exercise']} - {workout['sets']} sets x {workout['reps']} reps at {workout['weight']} lbs")

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
