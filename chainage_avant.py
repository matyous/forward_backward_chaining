def verifRule(rule, K):

    if set(rule).issubset(set(K)):
        return True
    else:
        return False


def stepForward(R, K):

    for rule in R:
        if verifRule(rule[0], K):
            K.append(rule[1])
            K = [set(K)]
            R.remove(rule)
            return True

    return False


def chainageAvant(R, K):
    while stepForward(R, K):
        print(K)
    return 'END'

"""
K = readknowledge()
R = readRules()
print(K)
print(R)

print(chainageAvant(R, K))
print(K)

"""