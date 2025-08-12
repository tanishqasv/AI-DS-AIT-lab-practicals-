print("welcome to water jug problem ")
def water_jug_problem(jug1_cap, jug2_cap2, target):
    jug1 = 0
    jug2 = 0
    jug1_cap=5
    jug2_cap2=7
    target=3
    steps = []

    while True:
        # If either jug has the target amount, stop
        if jug1 == target or jug2 == target:
            steps.append((jug1, jug2))
            break

        # Fill Jug1 if it's empty
        if jug1 == 0:
            jug1 = jug1_cap
            steps.append((jug1, jug2))

        # Pour water from Jug1 to Jug2
        elif jug2 != jug2_cap2:
            transfer = min(jug1, jug2_cap2 - jug2)
            jug2 += transfer
            jug1 -= transfer
            steps.append((jug1, jug2))

        # If Jug2 is full, empty it
        elif jug2 == jug2_cap2:
            jug2 = 0
            steps.append((jug1, jug2))

    # Print all steps
    print("Steps to reach target:")
    for step in steps:
        print(f"Jug1: {step[0]}, Jug2: {step[1]}")

# Example usage
water_jug_problem(4, 3, 2)
