def isUpdated(goals, K, R):

    for goal in goals:
        if goal in K:
            goals.remove(goal)
            return True

        elif goal in [r[1] for r in R]:
            goals.extend(R[[r[1] for r in R].index(goal)][0])
            goals.remove(goal)
            goals = [set(goals)]
            return True

    return False


def chainageAriere(goals, K, R):
    while goals[0] in [r[1] for r in R]:
        print(goals)
        g = goals.copy()
        i = [r[1] for r in R].index(goals[0])

        while isUpdated(goals, K, R):
            print(goals)

        if not goals:
            return True
        else:
            goals = g.copy()
            R.remove(R[i])

    return False


"""
K = readknowledge()
R = readRules()
G = readGoal()

print(chainageAriere(G, K, R))

"""